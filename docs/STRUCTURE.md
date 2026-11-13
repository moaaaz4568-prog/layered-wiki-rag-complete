# STRUCTURE — شجرة المستودع الشرحية

> الحالة: ملفات §§2-4 موجودة على القرص (42 ملفاً في repo/ في 2026-11-05 — `find repo/ -type f | wc -l` = 42) [OBSERVED 2026-11-05]؛ طبقات §5 raw/wiki/terms/src مخططة فقط، غير موجودة في repo/ الآن — بنية مخططة في `../work/repo-plan-01.md` §2 (خارج المستودع).
> المصدر: `analysis-wiki-talk-01.md` §4.3 + `repo-plan-01.md` §2.
> وسم الدليل: OBSERVED = مقاس على القرص، REPORTED = منقول من تقرير، PROPOSED = مقترح مستقبلي، UNKNOWN = لا دليل، NOT_RUN = لم يُشغَّل بعد.

## 1. المستودع الحالي

- الاسم المقترح: `layered-wiki-rag` | REPORTED — `analysis-wiki-talk-01.md` §4.1
- مستودع خاص (Private) | REPORTED — `analysis-wiki-talk-01.md` §1.2 + §3.2
- المستودع الحالي `layered-wiki-rag` | REPORTED — `../work/repo-plan-01.md` §1.3 (خارج المستودع) — العدد التاريخي كان 5 ملفات حسب الخطة وقت كتابتها [REPORTED تاريخي — `../work/repo-plan-01.md` §1.3]؛ الحالي في 2026-11-05 = 42 ملفاً على القرص (`find repo/ -type f | wc -l`) [OBSERVED 2026-11-05]
- القرار: استخدام الحالي لا جديد | REPORTED — `repo-plan-01.md` §1.3
- إجمالي المستودع النصي المستهدف | PROPOSED — `repo-plan-01.md` §2

## 2. الجذر

- `README.md` — نقطة الدخول: الغاية + السياسات الست + خريطة القراءة | PROPOSED — `repo-plan-01.md` §3.1
- `CONTEXT.md` — ملف سياق: يكفي لـ AI جديد دون قراءة الأرشيف | PROPOSED — `repo-plan-01.md` §3.1
- `MESSAGES.md` — «كل ما قلته» مرتبة زمنيًا | PROPOSED — `repo-plan-01.md` §3.1
- `IDEAS.md` — الأفكار والقرارات المفصلة | PROPOSED — `repo-plan-01.md` §3.1
- `ARCHITECTURE.md` — المعمارية الهجينة الكاملة | PROPOSED — `repo-plan-01.md` §3.1
- `MASTER.md` — تعريف الماستر + فهرس الماسترز | PROPOSED — `repo-plan-01.md` §3.1
- `REJECTED.md` — المرفوض المعلل + بديله | PROPOSED — `repo-plan-01.md` §3.1
- `CHANGELOG.md` — سجل التغييرات من commit الحالي | PROPOSED — `repo-plan-01.md` §3.1
- `PROVENANCE.md` — المنشأ والتحقق: مصادر + MANIFEST | PROPOSED — `repo-plan-01.md` §3.1
- `AGENTS.md` — تعليمات الوكلاء | PROPOSED — `repo-plan-01.md` §3.1
- `.gitignore` + `.env.example` — منع الأسرار والضخم (مرجع بلا قيمة) | PROPOSED — `repo-plan-01.md` §2

## 3. مجلد docs/

- `docs/` — ملفات مفهرسة مختصرة (≤8KB لكل ملف حسب الخطة) | PROPOSED — `repo-plan-01.md` §3.2
- `docs/STRUCTURE.md` (هذا الملف) — الشجرة الشرحية | PROPOSED — `repo-plan-01.md` §3.2
- `docs/GOALS.md` — الأهداف القابلة للاختبار (5 نقاط) | PROPOSED — `repo-plan-01.md` §3.2
- `docs/RULES.md` — القواعد الحاكمة (13 قاعدة) | PROPOSED — `repo-plan-01.md` §3.2
- `docs/CONCEPTS.md` — قاموس المفاهيم | PROPOSED — `repo-plan-01.md` §3.2
- `docs/METADATA-SCHEMA.md` — حقول المقطع حقلًا حقلًا | PROPOSED — `repo-plan-01.md` §3.2
- `docs/CHUNKING.md` — سياسة التقطيع | PROPOSED — `repo-plan-01.md` §3.2
- `docs/EVALUATION.md` — التقييم: Recall@k / Faithfulness | PROPOSED — `repo-plan-01.md` §3.2
- `docs/CONTRADICTION-POLICY.md` — التناقض | PROPOSED — `repo-plan-01.md` §3.2
- `docs/KNOWN-ANSWER-SET.md` — 20 سؤالًا معروفًا (غير مبني بعد) | PROPOSED — `repo-plan-01.md` §3.2
- `docs/STAGES.md` — المراحل v0.1 وما بعدها | PROPOSED — `repo-plan-01.md` §3.2
- `docs/SOURCES.md` — روابط خارجية | PROPOSED — `repo-plan-01.md` §3.2

## 4. مجلدات أخرى

- `masters/` — الماسترز: لا تُزرع ماسترز حقيقية في v0.1؛ وثيقة طريقة التوليد فقط | PROPOSED — `repo-plan-01.md` §2
- `masters/review/checklist.md` — قائمة مراجعة بشرية قبل الاعتماد | PROPOSED — `repo-plan-01.md` §2
- `sources/` — فهارس خارجية: wiki-talk + archive + session + inventory + links | PROPOSED — `repo-plan-01.md` §2
- `timeline/` — تسلسل زمني 2026-10-06 → 2026-11-05 | PROPOSED — `repo-plan-01.md` §3.3
- `reference/` — الغايات وخارج النطاق (purposes + non-goals) | PROPOSED — `repo-plan-01.md` §3.3
- `templates/` — قالب مصطلح + قالب ماستر | PROPOSED — `repo-plan-01.md` §2
- `config/` — personas.yaml + books.yaml + models.yaml + thresholds.yaml | PROPOSED — `repo-plan-01.md` §2
- `index/` — مؤشر فهرس 5,896 صفحة + نتائج BM25 المقاسة على هيثم | PROPOSED + OBSERVED — `repo-plan-01.md` §2

## 5. طبقات البيانات (من التصميم)

> **ملاحظة صريحة:** طبقات §5 أدناه كلها [PROPOSED] — مخطط فقط، غير موجود في repo/ الآن. فُحص على القرص في 2026-11-05: `raw/` و`wiki/` و`terms/` و`src/` و`bin/` و`skills/` و`tests/` و`snapshots/` و`out/` كلها غائبة من repo/؛ `index/` الموجودة هي مجلد وثائق (bm25-results.md + manifest-pointer.md) لا طبقة كود. كل سطر أدناه يصف التصميم [REPORTED] لا موجودًا على القرص.

- `raw/` — طبقة الخام: للقراءة فقط، لا تُعدَّل أبدًا | PROPOSED — مخطط فقط، غير موجود في repo/ الآن | REPORTED — `../work/analysis-wiki-talk-01.md` §1.8 القاعدة 8 (خارج المستودع)
- `wiki/` — طبقة الويكي المترجمة (تجميع لا حقيقة) | PROPOSED — مخطط فقط، غير موجود في repo/ الآن | REPORTED — `../work/analysis-wiki-talk-01.md` §4.3 (خارج المستودع)
- `terms/` — المصطلحات أولاً وقبل الماستر | PROPOSED — مخطط فقط، غير موجود في repo/ الآن | REPORTED — `../work/analysis-wiki-talk-01.md` §1.8 القاعدة 3 (خارج المستودع)
- `index/` (كود) — BM25 ثم Dense ثم Hybrid/RRF/Rerank | PROPOSED — مخطط فقط، غير موجود في repo/ الآن (الموجود `index/` وثائق فقط) | REPORTED — `../work/analysis-wiki-talk-01.md` §4.3 (خارج المستودع)
- `src/` — ingest → retrieve → generate → audit → eval → tools | PROPOSED — مخطط فقط، غير موجود في repo/ الآن | REPORTED — `../work/analysis-wiki-talk-01.md` §4.3 (خارج المستودع)
- `bin/` — سكربتات yt-wiki النظيفة (download → build → ask) | PROPOSED — مخطط فقط، غير موجود في repo/ الآن | REPORTED — `../work/analysis-wiki-talk-01.md` §1.4 (خارج المستودع)
- `skills/` — مهارة yt-wiki + wiki-build + rag-pipeline | PROPOSED — مخطط فقط، غير موجود في repo/ الآن | REPORTED — `../work/analysis-wiki-talk-01.md` §4.3 (خارج المستودع)
- `tests/` — اختبارات BM25 + Dense-vs-keyword + Known-answer | PROPOSED — مخطط فقط، غير موجود في repo/ الآن | REPORTED — `../work/analysis-wiki-talk-01.md` §4.3 (خارج المستودع)
- `snapshots/before-bulk/` — لقطة قبل أي تغيير جماعي (هذا فقط يُرفع) | PROPOSED — مخطط فقط، غير موجود في repo/ الآن | REPORTED — `../work/analysis-wiki-talk-01.md` §4.3 (خارج المستودع)
- `out/` — مخرجات تجريبية (غير متتبع) | PROPOSED — مخطط فقط، غير موجود في repo/ الآن | REPORTED — `../work/analysis-wiki-talk-01.md` §4.3 (خارج المستودع)

## 6. القياسات الرقمية المرجعية

- 6 ويكيات، 5,896 صفحة، 31.3MB (31,262,266 بايت) | OBSERVED — `analysis-wiki-talk-01.md` §1.7
- ابن سيرين 780، ابن تيمية 81، ابن القيم 556، هيثم طلعت 210، عماد رشاد 1,423، علاء حامد 2,846 | OBSERVED — `analysis-wiki-talk-01.md` §1.7
- هيثم كامل: 210 صفحة، 601,084 بايت | OBSERVED — `analysis-wiki-talk-01.md` §1.10
- أصغر 20 صفحة لهيثم: 37,402 بايت، 129 مقطعًا | OBSERVED — `analysis-wiki-talk-01.md` §1.7
- متوسط صفحة هيثم 2,336 بايت مقابل ابن تيمية 10,458 بايت | OBSERVED — `analysis-wiki-talk-01.md` §1.7
- أرشيف الويكي الكامل: 212MB، 2,713 ملفًا على القرص | OBSERVED — `sources/file-inventory.md` + المصدر الخارجي `../work/archive-inventory-01.md` §2، §6 (خارج المستودع)
- `05_CONVERSATIONS`: 150M، 990 ملفًا (أكبر قسم) | OBSERVED — `sources/file-inventory.md` + المصدر الخارجي `../work/archive-inventory-01.md` §2 (خارج المستودع)

## 7. ما يُمنع رفعه أبدًا

- `MANIFEST.json` الكامل (780K) — يُشار إليه بمؤشر فقط | REPORTED — `repo-plan-01.md` §1.2 + §2
- `conversations_index.csv` + `source_inventory.csv` الكاملة | REPORTED — `repo-plan-01.md` §2
- كل `*.db` أو `*.opus` أو `*.env` (غير `.env.example`) أو `*.log` | REPORTED — `repo-plan-01.md` §2 + §1.2
- ملفات `cookies.txt` / `.hcnsec_key` / `zcode-*` / كل أسرار | REPORTED — `repo-plan-01.md` §1.2
- VTT الخام 47MB + TXT للأثرة الصحية — مؤشر فقط | REPORTED — `repo-plan-01.md` §2
- أي قيمة سرية (PAT/مفاتيح/كوكيز) — لا تُنسخ أبدًا | REPORTED — `repo-plan-01.md` §1.2

## 8. الحجم المستهدف للوثائق

- إجمالي المستودع النصي: 1.2–1.8MB (دون الأرشيف الخام) | PROPOSED — `repo-plan-01.md` §2
- ملفات `docs/` مختصرة: كل ملف ≤8KB | PROPOSED — `repo-plan-01.md` §3.2
