import os
import re
import sys
import html
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

def normalize_text(text):
    if text is None:
        return ""
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

SOURCES = [
    {"name": "The Verge", "feed": "https://www.theverge.com/rss/index.xml", "site": "https://www.theverge.com"},
    {"name": "Ars Technica", "feed": "https://feeds.arstechnica.com/arstechnica/index", "site": "https://arstechnica.com"},
    {"name": "TechCrunch", "feed": "https://techcrunch.com/feed/", "site": "https://techcrunch.com"},
    {"name": "Wired", "feed": "https://www.wired.com/feed/rss", "site": "https://www.wired.com"},
    {"name": "Engadget", "feed": "https://www.engadget.com/rss.xml", "site": "https://www.engadget.com"},
    {"name": "CNET", "feed": "https://www.cnet.com/rss/news/", "site": "https://www.cnet.com"},
    {"name": "Reuters Technology", "feed": "https://www.reutersagency.com/feed/?best-topics=tech&post_type=best", "site": "https://www.reuters.com/technology/"},
    {"name": "Bloomberg Technology", "feed": None, "site": "https://www.bloomberg.com/technology"},
    {"name": "The Information", "feed": None, "site": "https://www.theinformation.com"},
    {"name": "Financial Times — Tech", "feed": "https://www.ft.com/technology?format=rss", "site": "https://www.ft.com/technology"},
    {"name": "Hacker News", "feed": "https://news.ycombinator.com/rss", "site": "https://news.ycombinator.com"},
    {"name": "Lobsters", "feed": "https://lobste.rs/rss", "site": "https://lobste.rs"},
    {"name": "The Register", "feed": "https://www.theregister.com/headlines.atom", "site": "https://www.theregister.com"},
    {"name": "MIT Technology Review", "feed": "https://www.technologyreview.com/feed/", "site": "https://www.technologyreview.com"},
    {"name": "IEEE Spectrum", "feed": "https://spectrum.ieee.org/feeds/feed.rss", "site": "https://spectrum.ieee.org"},
    {"name": "VentureBeat (AI)", "feed": "https://venturebeat.com/category/ai/feed/", "site": "https://venturebeat.com/category/ai/"},
    {"name": "Import AI", "feed": "https://importai.substack.com/feed", "site": "https://importai.substack.com"},
    {"name": "Krebs on Security", "feed": "https://krebsonsecurity.com/feed/", "site": "https://krebsonsecurity.com"},
    {"name": "BleepingComputer", "feed": "https://www.bleepingcomputer.com/feed/", "site": "https://www.bleepingcomputer.com"},
    {"name": "Tom's Hardware", "feed": "https://www.tomshardware.com/feeds/all", "site": "https://www.tomshardware.com"},
]

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}


class FetchError(Exception):
    pass


def fetch_url(url, timeout=20):
    request = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as r:
            data = r.read()
            content_type = r.headers.get("Content-Type", "")
            return data, content_type
    except urllib.error.HTTPError as e:
        raise FetchError(f"HTTP {e.code} {e.reason}")
    except urllib.error.URLError as e:
        raise FetchError(str(e))


def first_text(element, tags):
    for tag in tags:
        child = element.find(tag)
        if child is not None and child.text:
            return child.text.strip()
    return None


def parse_datetime(value):
    if value is None:
        return None
    value = value.strip()
    try:
        dt = parsedate_to_datetime(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except (TypeError, ValueError, IndexError):
        pass
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        dt = datetime.fromisoformat(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError:
        return None


def resolve_atom_link(entry):
    for link in entry.findall("{http://www.w3.org/2005/Atom}link"):
        rel = link.attrib.get("rel", "alternate")
        if rel in ("alternate", ""):
            href = link.attrib.get("href")
            if href:
                return href
    return None


def parse_feed(content):
    try:
        root = ET.fromstring(content)
    except ET.ParseError as exc:
        raise FetchError(f"XML parse error: {exc}")

    entries = []
    if root.tag == "rss" or root.tag.endswith("rss") or root.find("channel") is not None:
        channel = root.find("channel")
        if channel is None:
            channel = root
        for item in channel.findall("item"):
            title = first_text(item, ["title"])
            link = first_text(item, ["link"])
            if not link:
                guid = item.find("guid")
                if guid is not None and guid.text:
                    link = guid.text.strip()
            summary = first_text(item, ["description", "summary", "content:encoded"])
            published = first_text(item, ["pubDate", "dc:date", "published"])
            entries.append({"title": title, "link": link, "summary": summary, "published": published})
    elif root.tag.endswith("feed") or root.tag == "{http://www.w3.org/2005/Atom}feed":
        for item in root.findall("{http://www.w3.org/2005/Atom}entry"):
            title = first_text(item, ["{http://www.w3.org/2005/Atom}title"])
            link = resolve_atom_link(item)
            summary = first_text(item, ["{http://www.w3.org/2005/Atom}summary", "{http://www.w3.org/2005/Atom}content"])
            published = first_text(item, ["{http://www.w3.org/2005/Atom}published", "{http://www.w3.org/2005/Atom}updated"])
            entries.append({"title": title, "link": link, "summary": summary, "published": published})
    else:
        raise FetchError("Unknown feed format")
    return entries


def pick_category(title, summary, source):
    text = f"{title} {summary} {source}".lower()
    if any(k in text for k in ["ai", "anthropic", "openai", "google", "microsoft", "nvidia", "meta", "invoice", "openai", "deepmind", "claude", "chatgpt", "gpt", "llm"]):
        return "AI / Big Tech"
    if any(k in text for k in ["chip", "gpu", "nvidia", "amd", "intel", "quantum", "processor", "cpu", "semiconductor", "silicon", "fabrication", "tsmc", "micron"]):
        return "Hardware / Chips"
    if any(k in text for k in ["mouse", "keyboard", "macbook", "phone", "laptop", "camera", "gadgets", "peripheral", "accessory", "docking", "product", "console"]):
        return "Hardware / Gadgets"
    if any(k in text for k in ["security", "malware", "breach", "vulnerability", "zero-day", "hack", "ransomware", "police", "fbi", "privacy", "encryption", "incident", "malicious"]):
        return "Security"
    if any(k in text for k in ["law", "regulation", "policy", "fcc", "eu", "export", "ban", "sanction", "court", "class-action", "lawsuit", "legislation", "government"]):
        return "Policy / Regulation"
    if any(k in text for k in ["open source", "linux", "debian", "git", "github", "developer", "rust", "python", "programming", "open-source", "stack", "software"]):
        return "Open Source / Developer"
    if any(k in text for k in ["data center", "datacenter", "power", "water", "grid", "infrastructure", "carrier", "network", "cloud", "aws", "azure", "google cloud", "oracle cloud"]):
        return "Data Centers / Infrastructure"
    if any(k in text for k in ["science", "nasa", "space", "quantum", "research", "lab", "robot", "biology", "physics", "mars", "spacecraft"]):
        return "Defense / Science"
    if any(k in text for k in ["union", "workers", "labor", "strike", "collective", "wages", "cwa", "arbitration", "hr"]):
        return "Labor / Industry"
    if any(k in text for k in ["wordle", "game", "media", "tv", "movie", "ad", "content", "streaming", "netflix", "disney", "broadcast"]):
        return "Big Tech / Media"
    return "AI / Big Tech"


def build_digest(entries, window_start, window_end, mode_label, notes):
    generated = window_end.astimezone().strftime("%Y-%m-%d %H:%M local")
    window_line = f"{window_start.astimezone().strftime('%Y-%m-%d %H:%M')} → {window_end.astimezone().strftime('%Y-%m-%d %H:%M')}"
    if mode_label:
        mode_line = f"*Mode: {mode_label}*"
    else:
        mode_line = ""
    lines = [
        "# Tech News — Last 48 Hours",
        f"*Generated: {generated}*",
        f"*Window: {window_line}*",
    ]
    if mode_line:
        lines.append(mode_line)
    lines.append("")
    categories = {}
    for entry in entries:
        categories.setdefault(entry["category"], []).append(entry)
    order = [
        "AI / Big Tech",
        "Hardware / Gadgets",
        "Hardware / Chips",
        "Policy / Regulation",
        "Security",
        "Big Tech / Media",
        "Data Centers / Infrastructure",
        "Defense / Science",
        "Open Source / Developer",
        "Labor / Industry",
    ]
    for cat in order + [c for c in categories.keys() if c not in order]:
        if cat not in categories:
            continue
        lines.append(f"## {cat}")
        lines.append("")
        for entry in categories[cat]:
            lines.append(f"### {entry['title']}")
            lines.append(entry['summary'])
            lines.append(f"**Source:** {entry['source']} · [Read original]({entry['link']}) · {entry['published_fmt']}")
            if entry.get("also"):
                lines.append(entry["also"])
            lines.append("")
    if notes:
        lines.append("## Notes")
        lines.append("")
        for note in notes:
            lines.append(f"- {note}")
    return "\n".join(lines).strip() + "\n"


def choose_dest_path(base_dir, timestamp):
    base = os.path.join(base_dir, f"{timestamp}_tech-news.md")
    if not os.path.exists(base):
        return base
    index = 2
    while True:
        candidate = os.path.join(base_dir, f"{timestamp}-" + str(index) + "_tech-news.md")
        if not os.path.exists(candidate):
            return candidate
        index += 1


def refine_entries(raw_entries, window_start, window_end, source_name):
    cleaned = []
    for raw in raw_entries:
        title = normalize_text(raw.get("title") or "Untitled")
        link = raw.get("link") or ""
        if not link:
            continue
        published = parse_datetime(raw.get("published"))
        if published is None:
            continue
        if not (window_start <= published <= window_end):
            continue
        summary = normalize_text(raw.get("summary") or title)
        if len(summary) > 500:
            summary = summary[:497].rstrip() + "..."
        published_fmt = published.astimezone().strftime("%d %b")
        cleaned.append({
            "title": title,
            "link": link,
            "summary": summary,
            "published": published,
            "published_fmt": published_fmt,
            "source": source_name,
        })
    return cleaned


def dedupe_entries(entries):
    seen = {}
    deduped = []
    for entry in entries:
        key = entry["link"].split("#")[0].rstrip("/")
        if key in seen:
            existing = seen[key]
            if len(entry["summary"]) > len(existing["summary"]):
                existing["summary"] = entry["summary"]
            existing["source"] = f"{existing['source']} / {entry['source']}"
        else:
            seen[key] = entry
            deduped.append(entry)
    return deduped


def find_latest_digest(digests_dir):
    candidates = []
    for filename in os.listdir(digests_dir):
        if not filename.endswith("_tech-news.md"):
            continue
        prefix = filename[:16]
        try:
            ts = datetime.strptime(prefix, "%Y-%m-%d_%H%M")
            candidates.append(ts)
        except ValueError:
            continue
    if not candidates:
        return None
    return max(candidates)


def delete_old_digests(digests_dir, cutoff_date):
    deleted = []
    for filename in os.listdir(digests_dir):
        if not filename.endswith("_tech-news.md"):
            continue
        date_part = filename[:10]
        try:
            file_date = datetime.strptime(date_part, "%Y-%m-%d").date()
        except ValueError:
            continue
        if file_date < cutoff_date:
            deleted.append(filename)
            os.remove(os.path.join(digests_dir, filename))
    return deleted


def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "digests"))
    if not os.path.isdir(base_dir):
        os.makedirs(base_dir, exist_ok=True)
    now = datetime.now(timezone.utc).astimezone()
    cutoff_date = (now.date() - timedelta(days=30))
    deleted = delete_old_digests(base_dir, cutoff_date)
    latest = find_latest_digest(base_dir)
    if latest is not None:
        latest_local = latest.replace(tzinfo=timezone.utc).astimezone()
        delta = now - latest_local
        if delta < timedelta(hours=48):
            window_start = latest_local - timedelta(hours=1)
            mode_label = f"incremental run: {latest_local.strftime('%Y-%m-%d %H:%M')} → {now.strftime('%Y-%m-%d %H:%M')} (last digest {latest_local.strftime('%Y-%m-%d_%H%M')}, +1h overlap)"
        else:
            window_start = now - timedelta(hours=48)
            mode_label = "full 48h run"
    else:
        window_start = now - timedelta(hours=48)
        mode_label = "full 48h run"
    window_end = now
    all_entries = []
    notes = []
    failed_sources = []
    no_items_sources = []
    for source in SOURCES:
        if not source["feed"]:
            failed_sources.append(source["name"] + " (no public feed)")
            continue
        try:
            content, _ = fetch_url(source["feed"])
            raw_entries = parse_feed(content)
        except FetchError as exc:
            failed_sources.append(f"{source['name']} ({source['feed']}): {exc}")
            continue
        cleaned = refine_entries(raw_entries, window_start.astimezone(timezone.utc), window_end.astimezone(timezone.utc), source["name"])
        if not cleaned:
            no_items_sources.append(source["name"])
        all_entries.extend(cleaned)
    if len(all_entries) < 5:
        expanded_start = now - timedelta(hours=72)
        expanded = []
        for source in SOURCES:
            if not source["feed"]:
                continue
            try:
                content, _ = fetch_url(source["feed"])
                raw_entries = parse_feed(content)
            except FetchError:
                continue
            cleaned = refine_entries(raw_entries, expanded_start.astimezone(timezone.utc), window_end.astimezone(timezone.utc), source["name"])
            expanded.extend(cleaned)
        if len(expanded) >= len(all_entries):
            all_entries = expanded
            window_start = expanded_start
            mode_label += " (expanded to 72h)"
    all_entries = dedupe_entries(all_entries)
    for entry in all_entries:
        entry["category"] = pick_category(entry["title"], entry["summary"], entry["source"])
    all_entries.sort(key=lambda item: item["published"], reverse=True)
    if no_items_sources:
        notes.append("Sources with no fresh items in window: " + ", ".join(sorted(no_items_sources)))
    if failed_sources:
        notes.append("Sources unavailable or no usable feed: " + ", ".join(sorted(failed_sources)))
    if len(all_entries) == 0:
        notes.append("No usable stories found in the current window.")
    content = build_digest(all_entries, window_start, window_end, mode_label, notes)
    timestamp = now.strftime("%Y-%m-%d_%H%M")
    dest = choose_dest_path(base_dir, timestamp)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated digest: {dest}")
    if deleted:
        print("Deleted old digests:", ", ".join(sorted(deleted)))
    else:
        print("No digests older than 30 days were deleted.")
    same_day_files = [f for f in os.listdir(base_dir) if f.startswith(now.strftime("%Y-%m-%d")) and f.endswith("_tech-news.md")]
    if len(same_day_files) > 1:
        print("Warning: more than one same-day digest file found. Manual merge may be needed.")
    else:
        print("No same-day merge needed.")


if __name__ == "__main__":
    main()
