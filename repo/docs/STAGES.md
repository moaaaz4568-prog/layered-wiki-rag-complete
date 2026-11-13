# STAGES — المراحل من v0.1 إلى الجراف

> الحالة: REPORTED + PROPOSED — من `../../work/analysis-wiki-talk-01.md` §1.11 + §4.2 + `../../work/repo-plan-01.md` §3.2.
> وسم الدليل: OBSERVED = مقاس على القرص، REPORTED = منقول من تقرير، PROPOSED = مقترح مستقبلي، UNKNOWN = لا دليل، NOT_RUN = لم يُشغَّل بعد.

## 1. المبدأ الحاكم للمراحل

- **العينة أولًا ثم شخصية شخصية:** لا نقل جماعي لـ5,896 صفحة ولا 212MB مرة واحدة | REPORTED — `../../work/repo-plan-01.md` §1.2
- **v0.1 على هيثم فقط:** git + بنية + 10 صفحات بمراجعة بشرية + BM25 على العينة | REPORTED — `../../work/analysis-wiki-talk-01.md` §4.2
- **لا تبنِ شيئًا جديدًا كاملًا الآن:** ابنِ v0.1 فقط على هيثم ثم قرّر بعد القياسين الأولين | REPORTED — `../../work/analysis-wiki-talk-01.md` §6
- **خارج v0.1:** فلتر متعدد المنظورات + إعادة الترتيب + الجراف + الواجهة + الصيانة الآلية | REPORTED — `../../work/analysis-wiki-talk-01.md` §4.2
- **قبل كل مرحلة:** مراجعة بشرية + إثبات حي + لا أرقام مخترعة | REPORTED — `../../work/analysis-wiki-talk-01.md` §1.8
- **مراجعات review-1..4:** لا إعلان DONE قبل 4 مراجعات؛ الفشل = إرجاع للإصلاح | REPORTED — `../../work/repo-plan-01.md` §6

## 2. السياق التقني الثابت

- نظام الحكم الهجين: RAG أساس + ويكي + namespace للشخصية + استشهاد بالمقطع الخام | REPORTED — `../../work/analysis-wiki-talk-01.md` §1.11
- كلامه النموذج الوحيد المنفذ فعليًا: BM25 قبل أي تضمين كثيف | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- فهرسة تسلسلية لكل شخصية لوحدها قبل التالية؛ فلتر الشخصية إجباري كما Metadata | REPORTED — `../../work/analysis-wiki-talk-01.md` §1.11
- الترقية من مسودة إلى canon بموافقة إنسان فقط؛ الوكيل لا يرقّي شغله | REPORTED — `../../work/analysis-wiki-talk-01.md` §1.8
- العمل بالـ sub-agents: المشرف يخطط ويوجه ويفحص فقط | REPORTED — `../../work/repo-plan-01.md` §1.2
- الواجهة: أداة واحدة تبحث في شخصية واحدة وتجيب بصوتها من المقاطع فقط | REPORTED — `../../work/analysis-wiki-talk-01.md` §1.11

## 3. جدول المراحل المقترح

| المرحلة | الهدف | الدليل |
|---|---|---|
| 0 | git init + بنية + 10 صفحات ويكي بمراجعة بشرية لمنظور واحد + خط تقطيع وتضمين وBM25 على العينة + 20 سؤالًا معروفًا مع Recall@10 (مقترح k=10 — القيمة النهائية UNKNOWN، config/thresholds.yaml) وزمن + بروتوكول محدث + REJECTED | REPORTED — `../../work/analysis-wiki-talk-01.md` §4.2 |
| 1 — نموذج | BM25 على هيثم 20 أصغر صفحة — كان قد نُفّذ BM25 وتم قياسه (أعلاه) | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.11 |
| 2 — شخصية | فهرسة تسلسلية واختبار استرجاع لكل شخصية لوحدها قبل التالية | REPORTED — `../../work/analysis-wiki-talk-01.md` §1.11 |
| 3 — واجهة | أداة سؤال واحدة بصوت الشخصية؛ glm يجاوب فقط عند توفر المفتاح + إعادة تشغيل الترمنال | REPORTED — `../../work/analysis-wiki-talk-01.md` §1.11 |
| 4 — صيانة لاحقًا | جراف علاقات + ذاكرة فرق/كتابة متزامنة — لا تُبنى مع مستخدم واحد | REPORTED — `../../work/analysis-wiki-talk-01.md` §1.11 |
| لاحقًا | GraphRAG لعلاقات الأسئلة فقط؛ Chunk/recall للتحقق من الوجود | REPORTED — `../../work/analysis-wiki-talk-01.md` §5 |

## 4. نتائج قائمة (OBSERVED)

- أصغر 20 صفحة لهيثم: 37,402 بايت، 129 مقطعًا — 4/4 عناوين في الأولى، 1/3 صياغات مختلفة | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- أكبر 20 صفحة لهيثم: 123,205 بايت — 14/15 في الأولى، 15/15 في أول 3 | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- كل 210 صفحة لهيثم: 601,084 بايت — 12/15 في الأولى، 14/15 في أول 3؛ العناوين 8/8 في الأولى | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- فجوة الصياغات العامة: الجلطة عند الولادة المرتبة 28، الدين الحق المرتبة 35 | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- 6 ويكيات: 5,896 صفحة، 31.3MB مقاسة | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.7
- أرشيف الويكي: 212MB، 2,713 ملفًا على القرص | OBSERVED — `../../work/archive-inventory-01.md` §2

## 5. العائق الحالي والاختبارات القادمة

- الرام المتاح حاليًا 429MB — لا تركيب موديل 1–2 جيجا | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.10
- التضمين الكثيف + إعادة الترتيب: NOT_RUN — انتظار انخفاض استهلاك الرام | NOT_RUN — `../../work/analysis-wiki-talk-01.md` §1.10
- فحص v0.1 على 210 هيثم بفلتر إلزامي: NOT_RUN — الاختبار الحقيقي القادم | NOT_RUN — `../../work/analysis-wiki-talk-01.md` §6
- اختبار bge-m3 مقابل e5 على العربية: NOT_RUN — يحتاج اختبار كلمات ضد كثيف | NOT_RUN — `../../work/analysis-wiki-talk-01.md` §6
- قيمة k والعتبة وحد زمن الإجابة: UNKNOWN — لا معاملات معلنة في البريف (مقترح k=10 — القيمة النهائية UNKNOWN، config/thresholds.yaml) | UNKNOWN — `../../work/analysis-wiki-talk-01.md` §3.1
