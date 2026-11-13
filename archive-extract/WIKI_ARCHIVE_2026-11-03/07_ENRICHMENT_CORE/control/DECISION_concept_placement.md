# قرار: أين يكتب enrich.py ملفات الـ concepts؟

- **الحالة:** مفتوح — بانتظار قرار المالك
- **التاريخ:** 2026-07-31
- **النطاق:** `src/enrich.py` + `config/settings.yaml`
- **ملاحظة:** هذا المستند فحص وتوثيق فقط. لم يُنقل ولم يُحذف ولم يُعدَّل أي كود أو ملف عقل.

---

## 1. تصحيح مهم لصياغة السؤال

السؤال افترض أن «الويكي يستخدم ملفات مسطحة `Concept_<Name>.md` في الجذر». **الفحص لا يؤكد هذا.**

جذر `/sdcard/Nexus_Brain` يحوي 3 ملفات `Concept_*.md` فقط، وكلها **فارغة (0 بايت)**. الويكي الحقيقي ليس في الجذر، بل في مسار **متداخل**:

```
/sdcard/Nexus_Brain/Nexus_Brain/wiki/concepts/
```

أي أن اسم المجلد `Nexus_Brain` مكرَّر مرتين في المسار. هذا يطابق ما ورد في سجل المحادثة القديم `insta.md:5401`.

---

## 2. الأرقام

### ملفات `Concept_*.md` حسب المجلد

| المسار | العدد | الحجم | الحالة |
|---|---|---|---|
| `Nexus_Brain/wiki/concepts/` (المتداخل) | **1608** | ~18 MB | الويكي الحقيقي، محتوى كامل |
| `nexus_vault/` | 3 | 0 بايت | أطلال فارغة |
| الجذر `/sdcard/Nexus_Brain/` | **3** | 0 بايت | أطلال فارغة |
| **الإجمالي** | **1614** | | |

- ملفات الجذر الثلاثة: `Concept_Cognitive_Dissonance.md`، `Concept_Compound_Trust_Flywheel.md`، `Concept_Psychology_Of_Ego.md` — تواريخها مايو، وكلها صفر بايت.
- داخل `wiki/concepts/`: **0** ملف بدون سابقة `Concept_` — التسمية متسقة 100%.
- أحدث نشاط حقيقي في الويكي: `Concept_Artist_vs_Entrepreneur_Mindset.md` (23 يوليو، 15 KB).

### ما يكتبه الوكيل فعلاً الآن

`/sdcard/Nexus_Brain/concepts/` — مجلد منفصل تماماً، فيه **4 ملفات** بتاريخ 31 يوليو 23:34:

```
playbook_النمو_المقود_بالمستخدم_Cursor.md
التواصل_المبني_على_الإشارات_بدل_الرش_العشوائي.md
تأهيل_العميل_قبل_مكالمة_البيع_بإظهار_العمل_السابق.md
تمثيل_سجل_المحادثات_كخريطة_معرفية_ثلاثية_الأبعاد.md
```

**فجوتان لا واحدة:**
1. **فجوة مسار:** `concepts/` مقابل `Nexus_Brain/wiki/concepts/`.
2. **فجوة تسمية:** أسماء عربية بلا سابقة، مقابل `Concept_<English_Name>.md`. السبب أن `_slug()` في `enrich.py:38` يعتمد `str.isalnum()` وهي `True` للحروف العربية، فتمرّ كما هي ولا تُضاف سابقة `Concept_` إطلاقاً.

### فجوة ثالثة: الـ frontmatter

الويكي القائم:
```yaml
type: concept
name: YouTube_SEO_Keywords
status: active
source_master: Master_YouTube_Strategy.md
```

ما يولّده `render_concept_md()` (`enrich.py:60`):
```yaml
type: tactical          # claim_type لا الكلمة الحرفية "concept"
sources_count: 2
confidence: 0.8
provenance_account: fluxa.grow
run_id: ...
created_at: ...
tags: [single-source]
related: []
deepened: false
```

الحقلان مختلفان في المفتاح `type` وفي غياب `name`/`status`. أي أداة تصنّف بـ `type: concept` لن ترى مخرجات الوكيل.

---

## 3. هل `concepts_subdir` قابل للضبط من `settings.yaml`؟

**لا.** قابل للضبط من الكود فقط، وغير موصول بالإعدادات إطلاقاً.

سلسلة الأدلة:

| الموضع | الحقيقة |
|---|---|
| `src/enrich.py:102` | `concepts_subdir: str = "concepts"` — معامل بانٍ بقيمة افتراضية |
| `src/enrich.py:111` | `self.concepts_dir = self.brain_root / concepts_subdir` |
| `src/run.py:184-189` | الاستدعاء الوحيد الحقيقي — **لا يمرّر `concepts_subdir` أبداً**، فتسري القيمة الافتراضية |
| `src/config.py:20-31` | `Config` dataclass لا يحوي أي حقل concepts |
| `config/settings.yaml` | لا مفتاح `concepts` ولا `concepts_subdir` (grep = صفر نتائج) |

الخلاصة: المعامل موجود ومُعَد للحقن، لكن السلك بين YAML و`Enricher` غير موصول. وضع `concepts_subdir:` في `settings.yaml` اليوم **لن يفعل شيئاً بصمت** — وهذا أسوأ من الخطأ الصريح.

---

## 4. الخياران

### الخيار أ — إصلاح بسطر واحد (تمرير القيمة الصحيحة عند الاستدعاء)

تمرير `concepts_subdir="Nexus_Brain/wiki/concepts"` في `run.py:184`.

- ✅ أصغر تغيير ممكن، سطر واحد، لا تغيير في بنية الإعدادات
- ✅ `Path` يقبل المسار متعدد المقاطع بلا مشاكل
- ❌ يدفن مسار عقل حقيقياً داخل كود المنطق
- ❌ لا يحل فجوة التسمية ولا فجوة الـ frontmatter
- ❌ تغييره لاحقاً يتطلب تعديل كود لا إعداد

### الخيار ب — توصيل المسار للإعدادات + توحيد التسمية والـ frontmatter

1. إضافة `concepts_subdir` إلى `settings.yaml` تحت `nexus_brain_root`.
2. إضافة الحقل إلى `Config` وقراءته في `load_config`.
3. تمريره في `run.py:184`.
4. تعديل `_slug()`/`_concept_path()` لإنتاج سابقة `Concept_` بما يطابق الويكي.
5. مواءمة `render_concept_md()` مع `type: concept` + `name:` + `status:` مع إبقاء حقول التتبّع الإضافية.

- ✅ يغلق الفجوات الثلاث معاً
- ✅ المسار يصبح إعداداً، والاختبار على مجلد وهمي يبقى ممكناً
- ✅ مخرجات الوكيل تندمج بصرياً ومنطقياً مع 1608 ملفاً قائماً
- ❌ يلمس 4 ملفات و`test_enrich.py`
- ❌ قرار التسمية العربية/الإنجليزية يحتاج حسماً من المالك (انظر §7)

---

## 5. التوصية

**الخيار ب، على مرحلتين.**

السبب أن الخيار أ يعالج العَرَض الأظهر (المسار) ويترك مخرجات الوكيل غريبة داخل الويكي: بلا سابقة `Concept_`، وبـ `type` لا يساوي `concept`. النتيجة 1608 ملفاً بقاعدة، وحفنة ملفات بقاعدة أخرى في المجلد نفسه — وهو أسوأ من فصلهما في مجلدين.

التقسيم المقترح:

- **مرحلة 1 (حاجزة، صغيرة):** المسار + الـ frontmatter. تجعل الكتابة تصل للمكان الصحيح بشكل صحيح.
- **مرحلة 2 (بعد حسم §7):** قاعدة التسمية والسابقة.

وحتى تُنفَّذ المرحلة 1، الأسلم إبقاء `mode: drafts-review` بدل `auto-write` الحالي، حتى لا تتراكم كتابات في المسار الخطأ.

---

## 6. خطوات التنفيذ

> لم يُنفَّذ أي منها. للتنفيذ بعد الموافقة.

**المرحلة 1**

1. **باك-أب:** أرشفة `Nexus_Brain/wiki/concepts/` قبل أول كتابة تلقائية.
2. `config/settings.yaml` — إضافة تحت `nexus_brain_root`:
   ```yaml
   concepts_subdir: Nexus_Brain/wiki/concepts
   ```
3. `src/config.py` — إضافة `concepts_subdir: str` إلى `Config`، وقراءتها في `load_config` بافتراضي `"Nexus_Brain/wiki/concepts"`.
4. `src/run.py:184` — تمرير `concepts_subdir=cfg.concepts_subdir`.
5. `src/enrich.py:60` — مواءمة الـ frontmatter: `type: concept`، إضافة `name:` و`status: active`، ونقل `claim_type` إلى حقل مستقل.
6. **اختبار:** `pytest tests/test_enrich.py` + تشغيل `drafts-review` واحد والتحقق من المسار الناتج قبل تفعيل `auto-write`.

**المرحلة 2** (بعد حسم §7)

7. تعديل `_slug()`/`_concept_path()` لإضافة سابقة `Concept_`.
8. تحديث `tests/test_enrich.py` للقاعدة الجديدة.

**تنظيف منفصل (لا يُخلط بما سبق)**

9. الملفات الستة الفارغة (3 في الجذر + 3 في `nexus_vault/`) — مرشّحة للحذف، **لكن الحذف يحتاج إذناً صريحاً ولا يدخل هذا القرار**.
10. الملفات الأربعة في `/sdcard/Nexus_Brain/concepts/` — محتوى حقيقي بتاريخ 31 يوليو. تحتاج قراراً منفصلاً: تُرحَّل بعد إعادة التسمية، أم تُترك.

---

## 7. سؤال واحد للمالك

الويكي كله مسمّى بالإنجليزية (`Concept_YouTube_SEO_Keywords`)، ومخرجات الوكيل عربية بالكامل. أيّهما؟

- **(أ)** سابقة + ترجمة للإنجليزية: `Concept_Signal_Based_Outreach.md` — اتساق تام مع 1608 ملفاً، لكن يتطلب خطوة ترجمة في التوليد.
- **(ب)** سابقة مع إبقاء العربية: `Concept_التواصل_المبني_على_الإشارات.md` — بلا ترجمة، لكن يكسر اتساق التسمية.
- **(ج)** إبقاء الوضع الحالي بلا سابقة.

**التوصية: (ب).** الترجمة الآلية للعناوين تولّد انحرافاً دلالياً وتخلق تكراراً حين يُترجم المفهوم نفسه بصيغتين مختلفتين في تشغيلين. السابقة وحدها تكفي لالتقاط الأدوات التي تعتمد نمط `Concept_*`.

---

## 8. ملاحظة جانبية اكتُشفت أثناء الفحص

`enrich.py:162` في مسار `deepen`:

```python
target = Path(d.target_file) if d.target_file else self._concept_path(d.concept)
```

`d.target_file` يُستخدم كما هو بلا ربط بـ `brain_root`. والقيمة في `tests/test_production_run.py:74` **نسبية**: `"Concept_Artist_vs_Entrepreneur_Mindset.md"`. مسار نسبي كهذا يُحلّ مقابل مجلد العمل الحالي، فقد يكتب `deepen` خارج العقل تماماً.

لم أعدّل شيئاً. يستحق قراراً مستقلاً (تحويل `target_file` النسبي إلى `brain_root / target_file`).
