---
name: geoai-build-weekly
description: Review the previous Friday-through-Thursday daily notes, propose candidates and commentary angles, then build the approved Friday Weekly GeoAI Markdown draft. Use when the user asks what should go in this week's issue, requests a Thursday review, or asks to compile the issue.
---

# Build a Weekly GeoAI issue

Work from the repository root.

1. Read `editorial/writing-guide.md` and `editorial/weekly-template.md` before editing.
2. Collect entries from the previous Friday through Thursday from `daily/`. Open every candidate source again; use the Atlas pages as context, not as a substitute for checking the source.

## Stage 1: Thursday review

3. Before creating a draft, present a compact proposal containing candidate items, a recommended selection and order, possible groupings, and two or three concrete angles for the writer's two commentary paragraphs.
4. Wait for the user's selection and comments when that choice would change the issue. Do not mark an item as selected merely because it appeared in a daily note.

## Stage 2: Markdown draft

5. After the selection is known, run `python scripts/build_weekly.py --date YYYY-MM-DD`, using the requested Friday. If no date was given, use the current or next Friday. The script assigns the next issue number unless the user explicitly supplies one. Remove unselected items from the generated draft.
6. Replace `タイトル要確認` with each verified title and replace every introduction placeholder with one or two concrete Japanese sentences in だ・である調.
7. Use daily comments only to understand selection intent. Do not silently convert them into factual claims. If a source cannot be checked, leave a clear `要確認` marker and report it instead of inferring details.
8. Incorporate the user's commentary when supplied. Otherwise leave both commentary placeholders unchanged. Re-read the result against the writing guide and report the Markdown path.

This skill creates a Markdown draft only. Never run `scripts/publish_issue.py`, create Substack HTML, or publish without a later explicit request after user review.
