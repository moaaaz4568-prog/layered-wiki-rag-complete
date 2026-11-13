# خطة المستودع الموحّد — layered-wiki-rag (لم تُكتب، تُخطط فقط)

> **الحالة:** خطة تخطيطية فقط. لا Deliverable نهائي هنا.
> **المصادر المقروءة:** `work/analysis-wiki-talk-01.md` (66KB, 712 سطرًا) · `work/analysis-session-01.md` (85 سطرًا) · `work/archive-inventory-01.md` (79 سطرًا) · `work/research-01.md` (<s>38 سطرًا، مسودة تُستكمل</s> 48 سطرًا — **COMPLETE**، صحّح في 2026-11-05؛ انظر تعديل §4 أدناه) · `transfernow-download/prompt.md` (233 سطرًا، فيديو — خارج النطاق ما عدا حدودًا) · `promptastra6fgss.md` (عناوين فقط، يُوسّع لاحقًا من `layered-wiki-rag-design.md` 92KB).
> **المالك:** `moaaaz4568-prog` — مستودع خاص (Private). المستودع الحالي `layered-wiki-rag` (commit `5b70e59`، 5 ملفات) موجود — انظر §1 للقرار.

---

## 1) الهدف والقيود

### 1.1 الهدف (بجملة واحدة)
مستودع GitHub واحد خاص، منظّم، يشرح **كل شيء** أُنجز وقيل عن الويكي بحيث يفتحه أي AI chat جديد فلا يحتاج إعادة مطالعة الأرشيف: README + ملف سياق + ملف «كل ما قلته» + ملفات أفكار + ملفات Masters/هيكل + مصادر — دون مطالبة بالنصوص الكاملة (2,713 ملف/212MB).

### 1.2 قيود صارمة (لا تُكسَر)
1. **Private فقط** — لا نشر عام، لا Manifest.json الكامل (780KB)، لا المحادثات الخام 150MB في GitHub. الأصلي يبقى محليًا.
2. **لا اختراع حقائق** — كل رقم له أمر قياس أو يُوسم تقديرًا. ما لم يُقرأ = **UNKNOWN**.
3. **وصم الدليل (Evidence Labels) إجباري** في كل ملف:
   - `OBSERVED` = مقاس/مقروء مباشرة على القرص (مع الأمر/المسار).
   - `REPORTED` = منقول من تقرير/رسالة آخر بدون فحص مباشر.
   - `PROPOSED` = اقتراح/قرار مستقبلي غير منفَّذ.
   - `UNKNOWN` = لا يوجد دليل.
   - `NOT_RUN` = تجربة/اختبار مقترح ولم يُشغَّل بعد.
4. **لا أسرار أبدًا** — منع: مفتاح GitHub PAT (ظهر في الجلسة — يُلغى ويُدوَّر)، مفاتيح Yukino/hcnsec، كوكيز يوتيوب، `.env`، `*.db` >50MB، سجلات `zcode-*`/`cloudflared.log`، ملفات `cookies.txt`. قيم الأسرار لا تُنسخ؛ يُذكر وجودها فقط.
5. **Raw للقراءة فقط** — حقائق من `MANIFEST.json`/`hashes.sha256` لا تُعاد كتبتها، بل تُشار إليها بمسار.
6. **العينة أولًا** — لا نقل جماعي لـ5,896 صفحة ولا 212MB مرة واحدة. v0.1 = هيثم فقط ثم شخصية شخصية.
7. **العمل بالـ sub-agents** — كل عملية بنظام حرفي، المشرف يخطط ويوجه ويفحص فقط.

### 1.3 قرار المستودع: استخدام الحالي أم جديد؟
**القرار: استخدام `moaaaz4568-prog/layered-wiki-rag` الحالي (لا جديد).**
المبرر: (أ) الاسم «layered-wiki-rag» هو المقترح أصلاً في التحليل §4.1؛ (ب) خاص وموجود وبه 5 ملفات «آمنة» وcommit موثّق؛ (ج) فيه التصميم `layered-wiki-rag-design.md` (92KB) والـ HTML المقروء؛ (د) إنشاء جديد يخلط المرجع. الخطر الوحيد: إصدار `v1.0.0` يعيد 404 (`analysis-session-01.md` §5) — يُوثَّق كعنصر مفقود لا يُخترع بديله. البديل (مستودع جديد `wiki-everything`): مرفوض — يصعب التتبع والمراجعة. **يُعاد تسمية/توحيد الغاية عبر README الجديد + توثيق الفجوة.**

---

## 2) شجرة المجلدات والملفات النهائية

> الحجم = حجم تقريبي للملف النصي المستهدف (توجيه لا وعد). إجمالي المستودع المنصوصي ≈ **1.2–1.8MB** (دون الأرشيف الخام).

```
layered-wiki-rag/                                   (خاص)
├─ README.md                     (~15KB)   نقطة الدخول ودليل القراءة
├─ CONTEXT.md                    (~30KB)   ملف السياق: ما يعرفه الـ AI الجديد دون إعادة قراءة
├─ MESSAGES.md                   (~45KB)   «كل ما قلته» — طلبات حرفية مرتبة زمنيًا
├─ IDEAS.md                      (~30KB)   الأفكار: قرارات/مفاهيم/مقترحات مخصصة
├─ ARCHITECTURE.md               (~25KB)   المعمارية الهجينة الكاملة (من التصميم)
├─ MASTER.md                     (~20KB)   الفهرس الجامع: كل الماسترز ومن أين جاءت
├─ REJECTED.md                   (~8KB)    المرفوض المعلل
├─ CHANGELOG.md                  (~5KB)    سجل التغييرات
├─ PROVENANCE.md                 (~10KB)   المنشأ والتحقق: قائمة مصادر + MANIFEST
├─ AGENTS.md                     (~6KB)   تعليمات الوكلاء (مرحلة v0.1: root فقط)
├─ .gitignore                    (~0.5KB) منع الأسرار والضخم
├─ .env.example                  (~0.2KB) مرجع بلا قيمة
├─ docs/
│  ├─ STRUCTURE.md               (~15KB)  شجرة المستودع الشرحية + معنى كل مجلد
│  ├─ GOALS.md                   (~5KB)   الأهداف القابلة للاختبار (5 نقاط)
│  ├─ RULES.md                   (~8KB)   القواعد الحاكمة (عدم الحذف/الادعاء/...)
│  ├─ CONCEPTS.md                (~10KB)  قاموس مفاهيم سطرين لكل مفهوم
│  ├─ METADATA-SCHEMA.md         (~6KB)  حقول المقطع/الصفحة حقلًا حقلًا
│  ├─ CHUNKING.md                (~5KB)  سياسة التقطيع (عنوان/فقرة/جدول)
│  ├─ EVALUATION.md              (~6KB)  التقييم: Recall@k / Faithfulness
│  ├─ CONTRADICTION-POLICY.md    (~5KB)  التناقض: ميكانيكي أم عرض الطرفين
│  ├─ KNOWN-ANSWER-SET.md        (~8KB)  20 سؤالًا معروفًا (هيثم: تُبنى بعد v0.1 — PROPOSED)
│  ├─ STAGES.md                  (~6KB)  المراحل v0.1 → شخصية → واجهة → جراف
│  └─ SOURCES.md                 (~10KB)  فهرس المصادر الخارجية والروابط
├─ masters/
│  ├─ README.md                  (~4KB)   كيف تُكتب الماستر (مصطلحات → مجلد → ماستر)
│  ├─ review/
│  │  └─ checklist.md           (~3KB)   قائمة مراجعة بشرية قبل الاعتماد
│  └─ (لا تُزرع ماسترز حقيقية في v0.1 — تُوثَّق طريقة التوليد فقط؛ أي ماستر لاحق = OBSERVED)
├─ sources/
│  ├─ wiki-talk-index.md         (~12KB)  فهرس 106 رسالة (2026-10-06 → 2026-11-03) + أول ذكر
│  ├─ archive-index.md           (~15KB)  خريطة الأرشيف 212MB/2713 ← مسار داخل الأرشيف
│  ├─ session-export-index.md    (~8KB)  فهرس الجلسة 18267 سطرًا + الرسائل الـ19
│  ├─ file-inventory.md          (~12KB)  جرد الملفات المقاسة (wiki-rag/wiki-project/...)
│  └─ links.md                   (~6KB)  روابط خارجية (يوتيوب/TransferNow/GitHub)
├─ timeline/
│  └─ timeline.md                (~15KB)  التسلسل الزمني من 2026-10-06 إلى 2026-11-05
├─ reference/
│  ├─ purposes.md                (~5KB)  الغايات: عقول متخصصة + ماسترز + وجود التفكير
│  └─ non-goals.md               (~3KB)  خارج النطاق: فيديو/صوت (نطاق الأمن §1.2.4)
├─ templates/
│  ├─ term.md                    (~1KB)   قالب مصطلح (اسم+تعريف+مصدر)
│  └─ master.md                  (~1KB)   قالب ماستر (رئيسي + إحالات)
├─ config/
│  ├─ personas.yaml              (~2KB)   6 شخصيات (slug + domain + بطاقة)
│  ├─ books.yaml                 (~2KB)   قوائم كتب (يُعاد من yt-wiki)
│  ├─ models.yaml                (~1KB)   مرشحون مشروطون بالاختبار (لا اختيار مفروض)
│  └─ thresholds.yaml            (~1KB)   عتبات k / Recall / زمن (تُملأ بعد أول قياسين)
├─ index/
│  ├─ manifest-pointer.md        (~3KB)  مؤشر لفهرس 5,896 صفحة (لا نسخة كاملة)
│  └─ bm25-results.md            (~8KB)  نتائج BM25 المقاسة على 20 + 210 هيثم
└─ DESIGN-REFERENCE.md           (~3KB)   موقع ملف التصميم في المستودع الحالي
```

**ملفات ممنوعة من الرفع (تُستبعد بـ `.gitignore`):** `MANIFEST.json` الكامل، `conversations_index.csv`، `source_inventory.csv`، كل `*.db`، `*.opus`، ملفات `cookies.txt`/`.hcnsec_key`/`zcode-*`، `VTT` الخام 47MB، TXT للأثرة الصحية → تُشار إليها فقط بمؤشر.

---

## 3) محتوى كل ملف على مستوى العناوين (Outline)

### 3.1 الجذور
- **README.md**
  - 1. ماذا يشرح كل شيء (الغاية العامة) · 2. السياسات الست الحاكمة (Private/لا اختراع/الوصم/الأسرار/Raw/العينة أولًا) · 3. خريطة القراءة: من أين تبدأ (CONTEXT → MESSAGES → IDEAS → MASTER) · 4. الغاية الكبرى (عقول متخصصة/الماسترز/النموذج الذي يرى كل ويكي) · 5. حالات OBSERVED المثبتة (5,896 صفحة/31.3MB؛ BM25 على 210 هيثم: 12/15) · 6. ما يجري NOT_RUN (bge-m3/إعادة الترتيب/الجراف) · 7. قرار المستودع والفجوة 404 · 8. الأسرار: لا شيء هنا — إن وُجدت أوقف.
- **CONTEXT.md** (يجب أن يكفي لـ AI جديد دون قراءة أي شيء آخر)
  - 1. المشروع باختصار (هدف معاذ الحرفي + «كل ملف يدخل بكل محتواه» + «مصطلحات أولاً») · 2. الوضع الحالي المقاس (OBSERVED: 6 ويكيات/5,896 صفحة؛ الأنظمة الثلاثة Muse/wikillm/Infinite Brain؛ BM25 نتائج) · 3. قواعد العمل (العينة أولًا؛ ملف نظام لكل عملية؛ sub-agents؛ مراجعة بشرية؛ لا ادعاء قبل فحص القرص) · 4. المفتوح/المتعارض (§1.2 + §3.3 الأصلي: الحجر vs كل ملف؛ رؤية شاملة vs استرجاع) · 5. من أين يُجلب أي شيء (مؤشرات أرشيف لا نسخ) · 6. كيف تُعلّم محتويات جديدة (تعليم وسوم الدليل + تحديث stamps).
- **MESSAGES.md**
  - 1. قائمة الطلبات الحرفية مرتبة زمنيًا (106 رسالة — نص كامل + تاريخ + سياق) · 2. قرارات حاسمة مشتقة (مثل 2026-10-19 17:32: yt-dlp TXT فقط) · 3. الطلبات المفتوحة (REMinder: glm مفتاح لحظياً/إعادة تشغيل) · 4. سجل الإقرارات/النفي (مثل: لم تُجرَّب الـ build-wiki على قناة جديدة).
- **IDEAS.md**
  - 1. المفهوم (ويكي/خام/مصطلح/ماستر/تضمين/مقطع/GraphRAG/OKF) · 2. الأفكار من برومبت المستخدم (ملف نظام متكامل + books.yaml + وضع المفاتيح) · 3. الأفكار المعمارية (RAG أساس + فلتر شخصية إجباري + استشهاد بالمقطع) · 4. الأفكار المؤجلة (جراف/ذاكرة فرق) · 5. كل فكرة بوسم دليل ومصدر.
- **ARCHITECTURE.md**
  - 1. الطبقات (raw → wiki → terms → masters → index) · 2. فلتر الشخصية الإجباري · 3. BM25/Dense/Hybrid → RRF → Rerank (بعد اختبار) · 4. Metadata Schema · 5. التقطيع · 6. التقييم (Recall@10) · 7. إدارة دورة الحياة (scratch→canon؛ ترقية بموافقة إنسان) · 8. فصل التوليد عن الفهرسة.
- **MASTER.md**
  - 1. تعريف الماستر (ملف يقرأه النموذج مرة ويصبح خبيرًا) · 2. طريقة التوليد (مصطلحات كاملة → مجلد → ماستر؛ رئيسي + فرعيات بالإحالة) · 3. فهرس الماسترز (الحقيقي الموجودة: لا ماسترز نشطة بمحتوى مثبت؛ 27,742 ذرة مقابل 5 ماسترز في wikillm = خرق) · 4. بوابة مراجعة الاعتماد (§review).
- **REJECTED.md**
  - قرار مرفوض + بديله + سبب الرفض (ماستر قبل مصطلح؛ نظام ادعاءات رغم الرفض؛ BGE-M3 قبل اختبار؛ بوابة G2 معطوبة؛ RRF/هجين بلا تنفيذ؛ نقل جماعي؛ جراف كبداية؛ نشر عام الآن).
- **CHANGELOG.md** — من commit الحالي `5b70e59` + الإضافة الجديدة + فجوة 404 (لا يُخترع بديل).
- **PROVENANCE.md** — 1. قائمة المصادر الأولية (كلام الويكي 106 رسالة/الأرشيف/Jلسة 18267/تصميم 92KB/برومبت) · 2. ما قُروء مباشرة (OBSERVED) مقابل منقول (REPORTED) · 3. روابط MANIFEST/hashes (دون قيم) · 4. ما لم يُفتح (wikillm على /sdcard).
- **AGENTS.md** — تعليمات الوكلاء: sub-agents دائمًا،: غياب git ذاتي، معايير QA، فحص قبل إعلان نجاح — يُبنى من `03_WIKI_LAYERS/BIG_FILE_POINTERS.csv`? لا: `04_NEXUS_LLM_WIKI_CORE/AGENTS.md` + `01_SDCARD_DOCS/wikillm/BUILD_PROTOCOL.md` (REPORTED حتى الفحص).

### 3.2 docs/ — (مفهرس، كل ملف ≤8KB مختصر)
- `STRUCTURE.md`: شجرة كاملة مشروحة (معنى كل مجلد + ما يُمنع رفعه).
- `GOALS.md`: 5 نقاط قابلة للاختبار (رؤية/تحديد/إجابة/صوت المنظور/ثقة).
- `RULES.md`: 13 قاعدة حاكمة (§1.8 الأصلي: لا اختراع/الخام حقيقة/لا توسع على فشل/...).
- `CONCEPTS.md`: كل مفهوم في سطرين.
- `METADATA-SCHEMA.md`: حقول المقطع الحقلية.
- `CHUNKING.md`: تعريف المقطع + حالات النص بلا عناوين/الجداول.
- `EVALUATION.md`: Recall@k / Faithfulness + الـ 20 سؤالًا + قاعدة «لا توسع على فشل».
- `CONTRADICTION-POLICY.md`: تناقض ميكانيكي ↔ عرض الطرفين ↔ آلية موافقة بشرية.
- `KNOWN-ANSWER-SET.md`: هيكل الـ 20 سؤالًا (PROPOSED — تُبنى من 10 صفحات هيثم بعد v0.1).
- `STAGES.md`: مرحلة 0 → نموذج → شخصية → واجهة → صيانة → جراف لاحقًا.
- `SOURCES.md`: روابط خارجية (Cognee/Infinite Brain OS/يوتيوب/144 فيديو/TransferNow).

### 3.3 masters/ و timeline/ و sources/
- **masters/README.md**: تعريف + خطوات التوليد + قاعدة «ماستر فقط بعد مصطلحات مجلده». **masters/review/checklist.md**: checklist الاعتماد (موافقة إنسان + إثبات حي + استشهاد).
- **timeline/timeline.md**: 2026-10-06 (ويكيات التعافي/السيرة) → 2026-10-19 (yt-wiki + yt-dlp فقط) → 2026-10-30 (RAG + قياس 5,896) → 2026-10-31 (144 فيديو + معمارية هجينة) → 2026-11-01 (Infinite Brain) → 2026-11-02 (BM25 210) → 2026-11-03 (الأرشيف 212MB + جمود الرام) → 2026-11-05 (هذه الخطة).
- **sources/**: `wiki-talk-index.md` (106 رسالة: تاريخ/موضوع/القرار المستنتج) · `archive-index.md` (خريطة كل مجلد أرشيف بالقياس الفعلي + استثناءات R6) · `session-export-index.md` (18267 سطرًا: مواضع الرسائل 19 + المفتوح) · `file-inventory.md` (جداول: yt-wiki/wiki-project/wiki-rag/manifest) · `links.md` (كل الروابط الخارجية مع سياقها وتاريخها).
- **reference/**: `purposes.md` (الغايات: عقول متخصصة؛ الماستر؛ النظام المتكامل بملف واحد) · `non-goals.md` (خارج النطاق: الفيديو/الصوت — قرار معاذ 2026-11-03 "لا علاقته بالفيديو" — و `prompt.md` الفيديوي لا يدرج هنا).

---

## 4) من أين يأتي محتوى كل قسم (خريطة المصادر)

| القسم في المستودع | المصدر المباشر (مسار) | الدليل |
|---|---|---|
| README.md + CONTEXT.md | `work/analysis-wiki-talk-01.md` §1.1, §1.7, §1.11 + `work/analysis-session-01.md` §2 | OBSERVED |
| MESSAGES.md | `work/analysis-wiki-talk-01.md` §1 (النصوص الحرفية) + `work/analysis-session-01.md` §1 (الرسائل الـ19) | OBSERVED |
| IDEAS.md | `analysis-wiki-talk-01.md` §1.8–§1.11 + `analysis-session-01.md` §3 (خطة v0.1 + التجارب الست) | REPORTED |
| ARCHITECTURE.md + REJECTED.md | `layered-wiki-rag-design.md` (92KB) + `analysis-wiki-talk-01.md` §4–§5 | REPORTED |
| MASTER.md + masters/ | `01_SDCARD_DOCS/wikillm/` (الأرشيف) + `BUILD_PROTOCOL.md` + §1.8 الأصلي | REPORTED |
| docs/STRUCTURE.md | `archive-inventory-01.md` + `analysis-wiki-talk-01.md` §4.3 | OBSERVED |
| docs/GOALS.md | `analysis-wiki-talk-01.md` §1.8–§1.9 | REPORTED |
| docs/RULES.md | `analysis-wiki-talk-01.md` §1.8 (القائمة 13) | REPORTED |
| docs/CONCEPTS.md + CHUNKING.md | `analysis-wiki-talk-01.md` §1.8 الأصلية | REPORTED |
| docs/METADATA-SCHEMA.md | `01_SDCARD_DOCS/wikillm/29_raw_sources_map.md` (الأرشيف) | REPORTED |
| docs/EVALUATION.md + KNOWN-ANSWER-SET.md | `analysis-wiki-talk-01.md` §1.10 (نتائج BM25) | OBSERVED (النتائج) / PROPOSED (الـ20 سؤالًا) |
| docs/CONTRADICTION-POLICY.md | `analysis-wiki-talk-01.md` §3.3 | PROPOSED (لم يُحسم) |
| docs/STAGES.md + SOURCES.md | `analysis-wiki-talk-01.md` §4.2 + §2.1 | REPORTED |
| sources/wiki-talk-index.md + timeline.md | `analysis-wiki-talk-01.md` §1–§2 | OBSERVED |
| sources/archive-index.md + file-inventory.md | `archive-inventory-01.md` + `du -sh` داخل `archive-extract/` (OBSERVED) | OBSERVED |
| sources/session-export-index.md + links.md | `analysis-session-01.md` §2–§5 + `prompt.md` (حدود فقط — لا يُدرج) | OBSERVED |
| PROVENANCE.md | `archive-inventory-01.md` §5–§6 + `analysis-wiki-talk-01.md` §2.5/§6 | OBSERVED |
| AGENTS.md | `04_NEXUS_LLM_WIKI_CORE/AGENTS.md` + `09`؟ + `01_SDCARD_DOCS/wikillm/BUILD_PROTOCOL.md` (لم يُقرأ مباشرة بعد) | REPORTED |
| config/* | `analysis-wiki-talk-01.md` §4.3 (config) + OBSERVED (العينة هيثم) | REPORTED |
| index/* | `analysis-wiki-talk-01.md` §1.10 (نتائج مقاسة) | OBSERVED |
| .gitignore + .env.example | `analysis-session-01.md` §4 (النكهات + التوصيات) | PROPOSED |

> **ملاحظة `research-01.md`:** ~~مسودة تُستكمل قريبًا (أفضل الممارسات: مدخل مخصص لـ AGENTS.md/CONTEXT.md/Claude memory) — لا تعتمد عليها. تُدمج أفكارها (قائمة من 200 سطر لـ CLAUDE.md؛ جلب كسول @file) كاقتراحات تحت وسم **REPORTED** بعد تُكمل، وإلى ذلك الحين تبقى بنية README/CONTEXT كما هي.~~
> **[تعديل مُضاف 2026-11-05 — النص الأصلي أعلاه محفوظ للتاريخ]:** تم التحقق داخل الملف نفسه — الحالة `COMPLETE` مؤيَّدة (OBSERVED: سطر 3 «Status: COMPLETE — evidence-labeled»، التاريخ 2026-11-05، قسم `## Sources` مكتمل بـ7 مصادر مرقّمة (1–7)، وأقسامها الأربعة موصومة بـ OBSERVED/REPORTED/PROPOSED). **المسار المُختار: جعل الخطة صادقة لا الملف.** تُعتمد ملاحظات `research-01.md` الآن كمدخل موثوق، وكل بند يُستخرج منها يبقى بوسمه كما ورد فيها (OBSERVED/REPORTED/PROPOSED)، ويبقى وسم السابق غير الملائم مُلغيًا لا مُعتمدًا.
> **[إعادة تحقق 2026-11-06 — النص أعلاه كما هو]:** أُعيد فحص `research-01.md` بالكامل مرة ثانية (48 سطرًا): `Status: COMPLETE` مؤيَّد — قسم `## Sources` مكتمل بـ7 مصادر مرقّمة (1–7)، والأقسام الأربعة كلها موصومة بـ وسوم الدليل. لا فجوة توجب تخفيض الحالة؛ المسار يبقى: **جعل الخطة صادقة لا الملف**، والنص الأصلي في السطر 166 محفوظ بشطب وتاريخ.

> **ملاحظة `prompt.md` (فيديو):** يبقى خارج النطاق. يُشار إليه في `non-goals.md` فقط — قرار معاذ 2026-11-03: «ليس لك علاقة بالفيديو»؛ الإخراج الوحيد المسموح: رابط القناة العامة + metadata خفيفة دون نسخ النصوص الكاملة.

---

## 5) خطة الرفع إلى GitHub

### 5.1 الأدوات والخطوات (git + API)
1. **المراجعة المحلية أولًا:** تشغيل `git init` داخل `/workspace/wiki/repo` (كان موجودًا كفكرة — يُنشأ جديدًا إن غائبًا)، فحص الدليل، `git add` محدد يدويًا.
2. **تجهيز البيئة (без أسرار):** استخدم `GH_TOKEN` من بيئة عملية **فقط** (لا توجد في ملف). تحقق: `git remote -v` يجب أن يظهر اسم المستودع فقط لا التوكن.
3. **الرفع المناسب (Pick one):**
   - **الخيار A (مستحسن):** `git push` إلى `layered-wiki-rag` عبر HTTPS مع credential helper مؤقت (`git -c credential.helper='!f() { echo "username=x-access-token"; echo "password=$GH_TOKEN"; }; f' push ...`) ثم حذف كل trace.
   - **الخيار B:** GitHub API (نقطة نهاية contents) للملفات النصية الصغيرة فقط — غير مناسب للأرشيف المضغوط.
4. **التزامات صغيرة:** كل commit صغير منطقي: `README/CONTEXT` ثم `docs/` ثم `sources/` ثم `timeline/` ثم `config/` — و CHANGELOG لكل دفعة.

### 5.2 قائمة فحص الأسرار قبل الرفع (checklist إجباري — يُوقع قبل الـ push)
- [ ] `grep -rn 'ghp_\|github_pat_\|AKIA\|BEGIN .*PRIVATE\|YUKINO\|HCNSEC\|COOKIES\|cookies.txt\|zcode-' .` — يجب أن يكون صفر تطابق لقيم حقيقية.
- [ ] تأكد من عدم وجود: `*.db` > 50MB، `MANIFEST.json` الكامل، `conversations_index.csv`، `*.opus`، `*.env` (غير `.env.example`)، `*.log`، مجلد `.git` ضخم.
- [ ] `git status --untracked` + `git check-ignore` لكل ملف مستثنى — المؤشرات فقط مسموح.
- [ ] `git log -p | grep -E 'ghp_|github_pat_|token|cookie'` — لم يدخل توكن في التاريخ قبل الدفعة الأولى.
- [ ] `sha256sum -c hashes.sha256` داخل الأرشيف (تحقق من المصدر لا من المستودع) — إجمالي <250MB.
- [ ] مفتاح PAT: إن استُخدم، يُلغى فورًا بعد الرفع (استناد مسبق: `analysis-session-01.md` §4–§5 — لا تأكيد تدوير موثق، يُوثَّق قبل الرفع ما إن أمكن).
- [ ] Remote URL خالٍ من التوكن (`git remote -v`).
- [ ] مراجعة README الجديدة قبل الرفع (AI جديد يفتح المستودع دون خطأ).

---

## 6) معايير المراجعة (review-1..4)

| المعيار | الوصف | النطاق |
|---|---|---|
| **review-1 (دقة)** | تطابق كل رقم/اقتباس مع مصدره المباشر (OBSERVED)؛ كل ما لا مصدر له مُوصوم UNKNOWN؛ لا محتوى مخترع | الجذر + `docs/` |
| **review-2 (أمان)** | غياب الأسرار فعليًا (5.2.2)؛ الروابط المنشورة صالحة للعلم لا للنصوص الضخمة؛ remote نظيف | كل الملفات قبل الرفع |
| **review-3 (قابلية الاستخدام)** | AI جديد يقرأ CONTEXT.md فقط فيستوعب المشروع دون حاجة لأي ملف آخر؛ لا حلقات مفقودة | README + CONTEXT + MASTER |
| **review-4 (اكتمال السياق)** | كل 106 رسالة/كل قرار/كل ملف مقترح في الأرشيف موجّه له مساره؛ مصادر/روابط/قواعد محوّدة؛ لا قسم يابس | MESSAGES + sources/ + timeline/ + reference/ |

> **يُحظر إعلان «DONE» قبل 4 مراجعات. أي فشل = إرجاع إلى الإصلاح/المراجعة المؤقتة دون استثناء.**

DONE

---

## تحديث 2026-11-05 — حالة ما بعد الدفعة C

> كل سطر أدناه فُحص على القرص قبل الكتابة (2026-11-05) بواسطة subagent؛ ما لم يُتحقَّق فُكِت ولا كُتب.

- **الدورة 1 من 4 مكتملة: OBSERVED** — مرحلاتها الأربع (explore/plan/execute/review) لها ملفات فعلية في `work/`: `analysis-session-01.md` و`analysis-wiki-talk-01.md` و`archive-inventory-01.md` (explore) · `repo-plan-01.md` (plan) · مخرجات البناء داخل `repo/` مع سجلاتها `.log-build-*` (execute) · `review-1..4.md` (review — ls + قراءة رؤوس الملفات الأربعة).
- **الدورات 2–4: NOT_RUN** — لا يوجد `review-5.md` حتى `review-8.md` ولا أي ملف يخصّها في `work/` (grep: صفر نتائج للدورات 2–4).
- **إعادة فحص review-2 بعد الرفع (post-push re-scan): NOT_RUN** — `.log-push:595` نصًّا: «No re-scan done.»
- **البرقع المحلي `repo/`: لا يحتوي `.git`: OBSERVED** — (`ls -d /workspace/wiki/repo/.git` → غائب).
- **مطالبة الرفع commit `79480a3`: REPORTED** — وردت في `work/upload-report.md` (سطر 3: `commit sha: 79480a3…`; سطر 11: `5b70e59..79480a3  main -> main`) وفي `.log-push`؛ لم يُتحقَّق منها من مستودع GitHub مباشر — تظل REPORTED لا OBSERVED، والتعارض مع غياب `.git` محليًا موثّق كما هو.
- **حالة تدوير مفتاح PAT: UNKNOWN** — لا يوجد تأكيد تدوير في أي ملف (`analysis-session-01.md:82`، `repo-plan-01.md §5.2`): «لا يوجد في التصدير تأكيد من المستخدم بأنه قام بالتدوير».

---

## تحديث 2026-11-06 — حالة ما بعد الدفعة C

> كل بند أدناه فُحص على القرص قبل الكتابة (2026-11-06) بواسطة subagent؛ ما لم يُتحقَّق فُكِت ولم يُكتب — صراحة: **بُدّل إثباتُ «تصحيح خطأ timeline» و«إصلاح ملاحظة wiki-talk-index» بإثبات آخرين محلّهما**؛ لم يُعثر على أثر يثبت هذين الإصلاحين، فاسقطا ولا يُدّعى أيٌّ منهما.

- **الدورة 1 من 4 مكتملة: OBSERVED · الدورات 2–4: NOT_RUN** — (`ls work/`): ملفات الدورة 1 موجودة فعلًا: `analysis-session-01.md` و`analysis-wiki-talk-01.md` و`archive-inventory-01.md` (explore) · `repo-plan-01.md` (plan) · `review-1.md` و`review-2.md` و`review-3.md` و`review-4.md` (review). لا يوجد أي ملف يخصّ الدورات 2–4 (`ls work/ | grep review-[5-8]` → NONE): تلك الدورات **NOT_RUN**.
- **إعادة فحص review-2 بعد الرفع (post-push re-scan): NOT_RUN** — (`grep` في `work/review-2.md`): لا ذكر لإعادة فحص بعد الرفع إطلاقًا؛ نطاقه المعلن سطر 3: `**Scope:** /workspace/wiki/repo/ (target: 42 files)` وتاريخه 2026-11-05 أي ما قبل الرفع. والنص الصريح في `.log-push:595`: «No re-scan done.» — كلا النصين مقروءان مباشرة (OBSERVED) والحالة **NOT_RUN**.
- **البرقع المحلي `repo/` لا يحتوي `.git`: OBSERVED** — (`test -d /workspace/wiki/repo/.git` → false اليوم 2026-11-06).
- **حجّة الرفع commit ‏`79480a3`: REPORTED** — وردت نصًّا في `work/upload-report.md` (سطر 3: `commit sha: 79480a3080d060d2919c2320f65ec329a9f25a7c`؛ سطر 11: `5b70e59..79480a3  main -> main`) — تقرير لوكيل آخر قُرئ مباشرة ولم يُعاد التحقق منه من GitHub مباشر، فـREPORTED لا OBSERVED؛ والتعارض مع غياب `.git` محليًا موثّق كما هو (لا يُحسم لصالح طرف بلا دليل).
- **حالة تدوير مفتاح PAT: UNKNOWN** — `work/analysis-session-01.md:82` نصًّا: «أوصى المساعد بإلغائه فورًا (س12935)؛ لا يوجد في التصدير تأكيد من المستخدم بأنه قام بالتدوير».
- **إقفال قيمة PAT داخل سجلات الجلسة: OBSERVED** — القيمة استُبدلت بالبديل `[REDACTED-PAT-40chars-ROTATE-REQUIRED]` في **6 أسطر** بالضبط عبر سجلّين: `work/.log-analysis-session-b` (سطر واحد) + `work/.log-session-c` (5 أسطر) — (`grep -rn … work/ | wc -l` = 6). الإقفال ≠ التدوير: التدوير يبقى UNKNOWN أعلاه.
- **تحصين `.gitignore`: OBSERVED** — `repo/.gitignore` يحوي قسمًا مضافًا حرفيًا: «ضوابط أمنية إضافية (تدقيق أمني 2026-11-05)» يضيف أنماطًا لم تكن مغطاة: `*.tar.gz` و`*.tgz` و`*.gz` و`.log-*` و`work/.log*` و`*.csv`؛ mtime للملف: `2026-11-05 21:21:04 +0200`.
