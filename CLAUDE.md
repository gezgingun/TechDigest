# SocialWork — Tech News Agents

This project hosts a set of agents that pull tech news from a shared list of credible sources and turn it into different deliverables. The default agent (this file) is a router — pick the right sub-agent based on what the user asks for, and follow that file's instructions.

## Available agents

| Agent | File | Output | Window | Source | Retention | Audience |
|---|---|---|---|---|---|---|
| Tech News Digest (daily) | [agents/tech-news-digest.md](agents/tech-news-digest.md) | `digests/YYYY-MM-DD_HHMM_tech-news.md` | last 48 hours | RSS feeds | 30 days | user only |
| Weekly Tech Digest | [agents/weekly-digest.md](agents/weekly-digest.md) | `digests/weekly/YYYY-MM-DD_HHMM_tech-news-weekly.md` | last 7 days | local daily digests | 60 days | user only |
| Monthly Tech Digest | [agents/monthly-digest.md](agents/monthly-digest.md) | `digests/monthly/YYYY-MM-DD_HHMM_tech-news-monthly.md` | last 30 days | local daily + weekly digests | 365 days | user only |
| Summary Tech Post (Instagram carousel) | [agents/summary-tech-post.md](agents/summary-tech-post.md) | `posts/YYYY-MM-DD_HHMM_tech-news-instagram.md` | last 24 hours | RSS feeds (or fresh daily digest) | 30 days | publishable |

## Routing

Pick based on what the user asks for:

- **"digest", "daily digest", "tech news roundup", "what's happening in tech", "summary with links"** → use **Tech News Digest** ([agents/tech-news-digest.md](agents/tech-news-digest.md)).
- **"weekly digest", "week in review", "this week in tech", "week's roundup"** → use **Weekly Tech Digest** ([agents/weekly-digest.md](agents/weekly-digest.md)).
- **"monthly digest", "month in review", "last month's tech news", "this month in tech"** → use **Monthly Tech Digest** ([agents/monthly-digest.md](agents/monthly-digest.md)).
- **"Instagram post", "carousel", "sliding post", "social post", "summary post"** → use **Summary Tech Post** ([agents/summary-tech-post.md](agents/summary-tech-post.md)).
- **Ambiguous** ("give me the news") → ask the user which one they want before running. The digest variants are private and long; the IG post is short and publishable.

When you invoke a sub-agent, **read its file first** and follow its instructions verbatim. Do not paraphrase its rules — re-read them each time so behavior stays consistent across runs.

## Network policy by agent

- **Daily digest** and **IG post** are allowed to call `WebFetch` / `WebSearch` (they consume RSS feeds).
- **Weekly digest** and **monthly digest** are **read-only against the local file system**. They aggregate from existing files in `digests/` and must not call `WebFetch` / `WebSearch`. If those files are missing, ask the user to run a daily digest first.

## Shared conventions

- **Source list of truth:** the 20 RSS sources live in [agents/tech-news-digest.md](agents/tech-news-digest.md). The IG post agent pulls from the same list (or reuses a recent daily digest). The weekly and monthly agents only consume daily/weekly files locally.
- **Filenames sort chronologically:** all output files start with `YYYY-MM-DD_HHMM` so directory listings are time-ordered.
- **Never overwrite output files.** If a file exists for the same minute, append `-2`, `-3`, etc.
- **Print the output path** after writing, so the user can open it.
- **Subdirectories are reserved for rollups:** `digests/weekly/` and `digests/monthly/` only. Daily digests stay flat in `digests/` so the weekly agent's `Glob('digests/*.md')` picks them up cleanly without recursing.

## Pipeline option (when multiple are wanted)

Do them in order so each step can reuse the previous step's output:
1. **Daily digest** → `digests/<timestamp>_tech-news.md`.
2. **Weekly digest** (consumes daily digests in window) → `digests/weekly/<timestamp>_tech-news-weekly.md`.
3. **Monthly digest** (prefers weekly digests, falls back to daily) → `digests/monthly/<timestamp>_tech-news-monthly.md`.
4. **Summary Tech Post** (reuses fresh daily digest if present) → `posts/<timestamp>_tech-news-instagram.md`.
