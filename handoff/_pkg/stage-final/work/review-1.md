# Accuracy Review 1 — Incremental Checks

## Method

Each repo claim was grepped in its source analysis file for PASS/FAIL with file:line evidence. Verbatim quotes checked with `grep -F` on a distinctive fragment per quote, run against the stated source. Evidence labels counted with `grep -c <label> /workspace/wiki/repo/*.md` (line-counts, a line with 2+ hits counts once). Part B item 6 re-checked with `grep '212\|2713' /workspace/wiki/work/archive-inventory-01.md` because the Part B checker searched only `analysis-wiki-talk-01.md`.

## Checks (18 total)

| # | claim | repo line | source match file:line | PASS/FAIL |
|---|---|---|---|---|
| 1 | 37,402 بايت · 129 مقطعًا — أصغر 20 صفحة | repo/index/bm25-results.md:10 | /workspace/wiki/work/analysis-wiki-talk-01.md:163,228 | PASS |
| 2 | 601,084 بايت — إجمالي هيثم (210 صفحة) | repo/index/bm25-results.md:18 | /workspace/wiki/work/analysis-wiki-talk-01.md:233 | PASS |
| 3 | 123,205 بايت — أكبر 20 صفحة | repo/index/bm25-results.md:18 | /workspace/wiki/work/analysis-wiki-talk-01.md:233 | PASS |
| 4 | 14/15 في المرتبة الأولى، 15/15 في أول 3 — على أكبر 20 | repo/index/bm25-results.md:19 | /workspace/wiki/work/analysis-wiki-talk-01.md:234 | PASS |
| 5 | 12/15 في المرتبة الأولى، 14/15 في أول 3 — على كل 210 | repo/index/bm25-results.md:24 | /workspace/wiki/work/analysis-wiki-talk-01.md:235,454 | PASS |
| 6 | 429 ميجا — الرام المتاح 2026-11-03 09:07 | repo/index/bm25-results.md:38 | /workspace/wiki/work/analysis-wiki-talk-01.md:165,246 | PASS |
| 7 | ست ويكيات ضمت 5896 صفحة بحجم 31.3MB وبالحجم بالبايت 31262266 | `repo/CONTEXT.md:20` | `work/analysis-wiki-talk-01.md:156` | PASS |
| 8 | BM25 على كامل 210 صفحة أعطت 12 من 15 في المرتبة الأولى و14 من 15 في أول 3 | `repo/CONTEXT.md:26` | `work/analysis-wiki-talk-01.md:235` | PASS |
| 9 | الرام المتاح لحظة القياس كان 429 ميجا | `repo/CONTEXT.md:30` | `work/analysis-wiki-talk-01.md:246` | PASS |
| 10 | بناء `yt-wiki` الموحد؛ فهرس 4,262 صفحة (2026-10-19) | `repo/timeline/timeline.md:11` | `work/analysis-wiki-talk-01.md:87` | PASS |
| 11 | تحميل 144 فيديو وقراءتها (2026-10-31) | `repo/timeline/timeline.md:20` | `work/analysis-wiki-talk-01.md:187` | PASS |
| 12 | الأرشيف 212MB/2713 ملف (`WIKI_ARCHIVE_2026-11-03`) | `repo/timeline/timeline.md:28` | `work/archive-inventory-01.md:3,77` | PASS |
| 13 | `read the file named promptastra6fgss.md and do what the prompt says` (MESSAGES.md أ-1) | `work/analysis-session-01.md` | `work/analysis-session-01.md:9` | PASS |
| 14 | `continue your work and never stop` (MESSAGES.md أ-5) | `work/analysis-session-01.md` | `work/analysis-session-01.md:13` | PASS |
| 15 | `Wait a minute, why are you clicking on the video?` (MESSAGES.md أ-10) | `work/analysis-session-01.md` | `work/analysis-session-01.md:18` | PASS |
| 16 | `مفيش حجر خالص، ونعرض الطرفين دايماً` (MESSAGES.md ب-3) | `work/analysis-wiki-talk-01.md` | `work/analysis-wiki-talk-01.md:38` | PASS |
| 17 | `مفيش نشر، المستودع خاص` (MESSAGES.md ب-4) | `work/analysis-wiki-talk-01.md` | `work/analysis-wiki-talk-01.md:42` | PASS |
| 18 | `الخام (Raw) للقراءة فقط، لا يُعدَّل أبداً` (MESSAGES.md ب-17) | `work/analysis-wiki-talk-01.md` | `work/analysis-wiki-talk-01.md:178` | PASS |

Notes: Item 12 originally FAIL in Part B (wrong-file search `analysis-wiki-talk-01.md` only); re-check `grep '212\|2713' /workspace/wiki/work/archive-inventory-01.md` found matches at lines 3 and 77 → PASS with source `archive-inventory-01.md`. All three wiki quotes live in the §1 verbatim section (`analysis-wiki-talk-01.md:38/42/178`); later lines repeat them in discussion. Session quotes sit at `analysis-session-01.md:9/13/18`, matching §1 in order.

## Evidence-label usage counts across repo/*.md (`grep -c`, line-counts)

| label | AGENTS | ARCHITECTURE | CHANGELOG | CONTEXT | DESIGN-REFERENCE | IDEAS | MASTER | MESSAGES | PROVENANCE | README | REJECTED | **total** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OBSERVED | 2 | 3 | 11 | 28 | 7 | 9 | 4 | 1 | 8 | 18 | 1 | **92** |
| REPORTED | 2 | 67 | 13 | 39 | 12 | 10 | 17 | 0 | 22 | 16 | 22 | **220** |
| PROPOSED | 2 | 8 | 2 | 6 | 5 | 11 | 5 | 0 | 3 | 10 | 2 | **54** |
| UNKNOWN | 3 | 9 | 4 | 4 | 4 | 1 | 5 | 0 | 7 | 3 | 2 | **42** |
| NOT_RUN | 3 | 7 | 2 | 3 | 3 | 0 | 3 | 0 | 3 | 7 | 1 | **32** |

Observations:
- REPORTED dominates (220) — ARCHITECTURE.md alone carries 67, mostly as a label-distribution header rather than per-claim tags.
- MESSAGES.md uses only 1 evidence label total (OBSERVED:1) — quotes are cited as verbatim by construction, not tagged per-line.
- IDEAS.md has 0 NOT_RUN despite being a proposals file — proposals are tagged PROPOSED but not NOT_RUN where untested.
- Totals equal the sum of per-file line-counts; a line containing two different labels contributes to both rows.

## Verdict

**Overall: PASS** — 18/18 checks PASS (Part A 6/6, Part B 6/6 after re-check, Part C 6/6).

Required fixes: none.
