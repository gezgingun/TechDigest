# Agent: Monthly Tech News Digest (30-day rollup)

## Purpose
Aggregate the past **30 days** of tech news from existing daily digests in `digests/` (and weekly digests in `digests/weekly/` when available). **No internet fetching.** Pulls only from files Claude has already produced. **For the user's eyes only.**

## When to use
Invoke when the user asks for:
- "monthly digest", "monthly tech news", "this month in tech"
- "month in review", "last month's tech news"
- a 30-day rollup distinct from the daily and weekly digests

## Behavior

### 0. Pre-run hygiene — prune monthly digests older than 365 days
At the **start** of every run, before doing anything else:

1. List the contents of `digests/monthly/` (e.g. via `Glob` on `digests/monthly/*.md`).
2. For each filename, parse the leading `YYYY-MM-DD` date prefix.
3. If that date is **more than 365 days before today**, delete the file. Cutoff is `today − 365 days`, inclusive.
4. If a filename does not start with `YYYY-MM-DD`, skip it.
5. Print one line listing what was deleted (or "no monthly digests older than 365 days").

### 1. Gather source files — local files only, no internet
1. List `digests/*.md` (daily files at the flat level).
2. List `digests/weekly/*.md` (weekly rollups if any exist).
3. Parse the leading `YYYY-MM-DD` from each filename and keep files dated within the **last 30 days** (today − 30 days, inclusive).
4. **Source-selection rule:**
   - For each fully-covered 7-day stretch in the window, prefer the corresponding **weekly digest** if one exists (it's already deduped).
   - For days not covered by a weekly, fall back to the **daily digests** for that span.
   - If no weekly digests exist in the window at all, just consume all in-window daily digests.
5. Read each chosen file.
6. **Do NOT call `WebFetch`, `WebSearch`, or fetch any RSS feeds.**

If no daily or weekly digests exist within the window, print "No digests in the last 30 days — generate a daily or weekly digest first" and stop.

### 2. Aggregate and dedupe across the month
- **Dedupe** stories that span multiple files. Keep the most authoritative source and the most up-to-date framing.
- **Compress timelines.** A story that has more than ~3 beats can collapse to "evolved over <date range>: <one-line arc>" rather than a full per-day list. Reserve full timelines for the month's biggest stories (top ~10).
- **Drop chatter.** If a story showed up once in a daily digest and went nowhere, omit it unless it's notable for the month overall.
- **Group by category** (AI, Security, Hardware, Cloud/Infra, Big Tech, Policy, Funding, Open Source, Science).

### 3. Lead with two synthesis sections
1. **Month at a Glance** — 5–8 bullets capturing the month's dominant narratives. One sentence each.
2. **Top 10 Stories of the Month** — a numbered list of the single most consequential items, each with a one-line rationale ("why this matters more than the rest").

Then the categorized story list.

### 4. Output File
Write to `digests/monthly/` (create if missing). Filename:
```
digests/monthly/YYYY-MM-DD_HHMM_tech-news-monthly.md
```
Example: `digests/monthly/2026-05-09_1845_tech-news-monthly.md`

Use 24-hour local time. Do not overwrite — append `-2`, `-3` if the same minute exists. After writing, print the path.

## Output Format
```markdown
# Tech News — Monthly Rollup
*Generated: <timestamp>*
*Window: <YYYY-MM-DD> → <YYYY-MM-DD>*
*Sources: <list of daily and/or weekly digest filenames consumed>*

## Month at a Glance
- <theme 1>
- <theme 2>
...

## Top 10 Stories of the Month
1. **<Headline>** — <one-line why this matters most>
2. ...

## <Category>

### <Headline>
<aggregated summary, 2–4 sentences>

**Source:** <Outlet> · [Read original](<URL>) · <published>

*Arc:* <YYYY-MM-DD> → <YYYY-MM-DD>: <one-line arc summary>
```

## Notes for the Agent
- The monthly is **synthesis, not catalog.** Resist re-listing every story. Reach for the top ~30–50 items the user actually wants to remember a month from now.
- Prefer weekly digests when both daily and weekly cover the same span — weeklies have already done the cross-day dedupe work.
- If a story is still active at the time of the monthly run, label its status clearly ("ongoing", "unresolved as of <date>").
- This agent is **read-only against the local file system** plus file deletions for retention. No `WebFetch`, no `WebSearch`.
