# Micro-review Part C — MESSAGES.md verbatim + evidence labels

Method: `grep -F` on a distinctive fragment per quote, run against the stated source. Evidence labels counted with `grep -c <label> /workspace/wiki/repo/*.md` (line-counts, a line with 2+ hits counts once).

## Verbatim verification

| quote fragment | stated source | grep result file:line | PASS/FAIL |
|---|---|---|---|
| `read the file named promptastra6fgss.md and do what the prompt says` (MESSAGES.md أ-1) | `work/analysis-session-01.md` | `work/analysis-session-01.md:9` | PASS |
| `continue your work and never stop` (MESSAGES.md أ-5) | `work/analysis-session-01.md` | `work/analysis-session-01.md:13` | PASS |
| `Wait a minute, why are you clicking on the video?` (MESSAGES.md أ-10) | `work/analysis-session-01.md` | `work/analysis-session-01.md:18` | PASS |
| `مفيش حجر خالص، ونعرض الطرفين دايماً` (MESSAGES.md ب-3) | `work/analysis-wiki-talk-01.md` | `work/analysis-wiki-talk-01.md:38` | PASS |
| `مفيش نشر، المستودع خاص` (MESSAGES.md ب-4) | `work/analysis-wiki-talk-01.md` | `work/analysis-wiki-talk-01.md:42` | PASS |
| `الخام (Raw) للقراءة فقط، لا يُعدَّل أبداً` (MESSAGES.md ب-17) | `work/analysis-wiki-talk-01.md` | `work/analysis-wiki-talk-01.md:178` | PASS |

Note: all three wiki quotes live in the §1 verbatim section (`analysis-wiki-talk-01.md:38/42/178`); later lines (428, 431, …) repeat them in discussion tables — the §1 line is the verbatim source. Session quotes sit at `analysis-session-01.md:9/13/18`, matching §1 in order. No mismatches found in this 6-quote sample.

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
