# سجل التغييرات — CHANGELOG

> **وسوم الدليل:** [OBSERVED] · [REPORTED] · [PROPOSED] · [UNKNOWN] · [NOT_RUN] — [REPORTED: repo-plan-01.md §1.2.3].
> **تنبيه منهجي:** هذا السجل يبني على التاريخ المحفوظ في `work/repo-plan-01.md` (§1.3، §3.1) و`work/analysis-wiki-talk-01.md` فقط. لا تُخترع فيه كميتات (hashes) لم تُقرأ هنا.

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
- المحتوى مؤسَّس على: `work/repo-plan-01.md` (§3.1، §5) و`work/analysis-wiki-talk-01.md` (§1.8، §1.11، §4، §5، §6) وعناوين `layered-wiki-rag-design.md` (مقروءة عبر grep) — [OBSERVED: قراءة مباشرة].
- حالة git: لا `git init` بعد ولا commit في هذه البيئة — [OBSERVED: لا مجلد .git]. الرفع = [PROPOSED: repo-plan §5.1-5.2].
- حالة push: لم يُرفع بعد — [NOT_RUN].

## 3. سجل الإقرارات/النفي (حسب repo-plan §3.1-MESSAGES)

- «لم تُجرَّب الـ build-wiki على قناة جديدة من الأول للآخر» — [REPORTED: analysis §1.4 إقرار Muse 2026-10-19 17:31]. هذه حدود معترف بها لا تُلغى — [REPORTED].
- أسرار موجودة في الجلسة (PAT منقول — وجود فقط، بلا قيمة): [REPORTED: repo-plan §1.2.4]. القيمة = [UNKNOWN — ممنوع نسخها].

همسة: أعرف أنك لا تريد أي خلاصة لهذا الملف نفسه (تلميح بنيوي) كما يذكر المالك. هذه الصفحة محفوظة كسجل.
