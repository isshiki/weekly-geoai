---
name: geoai-save-daily
description: Save URLs shared for Weekly GeoAI as today's public daily notes, including an optional user comment. Use when the user says a URL is interesting, asks to save it for the newsletter, or calls it 今日の気になったもの.
---

# Save a Weekly GeoAI daily note

Work from the repository root.

1. Read `editorial/writing-guide.md`, especially the public-scope rule for daily notes.
2. Preserve each URL exactly. Preserve an attached user comment unless it appears to contain a secret, personal data, internal information, or other material unsuitable for a public repository; in that case, do not write it and ask for publishable wording. Saving only the URL remains valid.
3. Run `python scripts/capture_daily.py "<url>"` once per URL. Add `--note "<comment>"` only for the comment associated with that URL. Add `--title` only when the title is known from reliable context; do not invent it.
4. Report the date-based file updated and whether any URL was already present.

Do not summarize, rank, publish, or move the URL into a weekly issue during this workflow.
