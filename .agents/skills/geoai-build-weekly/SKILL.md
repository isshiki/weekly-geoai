---
name: geoai-build-weekly
description: Review the previous Friday-through-Thursday daily notes, propose candidates and commentary angles, then build the approved Friday Weekly GeoAI Markdown draft. Use when the user asks what should go in this week's issue, requests a Thursday review, or asks to compile the issue.
---

# Build a Weekly GeoAI issue

Work from the repository root.

1. Read `editorial/writing-guide.md`, `editorial/weekly-template.md`, and `editorial/substack-handoff.md` before editing. From the 2026-10-16 issue, use the approved news-first format: three lead news items, three to five briefs, and optionally one map. Prioritize concrete announcements and their significance over tutorials; keep the general-developer audience. Select zero to two useful images with verified reuse permission or original explanatory artwork.
2. Collect entries from the previous Friday through Thursday from `daily/`. Open every candidate source again; use the Atlas pages as context, not as a substitute for checking the source.

## Stage 1: Thursday review

3. Before creating a draft, present a compact proposal containing candidate items, a recommended selection and order, possible groupings, and two or three concrete angles for the writer's two commentary paragraphs.
4. Wait for the user's selection and comments when that choice would change the issue. Do not mark an item as selected merely because it appeared in a daily note.

## Stage 2: Markdown draft

5. After the selection is known, run `python scripts/build_weekly.py --date YYYY-MM-DD`, using the requested Friday. If no date was given, use the current or next Friday. The script assigns the next issue number unless the user explicitly supplies one. Remove unselected items from the generated draft.
6. Keep `editorial_format: news-v1`, remove unselected candidates, and group the items under 今週の注目ニュース, 短報, and optionally 今週の地図. Use consecutive linked headings. Replace title and introduction placeholders with verified news: lead items have two to six sentences; briefs and maps have one or two. Use です・ます調 for news. Give the subtitle concrete announcements, not a slogan. Save local images under drafts/assets/YYYY-MM-DD with alt text and separate italic captions; record sources and reuse conditions in editorial notes. See substack-handoff.md for the supported syntax.
7. Use daily comments only to understand selection intent. Do not silently convert them into factual claims. If a source cannot be checked, leave a clear `要確認` marker and report it instead of inferring details.
8. Incorporate the user's commentary when supplied. Otherwise leave both commentary placeholders unchanged. Re-read the result against the writing guide and report the Markdown path.

This skill creates a Markdown draft only. Never run `scripts/publish_issue.py`, create Substack HTML, or publish without a later explicit request after user review.
