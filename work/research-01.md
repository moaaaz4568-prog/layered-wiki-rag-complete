# Research 01 — Personal Knowledge GitHub Repo from Chat Exports: Best Practices

**Status:** COMPLETE — evidence-labeled
**Date:** 2026-11-05
**Scope:** (1) Structuring a personal knowledge GitHub repo from chat exports, (2) Context files so a fresh AI chat needs no re-reading, (3) Converting chat logs into wiki/second-brain, (4) Agent memory skills on GitHub

## 1. Structuring a Personal Knowledge GitHub Repo from Chat Exports
- OBSERVED (page fetched https://agents.md/): AGENTS.md is defined as "a simple, open format for guiding coding agents", a README-for-agents giving agents a clear, predictable place for instructions, separate from human README.md.
- OBSERVED (page fetched https://agents.md/): Recommended contents: project overview, build/test commands, code style, testing instructions, security considerations, plus PR/commit guidelines and deployment steps — "anything you'd tell a new teammate".
- OBSERVED (page fetched https://agents.md/): For large monorepos use nested AGENTS.md files per subproject; the nearest file in the directory tree takes precedence (OpenAI repo cited with 88 AGENTS.md files).
- PROPOSED (recommendation from https://agents.md/): Use a root AGENTS.md at repo root plus nested AGENTS.md per topical subfolder to scope instructions, mirroring the nested-file pattern for personal knowledge folders.

## 2. Context Files So a Fresh AI Chat Needs No Re-Reading
- OBSERVED (page fetched https://opencode.ai/docs/rules/): OpenCode reads AGENTS.md as custom instructions injected into LLM context; `/init` scans important repo files and creates/updates AGENTS.md with build/lint/test commands, command order, non-obvious architecture, conventions and gotchas — improving in place if one exists.
- OBSERVED (page fetched https://opencode.ai/docs/rules/): Precedence order: (1) local files traversing up from cwd (AGENTS.md, CLAUDE.md), (2) global ~/.config/opencode/AGENTS.md, (3) ~/.claude/CLAUDE.md unless disabled; first match wins per category, so AGENTS.md beats CLAUDE.md when both exist. Project AGENTS.md should be committed; global is personal-only.
- OBSERVED (page fetched https://opencode.ai/docs/rules/): Extra instruction files can be declared via `instructions` in opencode.json (files, globs like `packages/*/AGENTS.md`, or remote URLs fetched with 5s timeout); OpenCode does NOT auto-parse @file references in AGENTS.md — manual lazy-loading instructions are the pattern (explicit Read tool on need-to-know basis).
- OBSERVED (page fetched https://docs.anthropic.com/en/docs/claude-code/memory): Claude Code carries knowledge across fresh sessions via two mechanisms: CLAUDE.md/AGENTS.md files you write, and auto memory notes Claude writes from corrections/preferences.
- OBSERVED (page fetched https://docs.anthropic.com/en/docs/claude-code/memory): CLAUDE.md scope ladder load order: managed policy > user (~/.claude/CLAUDE.md) > project (./CLAUDE.md or ./.claude/CLAUDE.md) > local (./CLAUDE.local.md, gitignored); ancestors above working dir load at launch, subdirectory files load on demand when a file there is read/written/edited.
- OBSERVED (page fetched https://docs.anthropic.com/en/docs/claude-code/memory): Guidance — keep CLAUDE.md under 200 lines, scannable headers/bullets, concrete verifiable instructions ("Run npm test before committing" not "Test your changes"); multi-step or topic-scoped material goes to skills or path-scoped .claude/rules/ instead.
- OBSERVED (page fetched https://docs.anthropic.com/en/docs/claude-code/memory): CLAUDE.md supports @path imports (relative paths resolve to importing file, recursive to depth 4), and HTML comments are stripped before context injection; MEMORY.md index loads only first 200 lines / 25KB, topic files load on demand.
- PROPOSED (recommendation from https://docs.anthropic.com/en/docs/claude-code/memory): Mirror for chat-export wiki: root CLAUDE.md/AGENTS.md loaded every chat + topic-scoped rule files that load on demand, with an index file deciding what loads.

## 3. Converting Chat Logs into a Wiki / Second-Brain
- OBSERVED (page fetched https://help.obsidian.md/importer/overview): (Fetch returned only page title in text format; body not captured — no substantive claim recorded from this source.)
- REPORTED (repo claim https://github.com/YeonDu1/claude-archive-to-obsidian): Pipeline: conversations.json → convert.py (one .md per conversation) → extract_summaries.py (classification signal CSV) → apply_tags.py (frontmatter tags + [[wikilinks]]) → Obsidian, output to `vault/claude-chats/<account>/<year>/<YYYY-MM-DD>_<slug>.md` with `source_uuid` frontmatter as the dedupe key making re-runs additive.
- REPORTED (repo claim https://github.com/YeonDu1/claude-archive-to-obsidian): Design decisions — controlled vocabulary (~32 hierarchical tags) not free tagging; entity list built corpus-wide before application requiring 2+ occurrences; batch→verify→commit per account; UTF-8 explicitly everywhere.
- REPORTED (repo claim https://github.com/YeonDu1/claude-archive-to-obsidian): Privacy/workspace layout — the vault itself is not in the repo; `raw_exports/` and `vault/` are gitignored and must stay that way since a full export is years of personal conversation; keeping current = fresh export → re-run convert.py (source_uuid dedupe) → tag only new files.
- PROPOSED (recommendation from https://github.com/YeonDu1/claude-archive-to-obsidian): Adopt this pipeline pattern for chat-export wiki content: one note per conversation, fixed tag vocabulary designed from the full corpus, entity wikilinks, and generated Maps of Content — keeping raw exports gitignored.

## 4. Agent Memory Skills on GitHub
- REPORTED (repo claim https://github.com/mem0ai/mem0): Mem0 positions as "The Memory Layer for AI Agents" — drop-in memory infrastructure with multi-level memory (User/Session/Agent state), self-hosted server + cloud platform, cross-platform SDKs and a CLI (`mem0 init/add/search` with `--user-id`).
- REPORTED (repo claim https://github.com/mem0ai/mem0): Agent skills are installable via `npx skills add` — reference skills (mem0, mem0-cli, mem0-vercel-ai-sdk) always-on, plus on-demand pipeline skills (mem0-integrate, mem0-test-integration, mem0-oss-to-platform) for wiring Mem0 into existing repos.
- REPORTED (repo claim https://github.com/mem0ai/mem0): Retrieval fuses semantic + BM25 keyword + entity matching with temporal reasoning; reported April 2026 algorithm: LoCoMo 92.5, LongMemEval 94.4, single-pass ADD-only extraction (no UPDATE/DELETE) — platform numbers, open-source expected directionally similar not identical.
- OBSERVED (page fetched https://github.com/mem0ai/mem0): Repo ships both AGENTS.md and CLAUDE.md at root and per-tool plugin directories (.claude-plugin, .codex-plugin, .cursor-plugin, .kimi-plugin), indicating cross-agent instructional files are part of the repo structure.
- PROPOSED (recommendation from https://github.com/mem0ai/mem0): For chat-export wiki memory, prefer explicit additive memory (append-only, never overwrite) with entity linking and temporal retrieval over lossy auto-summarization.
- REPORTED (repo claim https://github.com/obra/superpowers): Superpowers is "a complete software development methodology ... built on top of a set of composable skills" — skills auto-trigger (agent checks for relevant skills before any task; mandatory workflows not suggestions), with a `using-superpowers` bootstrap skill injected at session start.
- REPORTED (repo claim https://github.com/obra/superpowers): Skills library example of composable workflows: brainstorming → using-git-worktrees → writing-plans → subagent-driven-development/executing-plans → test-driven-development (RED-GREEN-REFACTOR) → requesting-code-review → finishing-a-development-branch; plus debugging/collaboration/meta clusters (systematic-debugging, writing-skills).
- OBSERVED (page fetched https://github.com/obra/superpowers): Repo ships per-harness plugin directories (.claude-plugin, .codex-plugin, .cursor-plugin, .devin-plugin, .opencode, etc.) and AGENTS.md/GEMINI.md, showing how one skills library is adapted per agent harness.
- PROPOSED (recommendation from https://github.com/obra/superpowers): For the chat-export wiki, bundle each conversion step (export→convert→tag→sync) as a composable skill with a mandatory bootstrap that forces the agent to check relevant skills before any task.

## Sources
1. https://agents.md/
2. https://opencode.ai/docs/rules/
3. https://docs.anthropic.com/en/docs/claude-code/memory
4. https://help.obsidian.md/importer/overview
5. https://github.com/YeonDu1/claude-archive-to-obsidian
6. https://github.com/mem0ai/mem0
7. https://github.com/obra/superpowers
