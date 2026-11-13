# بنية الويكي — حقائق مقاسة

**تاريخ الفحص:** 2026-07-31
**المسار المفحوص:** `/sdcard/Nexus_Brain/Nexus_Brain/wiki/`
**نوع المهمة:** استكشاف فقط — لم يُعدّل أو يُحذف أو يُنقل أي ملف.

> كل رقم في هذا الملف مقيس بأمر فعلي على الملفات. لا تخمين.

---

## 0) الخلاصة الحاسمة أولاً

أهم نتيجة في هذا الفحص: **"الماستر" ليس داخل `wiki/` إطلاقاً.**

الماسترات تسكن في **مخزن (vault) منفصل** هو `/sdcard/Nexus_Brain/nexus_vault/`، وفيه **70 ملف `Master_*.md`** موزعة على 26 مجلد موضوعي. أما `wiki/` فلا يحتوي ولا ملف واحد اسمه `Master_*`:

```
find /sdcard/Nexus_Brain/Nexus_Brain -name 'Master_*'   →  0
find /sdcard/Nexus_Brain/nexus_vault -name 'Master_*.md' → 70
```

هذا يعني أن النظام **مشقوق على شجرتين**: شجرة المفاهيم الذرّية (`wiki/`) وشجرة التجميع/التركيب (`nexus_vault/`). أي عامل إثراء يقرأ `wiki/` فقط سيستنتج — خطأً — أن الماستر غير موجود.

---

## 1) البنية الكاملة للمجلدات تحت `wiki/`

المستوى 1 فقط. **لا يوجد أي مجلد في المستوى 2** (`find wiki/ -mindepth 2 -type d` = 0).

| المجلد | عدد الملفات | كلها `.md`؟ |
|---|---|---|
| `concepts/` | **1608** | نعم (1608) |
| `sources/` | 437 | نعم |
| `entities/` | 161 | نعم |
| `tools/` | 88 | نعم |
| `keywords/` | 19 | نعم |
| `duplicates/` | 4 | نعم |
| `batch_output/` | 2 | نعم |
| `checkpoints/` | 1 | نعم |

**ملفات في جذر `wiki/` مباشرة:**

| الملف | الحجم | ملاحظة |
|---|---|---|
| `index.md` | 73,820 B | الفهرس العام (انظر §2) |
| `log.md` | 328,210 B | سجل الجلسات — الأكبر حجماً |
| `link_repair_report.md` | 229,409 B | تقرير إصلاح روابط سابق |
| `CHECKPOINT.md` | 42,547 B | |
| `KEYWORDS.md` | 24,271 B | |
| `business_plan_index.md` | 7,197 B | |
| `fix_links.py` | 4,130 B | سكربت — الويكي ليس بيانات صافية |

الإجمالي المقيس: **2320 ملف `.md`** داخل `wiki/`.

**ملاحظة على العدّ المذكور في السؤال:** `~1608 ملف تحت concepts/` رقم دقيق تماماً — 1608 بالضبط.

---

## 2) ما هو "الماستر"؟

الجواب على ثلاث طبقات، لأن ثلاثة أشياء مختلفة تتنافس على تسمية "ماستر":

### الطبقة أ — `nexus_vault/Master_*.md` (الماستر الحقيقي)

70 ملف. أمثلة بمساراتها:

```
nexus_vault/01_outreach/Master_Cold_Email_System.md
nexus_vault/01_outreach/Master_Lead_Generation.md
nexus_vault/02_sales_closing/Master_Sales_Conversation.md
nexus_vault/02_sales_closing/Master_Objection_Handling.md
nexus_vault/03_pricing_offers/Master_Pricing_And_Offer_Design.md
```

`nexus_vault/_INDEX.md` يصرّح بأرقامه الخاصة:

```
- **Canonical masters:** 39
- **Active clusters:** 26
```

انتبه للتناقض المقيس: الفهرس يقول **39 ماستر قانوني**، والقرص فيه **70 ملف `Master_*.md`**. الفارق يفسّره وجود `_archive/` ونسخ مثل `Master_Video_Production.md` مقابل `Master_Video_Production_Scripting.md`، ومجلدات مكرّرة الاسم (`13_agency` و `13_agency_ops`، `17_niche` و `17_niche_positioning`). أي أن الـ 70 تشمل نسخاً متجاوزة (superseded).

**كثافة الربط:** الماسترات تحتوي **1412 رابط `[[Concept_*]]` فريد**.

### الطبقة ب — `wiki/index.md` (فهرس، لا ماستر موضوعي)

أكثف ملف بالروابط في الويكي كله:

| الملف | عدد `[[` |
|---|---|
| `index.md` | **943** |
| `KEYWORDS.md` | 582 |
| `log.md` | 447 |
| `concepts/Concept_Identity_Selling.md` | 342 |
| `entities/Entity_Caleb_Rston.md` | 181 |
| `sources/Source_Build_$100k_MRR_Agency.md` | 173 |

لكنه فهرس إداري مقسّم بالنوع لا بالموضوع: `## Entities (145)` / `## Sources (429)` / `## Tools (79)` / `## Concepts (1,235)`.

وهو **قديم ومتخلّف عن الواقع**. جدول إحصائياته يقول:

```
| [[Concepts]] | **1,240** |
```

والواقع المقيس 1608 مفهوماً. آخر تحديث مكتوب فيه: `2026-05-22`. أي أن **~368 مفهوماً أُضيفت بعده دون تسجيل**. ولا يحتوي إلا **215 رابط مفهوم فريد** (213 منها فقط تُحلّ إلى ملف موجود) — أي أن `index.md` يغطي **13% من المفاهيم**، لا كلها.

### الطبقة ج — `wiki/keywords/` (MOCs موضوعية، تغطية جزئية)

18 ملف تصنيف + `_INDEX.md`. صيغتها قائمة روابط بسهم:

```
# Keywords: Agency, Operations, CDA Agency, Services

→ [[Concept_AI_Chatbot_Types]]
→ [[Concept_Account_Setup_and_Warmup_SOP]]
→ [[Concept_Agency_Enlightened]]
```

| الملف | عدد `[[` |
|---|---|
| `06_agency.md` | 108 |
| `05_algorithm.md` | 108 |
| `13_business.md` | 103 |
| `10_psychology.md` | 91 |
| `07_team.md` | 85 |
| `02_vsl_sales.md` | 82 |
| `03_content_creation.md` | 78 |

المقيس: **289 مفهوماً فريداً فقط** عبر كل `keywords/` — أي **18% تغطية**. الجانب المشرّف: **0 رابط ميت** فيها؛ كل 289 يُحلّ إلى ملف حقيقي.

وأرقام `keywords/_INDEX.md` نفسها غير مطابقة لمحتوى ملفاتها — يقول `06_agency` ≈ 16 صفحة والملف فيه 108 روابط.

**الاتحاد (index.md + keywords/) = 434 مفهوماً من 1608 = 27% فقط.**

---

## 3) ثلاث ملفات مفاهيم — frontmatter كامل

### أ) `Concept_1_10_3_Rule.md` — النموذج الأنضج

```yaml
---
type: concept
name: 1-10-3 Rule
created: 2026-05-17
updated: 2026-05-21
deepened: 2026-05-21
deepener: phase2
tags: [validation, growth, metric, scaling, readiness]
related: [[Concept_Three_Phase_Growth_System]], [[Concept_Zero_To_One_Foundational_Phase]], [[Concept_Business_Launchpad]], [[Concept_Validated_Offer_Launch]], [[Concept_Marketing_Runway_80_20]]
sources: Source_Ahmed_Saddique_Channel
video: 26 — "This 3-Phase System Generated $1M+ For Our Clients"
---

# [[Concept_1_10_3_Rule]]

## من أين جاء المفهوم

أحمد صادق، من فيديو 26 (3-Phase System). يقدم قاعدة الـ 1-10-3 كمؤشر للجاهزية للانتقال من المرحلة الأولى (Sell 10) إلى المرحلة الثانية (Growth Flywheel).

## القاعدة
**1 Offer → $10K/Month → 3 Months Consecutive**
```

### ب) `Concept_Instagram_Lead_Gen_System.md` — يستخدم `title` لا `name`

```yaml
---
type: concept
title: Instagram Lead Gen System
date: 2025-05-18
deepened: 2026-05-22
deepener: phase2
tags: [outreach, lead-generation, instagram, similar-accounts, data-collection]
related: [[Concept_Similar_Accounts_Technique]], [[Concept_Client_Avatar_Instagram_Framework]]
sources: Source_3_Best_Ways_Clients_Online
---

# Concept_Instagram_Lead_Gen_System

## التعريف
نظام متكامل لجمع بيانات العملاء المحتملين (إيميلات) عبر Instagram...
```

فروق مقيسة عن (أ): `title` بدل `name`، `date` بدل `created`/`updated`، والعنوان H1 **بلا** `[[ ]]`.

### ج) `Concept_Dark_Needle_Self_Confidence.md` — **frontmatter مكسور**

```yaml
---
type: concept
name: Dark Needle Self-Confidence
created: 2026-05-15
updated: 2026-05-15
deepened: 2026-05-22
deepener: phase2
tags: [psychology, self_development, confidence, social_skills]
related: [[Concept_Psychopathic_Confidence]]
  - [[Concept_Self_Acceptance_Charisma]]
  - [[Concept_Self_Worth]]
  - [[Concept_Social_Value_Principle]]
  - [[Concept_Outcome_Independence]]
sources: []

# [[Concept_Dark_Needle_Self_Confidence]]
```

عيبان حقيقيان: (1) `related` يخلط صيغة inline مع صيغة القائمة `- ` — YAML غير صالح. (2) **لا يوجد `---` إغلاق** — الـ frontmatter مفتوح، فيبتلع المتن.

**قياس حجم المشكلة:** من 1608 ملف، **1550 سليم** و **58 ملف frontmatter غير مغلق** (3.6%). أمثلة: `Concept_Dream_100.md`, `Concept_Digital_Footprint.md`, `Concept_Dot_Point_Scripting.md`, `Concept_Desire_Mapping_Framework.md`.

### الحقول المستخدمة — إحصاء على 1608 ملف

| الحقل | العدد | التغطية |
|---|---|---|
| `type` | 1605 | 99.8% |
| `deepener` | 1538 | 95.6% |
| `deepened` | 1526 | 94.9% |
| `tags` | 1431 | 89.0% |
| `related` | 1388 | 86.3% |
| `sources` | 1301 | 80.9% |
| `created` | 1252 | 77.9% |
| `name` | 1165 | 72.4% |
| `updated` | 1054 | 65.5% |
| `title` | 177 | 11.0% |
| `status` | 93 | 5.8% |
| **`source_master`** | **62** | **3.9%** |
| `aliases` | 60 | 3.7% |
| `category` | 57 | 3.5% |
| `date` | 55 | 3.4% |
| `lang` | 52 | 3.2% |
| `entities` | 42 | 2.6% |
| `source` | 37 | 2.3% |
| `domain` | 10 | 0.6% |
| `cluster` | 7 | 0.4% |

الذيل يكشف تلوثاً: قيم تُقرأ كأسماء حقول لأن الـ frontmatter مكسور — `Taylor` (4)، `Curious` (2)، `Hook`، `CTA`، `Framework`، `Freelancing` (1 لكل).

### هل يوجد حقل يربط المفهوم بماستره؟

**نعم، لكن في 62 ملف فقط من 1608 (3.9%).** اسمه `source_master`، وقيمته اسم ملف نصي **لا wikilink**:

```yaml
source_master: Master_Content_Creation_Framework_V1.md
```

لا وجود لـ `parent:` ولا `master:` ولا `up:` (المقيس = 0 لكل منها). أقرب البدائل: `category:` (57)، `domain:` (10)، `cluster:` (7).

**تحقق حاسم:** الـ 62 مرجعاً تشير إلى **37 اسم ماستر فريد**، و **كلها الـ 37 موجودة فعلاً** في `nexus_vault/` — صفر مرجع مكسور. فالروابط سليمة؛ المشكلة أنها **نادرة**، لا أنها خاطئة.

مثال حرفي كامل — `Concept_11_Lego_Bricks_Video_Framework__11_Lego_Bricks.md`:

```yaml
---
type: concept
name: 11_Lego_Bricks_Video_Framework
status: active
source_master: Master_Content_Creation_Framework_V1.md
---
# 11 Lego Bricks Video Framework

domain: content_creation
concepts_covered: 18
tags: [content-creation, framework, strategy, ...]
related_masters: []
```

لاحظ أن `domain:` و `tags:` و `related_masters:` سقطت **تحت** سطر H1 — أي خارج الـ frontmatter، فلا يقرأها Obsidian كميتاداتا.

---

## 4) كيف يُربط المفهوم بالماستر عملياً؟

**الاتجاه السائد: الماستر يذكر المفهوم.** العلاقة أحادية بأغلبية ساحقة.

| الاتجاه | المقيس |
|---|---|
| ماستر → مفهوم | **1407** مفهوماً (87.5% من 1608) |
| مفهوم → ماستر (`source_master`) | **62** فقط (3.9%) |

من 1412 رابط `[[Concept_*]]` في الماسترات، **1407 يُحلّ** إلى ملف موجود و **5 معطوبة** — وسبب عطبها كلها شرطة مائلة عالقة من هروب `\|`:

```
Concept_11_Lego_Bricks_Video_Framework\
Concept_702010_Content_Framework\
Concept_75205_Content_Ratio\
Concept_Content_Diagnostic\
Concept_Youtube_Funnel
```

### مثال حرفي على الأحادية

الماستر يذكر المفهوم — `nexus_vault/01_outreach/Master_Lead_Generation.md:1469`:

```
| 3 | [[Concept_Dream_100]] | قصة Chet Holmes، قصة BetterAMS، Client+Partner Lists، مبادئ Destiny | غير محدد (Chet Holmes + BetterAMS) |
```

وسطر 1499 من الملف نفسه:

```
**المصادر الأعلى كثافة معلومات:** Concept_ICP_Client_Avatar، Concept_Dream_100، Concept_Lead_Progression_Pipeline — تُقدم أطر استراتيجية كاملة مع أمثلة واقعية موثّقة.
```

والمفهوم **لا يرد الرابط** — `wiki/concepts/Concept_Dream_100.md` كامل الـ frontmatter:

```yaml
---
type: concept
name: Dream 100 (المئة الحلم)
created: 2026-05-16
updated: 2026-05-21
deepened: 2026-05-21
deepener: phase2
tags: [marketing, partnerships, outreach, growth, inbound, networking]
related: [[Concept_Inbound_System_Agency]], [[Concept_Digital_Footprint]], ...
sources: []
```

لا `source_master`. ولا ذكر لـ `Master_Lead_Generation`. فمن داخل الويكي **لا سبيل لمعرفة ماستر هذا المفهوم** — المعرفة موجودة في اتجاه واحد فقط، ولا يستعيدها Obsidian إلا عبر لوحة Backlinks وبشرط أن يكون الـ vault الجامع مفتوحاً معه.

**201 مفهوماً لا يذكرها أي ماستر** — لا من هنا ولا من هناك.

---

## 5) هل المفاهيم موزعة في مجلدات فرعية؟

**كلها مسطحة. 1608 ملف في `concepts/` مباشرة، صفر مجلد فرعي.**

```
find concepts -mindepth 1 -type d | wc -l  →  0
```

التصنيف الموضوعي لا يسكن الشجرة، بل ثلاث آليات موازية خارجها: `tags:` في الـ frontmatter (1431 ملف)، وملفات `keywords/` (289 مفهوماً)، ومجلدات `nexus_vault/` الـ 26. المفارقة أن **الـ vault هو من يحمل التصنيف الهرمي الذي يفتقده الويكي**.

أثر عملي: `ls concepts/` يخرج 1608 سطراً بلا أي تجميع، ودليل واحد بحجم 250KB.

---

## 6) نمط تسمية الملفات

مقيس على 1608 ملف:

| الخصيصة | العدد |
|---|---|
| بادئة `Concept_` | **1608 (100%)** |
| فيه `_` | **1608 (100%)** |
| اسم عربي (حروف عربية) | **0 (0%)** |
| فيه مسافة | **1** |

**القاعدة: إنجليزي بالكامل، `Concept_` + Title_Case، شرطة سفلية بدل المسافة، لا حرف عربي واحد.** العربية محصورة في *محتوى* الملفات وقيمة `name:`، لا في أسمائها.

عينة 10 (كل 160 ملفاً):

```
Concept_1_10_3_Rule.md
Concept_BeContent_Video_Pipeline.md
Concept_Cold_Email_PSL_Strategies.md
Concept_Dark_Needle_Self_Confidence.md
Concept_Follow_Up_Sequence.md
Concept_Instagram_Lead_Gen_System.md
Concept_Name.md
Concept_Pre_Send_Email_Checks.md
Concept_Selective_Branding_Harvard_Model.md
Concept_Three_Motivators_Framework.md
```

عينة أول 10 أبجدياً — تكشف شذوذاً:

```
Concept_100K_Entrepreneur_Journey.md
Concept_100M_Views_Service_Guarantee.md
Concept_10x_Batch_Process.md
Concept_10x_vs_2x_Thinking.md
Concept_11_Lego_Bricks_Video_Framework.md
Concept_11_Lego_Bricks_Video_Framework__11_Lego_Bricks.md
Concept_1_10_3_Rule.md
Concept_20_80_Coaching_Rule.md
Concept_2C_Rule_Pattern_Cutting.md
Concept_360_Topic_Mapping.md
```

ملاحظات مقيسة على الشذوذ:
- `Concept_Name.md` — ملف قالب/نائب باسم حرفي `Name`.
- `__` مزدوجة في `Concept_11_Lego_Bricks_Video_Framework__11_Lego_Bricks.md`، وهو **تكرار** لـ `Concept_11_Lego_Bricks_Video_Framework.md` — لاحقة اندماج آلي.
- البدء برقم يفكك الترتيب الأبجدي (`10x` قبل `1_10_3`).

---

## 7) ما يجب أن يعرفه عامل الإثراء

مرتّبة بحسب الخطورة، وكلها مستنتجة من أرقام أعلاه لا من ظن:

1. **الويكي ليس مكتفياً بذاته.** الماسترات في `/sdcard/Nexus_Brain/nexus_vault/`. من يقرأ `wiki/` وحده سيرى 62 مرجع `source_master` معلّقاً في الهواء ويحكم خطأً بأنها روابط ميتة — وهي في الحقيقة صحيحة 37/37.
2. **الربط أحادي الاتجاه.** ماستر→مفهوم 1407، مفهوم→ماستر 62. لا تعتمد على الـ frontmatter لمعرفة ماستر مفهوم؛ لن تجده في 96% من الحالات.
3. **58 ملف frontmatter غير مغلق.** أي parser YAML صارم سيتعطل أو يبتلع المتن. تعامل بحذر قبل أي كتابة.
4. **`index.md` قديم:** يقول 1,240 مفهوماً، والواقع 1608. لا تستخدمه مصدر حقيقة للعدّ.
5. **201 مفهوماً بلا أي ماستر** — أوضح فجوة تغطية.
6. **الأسماء إنجليزية 100%، المحتوى عربي غالباً.** أي ملف جديد يجب أن يتبع `Concept_Title_Case_With_Underscores.md`.
7. **`_INDEX.md` في الموضعين لا يطابق القرص** (39 ماستر مُعلن مقابل 70 ملف؛ أرقام keywords مغلوطة). الملفات هي الحقيقة، لا الفهارس.
8. **Obsidian + Syncthing نشطان.** المجلد مسطح وضخم (1608 ملف/250KB دليل) — أي كتابة جماعية تُشعل مزامنة واسعة.

---

## ملحق — الأوامر المستخدمة

```bash
find wiki/ -maxdepth 2 -type d
find wiki/concepts -mindepth 1 -type d | wc -l
grep -roH '\[\[' --include='*.md' wiki/ | cut -d: -f1 | sort | uniq -c | sort -rn
awk 'FNR==1{inf=0} FNR==1&&/^---/{inf=1;next} inf&&/^---/{inf=0;next} \
     inf&&/^[a-zA-Z_]+:/{split($0,a,":");print a[1]}' wiki/concepts/*.md | sort | uniq -c | sort -rn
grep -h '^source_master:' wiki/concepts/*.md | sed 's/^source_master: *//' | sort -u
find /sdcard/Nexus_Brain/nexus_vault -name 'Master_*.md' | wc -l
grep -oh '\[\[Concept_[^]|#]*' $(find nexus_vault -name 'Master_*.md') | sed 's/^\[\[//' | sort -u
comm -23 all_concepts.txt master_concepts.txt | wc -l   # 201
ls -1 wiki/concepts | grep -cP '[\x{0600}-\x{06FF}]'    # 0
```

**لم يُنفَّذ أي أمر كتابة أو حذف أو نقل على `/sdcard/`.**
