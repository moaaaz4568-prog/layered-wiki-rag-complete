# سجل التغييرات — CHANGELOG

> **وسوم الدليل:** [OBSERVED] · [REPORTED] · [PROPOSED] · [UNKNOWN] · [NOT_RUN] — [REPORTED: repo-plan-01.md §1.2.3].
> **تنبيه منهجي:** هذا السجل يبني على التاريخ المحفوظ في `../work/repo-plan-01.md` (§1.3، §3.1) و`../work/analysis-wiki-talk-01.md` (ولاشتراك الدفعة D وحده: `../work/upload-report.md`). لا تُخترع فيه كميتات (hashes) لم تُقرأ هنا.

## 1. الحالة الراهنة للمستودع — [REPORTED: repo-plan-01.md §1]

- المستودع الحالي: `moaaaz4568-prog/layered-wiki-rag` — خاص — [REPORTED: repo-plan §1].
- Commit الموثّق الوحيد المذكور في المصادر المقروءة: `5b70e59` — عدد الملفات في نسخته: **5 ملفات** — [REPORTED: repo-plan-01.md §1].
- فهرس هذه البيئة الحالي (2026-11-05): مجلد `/workspace/wiki/repo/` فارغ قبل هذه الدفعة — [OBSERVED: `ls -la /workspace/wiki/repo/` — لا ملفات، لا مجلد .git].
- ملف التصميم `layered-wiki-rag-design.md` (92KB): موجود بجذر المستودع الحالي على GitHub — [REPORTED: repo-plan §1.3] وموجود أيضًا في هذه البيئة عند `/workspace/layered-wiki-rag-design.md` (94,124 بايت) — [OBSERVED: `ls -lh`].
- إصدار `v1.0.0` يُرجع 404 (لا يُخترع بدله) — موثّق كعنصر مفقود/فجوة — [REPORTED: repo-plan-01.md §1.3 + §3.1-CHANGELOG].

## 2. الدفعات المسجّلة

### الدفعة A — رفع ملفات التصميم (تاريخ تقريبي — [UNKNOWN: التاريخ الدقيق غير مذكور في المصادر المقروءة])

- المحتوى: `layered-wiki-rag-design.md` (92KB كما في repo-plan §1) + ملفات HTML مقروءة — [REPORTED: repo-plan §1.3]. وصف «HTML المقروء» كما هو في الخطة دون تفصيل هويات الملفات — [REPORTED].
- دليل الوجود الحالي: الملف `layered-wiki-rag-design.md` بجذر GitHub — [REPORTED: repo-plan §1.3]. الهوية الكاملة للخمسة ملفات = [UNKNOWN في المصادر المقروءة].
- Commit: `5b70e59` — [REPORTED: repo-plan §1].

### الدفعة B — إصدار v1.0.0 (أرشيف — مفقود)

- الحالة: الإصدار يُرجع 404 — [REPORTED: repo-plan §1.3 + §3.1].
- لا يُخترع بديل ولا محتوى لهذا الإصدار — موثّق كفجوة فقط — [REPORTED: repo-plan §3.1: «لا يُخترع بديل»].

### الدفعة C — دفعة التنظيم الحالية (هذه الدفعة: 6 ملفات جذر)

- الملفات المكتوبة في `/workspace/wiki/repo/` (2026-11-05):
  - `ARCHITECTURE.md` — [OBSERVED: أُنشئ في هذه الدفعة].
  - `MASTER.md` — [OBSERVED: أُنشئ في هذه الدفعة].
  - `REJECTED.md` — [OBSERVED: أُنشئ في هذه الدفعة].
  - `CHANGELOG.md` (هذا الملف) — [OBSERVED: أُنشئ في هذه الدفعة].
  - `PROVENANCE.md` — [OBSERVED: أُنشئ في هذه الدفعة].
  - `DESIGN-REFERENCE.md` — [OBSERVED: أُنشئ في هذه الدفعة].
- المحتوى مؤسَّس على: `../work/repo-plan-01.md` (§3.1، §5) و`../work/analysis-wiki-talk-01.md` (§1.8، §1.11، §4، §5، §6) وعناوين `layered-wiki-rag-design.md` (مقروءة عبر grep) — [OBSERVED: قراءة مباشرة].
- حالة git حين كتابة هذه الدفعة (2026-11-05): لا `git init` بعد ولا commit في هذه البيئة — [OBSERVED: لا مجلد `.git`]. الرفع = [PROPOSED: repo-plan §5.1-5.2] — وقد نُفِّذ لاحقًا، انظر «الدفعة D» أدناه.
- حالة push عند إغلاق هذه الدفعة: لم يُرفع بعد — [NOT_RUN: صدر قبل الرفع الفعلي الموثّق في الدفعة D أدناه؛ لم يُلغَّ بالمراجعة بل أُبقي كما كان عليه وقت كتابته].

### الدفعة D — رفع الدفعة C إلى GitHub (2026-11-05)

- حجّة الرفع وفق `../work/upload-report.md`: commit ‏`79480a3080d060d2919c2320f65ec329a9f25a7c` على فرع `main`، 60 ملفًا في `git ls-tree -r --name-only HEAD`، ونتيجة `5b70e59..79480a3  main -> main` إلى `https://github.com/moaaaz4568-prog/layered-wiki-rag.git`، وحالة ما بعد الرفع `## main...origin/main`، وفحص أسرار قبل الرفع بصفر تطابق — كلها [REPORTED: ../work/upload-report.md — تقرير من وكيل آخر قُرِئ مباشرة، ولم يُعاد فحصه من هذه البيئة].
- تاريخ التقرير: 2026-11-05 (وقت تعديل ملف upload-report.md: 01:09:42 بتوقيت +0200) — [OBSERVED: `stat` على الملف]. (التاريخ اليومي نفسه؛ الساعة الدقيقة للـpush لا تظهر في التقرير — [UNKNOWN].)
- التحقق المحلي من هذه البيئة: مجلد `/workspace/wiki/repo/` ما يزال **بلا `.git`** — [OBSERVED: `ls -la /workspace/wiki/repo/`]، فلا يمكن إعادة التحقق محليًا من الـcommit ولا من حالة remote.
- حالة المستودع على GitHub بعد الرفع = [UNKNOWN: لم يُقرأ من هذه البيئة ولم يُعاد التحقق من الطرف البعيد] — الاعتماد كله على [REPORTED] أعلاه.
- لاحظ: هذا الملف نفسه كُتب/حُدِّث بعد الرفع، فمحتواه الحالي لم يُرَ على GitHub بالضرورة — [UNKNOWN: لم يُقارن].

## 3. سجل الإقرارات/النفي (حسب repo-plan §3.1-MESSAGES)

- «لم تُجرَّب الـ build-wiki على قناة جديدة من الأول للآخر» — [REPORTED: analysis §1.4 إقرار Muse 2026-10-19 17:31]. هذه حدود معترف بها لا تُلغى — [REPORTED].
- أسرار موجودة في الجلسة (PAT منقول — وجود فقط، بلا قيمة): [REPORTED: repo-plan §1.2.4]. القيمة = [UNKNOWN — ممنوع نسخها].

همسة: أعرف أنك لا تريد أي خلاصة لهذا الملف نفسه (تلميح بنيوي) كما يذكر المالك. هذه الصفحة محفوظة كسجل.
