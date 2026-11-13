# GOALS — الأهداف القابلة للاختبار

> الحالة: PROPOSED — أهداف مخططة في `repo-plan-01.md` §3.2 + `analysis-wiki-talk-01.md` §1.8–§1.9.
> وسم الدليل: OBSERVED = مقاس على القرص، REPORTED = منقول من تقرير، PROPOSED = مقترح مستقبلي، UNKNOWN = لا دليل، NOT_RUN = لم يُشغَّل بعد.

## 1. الغاية الكبرى

- إخراج عقول متخصصة: ويكي بزنس مثلًا تُنتج نموذجًا يعرف كل المحتوى في دماغه | REPORTED — `analysis-wiki-talk-01.md` §1.1 (نص البريف الأصلي)
- سؤال موحّد يستعين بكل العقول معًا بدل ويكي بشرية للقراءة | REPORTED — `analysis-wiki-talk-01.md` §1.1
- مستودع واحد خاص يفتحه أي AI chat جديد فلا يحتاج إعادة مطالعة الأرشيف | REPORTED — `repo-plan-01.md` §1.1
- كل ملف يدخل بكل محتواه: «كل ملف يدخل الويكي يدخل بكل محتواه بلا استثناء» | REPORTED — `analysis-wiki-talk-01.md` §1.8 القاعدة 1
- مصطلحات أولاً، وماستر فقط بعد اكتمال مصطلحات مجلد تبعي | REPORTED — `analysis-wiki-talk-01.md` §1.8 القاعدة 3
- الاعتماد: لا نجاح بلا فحص على القرص ولا أرقام مخترعة | PROPOSED — `repo-plan-01.md` §6 (مراجعات review-1..4)

## 2. الأهداف الخمسة القابلة للاختبار

- **رؤية (Visibility):** كل مقطع يحمل استشهادًا بالمقطع الخام (مسار خام + بصمة) | PROPOSED — `repo-plan-01.md` §3.2
- **تحديد (Precision):** فلتر الشخصية إجباري كما Metadata، لا وزن تشابه | REPORTED — `analysis-wiki-talk-01.md` §1.8 القاعدة 13
- **إجابة (Answer):** كل إجابة باستشهاد للمقطع الخام + الويكي طبقة مجمعة فوق RAG | REPORTED — `analysis-wiki-talk-01.md` §1.11
- **صوت المنظور (Persona voice):** أداة واحدة تبحث في شخصية واحدة وتجيب بصوتها من مقاطعها فقط | PROPOSED — `analysis-wiki-talk-01.md` §1.11
- **ثقة (Trust):** مراجعة بشرية قبل نشر أي صفحة مجمعة + خام للقراءة فقط | REPORTED — `analysis-wiki-talk-01.md` §1.11

## 3. قياسات الحالة الراهنة (OBSERVED)

- 6 ويكيات: ابن سيرين، ابن تيمية، ابن القيم، هيثم طلعت، عماد رشاد، علاء حامد | OBSERVED — `analysis-wiki-talk-01.md` §1.7
- إجمالي صفحات الويكي المقاس: 5,896 صفحة، 31.3MB | OBSERVED — `analysis-wiki-talk-01.md` §1.7
- هيثم طلعت كامل: 210 صفحة، 601,084 بايت | OBSERVED — `analysis-wiki-talk-01.md` §1.10
- أصغر 20 صفحة لهيثم: 37,402 بايت، 129 مقطعًا | OBSERVED — `analysis-wiki-talk-01.md` §1.7
- أرشيف الويكي الكامل: 212MB، 2,713 ملفًا على القرص | OBSERVED — `archive-inventory-01.md` §2
- `05_CONVERSATIONS`: 150M (71% من حجم الأرشيف) | OBSERVED — `archive-inventory-01.md` §2

## 4. النجاح القابل للقياس (BM25 على هيثم)

- على أكبر 20 صفحة لهيثم: 14/15 في المرتبة الأولى، 15/15 في أول 3 | OBSERVED — `analysis-wiki-talk-01.md` §1.10
- على كل 210 صفحة لهيثم: 12/15 في المرتبة الأولى، 14/15 في أول 3 | OBSERVED — `analysis-wiki-talk-01.md` §1.10
- على كل 210: 8/8 أسئلة عناوين بقيت في المرتبة الأولى | OBSERVED — `analysis-wiki-talk-01.md` §1.10
- على 210: صياغات مختلفة ذهبت 1/3 فقط في الأولى؛ الجلطة عند الولادة المرتبة 28 | OBSERVED — `analysis-wiki-talk-01.md` §1.10
- على 210: «كيف أعرف أن الدين حق» في المرتبة 35 | OBSERVED — `analysis-wiki-talk-01.md` §1.10
- على أصغر 20 صفحة: 4/4 أسئلة عناوين في المرتبة الأولى + 1/3 صياغات مختلفة | OBSERVED — `analysis-wiki-talk-01.md` §1.10

## 5. العتبات المستقبلية (غير مُملأة بعد)

- قيمة k والعتبة وحد زمن الإجابة: UNKNOWN — لا قيمة k معلنة في البريف | UNKNOWN — `analysis-wiki-talk-01.md` §3.1
- مجموعة 20 سؤالًا معروفًا: PROPOSED — تُبنى بعد v0.1 من صفحات هيثم | PROPOSED — `repo-plan-01.md` §3.2
- `thresholds.yaml` يُملأ بعد أول قياسين فقط (لا رقم مخترع قبلها) | PROPOSED — `analysis-wiki-talk-01.md` §4.4
- التضمين الكثيف + إعادة الترتيب: NOT_RUN — الرام المتاح 429MB | NOT_RUN — `analysis-wiki-talk-01.md` §1.10
- فحص v0.1 على 210 صفحة هيثم بفلتر إلزامي: NOT_RUN — الاختبار الحقيقي القادم | NOT_RUN — `analysis-wiki-talk-01.md` §6
- اختبار التضمين الكثيف bge-m3 مقابل e5 على العربية: NOT_RUN — يحتاج اختبار كلمات ضد كثيف | NOT_RUN — `analysis-wiki-talk-01.md` §6

## 6. خارج النطاق المعلن

- الفيديو/الصوت: خارج النطاق — «لا علاقته بالفيديو» | REPORTED — `repo-plan-01.md` §3.3
- النشر العام الآن: مؤجل — خاص حتى v0.1 مكتمل | REPORTED — `analysis-wiki-talk-01.md` §5
- نقل جماعي لـ5,896 صفحة دفعة واحدة: مرفوض — العينة أولًا | REPORTED — `analysis-wiki-talk-01.md` §5
- تحميل كامل لـ 2,713 ملف/212MB إلى GitHub: ممنوع — مؤشرات فقط | REPORTED — `repo-plan-01.md` §1.2
