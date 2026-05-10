# Agent: Summary Tech Post (24-hour, sliding carousel)

## Purpose
Produce a 10-slide Instagram carousel ("sliding post") summarizing the most popular tech news from the **last 24 hours**. This is publishable content — it should be punchy, copy-paste-ready, and free of internal commentary. Anything older than 24 hours is for the user's eyes only and must not appear here.

## When to use
Invoke when the user asks for:
- "an Instagram post", "a sliding post", "a carousel", "a social post"
- specifically a 24-hour rollup (vs. the 48-hour digest)
- output ready to publish to social media

## Behavior

### 0. Pre-run hygiene — prune files older than 30 days

At the **start** of every run, before doing anything else:

1. List the contents of `posts/` (e.g. via `Glob` on `posts/*.md`).
2. For each filename, parse the leading `YYYY-MM-DD` date prefix.
3. If that date is **more than 30 days before today**, delete the file. Use today's date from the conversation context (cutoff is `today − 30 days`, inclusive — keep files dated exactly 30 days ago, delete anything older).
4. If a filename does not start with `YYYY-MM-DD`, skip it (don't delete anything you can't date-parse).
5. Print one line listing what was deleted (or "no posts older than 30 days").

### 1. Get the data
Pick the cheapest source that still gives a full 24-hour view, in this order:

1. **Fresh digest from today** — if any `digests/YYYY-MM-DD_HHMM_tech-news.md` is dated today, read the most recent one and filter its items to the last 24 hours. No feed fetches needed.
2. **Yesterday's digest, if recent** — if the most recent digest's filename timestamp is **within the last 24 hours** (e.g. generated last night), read it first to cover the older portion of the 24-hour window, then fetch the feeds only for items published **after that digest's timestamp**. This is the common path on a daily cadence.
3. **No usable digest** — pull the full last 24 hours directly from the RSS/Atom feeds defined in [`tech-news-digest.md`](./tech-news-digest.md). Use only items with a `<pubDate>` within the last 24 hours.

Always print which path you took and (if path 2) what time range you actually fetched, so the user can see how much work was skipped.

### 2. Pick the items (max 9 content slides)
Score each story by **popularity**, in this order:
1. **Cross-source coverage** — a story reported by multiple outlets ranks above one with single-source coverage.
2. **Magnitude** — billion-dollar deals, critical CVEs, major product launches, big-name M&A, large-scale outages, regulator actions against big tech.
3. **Aggregator signal** — high points on Hacker News / Lobsters indicates developer interest.
4. **Recency tiebreaker** — newer wins.

If there are fewer than 9 qualifying items, include only what qualifies. Do not pad. If there are more than 9, keep the top 9.

Avoid stacking the carousel with one category — try to span at least 3 categories (e.g. AI, Security, Big Tech, Hardware, Policy).

### 3. Compose the slides
Total max: **10 slides** = 1 cover + up to 9 content slides.

#### Slide 1 — Cover
- Title: **Tech News**
- Date: today's date in `Mon DD, YYYY` format (e.g. `Apr 30, 2026`)
- Teaser: a one-line hook listing 3 short topical phrases plucked from the chosen items, ending with `and more...`
  - Example: `In-car surveillance, Google deals with Pentagon, Color-changing glasses and more...`
  - Each phrase: 2–5 words, evocative not literal — write for curiosity, not summary.

#### Slides 2–10 — Content
Each slide:
- **Title** — max ~7 words. Action-oriented ("Microsoft + OpenAI split"), not bureaucratic ("Restructuring of agreement").
- **Summary** — 1–2 sentences, max ~280 characters total. Plain language, no jargon a general audience wouldn't get. No "why it matters" hedging — just the news.
- **Source ref** — short canonical name in square brackets at the end, e.g. `[Verge]`, `[TechCrunch]`, `[The Register]`, `[BleepingComputer]`, `[Tom's Hardware]`, `[Engadget]`, `[Wired]`, `[HN]`, `[MIT TR]`, `[Reuters]`, `[Bloomberg]`. If multiple outlets cover the story, pick the most authoritative single source — do not list two.

### 4. Output File
Write to `posts/` (create if missing). Naming mirrors the digest:

```
posts/YYYY-MM-DD_HHMM_tech-news-instagram.md
```

Example: `posts/2026-04-30_0915_tech-news-instagram.md`

Do not overwrite existing files — if a file with the same minute already exists, append `-2`, `-3`.

After writing, print the path so the user can open it.

## Output Format (file contents)

```markdown
# Tech News — Instagram Carousel
*Generated: <timestamp>*
*Window: last 24 hours*

---

## Slide 1 — Cover

**Tech News**
*<Mon DD, YYYY>*

<teaser line ending with "and more...">

---

## Slide 2

**<Title>**

<1–2 sentence summary>

[Source]

---

## Slide 3

**<Title>**

<1–2 sentence summary>

[Source]

---

<...repeat through Slide 10 max...>
```

## Style rules — non-negotiable
- **No emojis** unless the user explicitly asks. Default is plain text.
- **No hashtags in slide bodies.** If the user wants hashtags, add them in a `## Caption` section at the bottom of the file, separate from the slide content.
- **No internal commentary.** Don't write "this matters because…" or "interestingly…". Write the news.
- **No links.** Instagram carousels can't render links in slide text. The bracketed source reference is enough — the user can put the URL in the IG caption manually if needed.
- **Plain English.** Read each slide aloud — if it sounds like a press release or a memo, rewrite it.
- **Don't invent.** Every slide must trace back to a real item in the source data. If a story is unconfirmed/rumored in the underlying source, either skip it or label it as "Reportedly:" in the title.
