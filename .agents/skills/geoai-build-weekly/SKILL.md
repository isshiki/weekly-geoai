---
name: geoai-build-weekly
description: Build the Friday Weekly GeoAI draft from Monday-through-Thursday daily notes, then verify linked sources and write concise Japanese introductions. Use when the user asks to compile, draft, or summarize this week's issue.
---

# Build a Weekly GeoAI issue

Work from the repository root.

1. Read `editorial/writing-guide.md` and `editorial/weekly-template.md` before editing.
2. Run `python scripts/build_weekly.py --date YYYY-MM-DD`, using the requested Friday. If no date was given, use the current or next Friday. The script assigns the next issue number unless the user explicitly supplies one.
3. For every item in the new `drafts/YYYY-MM-DD.md`, open the actual linked source. Replace `タイトル要確認` with the verified title and replace the introduction placeholder with one or two concrete Japanese sentences in だ・である調.
4. Use source notes only to understand the user's selection intent. Do not silently convert them into claims. If a source cannot be checked, leave a clear `要確認` marker and report it instead of inferring details.
5. Re-read the finished draft against the writing guide. Leave both editorial-commentary placeholders unchanged for the user.

This skill creates a draft only. Never run `scripts/publish_issue.py`, create Substack HTML, or modify `docs/issues/` without a later explicit request to publish after user review.
