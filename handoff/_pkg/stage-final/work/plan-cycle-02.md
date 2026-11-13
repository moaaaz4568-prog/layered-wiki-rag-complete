# خطة الدورة 2 — layered-wiki-rag

> **المالك الحصري لهذا الملف:** subagent جارٍ (يملك هذا الملف وحده).
> **الحالة:** خطة تخطيطية فقط — لا يُنفَّذ أي بند هنا قبل موافقة المستخدم على §5.
> **تاريخ القياس:** كل رقم أدناه قيست بأمر مذكور صراحةً في 2026-11-06 (أو بتاريخ أقدم إن ذُكر الملف المصدر).
> **الوسوم:** `OBSERVED` = قيست/قُرئت مباشرة · `REPORTED` = منقولة من تقرير آخر · `PROPOSED` = مقترح غير منفَّذ · `UNKNOWN` = لا دليل · `NOT_RUN` = لم يُشغَّل.
> **السرية:** لا يحتوي هذا الملف على أي قيمة مفتاح؛ تُذكر الإحالات فقط.
> **السياق:** الدورة 1 (explore→plan→execute→review) مكتملة `OBSERVED` (ملفات `work/`: analysis-session-01 · analysis-wiki-talk-01 · archive-inventory-01 · repo-plan-01 · review-1..4). الدورات 2–4 كلها `NOT_RUN` (`ls work/ | grep -c '^review-[5-8]'` = **0** — `OBSERVED`).

---

## 1) نطاق الدورة 2 — أهداف قابلة للقياس

| # | الهدف (قابل للقياس) | مقياس القبول | القياس الحالي | الوسم |
|---|---|---|---|---|
| G1 | إغلاق فجوة `MESSAGES.md`: كل رسالة من الرسائل الـ106 مُوثَّقة كصف بيانات | `grep -c '^| [0-9]' repo/MESSAGES.md` ≥ 106 | **57** (الفارق **49**) | `OBSERVED` (57) / `REPORTED` (106 — رقم من `analysis-wiki-talk-01.md`) |
| G2 | توثيق/احتواء إحالات `work/` داخل repo بدل تركها عارية غير قابلة للتنفيذ خارج البيئة | عدد الملفات المعرَّفة في repo التي تحتوي `work/` = 0 بعد الاستبدال/التغليف | **31 ملفًا** تحتوي `work/`؛ **460** سطرًا مطابقًا؛ **480** إحداق `../work/…` بـ**6** أهداف فريدة | `OBSERVED` |
| G3 | تصدير تقارير الأرشيف المحتجزة في السجلات المخفية كملفات `.md` (إن قُرر تصديرها — قرار §5.5) | تقرير `.log-archive` إما أن يُصدَّر إلى `work/archive-*.md` أو يُوثَّق رفضه في `PROVENANCE.md` | `.log-archive`: **295 سطرًا / 15,299 بايت**، مخفي، غير مُصدَّر؛ مقابله `archive-inventory-01.md` = **79** سطرًا | `OBSERVED` |
| G4 | إعادة فحص الأسرار بعد الرفع (post-push re-scan) — كانت `NOT_RUN` | نتائج فحص مسجَّلة في `work/review-5.md` مع أمر وتاريخ | `NOT_RUN` نصًّا: `.log-push:595` «No re-scan done.» (`OBSERVED`)؛ و`review-2.md` بتاريخ ما قبل الرفع بلا ذكر لإعادة الفحص (`grep -c 'post-push\|re-scan' work/review-2.md` = **0**، الملف 19 سطرًا) | `NOT_RUN` |
| G5 | تحقق YAML لملفات `config/*.yaml` الأربعة | أمر تحقق ينجح على الملفات الأربعة ويسجّل نتيجة | `NOT_RUN` — تعذّر التنفيذ محليًا (python3 بلا وحدة yaml، ruby غير مثبّت)؛ `thresholds.yaml` فيه **6** قيم `null` منها `top_k` و`recall_at_k` (سطرا 9–10) | `NOT_RUN` |
| G6 | تحقق روابط Markdown داخل repo | صفر رابط نسبي مكسور | `NOT_RUN` — القياس لم يُشغَّل؛ عدد الملفات المراد تدقيقها: **36** ملف `*.md` (`find repo -name '*.md' | wc -l` = 36 — `OBSERVED`)، و**24** رابطًا خارجيًا فريدًا (`OBSERVED`) | `NOT_RUN` |
| G7 | عدم إدخال/إزالة قرارات الستة المعتمدة على المستخدم (§5) | كل بنود §5 تبقى `UNKNOWN/awaiting-user` حتى ردّ صريح | مُستقاة من `promptastra6fgss.md:230-239` (`OBSERVED` كنص البريف) | `UNKNOWN` |

> **خارج نطاق الدورة 2** (كلها `NOT_RUN`): `review-5..8` النهائية قبل إعلان الدورة 2 منتهية · توسع المحتوى الجماعي (العينة أولًا — `repo-plan-01.md §1.2.6`) · اختيار bge-m3 (`config/models.yaml`: `selection_status: "NOT_RUN"` — `OBSERVED`).

---

## 2) الفجوات المعروفة — كلها مقاسة بأمر

| الفجوة | أمر القياس | النتيجة | الوسم |
|---|---|---|---|
| صفوف `MESSAGES.md` مقابل هدف 106 | `grep -c '^| [0-9]' /workspace/wiki/repo/MESSAGES.md` | **57** (ضمن **109** سطرًا كليًّا؛ إجمالي صفوف الجداول `grep -c '^| '` = **60**) | `OBSERVED` |
| فجوة الرسائل المتبقية | 106 − 57 | **49** رسالة لم تُوثَّق بعد كصفوف | `PROPOSED` (الهدف 106 = `REPORTED`) |
| مراجع `work/` العارية داخل repo (أي ملف) | `grep -rn 'work/' /workspace/wiki/repo \| wc -l` | **460** سطرًا | `OBSERVED` |
| ملفات repo المعرَّفة في `work/` | `grep -rln 'work/' /workspace/wiki/repo \| wc -l` | **31** ملفًا (منها الجذور كلها + docs/ + sources/ + config/) | `OBSERVED` |
| إحداق `../work/` المطلقة | `grep -rno '\.\./work/[A-Za-z0-9._-]*' repo \| wc -l` و`cut -d: -f3 \| sort -u` | **480** إحداقًا، **6** أهداف فريدة: `../work/` + `analysis-session-01.md` + `analysis-wiki-talk-01.md` + `archive-inventory-01.md` + `repo-plan-01.md` + `upload-report.md` | `OBSERVED` |
| تقارير محتجزة في `.log-archive` (غير مُصدَّرة `.md`) | `grep -c '' work/.log-archive` + `ls work/.log-* \| wc -l` | `.log-archive` = **295** سطرًا؛ السجلات المخفية المجمعة = **33** ملف `.log-*` (تقرير `history-2026-11-06.md` يرفع مجموعها إلى **9,668** سطرًا = `REPORTED` — لم يُعَد قراءتها سطرًا سطرًا هنا) | `OBSERVED` (295، 33) / `REPORTED` (9,668) |
| إعادة فحص الأسرار بعد الرفع | (كانت في §5.2 من `repo-plan-01.md`) | `.log-push:595`: «No re-scan done.» | `NOT_RUN` |
| فحص أسرار محلي على repo الآن | `grep -rEn 'ghp_\|github_pat_\|AKIA\|BEGIN .*PRIVATE\|YUKINO_API_KEY=[A-Za-z0-9]\|HCNSEC' repo \| wc -l` | **2** تطابق، وكلاهما **ذكر وصفي لا قيمة**: `README.md:70` (نص يدّعي فحصًا سابقًا بصفر تطابق) و`PROVENANCE.md:59` (بند قائمة فحص `PROPOSED`)؛ فحص regex للقيم الحقيقية `grep -rEln 'ghp_[A-Za-z0-9]{8}\|github_pat_[A-Za-z0-9_]{8}' repo` = **0** | `OBSERVED` (الوجودان) — لكن الفحص **الشامل** بعد الرفع يبقى `NOT_RUN` |
| علامات `[REDACTED]` داخل repo | `grep -rn '\[REDACTED' repo \| wc -l` | **2** (س11911 في `MESSAGES.md:17` و`session-export-index.md:15`) = الإخفاء يعمل؛ مقابل **6** علامات في سجلات `work/` (`REPORTED` من `repo-plan-01.md:233` = `OBSERVED` سابق) | `OBSERVED` |
| تحقق YAML | `python3 -c "import yaml…"` / `ruby -e 'require \"yaml\"…'` | كلا الأمرين **فشل**: `ModuleNotFoundError: No module named 'yaml'` و`ruby: command not found` | `NOT_RUN` |
| تحقق الروابط | (أمر §4-K6) | لم يُشغَّل | `NOT_RUN` |
| الدورات 2–4 | `ls work/ \| grep -c '^review-[5-8]'` | **0** → `NOT_RUN` | `NOT_RUN` |
| `.git` في `repo/` | `test -d /workspace/wiki/repo/.git && echo yes \|\| echo no` | **no** (لا يوجد) | `OBSERVED` |
| تدوير PAT | `grep -c 'PAT\|تدوير' work/repo-plan-01.md` = **5** إشارات، لا تأكيد تدوير | لا يوجد تأكيد في أي ملف | `UNKNOWN` |

---

## 3) مهام بملكية ملف مفردة (كل مهمة تُكتب في ملف واحد فقط — لا تعدّل غيره)

| # | المهمة | الملف المملوك (وحده) | أمر التحقق |
|---|---|---|---|
| T1 | استكمال صفوف الرسائل الناقصة (49) من المصدر المباشر | `repo/MESSAGES.md` | `grep -c '^| [0-9]' /workspace/wiki/repo/MESSAGES.md` ← النتيجة المتوقعة: **≥106** بعد التنفيذ (حالياً 57) |
| T2 | تغليف/توثيق إحالات `work/` الستة الفريدة داخل repo (بديل قابل للتنفيذ أو إعلان `UNKNOWN` صريح) | `repo/PROVENANCE.md` | `grep -rno '\.\./work/[A-Za-z0-9._-]*' /workspace/wiki/repo \| cut -d: -f3 \| sort -u` ← المتوقع بعد التنفيذ: **0** هدف غير موثَّق ببديل |
| T3 | إعادة فحص الأسرار بعد الرفع + تسجيل الأمر/التاريخ/النتيجة | `work/review-5.md` (جديد، مملوك) | `grep -c 'OBSERVED' work/review-5.md` ← **≥1**، و`grep -n 'post-push\|بعد الرفع' work/review-5.md` ← **≥1** |
| T4 | تحقق YAML بأي أداة متاحة (تثبيت محلي معتمد؟ — أنظر §5) | `work/review-5.md` أيضًا (قسم «تحقق YAML») أو `work/yaml-check-01.md` إن فُصل | `python3 -c "import yaml,glob; [yaml.safe_load(open(f)) for f in glob.glob('/workspace/wiki/repo/config/*.yaml')]; print('yaml-ok')"` ← المتوقع: **yaml-ok** (حالياً `NOT_RUN` — الوحدة غائبة) |
| T5 | تحقق الروابط النسبية داخل 36 ملف `*.md` | `work/link-check-01.md` (جديد، مملوك) | `grep -rEn '\]\((?!http)[^)]+\)' /workspace/wiki/repo --include='*.md'` (أو بديل grep عادي) ← المتوقع: **صفر رابط مكسور موثَّق** |
| T6 | تحرير/ترجيع السجلات المحتجزة (قرار §5.5 أولاً) | `work/archive-export-01.md` (جديد، مملوك) — إن قُرر | إن نُفِّذ: `test -f /workspace/wiki/work/archive-export-01.md && echo exists` ← **exists**؛ إن رُفض: `grep -n 'مرفوض' work/archive-export-01.md` أو توثيق الرفض داخل `repo/PROVENANCE.md` عبر T2 |
| T7 | مراجعة أمان ما بعد الرفع (تعميم review-2 على الحالة الحالية) | `work/review-2-postpush.md` (جديد، مملوك — غير `review-2.md` القديم المحفوظ) | `grep -c 'OBSERVED\|NOT_RUN' work/review-2-postpush.md` ← **≥2** |
| T8 | تدوين حالة `.git` الغائبة + تعارض مطالبة الرفع REPORTED مقابل الخصم بلا `.git` | `repo/CHANGELOG.md` | `grep -n 'REPORTED\|\.git' /workspace/wiki/repo/CHANGELOG.md` ← **≥1** لكل وسم |
| T9 | فهرسة ملفات `work/*.md` الـ24–28 (ما لا `.log`) بمؤشرات لا نسخ | `repo/sources/session-export-index.md` | `grep -c 'work/' /workspace/wiki/repo/sources/session-export-index.md` — يُعتمد بديل T2: بعد التغليف = **0** مرجع عارٍ |
| T10 | سجل تغيير الدورة 2 (ماذا تغيّر ومتى) | `work/plan-cycle-02.md` (**هذا الملف — حصري**) | `grep -c '^|' /workspace/wiki/work/plan-cycle-02.md` ← يزيد بعد كل مهمة مُسلَّمة |

> **قاعدة الملكية:** مهمة تُنفَّذ = ملف واحد يُعدَّل + سطر يُضاف إلى هذا الجدول (T10) — وإلا أُعيدت المهمة.

---

## 4) فحوص القبول — أوامر دقيقة ونتائج متوقعة

| # | الفحص | الأمر | النتيجة المتوقعة | الحالة الآن |
|---|---|---|---|---|
| K1 | اكتمال MESSAGES | `grep -c '^| [0-9]' /workspace/wiki/repo/MESSAGES.md` | **≥106** (المتوقع بعد T1؛ اليوم **57**) | `NOT_RUN` |
| K2 | صفر إحاد `../work/` عارٍ غير موثَّق | `grep -rno '\.\./work/[A-Za-z0-9._-]*' /workspace/wiki/repo \| cut -d: -f3 \| sort -u \| wc -l` | **0** (اليوم **6**) — أو قائمة موثَّقة ببديل داخل `PROVENANCE.md` | `NOT_RUN` |
| K3 | فحص أسرار شامل بعد الرفع | `grep -rEln 'ghp_[A-Za-z0-9]{8}\|github_pat_[A-Za-z0-9_]{8}\|AKIA[0-9A-Z]{12}\|YUKINO_API_KEY=[^[:space:]]+' /workspace/wiki/repo` | **صفر ملفات** (اليوم: 0 بفحص regex للقيم، لكن الفحص الشامل المُوسَّم والمؤرَّخ = `NOT_RUN`) | `NOT_RUN` |
| K4 | `.env.example` بلا قيم | `cat /workspace/wiki/repo/.env.example \| grep -c '='` وفحص القيمة فارغة | **1** سطر `YUKINO_API_KEY=` **بقيمة فارغة** — `OBSERVED` اليوم (صحيح، يبقى كذلك) | `OBSERVED` (ناجح) |
| K5 | YAML صالح | `python3 -c "import yaml,glob; [yaml.safe_load(open(f)) for f in glob.glob('/workspace/wiki/repo/config/*.yaml')]; print('yaml-ok')"` | **yaml-ok** (4 ملفات) | `NOT_RUN` (أداة yaml غير مثبتة) |
| K6 | روابط Markdown | `grep -rEo '\]\([^)]+\)' /workspace/wiki/repo --include='*.md' \| grep -v 'http' \| wc -l` ثم فحص وجود كل هدف | كل هدف نسبي موجود على القرص؛ **0** مكسور | `NOT_RUN` |
| K7 | عدّة الملفات | `find /workspace/wiki/repo -name '*.md' \| wc -l` | **36** (القياس الحالي `OBSERVED`) — لا ينقص بعد أي تعديل | `OBSERVED` |
| K8 | وسوم الدليل موجودة | `grep -c 'OBSERVED\|REPORTED\|PROPOSED\|UNKNOWN\|NOT_RUN' /workspace/wiki/repo/README.md` | **≥50** سطرًا يحمل وسمًا (اليوم **50** — `OBSERVED`)؛ `NOT_RUN` في README=**7**, CONTEXT=**3**, PROVENANCE=**4** (`OBSERVED`) | `OBSERVED` |
| K9 | غياب `review-5..8` قبل انتهاء الدورة 2 فعليًا | `ls /workspace/wiki/work \| grep -c '^review-[5-8]'` | **≥1** ملف review يُخلص الدورة (اليوم **0** = `NOT_RUN`) | `NOT_RUN` |
| K10 | remote خالٍ من التوكن | `git -C /workspace/wiki/repo remote -v` (إن أُنشئ `.git` — قرار §5) | يظهر الاسم فقط بلا توكن | `NOT_RUN` (لا `.git` — `OBSERVED` غيابها) |
| K11 | لا تكذب الأرقام | مطابقة كل رقم في `README/CONTEXT` بأمر | كل رقم `OBSERVED` له أمر؛ الباقي `REPORTED/UNKNOWN` | `NOT_RUN` (عينة اليوم: أرقام README محالة لـ`../work/` أغلبها = مشكلة K2) |
| K12 | `.log-*` خارج repo | `find /workspace/wiki/repo -name '.log-*' \| wc -l` | **0** (سجلات `work/` = **33** — `OBSERVED`) | `OBSERVED` (ناجح اليوم) |

---

## 5) ستة قرارات محجوبة على المستخدم — كلها `UNKNOWN / awaiting-user`

> **لا يُنفَّذ أي بند من §1–§4 المتعلق بهذه القرارات قبل ردّ صريح من المستخدم.** البريف نفسه يحيلها للمستخدم (`promptastra6fgss.md:230-239` — `OBSERVED` كنص).

| # | القرار | البدائل | الوسم | لماذا محجوب |
|---|---|---|---|---|
| D1 | **الحجر الصحي ↔ عرض الطرفين**: هل يُحجر التناقض الميكانيكي (رقم/تاريخ) من الاسترجاع، أم تُعرض الروايتان معًا لينظر المستخدم؟ | حجر مصريّ · عرض الطرفين · هجين (حجر مع عرض مُعلَّم) | `UNKNOWN` | `CONTRADICTION-POLICY.md` غير مُحسم (`PROPOSED` في `repo-plan-01.md §3.2`)؛ حرية المحتوى مقابل دقّة الأرقام قرار ملكية لا وكيل |
| D2 | **حدّ «الرأي الغبي»**: متى يصبح الرأي المختلف «глупо جدًا أو خارج المجال» فيُحذف كليًّا (خانة الوحيدة المسموح حذفها في قاعدة «كل ملف يدخل»)؟ | تعريف دلالي · لائحة أمثلة · لجنة بشرية لكل حالة | `UNKNOWN` | البريف يسمّيه «أخطر قرار غير محسوم» (`promptastra6fgss.md:239`)؛ الوكيل لا يمتلك معيار الحذف |
| D3 | **قيمة k** (Top-k) | قيمة ثابتة · `null` حتى أول قياسين · متعددة حسب نوع السؤال | `UNKNOWN` | `config/thresholds.yaml:9-10`: `top_k: null` و`recall_at_k: null` (`OBSERVED`)؛ لا قيمة معلنة في البريف أصلًا (`promptastra6fgss.md:74`) — تُملأ بعد أول قياسين بموافقة |
| D4 | **خاص ↔ عام** | إبقاء خاص (سياسة `§1.2.1`) · نشر عام · نشر جزئي README فقط | `UNKNOWN` | `repo-plan-01.md §1.2.1` يفرض خاصًا، لكن البريف يسجّل سؤال «النشر العام هدف أم وسيلة؟ (مستخدم)» (`promptastra6fgss.md:236`) — أي تغيير يحتاج إذنًا صريحًا |
| D5 | **تدوير الـPAT** | تدوير موثَّق · عدم التدوير مع مبرر · مسح فقط | `UNKNOWN` | لا تأكيد تدوير في أي ملف (`repo-plan-01.md:232`، `history-2026-11-06.md:98` — `OBSERVED` غياب التأكيد)؛ الإقفال ≠ التدوير (`repo-plan-01.md:233`) |
| D6 | **إطلاق الدورة 2** | إطلاق الآن · إطلاق بعد إغلاق D1–D5 · إلغاء الدورات 2–4 | `UNKNOWN` | الدورات 2–4 كلها `NOT_RUN` (`ls | grep -c '^review-[5-8]'` = **0** — `OBSERVED`)؛ «يُحظر إعلان DONE قبل 4 مراجعات» (`repo-plan-01.md:205`) لا يُفسَّر كإطلاق تلقائي للدورة التالية |

---

## 6) كل ما لم يُنفَّذ — موسوم `NOT_RUN`

كل بند غير مُوسَّم `OBSERVED` في هذا الملف أعلاه هو `NOT_RUN` صراحةً، وأهمه على وجه التحديد:

- **كل فحوص §4:** K1 · K2 · K3 (إعادة الفحص الشامل) · K5 (YAML) · K6 (روابط) · K9 · K10 · K11 — كلها `NOT_RUN`.
- **كل مهام §3:** T1–T10 — لم تبدأ؛ لا `work/review-5.md` ولا `link-check-01.md` ولا `archive-export-01.md` ولا `review-2-postpush.md` موجودة اليوم (`ls` — `OBSERVED` غيابها، فالتنفيذ `NOT_RUN`).
- **الدورات 2–4 كاملة:** `review-5..8` — `NOT_RUN` (`grep -c '^review-[5-8]' = 0`).
- **إعادة فحص ما بعد الرفع:** `NOT_RUN` (`No re-scan done.` — `.log-push:595`).
- **تصدير تقارير `.log-archive` و`.log-build-*` (33 ملفًا):** `NOT_RUN`.
- **أي تثبيت أداة YAML:** `NOT_RUN` (`ModuleNotFoundError` + `ruby: command not found` — `OBSERVED`).
- **فتح `v1.0.0` (فجوة 404):** `UNKNOWN`/`NOT_RUN` — لم يُفحص من هذه البيئة (لا شبكة).
- **التحقق المباشر من GitHub لـcommit `79480a3`:** `REPORTED` لا `OBSERVED` (`upload-report.md:3,11` — `OBSERVED` الملف، `REPORTED` المطالبة)؛ التحقق المباشر `NOT_RUN` (بلا شبكة).
- **قاعدة عدم التوسع:** أي باب في `repo-plan-01.md §3` خارج مُخرجات الدورة 1 القائمة = `NOT_RUN`.

---

## سجل تعديلات هذا الملف (T10)

| التاريخ | التعديل | الدليل |
|---|---|---|
| 2026-11-06 | الإنشاء: كل الأرقام في §2 و§4 قُيست بأوامر مذكورة حرفيًا في هذه الجلسة | `OBSERVED` |
