# Review-3 — USABILITY: Fresh-AI Simulation

Method: read `CONTEXT.md` first in isolation, then `README.md`, `MASTER.md`, `AGENTS.md`, `docs/STRUCTURE.md`, then `ls -R` / `find` against `/workspace/wiki/repo` (2026-11-05). No repo files edited.

## (a) Does CONTEXT.md alone convey purpose, measured state, rules, conflicts, where to fetch more?

| # | Check | Verdict | Evidence / Fix |
|---|---|---|---|
| A1 | Project purpose | PASS | CONTEXT §1 (lines 9-16) states YouTube→shared-wiki→ask, specialist "Masters", private repo, terms-before-masters. Self-contained. |
| A2 | Current measured state | PASS | §2 (lines 20-33) lists 5896 pages, 31.3MB, distribution, BM25 12/15 and 14/15, 429MB RAM, 144 videos, with OBSERVED tags. Line count 101 < 300 claim (§9 line 100) verified by `wc -l`. |
| A3 | Rules | PASS | §5 (lines 56-64) sample-first v0.1 Haitham-only, no-number-without-measure, raw read-only, human review, Git+snapshot, secrets ban. Mirrors README's 6 policies. |
| A4 | Open conflicts | PASS | §6 (lines 68-75) quarantines vs "مفيش حجر", all-seeing vs Top-k, "stupid opinion" boundary, public vs private, bge-m3 NOT_RUN, k/threshold UNKNOWN. Clear. |
| A5 | Where to fetch more (in-repo) | FAIL | §7 "من أين يُجلب أي شيء" (lines 79-84) cites only `work/*.md` and archive stats; it never points to the in-repo fetch points that now exist: `sources/wiki-talk-index.md`, `sources/session-export-index.md`, `sources/links.md`, `index/bm25-results.md`, `ARCHITECTURE.md`, `docs/`. A fresh agent starting at `repo/` cannot resolve `work/` (see C1). Fix: add an in-repo fetch map table (repo path → what it gives) in §7, keep `work/` as provenance only. |
| A6 | "Alone suffices" self-claim | FAIL (misleading) | Line 3 and §9 line 99 claim CONTEXT alone suffices. Tagged `[PROPOSED]` (line 99) — honest tag, but phrasing is absolute. In practice CONTEXT omits: (1) working-dir anchor (CONTEXT lives at `repo/CONTEXT.md`; `work/` is a sibling, not `repo/work/`), (2) repo file map, (3) pointer to `AGENTS.md` first-action rule. Fresh reader believing "alone" will miss `AGENTS.md` workflow and in-repo indexes. Fix: soften to "CONTEXT alone orients; AGENTS.md + README map govern work" or add a 3-line "next read" box. |

Overall (a): PASS with one fix — content complete, navigation incomplete.

## (b) Is the README reading map correct and do paths exist?

`ls -R`/`find` (42 files): root has 11 .md + `.env.example` + `.gitignore`; `config/`4, `docs/`11, `index/`2, `masters/`2, `reference/`2, `sources/`5, `templates/`2, `timeline/`1.

| README §3 line | Path stated | Exists? | Verdict |
|---|---|---|---|
| أولا `CONTEXT.md` | yes | PASS |
| ثانيا `MESSAGES.md` | yes | PASS |
| ثالثا `IDEAS.md` | yes | PASS |
| رابعا `MASTER.md` + `ARCHITECTURE.md` | yes | PASS |
| عند الحاجة `docs/` | yes (11 files) | PASS (exists, vague) |
| عند الحاجة `sources/` | yes (5 files) | PASS (exists, vague) |
| عند الحاجة `timeline/` | yes (1 file) | PASS (exists, vague) |

Completeness FAIL:
- Map omits existing top-level files a newcomer needs: `AGENTS.md` (agent workflow), `PROVENANCE.md` (verify sources), `REJECTED.md`, `CHANGELOG.md`, `DESIGN-REFERENCE.md`. None appear in the table.
- Map omits whole folders that exist: `config/` (4 yamls), `index/` (BM25 measured results), `masters/` + `masters/review/checklist.md`, `templates/` (term/master), `reference/` (purposes/non-goals).
- `docs/` row does not enumerate which of the 11 docs files to open (GOALS, RULES, CONCEPTS, METADATA-SCHEMA, CHUNKING, EVALUATION, CONTRADICTION-POLICY, KNOWN-ANSWER-SET, STAGES, SOURCES). Fix: either list `docs/*.md` explicitly or point to `docs/STRUCTURE.md` as the full tree (currently no cross-link; STRUCTURE.md header still says "لم تُبنَ كاملة بعد" while all listed docs exist).

Overall (b): FAIL (minor) — every listed path exists (no wrong path), but map is materially incomplete and stale in tone.

## (c) Dangling references to non-existent files

| Ref in | Reference | On disk? | Verdict / Fix |
|---|---|---|---|
| CONTEXT L3-L101, README L3-L79, AGENTS L35 | `work/repo-plan-01.md`, `work/analysis-wiki-talk-01.md`, `work/analysis-session-01.md` | NO under `repo/work/` (`ls repo/work/` → No such file). Files exist only at sibling `/workspace/wiki/work/`. All citations are dangling relative to repo root. | FAIL — Fix: prefix as `../work/...` or, better, add `sources/` in-repo equivalents and mark `work/` as "not in repo; provenance only". AGENTS.md L35 is the worst: it orders the agent to obey a file it cannot find from repo root. |
| MASTER L48 | `analysis-wiki-talk-01.md` (no `work/` prefix) | No such file in repo root. | FAIL — same prefix fix as above. |
| MASTER L51 | `layered-wiki-rag-design.md` | NO. Repo has `DESIGN-REFERENCE.md` (5KB) and `ARCHITECTURE.md` (13KB), neither named `layered-wiki-rag-design.md` and neither 92KB. | FAIL — Fix: rename ref to actual file or add alias note. |
| STRUCTURE L75 | `archive-inventory-01.md` | NO in repo. Work sibling has `archive-inventory-01.md`; in-repo equivalent is `sources/file-inventory.md`. | FAIL (minor naming mismatch) — Fix: cite `sources/file-inventory.md`. |
| STRUCTURE §5 L57-L66 | `raw/`, `wiki/`, `terms/`, `src/`, `bin/`, `skills/`, `tests/`, `snapshots/before-bulk/`, `out/` | All ABSENT (`test -e` each → missing). Section header says "من التصميم" but body tags are REPORTED (from design) — fresh reader will infer these folders exist in this repo. | FAIL (misleading) — Fix: tag each line PROPOSED/design-only + add header note "none exist in repo/ yet". |
| README L65, AGENTS L3 | `https://raw.githubusercontent.com/moaaaz4568-prog/layered-wiki-rag/main/AGENTS.md` | Noted 404 in-file; fresh `webfetch` will still 404. | PASS (honestly disclosed) — keep 404 note; do not present URL as fetchable primary source. |
| STRUCTURE §7 L80-L85 | `MANIFEST.json`, `conversations_index.csv`, `*.db/*.opus/*.env/*.log`, `cookies.txt`, `.hcnsec_key`, `zcode-*`, VTT/TXT | Intentionally absent (forbidden list). | PASS — not dangling; these are never-copy rules. |
| CONTEXT L79, README L78 | "ملف التصميم في المستودع الحالي حجمه 92KB" | No 92KB file in repo; largest is `CONTEXT.md` 15KB, `MESSAGES.md` 16.6KB. | FAIL (stale size) — Fix: re-measure `DESIGN-REFERENCE.md` + `ARCHITECTURE.md` and update or drop the 92KB claim. |

No Markdown-style `[text](path)` links exist in the four files checked — all refs are backtick paths, so there are no broken hyperlinks per se; the failures above are path-level.

## (d) Statements a fresh reader would misinterpret

| # | Statement | Truth on disk 2026-11-05 | Verdict / Fix |
|---|---|---|---|
| D1 | README L50 + L69: "5 ملفات آمنة" / "الملفات الخمسة المكتوبة" [OBSERVED] | Repo has 42 files. Claim was true at build time, now stale but tagged OBSERVED — the strongest tag — so a fresh reader trusts it and is misled. | FAIL — Fix: re-run secret scan over all 42 files or re-tag as historical "[OBSERVED 2026-11-03, 5 files at that date]". |
| D2 | README L50: "المستودع الحالي له commit واحد" [OBSERVED] | `git status` in `repo/` → "not a git repository" (no `.git/`). Unverifiable from this tree. | FAIL — Fix: state where the `.git/` lives or that clone is expected elsewhere; do not claim verifiability here. |
| D3 | MASTER L21 table: "لا يوجد مجلد masters/ ولا أي ملف .md إلا الملفات الستة هذه" [OBSERVED 2026-11-05] | FALSE. `masters/README.md` + `masters/review/checklist.md` exist, plus `DESIGN-REFERENCE.md`, `config/`, etc. | FAIL (most serious) — Fix: correct row to "صفر ماستر نشط بمحتوى مثبت; مجلد masters/ توثيقي فقط" with fresh `find` evidence. |
| D4 | MASTER L36: checklist "الملف غير موجود في repo/" [UNKNOWN] | `masters/review/checklist.md` EXISTS with 10-item human checklist. | FAIL (stale) — Fix: flip to REPORTED/OBSERVED and summarize checklist; remove UNKNOWN. |
| D5 | STRUCTURE L3: "لم تُبنَ كاملة بعد" | All §2-§4 files it lists now exist (11/11 root docs, 11/11 docs/, 5/5 sources/, 4/4 config/, 2/2 templates/, etc.). | FAIL (stale) — Fix: update header to PROPOSED→OBSERVED with date, or note "structure planned; data layers §5 still absent". |
| D6 | STRUCTURE L11: "حسب الخطة، 5 ملفات" | 42 files present. | FAIL (stale) — same fix as D1. |
| D7 | CONTEXT L83: "AGENTS من ملف نظام آخر لم يُفحص مباشرة" + AGENTS L3 404 URL | `AGENTS.md` now exists in repo (40 lines, readable). Fresh reader may think AGENTS is unavailable. | PASS with note — disclose that this copy was written in-session; link to local file, external URL is archival 404. |
| D8 | CONTEXT L99 / README L25 "يكفي وحده" [PROPOSED] | True for orientation (A1-A4 PASS) but not for navigation (A5/A6 FAIL). Tag PROPOSED actually softens it, but absolute Arabic "يكفي وحده / دون قراءة أي ملف آخر" invites overconfidence. | FAIL (soft) — Fix: "يكفي وحده للتوجه; للعمل اقرأ AGENTS.md وبعده الخريطة". |
| D9 | CONTEXT L11-L12 vs L68: "كل ملف يدخل بكل محتواه" + "مفيش حجر خالص" reported as literal rule while §6 flags quarantine as undecided | Fresh reader may implement "no quarantine" and violate human-review rule (§5 L61). | PASS with note — wording is correctly REPORTED and §6 marks conflict; keep both; consider bolding conflict link in §1. |
| D10 | README L62-L65 repo decision + v1.0.0 404 | Honest; fresh reader might still try the URL. | PASS — keep 404 note; no action. |

## Overall verdict

**CONDITIONAL PASS — usable by a fresh AI for orientation, but not trustworthy for navigation without fixes.**

- Strengths: CONTEXT.md (§1-§6) genuinely covers purpose, numbers, rules, conflicts; every README-listed path exists; forbidden-list files correctly absent.
- Blockers: (1) all `work/` citations dangle from repo root (C1); (2) MASTER.md's OBSERVED "no masters/ folder" is false on disk (D3) — the single most damaging stale claim; (3) README "5 files" + STRUCTURE "5 files / not yet built" are stale (D1, D5, D6); (4) STRUCTURE §5 design layers look like present folders (C5).

Minimum fix set before calling it fresh-reader-safe: add in-repo fetch map to CONTEXT §7, fix `work/` prefixes (or add `sources/` mapping), correct MASTER L21/L36 to current `masters/` reality, update README L50/L69 + STRUCTURE header counts with a fresh dated `find`/`grep` evidence line, and tag STRUCTURE §5 layers as design-only/absent. No repo edits made in this review.

DONE
