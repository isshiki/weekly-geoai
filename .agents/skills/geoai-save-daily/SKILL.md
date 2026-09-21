---
name: geoai-save-daily
description: Verify and organize URLs shared for Weekly GeoAI into a public daily log, the GeoAI Atlas, and its dated update record. Use when the user shares one or more interesting links, asks to save news checks, or calls them 今日の気になったもの.
---

# Organize a Weekly GeoAI daily batch

Work from the repository root.

1. Read `editorial/writing-guide.md`, `editorial/atlas-guide.md`, `editorial/atlas-visual-guide.md`, and `editorial/atlas-entry-template.md`.
2. Treat pasted summaries as leads, not source text. Open each URL and verify its canonical URL, title, publisher, date, and the facts needed for a short public summary. Remove tracking parameters only after confirming that the canonical page resolves correctly.
3. Do not store the raw conversation or pasted summary. Preserve an attached user comment only when it is public-safe and useful as selection intent. If it contains a secret, personal data, internal information, or unpublished evaluation, omit it and ask for publishable wording; saving without a comment remains valid.
4. Choose one primary Atlas category from the guide. Update an existing page when the topic already exists; otherwise create a minimal page from the template. Do not create a durable page for a purely transient item with no reusable knowledge.
5. Run `python scripts/capture_daily.py "<url>"` once per URL. Supply the verified `--title`, `--kind`, `--topics`, `--summary`, and `--atlas-path` when available. Use `--note` only for the user's public-safe comment.
6. Create or update `docs/updates/YYYY-MM-DD.md` with links to the Atlas page and source. Add any new page to `docs/atlas/index.md` so it is discoverable.
7. For every new or updated Atlas page, apply `editorial/atlas-visual-guide.md`. Decide whether a visual materially improves understanding. Reuse an authorized figure or create a deterministic SVG, map, or chart when appropriate; otherwise record that no visual is needed. For generative illustration, provide a prompt unless the user explicitly asked for image generation.
8. When replacing or removing a visual, verify all references before deleting an unused generated asset. Preserve user-provided source material and assets used elsewhere.
9. Before committing, run `.venv/Scripts/python.exe scripts/sync_update_history.py --date YYYY-MM-DD --base HEAD` using the date of the daily log. This generates the Atlas-only review links with text fragments and synchronizes the year/month history indexes and navigation. If the day's Atlas changes have already been committed, use `--base <commit-before-those-changes>` instead; when extending the same day's batch, include the earlier changes in that comparison. Do not regenerate a committed day's links against an unchanged HEAD, which would erase its change list. Reserve `--backfill` for missing historical link lists.
10. Verify the generated `変更したAtlasページ` section against the actual Atlas edits: one link per changed page, no external sources, and fragment text matching the rendered target page. Preserve existing daily URLs and use the label `更新履歴` with year/month/day navigation. Run `.venv/Scripts/python.exe -m mkdocs build --strict` and the repository's public-content check before committing. Follow `editorial/atlas-guide.md` for the standing commit, push, and site-deployment workflow.
11. Report the files changed, duplicates skipped, sources that could not be verified, and the visual decision for each affected Atlas page.

Do not rank items, create a weekly issue, generate Substack HTML, or distribute the newsletter during this workflow. Site deployment follows the repository guide and the user’s authorization. Do not add a visual merely to decorate a page.
