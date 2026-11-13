# جرد أرشيف الويكي — WIKI_ARCHIVE_2026-11-03

**المصدر:** `/workspace/wiki/archive-extract/WIKI_ARCHIVE_2026-11-03/` (212MB فعلي، 2713 ملفاً مقاساً بـ `find -type f`؛ الوثيقة تذكر 2707)
**الأرشيف المضغوط:** `/workspace/wiki/WIKI_ARCHIVE_2026-11-03.tar.gz` — 58MB (لا يوجد `source-transfers/` داخل `/workspace/wiki/archive-extract/`)
**النطاق:** هذه الوثائق العلوية فقط + قياسات `du -sh` لكل مجلد.
**الميزانية المعلنة:** 250MB → الفعلي ~211–212MB. المساحة الحرة المعلنة على `/mnt/sdcard`: 497MB.

---

## 1) ملفات الجذر

| الملف | الدور |
|---|---|
| `README.md` (20K) | الوثيقة السيادية: شجرة، ميزانيات، التحقق `sha256`، مبدأ صفر حذف |
| `MANIFEST.json` (780K) | فهرس آلي لكل ملف: مسار + حجم + SHA-256 |
| `EXPORT_NOTES.md` | منهجية تصدير المحادثات الأربعة (استعلامات/هياكل) |
| `FALLBACK.md` | سلّم طوارئ F0–F6 عند نقص المساحة دون 30MB |
| `RISKS.md` | مصفوفة مخاطر R1–R6 — كلها مُغلقة (انظر §5) |

## 2) خريطة المجلدات (قياس فعلي `du -sh` داخل `/workspace/wiki/archive-extract/`)

| المجلد | الحجم المقاس | ملفات | الغرض | ملفات/أقسام رئيسية |
|---|---|---|---|---|
| `00_INDEXES` | 1.4M | 17 | فهارس الحقيقة وتقارير ما قبل الأرشفة | `hashes.sha256` (395K)، `source_inventory.csv` (482K)، `conversations_index.csv` (165K)، `master_inventory.json`، `excluded_files.csv`، 10 تقارير `*.md` (GAP/SCAN/PLAN) |
| `01_SDCARD_DOCS` | 19M | 480 | وثائق/مشاريع ويكي أصل بطاقة الذاكرة | `wikillm/` (8.4M)، `root_files/` (9.0M: `NEW_WIKI_MASTER_PLAN.md`، `NEXUS_LLM_WIKI_REPORT.html`، `IGWIKI_ALL_IN_ONE.txt`، وثيقة السياق 8.7M)، `nexus_brain_wiki_docs/` (516K)، `NEXUS_WIKI_SKILLS/` (196K)، `NEXUS_PROJECT/` (192K: `INGEST_*`، `memory.md`) |
| `02_ROOT_DOCS` | 2.2M | 16 | توثيق بيئة الجذر `/root/r` | `session_logs/` (`wiki`، `wiki.md`، `wiki1.md`، `الويكي.md`)، `architecture/` (V3 + تدقيق NB2/V1 + كتالوجات)، `hubs/` (`WIKI_HUB/`، `nexus_wiki_links/`)، `scripts/process_wiki_loop.sh` |
| `03_WIKI_LAYERS` | 14M | 434 | طبقات V1/V2/V3 دون تكرار ثقيل | `nexus_wiki/` (8.0M: `00_PROJECT`→`06_TOOLS`)، `wiki_small_layers/` (6.1M: نسخ V1/V2/S-V1 مقلَّمة)، `BIG_FILE_POINTERS.csv` |
| `04_NEXUS_LLM_WIKI_CORE` | 7.2M | 291 | نواة تشغيل Nexus LLM Wiki | `reports/` (1.8M)، `indexes/` (2.7M)، `done/` (784K)، `tools/` (500K)، `systems/` (440K)، `concepts/` (192K)، `config/` (52K)، `BIG_FILE_POINTERS.csv` (389K)؛ مدخلات: `INDEX.md`، `START_HERE.md`، `AGENTS.md`، `SCHEMA.md`، مواثيق 2026-10-08..10 |
| `05_CONVERSATIONS` | 150M | 990 | محادثات المصادر الأربعة (أكبر قسم: 71% من الحجم) | `agy/` 46M، `omnirush/` 46M، `opencode/` 34M، `claude/` 26M (تفصيل §3) |
| `06_CODE_TOOLS` | 17M | 304 | كود بناء/إضافة الويكي | `llm-wiki-compiler/` (11M)، `llm-wiki-plugin/` (5.5M) |
| `07_ENRICHMENT_CORE` | 2.1M | 175 | خط إثراء وتوجيه الماسترز | `control/` 456K، `wiki_routing/` 1.6M (146 ملف `Master_*`)، `reports_subset/` 80K (11 تقرير) |
| `_RESERVE` | 8K | 1 | حيز أمان طوارئ | `README.md` فقط — سقف مُعلن 24MB غير مستخدم |

## 3) تفصيل `05_CONVERSATIONS` (المحادثات)

| القسم | الحجم | المحتوى | ملاحظة |
|---|---|---|---|
| `claude/` | 26M | 14 JSONL خام، `conversations_backup/` 7 جلسات يونيو 2026 (16M)، 8 مهارات، `digest-96.md`، `history_wiki_filtered.jsonl` (28 سطراً) | مكتمل |
| `opencode/` | 34M | 52 جلسة: `main_db/` 45 (24.3M: 2607 رسالة) + `backup_db/` 7 (9.3M: 143 رسالة) = 2750/8594 | النطاق A فقط؛ لا تُنسخ `.db`؛ `README` كتبه في يونيو يصف AGY/OmniRush «لاحقاً» بينما الأرشيف النهائي يشملهما |
| `agy/` | 46M | `core_wiki_sessions/` 20 جلسة تأسيسية (SQLite أصلي) + `brain_logs/` + `tier1_strong/` JSONL + `index.csv` موثق 173 جلسة | نواة Cognitive Wiki OS + SYS_01..15 |
| `omnirush/` | 46M | `topic_sessions/` (من 826 جلسة مطابقة) + `db_extracted/` نصوص `part` JSONL + `index.csv` | الأعلى عدداً (~620 ملفاً حسب الوثيقة) |

## 4) أهم 20 نقطة دخول (مسارات دقيقة داخل الأرشيف)

1. `WIKI_ARCHIVE_2026-11-03/README.md` — خريطة سيادية + تحقق
2. `WIKI_ARCHIVE_2026-11-03/MANIFEST.json` — فهرس SHA-256 الشامل
3. `WIKI_ARCHIVE_2026-11-03/00_INDEXES/source_inventory.csv` — جرد كل ملف مصدري
4. `WIKI_ARCHIVE_2026-11-03/00_INDEXES/conversations_index.csv` — فهرس المحادثات الموحد
5. `WIKI_ARCHIVE_2026-11-03/04_NEXUS_LLM_WIKI_CORE/AGENTS.md` — تعليمات تشغيل النواة وقواعدها
6. `WIKI_ARCHIVE_2026-11-03/04_NEXUS_LLM_WIKI_CORE/INDEX.md` — فهرس ملاحي + بوابات `sales`→`outreach`→`pricing_offers`→`content_strategy`
7. `WIKI_ARCHIVE_2026-11-03/04_NEXUS_LLM_WIKI_CORE/START_HERE.md` — أول ما يُقرأ في النواة
8. `WIKI_ARCHIVE_2026-11-03/04_NEXUS_LLM_WIKI_CORE/config/processing_order.json` — الحالة الوحيدة للترتيب
9. `WIKI_ARCHIVE_2026-11-03/01_SDCARD_DOCS/wikillm/BUILD_PROTOCOL.md` — بروتوكول بناء wikillm
10. `WIKI_ARCHIVE_2026-11-03/01_SDCARD_DOCS/root_files/NEW_WIKI_MASTER_PLAN.md` — الخطة الأم
11. `WIKI_ARCHIVE_2026-11-03/01_SDCARD_DOCS/nexus_brain_wiki_docs/NEXUS_BRAIN.md` — مخطط الدماغ المعرفي
12. `WIKI_ARCHIVE_2026-11-03/05_CONVERSATIONS/claude/README.md` + `.../claude/index.csv`
13. `WIKI_ARCHIVE_2026-11-03/05_CONVERSATIONS/opencode/README.md` + `.../opencode/index.csv`
14. `WIKI_ARCHIVE_2026-11-03/00_INDEXES/WIKI_ARCHIVE_EXECUTION_PLAN.md` (46K) — خطة التنفيذ والميزانيات
15. `WIKI_ARCHIVE_2026-11-03/00_INDEXES/GAP_CLOSURE_REPORT.md` + `GAP_SIZES_REPORT.md` — سد الفجوات وقياسها
16. `WIKI_ARCHIVE_2026-11-03/03_WIKI_LAYERS/BIG_FILE_POINTERS.csv` — توثيق استثناء `index.json.gz`
17. `WIKI_ARCHIVE_2026-11-03/07_ENRICHMENT_CORE/control/BRAIN_GOVERNANCE.md` — حوكمة الإثراء
18. `WIKI_ARCHIVE_2026-11-03/FALLBACK.md` — سلّم F0–F6
19. `WIKI_ARCHIVE_2026-11-03/RISKS.md` — مصفوفة R1–R6
20. `WIKI_ARCHIVE_2026-11-03/00_INDEXES/hashes.sha256` — التحقق السريع لكل ملف

## 5) مخاطر/استثناءات/مفقودات (من `RISKS.md` و`FALLBACK.md` و`00_INDEXES`)

- **لا حذف:** R2 مغلق؛ أي تفعيل FALLBACK يكون باختيار انتقائي لا `rm`.
- **R1/R4:** حظر نسخ `.db` >50MB وتضخمه (QX العملاقة 958/446MB)؛ الاستخراج فقط JSONL بـ `mode=ro`.
- **R6 — مستثناة وموثقة (لا مفقودة أبداً):** `index.json.gz` 17.8MB ×2 (بصمة `99c8cb…`)؛ `raw/` النواة 53MB؛ سجل `full_evidence_ledger`؛ كاش `pycache`/`node_modules`/`.git` (توفير 3.7MB)؛ `state/runs` و`media_shard*` و`kaggle/standalone_*` من `nexus_enrichment` (~207MB)؛ كلها مفصلة بـ `BIG_FILE_POINTERS.csv` و`excluded_files.csv` وأقسام «ما استُثني» في READMEs.
- **FALLBACK (F0–F6):** F1 OmniRush ~27MB، F2 AGY ~15MB، F3 كود غير نصي ~8MB، F4 توجيه النواة ~10MB، F5 `nexus_wiki` فقط ~4MB، F6 OpenCode أعلى 20 ~13MB. **النواة المحمية أبداً:** `00_INDEXES` + `01_SDCARD_DOCS` + `02_ROOT_DOCS` + `claude`.
- **تضارب موثق واحدة:** `05_CONVERSATIONS/README.md` (كتابة مبكرة) يصف `agy/omnirush` «مجدول لاحقاً» بينما `README.md` الجذري و`EXPORT_NOTES.md` والأرشيف الفعلي (46+46MB) يؤكدان اكتمالهما. القاعدة: الفعلي على القرص + الجذري هو المرجع.
- **ما لم يفعَّل:** سلّم FALLBACK لم يُفعَّل (توفَّر 497MB حرة بدل عتبة 30MB).

## 6) خلاصة كمّية

الجذر ~1MB · `00` 1.4M · `01` 19M · `02` 2.2M · `03` 14M · `04` 7.2M · `05` 150M · `06` 17M · `07` 2.1M · `_RESERVE` 8K = **~212M / 2713 ملفاً** — ضمن ميزانية 250MB ✅

DONE
