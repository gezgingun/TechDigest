# SocialWork — Tech News Agents

This project hosts a set of agents that pull tech news from a shared list of credible sources and turn it into different deliverables. The default agent (this file) is a router — pick the right sub-agent based on what the user asks for, and follow that file's instructions.

## Available agents

| Agent | File | Output | Window | Audience |
|---|---|---|---|---|
| Tech News Digest | [agents/tech-news-digest.md](agents/tech-news-digest.md) | `digests/YYYY-MM-DD_HHMM_tech-news.md` | last 48 hours | user only |
| Instagram Tech Post | [agents/instagram-tech-post.md](agents/instagram-tech-post.md) | `posts/YYYY-MM-DD_HHMM_tech-news-instagram.md` | last 24 hours | publishable |

## Routing

Pick based on what the user asks for:

- **"digest", "tech news roundup", "what's happening in tech", "summary with links"** → use **Tech News Digest** ([agents/tech-news-digest.md](agents/tech-news-digest.md)).
- **"Instagram post", "carousel", "sliding post", "social post"** → use **Instagram Tech Post** ([agents/instagram-tech-post.md](agents/instagram-tech-post.md)).
- **Ambiguous** ("give me the news") → ask the user which one they want before running. Don't guess — the digest is long and private; the IG post is short and publishable.

When you invoke a sub-agent, **read its file first** and follow its instructions verbatim. Do not paraphrase its rules — re-read them each time so behavior stays consistent across runs.

## Shared conventions

- **Source list of truth:** the 20 sources and their RSS feeds live in [agents/tech-news-digest.md](agents/tech-news-digest.md). The Instagram agent pulls from the same list (and may reuse a recent digest if one exists).
- **Filenames sort chronologically:** all output files start with `YYYY-MM-DD_HHMM` so directory listings are time-ordered.
- **Never overwrite output files.** If a file exists for the same minute, append `-2`, `-3`, etc.
- **Print the output path** after writing, so the user can open it.

## Pipeline option (when both are wanted)

If the user wants both deliverables in one run, do them in order:
1. Run **Tech News Digest** first → produces `digests/<timestamp>_tech-news.md`.
2. Run **Instagram Tech Post** second → it will pick up the fresh digest from step 1 and filter to the last 24 hours, avoiding redundant feed fetches.
