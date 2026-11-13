# CONCEPTS — قاموس المفاهيم

> الحالة: REPORTED — من `analysis-wiki-talk-01.md` §1.8–§1.11 + §2.3 + §4.3.
> وسم الدليل: OBSERVED = مقاس على القرص، REPORTED = منقول من تقرير، PROPOSED = مقترح مستقبلي، UNKNOWN = لا دليل، NOT_RUN = لم يُشغَّل بعد.

## 1. المفاهيم الأساسية

- **الويكي:** طبقة تجميع مترجمة فوق الخام؛ ليست حقيقة مصدر — الخام هو الحقيقة | REPORTED — `analysis-wiki-talk-01.md` §1.11
- **الخام (Raw):** النصوص الأصلية كما هي؛ للقراءة فقط، لا تُعدَّل أبدًا، وهو الشاهد الوحيد | REPORTED — `analysis-wiki-talk-01.md` §1.8
- **المصطلح:** اسم + تعريف + مصدر؛ أولًا وقبل الماستر، والنقل لا الحذف | REPORTED — `analysis-wiki-talk-01.md` §1.8
- **الماستر:** ملف يقرأه النموذج مرة فيصبح خبيرًا؛ يأتي بعد اكتمال مصطلحات مجلد تبعي | REPORTED — `analysis-wiki-talk-01.md` §1.8
- **المقطع (Chunk):** عنوان/فقرة أو نطاق محارف أو جدول/قائمة — لا تقطيع أعمى بالحروف | REPORTED — `analysis-wiki-talk-01.md` §1.8
- **الاستشهاد بالمقطع:** كل إجابة باستشهاد بمصدر المقطع الخام وبصمته وموقعه | REPORTED — `analysis-wiki-talk-01.md` §1.11
- **الفلتر المنظوري (شخصية):** إجباري كما Metadata لا وزن تشابه؛ يميز مصدرين بنفس الموضوع مختلفين المؤلف | REPORTED — `analysis-wiki-talk-01.md` §1.8

## 2. مفاهيم الاسترجاع

- **RAG:** أساس النظام؛ الويكي طبقة مجمّعة فوقه، وكل إجابة باستشهاد للمقطع الخام | REPORTED — `analysis-wiki-talk-01.md` §1.11
- **BM25:** استرجاع كلمات؛ النموذج الوحيد المنفذ فعليًا قبل أي تضمين كثيف | REPORTED — `analysis-wiki-talk-01.md` §1.10
- **التضمين الكثيف (Dense/Embedding):** مرشّح مشروط بالاختبار لا اختيار نهائي؛ إغلاق فجوة الصياغات العامة | REPORTED — `analysis-wiki-talk-01.md` §1.8
- **الهجين (Hybrid):** BM25 + Dense + RRF؛ RRF غير منفّذ في كود wikillm النشط | REPORTED — `analysis-wiki-talk-01.md` §3.3
- **إعادة الترتيب (Rerank):** بعد اختبار زمنه؛ طبقة ثانية بعد الكثيف لا رفاهية | REPORTED — `analysis-wiki-talk-01.md` §4.3
- **بيانات JSONL/فهرس:** قائمة مسار + بايت + slug + sha + nchunks لكل صفحة | REPORTED — `analysis-wiki-talk-01.md` §4.3

## 3. مفاهيم البنية والتقييم

- **المفاهيم من 144 فيديو:** أكثر المصطلحات تكرارًا: source 109، RAG 99، update 88، Claude 88، memory 86 | REPORTED — `analysis-wiki-talk-01.md` §1.9
- **GraphRAG:** طبقة علاقات لاحقة للأسئلة العلاقية فقط؛ جراف مؤجّل لا بداية | REPORTED — `analysis-wiki-talk-01.md` §5
- **OKF:** عقد تنسيق Open Source، Bundle = مجلد Markdown + type + روابط + index.md | REPORTED — `analysis-wiki-talk-01.md` §2.3
- **Recall@k:** نسبة الأسئلة التي يظهر جوابها في أول k نتيجة؛ لا توسع على فشل | REPORTED — `analysis-wiki-talk-01.md` §1.8
- **Faithfulness:** الإخلاص المقطعي — الإجابة مقيدة بالمقاطع فقط، وإلا رفض | REPORTED — `analysis-wiki-talk-01.md` §4.3
- **Namespace:** لكل شخصية مجموعة بيانات منفصلة؛ فلتر إجباري بصيغة جاهزة | REPORTED — `analysis-wiki-talk-01.md` §2.5
- **Canon/synthesis/support:** طبقات Infinite Brain OS: خام/مترجمة/معتمدة؛ الترقية بموافقة إنسان فقط | REPORTED — `analysis-wiki-talk-01.md` §2.5

## 4. نتائج مقاسة (OBSERVED)

- 6 ويكيات: 5,896 صفحة، 31.3MB | OBSERVED — `analysis-wiki-talk-01.md` §1.7
- هيثم 210 صفحة: 601,084 بايت؛ أصغر 20 صفحة: 37,402 بايت، 129 مقطعًا | OBSERVED — `analysis-wiki-talk-01.md` §1.10
- BM25 على أكبر 20 هيثم: 14/15 في الأولى، 15/15 في أول 3 | OBSERVED — `analysis-wiki-talk-01.md` §1.10
- BM25 على كل 210: 12/15 في الأولى، 14/15 في أول 3؛ العناوين 8/8 في الأولى | OBSERVED — `analysis-wiki-talk-01.md` §1.10
- الصياغات العامة وقعت: الجلطة عند الولادة المرتبة 28، الدين الحق المرتبة 35 | OBSERVED — `analysis-wiki-talk-01.md` §1.10
- أرشيف الويكي: 212MB، 2,713 ملفًا على القرص | OBSERVED — `archive-inventory-01.md` §2
