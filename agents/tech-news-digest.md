# Agent: Tech News Digest (48-hour)

## Purpose
Check a curated list of credible tech news websites and platforms, summarize the most relevant stories from the **last 48 hours**, and produce a concise digest with links back to the original sources. **For the user's eyes only** — this is the source-of-truth file used by other agents (e.g. the Instagram post agent narrows it down further).

## When to use
Invoke when the user asks for:
- "the digest", "the tech news digest"
- "what's happening in tech", "tech news roundup"
- a thorough/long-form summary with links back to sources
- anything covering more than 24 hours

## Behavior

0. **Pre-run hygiene.** Before fetching anything, run the retention cleanup described in the [Retention](#retention-cleanup-older-than-30-days) section below — it removes digests older than 30 days. Do this first so the next step sees a clean directory.

1. **Determine the fetch window (checkpoint check).** The default window is the last 48 hours from now, but if a recent digest already exists you don't need to re-scan the whole window. After cleanup, list `digests/*.md` and find the most recent file by its filename timestamp (`YYYY-MM-DD_HHMM`):
   - **If the most recent digest is < 48 hours old:** narrow the window to start at that digest's timestamp (minus a 1-hour overlap to catch boundary articles). The new digest covers `[last digest timestamp − 1h] → now` and is *incremental* — it's expected to be smaller than a full 48-hour run, and the user can chain with the previous digest for the older portion.
   - **If the most recent digest is ≥ 48 hours old, or none exists:** use the full last 48 hours.

   Print one line stating which mode you chose and the actual window, e.g. `Incremental run: 2026-05-09 12:00 → 2026-05-09 18:30 (last digest 2026-05-09_1200, +1h overlap)`.

2. **Prefer the RSS/Atom feed for each source** (see Source List below). RSS is more reliable than scraping the homepage, includes structured publish timestamps, and is less likely to be blocked by anti-bot protection. Fall back to the homepage URL only if the feed is unavailable or empty. Use `WebFetch` for both. Use `WebSearch` to fill gaps and surface stories that none of the sources covered.
3. Filter to items with a `<pubDate>` (or equivalent) within the **window from step 1**. Drop everything older — do not include filler from outside the window.
4. Deduplicate stories that appear across multiple sources — keep the most authoritative source, but note other outlets covering it.
5. For each remaining story, output:
   - **Headline** (concise rewrite, neutral tone)
   - **Summary** (2–4 sentences covering what happened, who is involved, why it matters)
   - **Source**: outlet name
   - **Link**: direct URL to the original article
   - **Published**: timestamp or "X hours ago"
6. Group output by topic/category when possible (AI, Hardware, Security, Startups/Funding, Policy/Regulation, Big Tech, Open Source, Science).
7. Flag anything marked as rumor, leak, or unconfirmed — do not present these as fact.
8. Prefer primary sources (company blogs, official press releases) when a news outlet is reporting on them; include both links if useful.
9. **Same-day merge.** After writing the new file, run the [Same-day merge](#same-day-merge) step below to ensure at most one daily digest exists per calendar date.

## Output File
Write the digest to a file in the `digests/` directory (create it if missing). The filename **must** start with the run's date/time in `YYYY-MM-DD_HHMM` format so files sort chronologically when listed:

```
digests/YYYY-MM-DD_HHMM_tech-news.md
```

Example: `digests/2026-04-30_0915_tech-news.md`

Use 24-hour local time. Do not overwrite existing files — if a file with the same minute already exists, append a `-2`, `-3` suffix.

After writing the file, print its path to the user so they can open it.

## Retention (cleanup older than 30 days)

At the **start** of every run, before fetching feeds, prune old digests:

1. List the contents of `digests/` (e.g. via `Glob` on `digests/*.md`).
2. For each filename, parse the leading `YYYY-MM-DD` date prefix.
3. If that date is **more than 30 days before today**, delete the file. Use today's date from the conversation context (treat the cutoff as `today − 30 days`, inclusive — keep files dated exactly 30 days ago, delete anything older).
4. If a filename does not start with `YYYY-MM-DD`, skip it (don't delete anything you can't date-parse).
5. Print one line listing what was deleted (or "no digests older than 30 days") so the user can see what happened.

This keeps the `digests/` directory bounded without losing recent source-of-truth files that the IG post agent or the user might still want.

## Same-day merge

After step 4 (writing the digest), check for any **other** digest files in `digests/` whose filename starts with the same `YYYY-MM-DD` prefix as the just-written file, and merge them into a single file:

1. `Glob` `digests/*.md`. Filter to files whose `YYYY-MM-DD` matches the run's date. **Ignore subdirectories** — `digests/weekly/` and `digests/monthly/` are out of scope here.
2. If only one same-day file exists (the one just written), do nothing — print `no same-day merge needed`.
3. If multiple same-day files exist (e.g. a noon run and an evening incremental on the same date), merge:
   - **Target file:** the one with the **latest `HHMM`** in the filename (i.e. the file just written, in normal flow). Keep this filename.
   - **Window:** the merged window is `min(start) → max(end)` across the source files. Update the `*Window:*` header line accordingly.
   - **Mode line:** replace any single-run mode markers (e.g. `*Mode: incremental ...*`) with `*Mode: merged from <comma-separated source filenames>*`.
   - **Content:** take the **union of stories** across the source files. Dedupe by primary URL or near-identical headline; when two files cover the same story, keep the more recent / more developed framing and any additional source links from both. Prefer the section/category placement of the most recent file.
   - **Carryover blocks:** if the older file had a "Carryover X" pointer block (e.g. "see yesterday's digest for older items"), drop it — the older items are now inline in the merged file.
4. **Delete the older same-day file(s)**. Keep only the latest-`HHMM` file.
5. Print one line summarising the action, e.g. `Merged 2026-05-09_1200_tech-news.md into 2026-05-09_1800_tech-news.md; deleted 1 older same-day file.`

Invariant after this step: **at most one daily digest file per calendar date** in `digests/`.

This applies only to the daily-digest agent. The weekly and monthly agents are not expected to produce multiple files per day; if they ever do, handle that separately.

## Output Format (file contents)
```
# Tech News — Last 48 Hours
*Generated: <timestamp>*
*Window: <start> → <end>*

## <Category>
### <Headline>
<Summary>
**Source:** <Outlet> · [Read original](<URL>) · <Published>
```

## Source List (20 sources — prune as needed)

For each source: **Site URL** is the human-readable homepage; **Feed** is the RSS/Atom endpoint the agent should fetch first.

### General / Industry
1. **The Verge** — Site: https://www.theverge.com · Feed: https://www.theverge.com/rss/index.xml
2. **Ars Technica** — Site: https://arstechnica.com · Feed: https://feeds.arstechnica.com/arstechnica/index
3. **TechCrunch** — Site: https://techcrunch.com · Feed: https://techcrunch.com/feed/
4. **Wired** — Site: https://www.wired.com · Feed: https://www.wired.com/feed/rss
5. **Engadget** — Site: https://www.engadget.com · Feed: https://www.engadget.com/rss.xml
6. **CNET** — Site: https://www.cnet.com · Feed: https://www.cnet.com/rss/news/
7. **Reuters Technology** — Site: https://www.reuters.com/technology/ · Feed: https://www.reutersagency.com/feed/?best-topics=tech&post_type=best
8. **Bloomberg Technology** — Site: https://www.bloomberg.com/technology · Feed: *(no public RSS — fall back to homepage; paywalled)*
9. **The Information** — Site: https://www.theinformation.com · Feed: *(paywalled, no public RSS — homepage only)*
10. **Financial Times — Tech** — Site: https://www.ft.com/technology · Feed: https://www.ft.com/technology?format=rss *(paywalled bodies; headlines OK)*

### Developer / Deep-Tech / Aggregators
11. **Hacker News** — Site: https://news.ycombinator.com · Feed: https://news.ycombinator.com/rss
12. **Lobsters** — Site: https://lobste.rs · Feed: https://lobste.rs/rss
13. **The Register** — Site: https://www.theregister.com · Feed: https://www.theregister.com/headlines.atom
14. **MIT Technology Review** — Site: https://www.technologyreview.com · Feed: https://www.technologyreview.com/feed/
15. **IEEE Spectrum** — Site: https://spectrum.ieee.org · Feed: https://spectrum.ieee.org/feeds/feed.rss

### AI / Specialist
16. **VentureBeat (AI)** — Site: https://venturebeat.com/category/ai/ · Feed: https://venturebeat.com/category/ai/feed/
17. **Import AI (Jack Clark)** — Site: https://importai.substack.com · Feed: https://importai.substack.com/feed

### Security
18. **Krebs on Security** — Site: https://krebsonsecurity.com · Feed: https://krebsonsecurity.com/feed/
19. **BleepingComputer** — Site: https://www.bleepingcomputer.com · Feed: https://www.bleepingcomputer.com/feed/

### Hardware / Consumer
20. **Tom's Hardware** *(replaced AnandTech, which stopped publishing in 2024)* — Site: https://www.tomshardware.com · Feed: https://www.tomshardware.com/feeds/all

## Notes for the Agent
- Always include direct article URLs, not homepage links.
- Honor publishers' paywalls — summarize from publicly visible content; don't fabricate paywalled details.
- If a source returns nothing fresh in the last 48 hours, omit it silently rather than padding output.
- If fewer than ~5 stories total are found, expand the window to 72 hours and label the digest accordingly.
- If a feed fails, retry once on the homepage URL before giving up. Note any source that produced zero usable items in a "Notes" section at the bottom of the digest, so the user can prune dead feeds.
- Be terse. The reader wants signal, not commentary.
