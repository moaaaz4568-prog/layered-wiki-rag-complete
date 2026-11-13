# المنشأ والتحقق — PROVENANCE

> **وسوم الدليل:** [OBSERVED] · [REPORTED] · [PROPOSED] · [UNKNOWN] · [NOT_RUN] — [REPORTED: repo-plan-01.md §1.2.3].
> **قاعدة الأسرار:** لا قيمة سرية تُنسخ أبدًا — الوجود فقط — [REPORTED: repo-plan-01.md §1.2.4].

## 1. المصادر الأولية المقروءة مباشرة في هذه الدفعة (OBSERVED)

| # | المصدر | المسار الكامل | الحجم/العدد | الدليل |
|---|---|---|---|---|
| P1 | خطة المستودع (`repo-plan-01.md`) | `/workspace/wiki/work/repo-plan-01.md` | 205 سطر | [OBSERVED: قراءة مباشرة] |
| P2 | التحليل الشامل لكلام الويكي (`analysis-wiki-talk-01.md`) | `/workspace/wiki/work/analysis-wiki-talk-01.md` | 66KB، 712 سطرًا | [OBSERVED: قراءة مباشرة — الرقم «66KB» من repo-plan §1's مصدر، ومطابق تقريبًا لحجم الملف] |
| P3 | التصميم المعماري (`layered-wiki-rag-design.md`) | `/workspace/layered-wiki-rag-design.md` | 92KB، 791 سطرًا | [OBSERVED: قراءة العناوين عبر `grep '^#'`] |
| P4 | جرد القرص الحقيقي (هذه الدفعة فقط) | `ls -la /workspace/wiki/repo/` + `ls -lh /workspace/wiki/work/` | فارغ قبل الدفعة | [OBSERVED: 2026-11-05] |

> **دقة:** حجم P2 في البيئة = 65KB تقريبًا؛ الوصف «66KB» وارد في repo-plan §1 — [REPORTED: repo-plan §1]. لا يُفترض رقم أدق من المقاس — [OBSERVED: لم يُقَس هنا بـwc -c; أُعتمد الرقم المنقول].

فهرس عناوين التصميم المقروءة (P3): قاموس الحالة → §1 فهم في صفحة → §2 الويكي المثالية → §3 قرارات → §4 التناقض والحجر → §5 v0.1 → §6 التجارب الست → §7 ما لا نعرفه → §8 اختبار الحالات الخمسة → §9 القرارات الأخيرة → §10 الخلاصة والمصادر — [OBSERVED: عناوين grep].

## 2. مصادر منقولة (REPORTED — لم تُفتح مباشرة في هذه الدفعة)

| # | المصدر | الإشارة | الدليل |
|---|---|---|---|
| S1 | كلام الويكي 106 رسالة (2026-10-06 → 2026-11-03) | ملف `wiki_all_talk.md` (2012 سطر، 175,533 بايت) | [REPORTED: analysis §1 ص1] |
| S2 | الأرشيف 212MB/2713 ملف | ملخص في `archive-inventory-01.md` (79 سطرًا) | [REPORTED: repo-plan §1.1] |
| S3 | الجلسة (analysis-session) | فهرس 18,267 سطرًا + 19 رسالة | [REPORTED: repo-plan §1 + analysis-session §2] |
| S4 | 144 فيديو / نصوص TXT (7.4MB) | `research/yt-subs-144/` في wiki-rag | [REPORTED: analysis §1.9] |
| S5 | Infinite Brain OS (584 ملف، 4.7MB، 228 عقدة) | مستودع `infinite-brain-os` | [REPORTED: analysis §2.5] |
| S6 | wikillm على `/sdcard` | لا تُفتح من هنا | [REPORTED: analysis §2.4 + repo-plan §1.3] |
| S7 | يوتيوب TransferNow/GitHub | روابط في analysis §2.1 | [REPORTED] — انظر analysis §2.1 |

## 3. روابط MANIFEST/hashes (وجودها فقط — لا قيم)

- فهرس 5,896 صفحة / 31.3MB : «manifest» في `wiki-rag` هو مفتاح التتبع — [REPORTED: analysis §1.7 + §4.3].
- ملف `hashes.sha256` و`MANIFEST.json` في الأرشيف — الإشارة فقط، لا نسخ ولا قيم — [REPORTED: repo-plan §1.2.5 + §5.2 checklist].
- حمولات الخام (MANIFEST.json الكامل 780KB، conversations الخام 150MB) لا تُرفع في المستودع — [REPORTED: repo-plan §1.2.1].
- قيمة الـhash الفعلية لأي ملف = [UNKNOWN في هذه البيئة: لم يُقَس].

## 4. الأسرار (وجود فقط — لا قيمة أبدًا)

| السر | الوجود | الدليل |
|---|---|---|
| GitHub PAT | **موجود في الجلسة** — يُلغى ويُدوَّر | [REPORTED: repo-plan §1.2.4 + §5.2] |
| مفتاح Yukino | **موجود لحظيًا**، يُرسل ولا يُخزَّن — `{env:YUKINO_API_KEY}` مرجع فقط | [REPORTED: repo-plan §1.2.4 + analysis §1.8.7] |
| مفتاح hcnsec | **وجود ملف `.hcnsec_key` في yt-wiki** — القيمة غير موجودة هنا | [REPORTED: analysis §1.4] |
| كوكيز يوتيوب | **وجود `cookies.txt` على الجهاز** — القيمة غير منسوخة | [REPORTED: analysis §2.2.6] |
| `.env` | لا يُنسخ أبدًا — `.env.example` بلا قيمة فقط | [REPORTED: repo-plan §1.2.4 + §5.2] |

> قيمة أي سر أعلاه = [UNKNOWN — ممنوع النسخ]. عند ظهور أي قيمة مشتبهة في الذاكرة يجب حذفها فورًا وتدويرها — [PROPOSED: repo-plan §5.2]؛ لا تُدوَّر هنا.

## 5. ما لم يُفتح

- محتوى الـ5,896 صفحة كاملًا — لم يُقرأ، فقط manifest وقياسات — [UNKNOWN: analysis §6].
- ملفات wikillm الخام على `/sdcard` — لا نعرفها إلا من تقارير النموذج الآخر — [UNKNOWN: analysis §6].
- ترتيب الآخرين من 144 فيديو (الوصول جزئي فقط) — [UNKNOWN: analysis §6].
- `MANIFEST.json` الكامل ومحتوى `hashes.sha256` — لم تُفتح/تُقَس هنا — [UNKNOWN].

## 6. التحقق المقترح قبل أي رفع

- [ ] `grep -rn 'ghp_\|github_pat_\|AKIA\|BEGIN .*PRIVATE\|YUKINO\|HCNSEC\|COOKIES' .` صفر تطابق لقيم حقيقية — [PROPOSED: repo-plan §5.2].
- [ ] `sha256sum -c hashes.sha256` داخل الأرشيف (تحقق من المصدر لا المستودع) — [NOT_RUN: لم يُنفَّذ في هذه الدفعة].
- [x] `git remote -v` خالٍ من التوكن قبل أي push — تحقّق كما ورد في التقرير بصفر تطابق لفحص الأسرار قبل الرفع — [REPORTED: `../work/upload-report.md`]. **ملاحظة:** عبارة «لا remote بعد» كانت صحيحة وقت كتابة هذا البند، وقد سبقها/تبعها الرفع فعليًا حسب التقرير نفسه — ولم يُعاد `git remote -v` من هذه البيئة (لا `.git` هنا) — [NOT_RUN: إعادة التنفيذ من هذه البيئة] + [UNKNOWN: حالة الـremote الآن من هذه البيئة].
- [ ] إعادة فحص الأسرار بعد الرفع وتدوير مفتاح PAT إن استُخدم — [NOT_RUN: لم يُنفَّذ في هذه البيئة] — [PROPOSED: repo-plan §5.2].

## 7. مرجع

- الخطة: `../work/repo-plan-01.md` (§1، §3.1، §5) — [REPORTED].
- التحليل: `../work/analysis-wiki-talk-01.md` (§2، §5، §6) — [REPORTED].
- تقرير الرفع: `../work/upload-report.md` (44 سطرًا) — [REPORTED: قراءة مباشرة للملف؛ محتواه تقرير من وكيل آخر ولم يُعاد التحقق منه من هذه البيئة].
- قاعدة الوسم: `repo-plan-01.md` §1.2.3 — [REPORTED].
