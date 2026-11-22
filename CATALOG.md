# The F-round Mega-Catalog

**Current count (November 22, 2026): 4,169 unique GitHub repositories.**

- [Single CSV master — data/F_ROUND_MASTER_4100.csv](data/F_ROUND_MASTER_4100.csv): **4,169 rows × 21 columns**, every row carrying GitHub's own metadata (description, topics, language, licence ID, stars, forks, dates, archive and fork flags) fetched November 22, 2026. Opens in Excel, Google Sheets and LibreOffice. This is the recommended starting point.
- [Batch 1](data/discovery_batch_01.csv): 1,598 unique hits from 16 targeted searches, 18 columns.
- [Batch 2](data/discovery_batch_02.csv): 1,399 additional unique hits from 14 unrelated searches, 18 columns.
- [Batch 3](data/discovery_batch_03.csv): 1,013 additional unique hits from 12 more searches, 18 columns.
- [ATLAS.md](ATLAS.md): 120 projects whose high-level description was inspected at a human-readable level.
- [GitHub metadata for 120 scouted projects](data/SCOUTED_METADATA_120.csv): real repo descriptions, GitHub-reported license IDs, stars, primary language, archive flag, size and last push; fetched November 22, 2026.
- [Original search query manifest](data/SEARCH_QUERIES.csv): all 42 GitHub discovery queries and their speculative research prompts.
- [BACK_ALLEYS.md](BACK_ALLEYS.md): 94 extra early leads, of which 72 were not already present in the 4,010-search-hit collection or the 120 scouted projects.

The **single master** deduplicates by case-insensitive `owner/repository`, yielding **4,169 = 4,010 GitHub search hits + 87 additional atlas projects + 72 extra leads**. The 120 scouted projects overlap the search sweep, so evidence tiers in the master are: **120 SCOUTED, 3,977 SEARCH, 72 LEAD**.

The collection covers **63 named topic shelves**. This is broad discovery, not proof of code quality, actual function, project maintenance, or license eligibility.

## What the master columns mean

| Column | Meaning |
|---|---|
| Repo | GitHub `owner/repository` returned by repository search or a previously checked repository |
| GitHub URL | Direct clickable source reference |
| Domain shelf | Search/query theme or previously scouted section; one primary shelf per repo |
| What it might do / stated purpose | **SCOUTED:** short summary from inspected repo overview. **SEARCH:** merely a hypothesis associated with the search theme, **not a verified project-specific description**. **LEAD:** blank |
| Collide with (idea) | An imaginative *other* field; **not an existing integration** |
| Potential artifact (idea) | Pure brainstorming; not a project deliverable promised by the repository |
| GitHub description | The repository's own one-line description, verbatim from GitHub, for every tier. Blank for the 455 repos that have none. Written by the maintainer, not checked against the code |
| Topics | The maintainer's GitHub topic tags (up to 12, `; `-separated). Present on 1,368 repos |
| Primary language | GitHub's detected main language; blank when none is detected |
| Stars / Forks | GitHub counts at fetch time. Popularity is not a selection criterion |
| Created / Last push | Dates from GitHub (`YYYY-MM-DD`) |
| Fork? | `true` when the repository is itself a fork of another project (212 rows) |
| Homepage | The project's own website link, when the maintainer set one |
| Metadata checked | Date the GitHub metadata in this row was fetched |
| License (verify) | GitHub-reported license ID for every row. `NO_LICENSE_DETECTED` and `NOASSERTION` are not reuse grants. GitHub's public visibility alone doesn't grant reuse rights |
| Archived? | Value from repo metadata when present; `Unknown` for some older leads |
| Repository size KB | GitHub-reported repository size from search metadata, not build size or code quality |
| Evidence tier | `SCOUTED` / `SEARCH` / `LEAD` as defined below |
| Your notes | Blank user-editable column: hypotheses, surprise, partial tests, license notes, failures |

The original batches contain additional `Search Query`, `Default branch`, and `GitHub repository ID` fields, useful for tracing what search produced a lead.

## Evidence tiers

- **SCOUTED (120):** Repository exists; its stated purpose was inspected, and GitHub license, stars, push date and other metadata were retrieved separately. This does **not** constitute a source-code audit, a run, or an integration.
- **SEARCH (3,977):** Repository was returned by GitHub repository search. Its URL and search category are grounded, and GitHub metadata (description, licence ID, language, activity) has been fetched, but nobody has inspected the project: actual function, quality and usability are not yet verified.
- **LEAD (72):** Previously collected secondary names with GitHub links, not promoted through this research pass.

The spreadsheet intentionally includes junk, unfinished student code, unusual interfaces, old science scripts and niche single-author work. Some entries may be forks, derivative implementations, or typo-prone projects. That is part of the discovery bias, but source provenance is never optional.

## The important distinction: topics vs transformations

A category like `biology` or `synthesizers` makes discovery easier. A transformation like `event → tone` or `image → stitch path` makes **combinations** possible.

When you become interested in a repository, add an experiment note with a proposed input type, output type, data rights, and the tiniest standalone proof. Then move it to the original [ATLAS.md](ATLAS.md) or a new experiment folder.

Use the [interactive offline collision browser](index.html) to pick entries, pin interesting parts and reroll others. It contains a compact embedded snapshot of all 4,169 repos so it works without a hosted API.

## Data safety and reproducibility

- Never run downloaded scripts as privileged code without examining them and their dependencies; public repos are untrusted.
- **Do not treat AI-created descriptions as verified facts.** In the 3,977 SEARCH rows, `What it might do / stated purpose` is intentionally generic research-angle text; the `GitHub description` column is the maintainer's own wording.
- A GitHub-reported license ID is a signal, not an audit. `NO_LICENSE_DETECTED` and `NOASSERTION` are not open-source licenses. Verify code, model, dataset, image, and audio terms separately.
- Date of catalog assembly: **2026-11-22**. Re-check project state before investing meaningful work.
- Historical and scientific datasets may contain errors; preserve citations, uncertainty and the distinction between data and speculative artwork.

This file describes a deliberately enormous *candidate catalog*, not a tested dependency list.

## License metadata

Across **all 4,169** rows, GitHub reports: **MIT 1,006, GPL-3.0 428, Apache-2.0 173, BSD-3-Clause 76, GPL-2.0 60, CC0-1.0 44, AGPL-3.0 35, LGPL-3.0 24, MPL-2.0 19, Unlicense 18, BSD-2-Clause 13, LGPL-2.1 10**, 30 rows across 13 rarer IDs, **NO_LICENSE_DETECTED 1,969** and **NOASSERTION 264**. So roughly 46% of the catalogue has a recognised licence ID and 54% does not. 123 repos are archived and 884 were last pushed before 2020.

For the **120** scouted entries, the GitHub repository metadata reports: **MIT 39, GPL-3.0 17, Apache-2.0 5, BSD-3-Clause 4, AGPL-3.0 3, MPL-2.0 1, BSD-2-Clause 1, GPL-2.0 1, NO_LICENSE_DETECTED 37, NOASSERTION 12**. This is a *snapshot of GitHub metadata*, not a legal opinion or a complete per-file/model/asset license audit. The same caveat applies to the full-catalogue figures above.
