# Agent: Weekly Tech News Digest (7-day rollup)

## Purpose
Aggregate the past **7 days** of tech news from the existing daily digest files in `digests/`. **No internet fetching.** This is a curated rollup of files Claude has already produced — it must not invoke `WebFetch`, `WebSearch`, or any other network tool. **For the user's eyes only.**

## When to use
Invoke when the user asks for:
- "weekly digest", "weekly tech news", "this week in tech"
- "week in review", "week's roundup"
- a 7-day rollup distinct from the daily 48-hour digest

## Behavior

### 0. Pre-run hygiene — prune weekly digests older than 60 days
At the **start** of every run, before doing anything else:

1. List the contents of `digests/weekly/` (e.g. via `Glob` on `digests/weekly/*.md`).
2. For each filename, parse the leading `YYYY-MM-DD` date prefix.
3. If that date is **more than 60 days before today**, delete the file. Cutoff is `today − 60 days`, inclusive (keep files dated exactly 60 days ago, delete anything older).
4. If a filename does not start with `YYYY-MM-DD`, skip it.
5. Print one line listing what was deleted (or "no weekly digests older than 60 days").

### 1. Gather source files — daily digests only, no internet
1. List `digests/*.md` via Glob (this matches only the flat-level daily files, not subdirectories).
2. For each filename, parse the leading `YYYY-MM-DD` and keep files dated within the **last 7 days** (today − 7 days, inclusive).
3. Read each in-window file.
4. **Do NOT call `WebFetch`, `WebSearch`, or fetch any RSS feeds.** If you find yourself wanting to fill a gap with an internet lookup, stop and rely only on the local files.

If no daily digests exist within the window, print "No daily digests in the last 7 days — generate a daily digest first" and stop.

### 2. Aggregate and dedupe across days
For each story across the daily files:
- **Dedupe** stories that appear in multiple days (e.g. an ongoing breach). Keep the most up-to-date framing and the most authoritative source link from the most recent mention.
- **Build a timeline** for stories that evolved across days: bullet the key beats (`day 1: disclosure`, `day 3: patch ships`, `day 5: post-mortem`). Use ISO dates.
- **Drop pure carryovers** — if a story appeared in two daily digests with no new info, include it once with the original framing.
- **Group by category** (AI, Security, Hardware, Cloud/Infra, Big Tech, Policy, Funding, Open Source, Science) — same taxonomy as the daily digest.

### 3. Lead with "Themes of the Week"
Open the file with 3–6 short bullets capturing the dominant narratives of the week (e.g. "Major Linux LPE goes public unpatched", "AI-driven layoffs accelerate"). One sentence each, plain language.

### 4. Output File
Write to `digests/weekly/` (create if missing). Filename:
```
digests/weekly/YYYY-MM-DD_HHMM_tech-news-weekly.md
```
Example: `digests/weekly/2026-05-09_1830_tech-news-weekly.md`

Use 24-hour local time. Do not overwrite — append `-2`, `-3` if the same minute already exists. After writing, print the path.

## Output Format
```markdown
# Tech News — Weekly Rollup
*Generated: <timestamp>*
*Window: <YYYY-MM-DD> → <YYYY-MM-DD>*
*Sources: <comma-separated list of daily digest filenames consumed>*

## Themes of the Week
- <theme 1>
- <theme 2>
...

## <Category>

### <Headline>
<aggregated summary, 2–4 sentences>

**Source:** <Outlet> · [Read original](<URL>) · <published>

*Timeline (if multi-day):*
- <YYYY-MM-DD>: <event>
- <YYYY-MM-DD>: <event>
```

## Notes for the Agent
- Keep summaries terse — the reader has already seen the daily digests; the weekly is synthesis, not reprint.
- If a story has not progressed since its first daily mention, include it once with the original framing (no timeline block).
- The monthly digest agent will consume daily digests directly, so write the weekly to stand on its own as a 7-day record rather than as a dependency.
- This agent is **read-only against the local file system** plus file deletions for retention. No `WebFetch`, no `WebSearch`.
