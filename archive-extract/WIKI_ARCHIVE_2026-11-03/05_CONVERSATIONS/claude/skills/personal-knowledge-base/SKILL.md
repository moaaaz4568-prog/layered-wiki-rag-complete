---
name: personal-knowledge-base
description: Build and maintain a persistent personal knowledge base / second brain in Obsidian or plain markdown — an LLM-owned wiki that compounds across sessions. Ingest sources into pages, maintain cross-references, keep a synthesis current, lint for orphans and contradictions. Triggers "second brain", "Obsidian wiki", "knowledge graph", "personal knowledge management", "PKM", "research wiki", "ingest this paper/article/book into my notes", "compound knowledge", "Memex", "my notes are a mess", or whenever knowledge should accumulate instead of being re-derived by RAG on every query.
version: 1.1.0
metadata:
  source_members:
    - llm-wiki (Karpathy LLM Wiki pattern)
  domain: personal / knowledge-management
  consolidated_from: 1 member
  fixed_in_this_merge:
    - link resolver now matches frontmatter `title`, not just filename (was reporting every title-named wikilink as broken)
    - init_vault.py accepts --vault like every other tool (--path kept as deprecated alias)
---

# Personal Knowledge Base — a compounding second brain

Turn the agent into a disciplined **wiki maintainer**: sources are read once,
integrated into a persistent interlinked markdown vault, and kept current. The
knowledge is already there, cross-referenced and de-contradicted, when a query
arrives — instead of being re-synthesised from scratch every time.

> Obsidian is the IDE. The LLM is the programmer. The wiki is the codebase.

Inspired by Andrej Karpathy's LLM Wiki pattern.

## When to use

- **Long research** — a weeks-long dive on a topic: papers, articles, reports, an evolving thesis.
- **Book companion** — file chapters as you read; build pages for characters, themes, plot threads.
- **Personal** — goals, health, journaling, self-improvement, hobby deep-dives.
- **Team/business** — an internal wiki fed by Slack, meeting notes, and calls; the agent does the
  maintenance nobody else wants to.
- **Competitive analysis, due diligence, trip planning, course notes.**

## When NOT to use

- **One-shot Q&A over a fixed document** — that is RAG's job; there is nothing to compound.
- **You will not add sources over time** — the vault's value is proportional to ingests.
- **You want the answer in chat, not in a file** — see `memory-capture` instead (below).
- **A single durable fact about the user or the project** — that is auto-memory, not a wiki page.

## The split from `memory-capture` (read this first)

| `memory-capture` | this skill |
|---|---|
| Auto-memory: one fact per file, loaded into context each session | A vault: hundreds of interlinked pages, read on demand |
| Sentence-scale, always in context | Page-scale, only what you open |
| Use for "the user prefers Arabic replies" | Use for "everything I learned about mechanistic interpretability" |
| Index is a flat pointer list (`MEMORY.md`) | Index is a generated catalogue; a link graph over it |

They cooperate: a wiki page about the user's working style can produce a
`memory-capture` entry, and repeated `memory-capture` entries on one topic are a
signal that a wiki page is warranted. Do not store the same content in both —
pick by scale.

Other boundaries:
- `claude-memory-rules` — the promotion/curation *policy* for auto-memory; it governs the
  `memory-capture` side, not this vault.
- `memory-health-dashboard` — AgentHub multi-agent *session* status. Despite the word "memory",
  it has nothing to do with this skill.
- `llm-wiki` sub-agents (`wiki-ingestor`, `wiki-librarian`, `wiki-linter`) — the original plugin
  shipped these as separate agent definitions. Their procedures are folded into the Modes below
  and preserved in `references/`; if the plugin's agent definitions are installed, either may be
  used — they follow the same workflow.

## Architecture (three layers)

```
vault/
├── raw/                    # Layer 1 — IMMUTABLE source of truth
│   ├── <source files>      # Articles, papers, PDFs, images, data
│   └── assets/             # Downloaded images from clipped articles
├── wiki/                   # Layer 2 — LLM-owned knowledge base
│   ├── index.md            # Content catalog (regenerated every ingest)
│   ├── log.md              # Append-only timeline: ## [YYYY-MM-DD] <op> | <title>
│   ├── entities/           # Person / Org / Place pages
│   ├── concepts/           # Ideas, theories, frameworks
│   ├── sources/            # One summary page per ingested source
│   ├── comparisons/        # Cross-source analysis pages
│   └── synthesis/          # High-level syntheses, theses, overviews
├── CLAUDE.md               # Layer 3 — schema + conventions (Claude Code)
└── AGENTS.md               # Same content, for Codex / Cursor / Antigravity / OpenCode
```

- **Layer 1 (`raw/`)** — the user owns it. The agent only reads. **Never write here.**
- **Layer 2 (`wiki/`)** — the agent owns it: creates, updates, cross-references.
- **Layer 3 (`CLAUDE.md` / `AGENTS.md`)** — the schema: conventions, workflows, frontmatter rules.

## Iron rule

**The agent never edits files in `raw/`.** Ever. Sources are immutable. All writes go to `wiki/`.
If a source needs correcting, the user fixes it in `raw/` and the agent re-ingests.

## Modes / frameworks

Three core operations, each credited to the source member:

### Mode A — Ingest (the compounding step)

Read a source, discuss takeaways with the user, write a source-summary page, update 10–15
relevant pages, regenerate `index.md`, append to `log.md`.

1. `ingest_source.py --vault <v> --source <path>` extracts text and frontmatter, ready for review.
2. Propose: a TL;DR, the key claims, which entity/concept/synthesis pages this touches, and any
   **contradiction with an existing page**. Get user confirmation before writing.
3. Write `wiki/sources/<slug>.md` from the source-summary template.
4. Update 5–15 related pages; add `[[wikilinks]]` in both directions.
5. `update_index.py --vault <v>` and `append_log.py --vault <v> --op ingest --title "<title>"`.

Full flow: `references/ingest-workflow.md`.

### Mode B — Query (search → synthesise → re-file)

Read `index.md` first, drill into 3–10 relevant pages, synthesise with inline `[[wikilinks]]`.
**Good answers get filed back** as a new comparison or synthesis page, so exploration compounds
instead of dying in chat history. Falls back to `wiki_search.py` (BM25) when the index is not enough.

Full flow: `references/query-workflow.md`.

### Mode C — Lint (health check)

Run periodically and after every batch ingest: contradictions, stale claims, orphan pages,
broken `[[wikilinks]]`, pages missing frontmatter, duplicate titles, log gaps.

```bash
python scripts/lint_wiki.py --vault ~/vaults/research
python scripts/graph_analyzer.py --vault ~/vaults/research   # hubs, orphans, clusters
```

Full heuristics: `references/lint-workflow.md`.

## Quick start

```bash
# 1. Initialize a vault (inside Obsidian's vault directory)
python scripts/init_vault.py --vault ~/vaults/research --topic "LLM interpretability"

# 2. Drop a source into raw/, then ingest it (Mode A)
# 3. Ask questions; re-file the good answers (Mode B)
# 4. Periodic health check (Mode C)
python scripts/lint_wiki.py --vault ~/vaults/research

# 5. See the timeline
grep -E '^## \[' ~/vaults/research/wiki/log.md | tail -10
```

## Tools (`scripts/` — Python standard library only, no pip installs)

| Script | Purpose |
|---|---|
| `init_vault.py` | Create the structure + seed schema files and templates. **`--vault`** (or deprecated `--path`) |
| `ingest_source.py` | Extract text/frontmatter from a source file, ready for review |
| `update_index.py` | Regenerate `index.md` from page frontmatter |
| `append_log.py` | Append a standardised `## [date] <op> \| <title>` entry |
| `wiki_search.py` | BM25 search over wiki pages — standalone fallback for Mode B |
| `lint_wiki.py` | Orphans, broken links, stale pages, missing frontmatter, duplicate titles, log gaps |
| `graph_analyzer.py` | Link-graph stats: hubs, orphans, sinks, clusters, disconnected components |
| `export_marp.py` | Render a page or subtree to a Marp slide deck |

All tools take `--json` for programmatic use. All read/write only the vault you point them at.

## Page frontmatter (required by `lint_wiki.py`)

Every page under `wiki/` — **except `index.md` and `log.md`** — must carry:

```yaml
---
title: <human-readable name>     # wikilinks resolve against this, not the filename
category: entity                  # entity | concept | source | comparison | synthesis
summary: <one line>
updated: <YYYY-MM-DD>
---
```

Templates for all five categories are in `assets/page-templates/`. A page missing any of
`title`/`category`/`summary` is reported by the linter — copy from the template rather than
improvising.

## Conflict resolutions (decision rules)

### C1 — `init_vault.py --path` vs everything else's `--vault` (HIGH, fixed)

The only script in the family taking `--path`; the other seven all take `--vault`. Any scripted
pipeline mixing them fails. **Resolution:** `--vault` is now the primary flag and `--path` a
deprecated alias, so existing commands keep working and new ones match the rest of the toolkit.
Verified: both spellings initialise a vault; omitting both errors clearly.

### C2 — Wikilinks resolved by filename, but pages are titled by frontmatter (HIGH, fixed)

The link graph matched `[[Alpha]]` against the filename stem only. The shipped templates name
files by short slug (`entities/A.md`) while setting `title: Alpha` — so *every* title-named link
was reported broken and its target counted as an orphan, in both `lint_wiki.py` and
`graph_analyzer.py`. A vault following the skill's own conventions could never lint clean.

**Resolution:** resolve in order full path → **frontmatter `title`** → filename stem.
Reproduced before/after on a two-page vault: 1 broken link + 1 orphan → 0 and 0.

### C3 — "the wiki never edits `raw/`" vs "correct the source and re-ingest" (MEDIUM, kept as-is)

Not a contradiction: the rule bounds the agent, the exception bounds the user. Kept verbatim as
the Iron Rule, with the actor named in each clause.

### C4 — RAG alternative vs scaling "past ~500 pages, bolt on retrieval" (MEDIUM, kept)

The skill positions itself against RAG, then recommends RAG at scale. Both are true: the wiki
wins on compounding and cross-references up to a few hundred pages; retrieval wins when the corpus
outgrows what `index.md` + filesystem search can serve. The crossover is a scale fact, not a
contradiction. Stated as a "when to graduate" note rather than a hard number.

### C5 — Sub-agents as separate plugin agent definitions vs Modes in one skill (LOW, folded)

The plugin shipped `wiki-ingestor` / `wiki-librarian` / `wiki-linter` as agent definitions. Their
procedures are the three Modes above; the definitions remain available if installed. No behaviour
lost — both paths execute the same workflow.

### C6 — `example-vault/` referenced by the member but absent (LOW, dropped)

The member's "Templates (`assets/`)" section lists an `example-vault/` that does not exist in the
shipped tree. Reference removed rather than restored — `init_vault.py` on a scratch directory
produces a real worked example on demand.

## Obsidian setup (recommended)

- **Web Clipper** — browser extension; converts articles to markdown and drops them in `raw/`.
- **Images** — Settings → Files and links → Attachment folder path = `raw/assets/`. Bind
  "Download attachments for current file" to `Ctrl+Shift+D`.
- **Graph view** — see hubs and orphans; the fastest way to spot structural problems.
- **Marp** — slide decks straight from wiki pages. **Dataview** — dynamic tables over frontmatter.
- **Git** — the vault is a plain markdown repo; version it.

Full walkthrough: `references/obsidian-setup.md`.

## Why this works (vs plain RAG)

| Plain RAG | This skill |
|---|---|
| Rediscover knowledge each query | Knowledge accumulates |
| Cross-references recomputed every time | Cross-references pre-written and maintained |
| Contradictions surface only if you ask | Contradictions flagged during ingest |
| Exploration disappears into chat history | Good answers re-filed as pages |
| Scales by embeddings infrastructure | Scales by markdown + `index.md` + optional local search |

At ~100 sources / a few hundred pages, `index.md` + filesystem search is enough. Past that, layer
in a local search tool, or graduate to a retrieval layer.

## Reference docs

- `references/wiki-schema.md` — full vault layout, page frontmatter, naming conventions
- `references/page-formats.md` — per-category page templates (also in `assets/page-templates/`)
- `references/ingest-workflow.md` — the detailed Mode A flow
- `references/query-workflow.md` — Mode B patterns, citation format, re-filing answers
- `references/lint-workflow.md` — Mode C heuristics
- `references/obsidian-setup.md` — plugins, hotkeys, vault config
- `references/cross-tool-setup.md` — per-agent-CLI setup (Codex, Cursor, Antigravity, OpenCode)
- `references/memex-principles.md` — Bush's Memex, and why an LLM changes the maintenance math

## Templates (`assets/`)

- `CLAUDE.md.template`, `AGENTS.md.template`, `.cursorrules.template` — schema loader per tool
- `index.md.template`, `log.md.template` — starter index and timeline
- `page-templates/` — entity, concept, source-summary, comparison, synthesis

## Confidence & unverified claims

- **HIGH** — C1 and C2, both reproduced by execution and fixed, with before/after output. The
  three-layer architecture, the Modes, and the Iron Rule are internal to the member and coherent.
  All eight scripts were smoke-tested: they run, parse frontmatter, resolve links, and report
  correctly on a scratch vault.
- **MEDIUM** — C4's crossover point and the Obsidian setup specifics: the settings paths and
  hotkeys are as shipped and plausible, but were not verified against a live Obsidian install.
- **LOW / unverified:**
  - The "~100 sources / ~500 pages" scale figures are rules of thumb from the member, never
    benchmarked here; treat as order-of-magnitude guidance.
  - No web search was performed. The Karpathy gist attribution is taken from the member's own
    header, not re-checked.
  - The qmd / Marp / Dataview ecosystem claims are as documented; none were installed or tested.
  - `export_marp.py` was syntax- and argparse-checked only — no Marp renderer was available to
    confirm the deck it emits renders correctly.
