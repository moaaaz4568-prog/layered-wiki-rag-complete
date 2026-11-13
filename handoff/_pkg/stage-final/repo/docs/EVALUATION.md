# EVALUATION — التقييم والقياس

> الحالة: OBSERVED (النتائج) + PROPOSED (المجموعة المعروفة) — من `../../work/analysis-wiki-talk-01.md` §1.10 + `../../work/repo-plan-01.md` §3.2.
> وسم الدليل: OBSERVED = مقاس على القرص، REPORTED = منقول من تقرير، PROPOSED = مقترح مستقبلي، UNKNOWN = لا دليل، NOT_RUN = لم يُشغَّل بعد.

## 1. ما قيس فعلًا (OBSERVED)

- النموذج الوحيد المنفذ فعليًا: BM25 قبل أي تضمين كثيف أو إعادة ترتيب | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- أصغر 20 صفحة لهيثم (مختصرات رفيعة): 37,402 بايت، 129 مقطعًا | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.7
- على أصغر 20: 4/4 أسئلة عناوين بالنص في المرتبة الأولى | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- على أصغر 20: 1/3 صياغات مختلفة في الأولى، والباقي الثانية | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- أكبر 20 صفحة لهيثم: 123,205 بايت من أصل 601,084 بايت (210 صفحة) | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- على أكبر 20: 14/15 في المرتبة الأولى، 15/15 في أول 3؛ الغلطة: دليل العين والرودسين في الثانية | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- على كل 210: 12/15 في المرتبة الأولى، 14/15 في أول 3 | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- على كل 210: كل 8 أسئلة عناوين بقيت في المرتبة الأولى | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10

## 2. قراءة النتائج

- طبقة الكلمات صامتة تقريبًا على التضخم ×10 في أسئلة العناوين بالظبط | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- الفجوة المقاسة: الأسئلة ذات الصياغات العامة المشتركة الكلمات | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- الكلمات فقط تكفي لصياغة العنوان بالظبط؛ الكثيف + إعادة الترتيب عائق لا رفاهية | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- على 210 الكاملة: 1/3 صياغات مختلفة في الأولى فقط | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- على 210: الجلطة عند الولادة في المرتبة 28؛ «دين حق» في المرتبة 35 | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- الصفحات الغنية الطويلة تفوقت على الصفحة الرفيعة التي فيها الإجابة فعلًا | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10

## 3. تحفظات موثقة

- الـ20 صفحة مختصرات رفيعة (~180 كلمة، 720-967 حرف/صفحة)، وبعض ترجمتها مقتطعة | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- الاختبار يثبت طبقة الكلمات على المختصرات لا على الصفحات الكاملة | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- هذا هيثم فقط، لا 5,686 صفحة الباقية | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- أسئلة العناوين أسهل من أسئلة حقيقية؛ المقياس الصادق هو صفوف الصياغات المختلفة | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10

## 4. المقاييس المقترحة (PROPOSED)

- **Recall@k:** نسبة الأسئلة التي يظهر جوابها في أول k نتيجة؛ لا توسع على فشل | PROPOSED — `../../work/repo-plan-01.md` §3.2
- **Faithfulness:** الإخلاص المقطعي — الإجابة مقيدة بالمقاطع فقط + استشهاد | PROPOSED — `../../work/repo-plan-01.md` §3.2
- **زمن الإجابة الأقصى:** UNKNOWN — لم يُعرَّف بعد | UNKNOWN — `../../work/analysis-wiki-talk-01.md` §3.1
- **قيمة k والعتبة:** UNKNOWN — لا قيمة k معلنة في البريف (مقترح k=10 — القيمة النهائية UNKNOWN، config/thresholds.yaml) | UNKNOWN — `../../work/analysis-wiki-talk-01.md` §3.1
- **20 سؤالًا معروفًا:** PROPOSED — تُبنى بعد v0.1 من 10 صفحات هيثم فعلًا لا أسئلة عامة | PROPOSED — `../../work/analysis-wiki-talk-01.md` §4.4

## 5. العائق الحالي (OBSERVED → NOT_RUN)

- الرام المتاح حاليًا 429MB، موديل 1–2 جيجا ممنوع | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- التضمين الكثيف + إعادة الترتيب: NOT_RUN — انتظار انخفاض استهلاك الرام | NOT_RUN — `../../work/analysis-wiki-talk-01.md` §1.10
- اختبار bge-m3 مقابل e5 على العربية: NOT_RUN — يحتاج اختبار كلمات ضد كثيف | NOT_RUN — `../../work/analysis-wiki-talk-01.md` §6
- فحص v0.1 على 210 هيثم بفلتر إلزامي: NOT_RUN — الاختبار الحقيقي القادم | NOT_RUN — `../../work/analysis-wiki-talk-01.md` §6
- مجموعة 20 سؤالًا على المحتوى الفعلي: NOT_RUN — النقد يفرضها قبل التوسع | NOT_RUN — `../../work/analysis-wiki-talk-01.md` §3.1

## 6. قياسات شاهدة إضافية (OBSERVED)

- 6 ويكيات: 5,896 صفحة، 31.3MB (31,262,266 بايت) | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.7
- هيثم 210 صفحة: 601,084 بايت؛ متوسط 2,336 بايت/صفحة | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- أرشيف الويكي: 212MB، 2,713 ملفًا على القرص | OBSERVED — `../../work/archive-inventory-01.md` §2
- 144 فيديو: 2,783,968 حرف إنجليزي، 509,906 كلمة | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.9
