# WORKFLOW — السلسلة الكاملة: من رابط حساب إلى معرفة في الويكي

الهدف الذي يريده المالك في جملة واحدة: **أعطِ رابط حساب إنستقرام، فتجري السلسلة كلها حتى تستقر المعرفة في العقل.**

هذا الملف هو الخريطة من طرف إلى طرف. الأوامر هنا منقولة كما هي من [`ACCOUNT_INSTRUCTION.md`](ACCOUNT_INSTRUCTION.md) — هو المرجع التفصيلي لكل flag وكل كود خروج، وهذا الملف هو الترتيب والمنطق بينها.

- جذر المشروع: `/root/r/nexus_enrichment` — **كل الأوامر تُنفَّذ من هنا**.
- المفسّر: `/usr/bin/python3` بالمسار الكامل دائماً.
- المرحلة الوحيدة التي **لا تُؤتمت**: بوابة القرار البشري بين الالتقاط والإثراء (§5).

---

## 0) الخريطة في سطر واحد

```
رابط الحساب → instruction.yaml → [اعتمادات] → [لوجن + كوكيز] → [التقاط بترقيم كامل]
      → handoff/batch_NN.md → ⛔ بوابة بشرية: decisions/*.json → [إثراء] → العقل
```

`run_mode` يحدّد أي جزء من هذا الخط يعمل. القيم الأربع المقبولة في `src/run.py`:

| `run_mode` | ما ينفّذه | متى تستخدمه |
|---|---|---|
| `capture` | المرحلة أ فقط: تصفّح + التقاط + dedup + بناء دفعات handoff، ثم يقف | أول لمسة لحساب جديد |
| `analyze` | المرحلة ب **لو وُجدت** `decisions/*.json` — وإلا لا يكتب شيئاً | بعد كتابة القرارات، تشغيل محافظ |
| `enrich` | المرحلة ب **دائماً**: يطبّق القرارات الموجودة على العقل | الوضع المعتاد بعد البوابة البشرية |
| `full` | أ ثم ب — والمرحلة ب تعمل **فقط لو وُجدت قرارات** | دورة كاملة على run قائم |

> ⚠️ `full` في `src/run.py` (المراحل أ+ب) شيء، و`orchestrate.py full` شيء آخر: الأخير يسلسل `login_only → capture → kaggle_sync` و**لا يشمل الإثراء إطلاقاً**. لا تخلط بينهما.

---

## 1) الاعتمادات — تُحمَّل ولا تُطبع

```bash
cd /root/r/nexus_enrichment
set -a; . control/credentials.env; set +a
```

قواعد ثابتة لا تُخرَق:

- الأسرار تعيش في `control/credentials.env` (صلاحية `600`) **فقط**.
- **ممنوع** `cat`/`grep`/`echo` على الملف أو أي من قيمه، وممنوع نسخ أي قيمة إلى توثيق أو سطر أوامر أو رسالة.
- الكود يقرأ من **متغيّرات البيئة حصراً**؛ لا يفتح الملف بنفسه. تحميله في الجلسة هو كل الربط المطلوب.
- المتغيّرات التي يقرأها الكود فعلاً: `IG_USERNAME`، `IG_PASSWORD`، `IG_2FA_CODE` (عند الطلب فقط)، و`KAGGLE_USERNAME`/`KAGGLE_KEY` تلتقطهما مكتبة kaggle من البيئة. `IG_ALIAS` موجود في الملف لكن **لا يقرأه أي كود** — الـ alias يأتي من `account_alias` في `config/settings.yaml`.

للتأكد أن التحميل نجح بلا كشف أي قيمة:

```bash
/usr/bin/python3 -c "import os; print('IG_USERNAME set:', bool(os.environ.get('IG_USERNAME'))); print('IG_PASSWORD set:', bool(os.environ.get('IG_PASSWORD')))"
```

يطبع `True/False` لا أكثر. لو ظهر `False` فالخطوة لم تُنفَّذ في **نفس** الطرفية.

---

## 2) الرابط → هدف

الرابط الذي يعطيه المالك يتحوّل إلى **username مجرّد**:

`https://www.instagram.com/suprava.ss/` ← `suprava.ss` (بلا `https://`، بلا `@`، بلا `/` في النهاية).

⚠️ يُكتب في `instruction.yaml` **وليس** في `config/settings.yaml`. `src/config.py` يقرأ `source_accounts` من ملف instruction حصراً؛ أي قيمة في `settings.yaml` تُهمَل بصمت ويقع الكود على `account_alias` كهدف تصفّح — أي أنك تكشط حسابك أنت لا الهدف.

```yaml
# /root/r/nexus_enrichment/instruction.yaml
source_accounts:
  - suprava.ss

run_mode: capture       # capture | analyze | enrich | full
max_items: 8
max_minutes: 15
resume_run: null
write_mode: auto-write
```

تحقّق قبل أي تشغيل حيّ:

```bash
/usr/bin/python3 scripts/orchestrate.py capture --dry-run
```

يطبع `Accounts: [...]` و`Alias: ...` والأمر المزمع دون تنفيذه. لو ظهر `Accounts: (لم تُحدَّد)` فالتعديل لم يُلتقط — لا تُكمل.

---

## 3) اللوجن والكوكيز

الجلسة تُحفظ في `state/session/<alias>.json` وتُعاد استخدامها. **لا تُعِد اللوجن إن كانت صالحة** — كل لوجن زائد مخاطرة كشف.

```bash
xvfb-run -a /usr/bin/python3 scripts/login_instagram.py --alias fluxa.grow
```

أو عبر الـ orchestrator (يلفّ `xvfb-run -a` تلقائياً عند غياب `DISPLAY`):

```bash
/usr/bin/python3 scripts/orchestrate.py login_only
```

**معيار النجاح ليس تغيّر الرابط** بل وجود كوكيز `sessionid` + `ds_user_id` فعلياً. التأكد بلا كشف أي قيمة:

```bash
/usr/bin/python3 -c "import sys; sys.path.insert(0,'src'); import session; \
s=session.load_storage_state('fluxa.grow'); \
n={c['name'] for c in (s or {}).get('cookies',[])}; \
print('sessionid:', 'sessionid' in n, '| ds_user_id:', 'ds_user_id' in n)"
```

أكواد الخروج: `0` نجاح · `1` اعتمادات ناقصة (ارجع لـ §1) · `2` انتهت المهلة بلا كوكيز — **لم يُحفظ شيء**.

لو ظهر `HardStop`: فحص السلامة يعمل على نص الصفحة **بعد** نجاح الدخول، فإطلاقه إشارة كشف حقيقية. **توقّف ولا تُعِد المحاولة فوراً.**

---

## 4) الالتقاط بترقيم كامل

```bash
/usr/bin/python3 src/run.py instruction.yaml
```

⚠️ **لا تستخدم `python3 -m src.run`** — وحدات `src/` تستورد بعضها مسطّحاً (`import capture`, `from config import ...`)، وتشغيلها كحزمة يرفع `ModuleNotFoundError`. النداء المباشر على المسار يضع `src/` في `sys.path` فيعمل الاستيراد.

كيف يعمل الترقيم فعلياً (`src/harvest.py`): **لا نرسل أي طلب بأنفسنا** — طلباتنا اليدوية يقابلها إنستقرام بـ 429 لأنها تفتقد بصمة المتصفح الكاملة. بدلاً من ذلك نستمع عبر `page.on("response")` لأجسام `/graphql/query` الحاملة `xdt_api__v1__feed__user_timeline_graphql_connection` (مخطط 2026)، و**السكرول اللطيف هو المحفّز الوحيد** لتحميل الدفعات التالية. صفر أفعال خارجية: لا نقر ولا إعجاب ولا متابعة.

> ⚠️ **حدّ الترقيم الحالي — قيد مفتوح.** `harvest_account` يسكرول `scroll_rounds = 4` جولات فقط ويقف عند `max_items`. لا يتتبّع `end_cursor`/`has_next_page`، فلا يوجد ترقيم غير محدود حتى آخر منشور. لاستيعاب حساب كامل: ارفع `max_items` و`max_minutes` وزد جولات السكرول. هذا هو العمل المتبقي المسجّل في [`STATUS.md`](STATUS.md).

السقوف تُقرأ من instruction (`max_items`, `max_minutes`) ومن `browse.*` في `settings.yaml`. حافة حقيقية: مهلة `_run_cmd` في الـ orchestrator **900 ثانية = 15 دقيقة** ومساوية تماماً لـ `max_minutes: 15`، فـ run يستهلك سقفه كاملاً قد يُقتل قبل كتابة `report.md`. اجعل `max_minutes` ≤ 12 أو شغّل `src/run.py` مباشرة.

المخرجات تحت `state/runs/<run_id>/`:

- `raw/items.jsonl` — الخام المُلتقط.
- `handoff/batch_NN.md` — الدفعات المعروضة للتحليل، كل عنصر بـ `item_id` ثابت.
- `report.md` — الحصيلة وأي hard stop.

ثم **يتوقّف**. بايثون لا يفهم المحتوى.

**مسار كاغل اختياري هنا** (نقل الجلسة للمعالجة الثقيلة): `orchestrate.py kaggle_sync` ثم `src/run_kaggle.py <run_id>`. قيد ترتيب إلزامي: `transfer_to_kaggle.py` أولاً لإنشاء `nexus-ig-session` قبل أي دفع كيرنل. راجع `ACCOUNT_INSTRUCTION.md` §4. **التوكن الحالي يرجع 401 على الرفع — قراءة فقط.**

---

## 5) ⛔ البوابة البشرية — القرارات

**هذه هي النقطة التي لا تُؤتمت، بالتصميم.**

بين المرحلتين يجلس قارئ (أنا) يفتح `state/runs/<run_id>/handoff/batch_NN.md`، ويقرّر لكل عنصر، ويكتب النتيجة في:

```
state/runs/<run_id>/decisions/*.json
```

كل قرار مربوط بـ `item_id` من الدفعة. الأفعال: `new` (مفهوم جديد) · `deepen` (إضافة إلى مفهوم قائم عبر `target_file`) · `skip` · `conflict`/needs_review (لا يلمس العقل إطلاقاً → `review/`).

**قاعدة البوابة الصارمة:**

> الإثراء لا يتقدّم خطوة واحدة ما لم توجد ملفات `decisions/*.json` فعلياً.

ما الذي يفرضها عملياً:

- `analyze` و`full` يشتغلان على المرحلة ب **فقط لو وُجدت قرارات**؛ بلا قرارات لا كتابة.
- `enrich` يقرأ عبر `handoff.DecisionReader`؛ مجلد بلا قرارات = كل الأعداد صفر و`report.md` يقول ذلك صراحةً.
- قرار فاسد الشكل يُعزل ولا يُطبَّق: يظهر `(quarantined) <source>` في التقرير.
- `conflict` لا يُكتب في العقل أبداً — يذهب إلى `review/` وينتظر إنساناً.

لا يوجد مسار في الكود يكتب في العقل بلا قرار مقابل. لو أردت السلسلة «كاملة بأمر واحد»، فالحلقة البشرية هي السقف: تُشغَّل أ، تُكتب القرارات، ثم تُشغَّل ب.

---

## 6) الإثراء — الكتابة في الويكي

الإثراء **يحتاج `resume_run`**. بدونه يولّد `src/run.py` معرّف run جديداً فارغاً ولن يجد أي قرار.

```yaml
# instruction.yaml
run_mode: enrich
resume_run: run_20260731_231038    # نفس اسم مجلد state/runs/<run_id> — لاحظ بادئة run_
write_mode: auto-write
```

`src/run.py` يولّد المعرّف بالشكل `run_<YYYYmmdd_HHMMSS>`، فقيمة `resume_run` لازم تحمل البادئة `run_`. (بخلاف `--run-id` في `transfer_to_kaggle.py` وهو توقيت خام بلا بادئة — معرّف نسخة داتاست لا مجلد run.)

```bash
/usr/bin/python3 src/run.py instruction.yaml
```

ترتيب الحواجز في `auto-write` — كلها إلزامية وبهذا الترتيب:

```
بوابة مساحة القرص → باك-أب الملف → سطر ledger + التحقق منه → كتابة ذرّية
```

لا كتابة بلا سطر ledger: يُكتب السجل **أولاً** ثم `verify_entry` قبل لمس الملف؛ الفشل يرفع `PermissionError` ولا يكتب شيئاً.

الوضع البديل `drafts-review` يوجّه الكتابة إلى `drafts/` و**لا يلمس** `/sdcard/Nexus_Brain` — استخدمه عند تجربة تغييرات جديدة.

شكل الصفحة المكتوبة: قالب `AUTO_GUIDE.md` بلا frontmatter — عنوان `# [[Concept_X]]` ثم **التعريف / الآلية / التطبيق / مثال / مرتبط بـ**، وبيانات الأصل كتعليق HTML في الذيل. اسم الملف يحمل بادئة `Concept_` الإلزامية. الحقل الناقص يُعلَّم `— (يحتاج تعميقاً من مصدر إضافي)` ولا يُختلق.

حاجز المسار: `target_file` القادم من قرار النموذج يُحلّ داخل `brain_root`؛ أي مسار يستقر خارج العقل (`../..` أو مسار مطلق أجنبي) يرفع `PermissionError` ولا يُكتب.

المخرجات: ملفات في مجلد المفاهيم داخل العقل، و`review/` للتعارضات، و`state/provenance/` (ledger)، و`report.md` محدَّث بأعداد كُتب/عُمّق/مسودات/مراجعة/تُجوهل.

> **ما لا يفعله الإثراء بعد:** لا يحدّث ملفات المسك الأربعة التي يفرضها `AUTO_GUIDE.md` (`wiki/index.md`، `NEXUS_LLM_WIKI.md`، `wiki/CHECKPOINT.md`، `wiki/keywords/`)، ولا يربط المفهوم بماستره في `nexus_vault/`. الربط مقترح يدوياً في [`MAPPING_concepts_to_masters.md`](MAPPING_concepts_to_masters.md) وينتظر موافقة المالك. تفاصيل في [`STATUS.md`](STATUS.md).

---

## 7) بطاقة السلسلة كاملة

```bash
cd /root/r/nexus_enrichment
set -a; . control/credentials.env; set +a          # 1. اعتمادات (لا تُطبع)

# 2. الرابط → instruction.yaml (source_accounts) + run_mode: capture
/usr/bin/python3 scripts/orchestrate.py capture --dry-run

# 3. لوجن (مرة واحدة، ثم أعِد استخدام الجلسة)
xvfb-run -a /usr/bin/python3 scripts/login_instagram.py --alias fluxa.grow

# 4. التقاط
/usr/bin/python3 src/run.py instruction.yaml

# ⛔ 5. بوابة بشرية: اقرأ handoff/batch_NN.md واكتب decisions/*.json
#     بلا هذه الملفات لا يتقدّم الإثراء خطوة واحدة.

# 6. إثراء (run_mode: enrich + resume_run: run_<ts>)
/usr/bin/python3 src/run.py instruction.yaml
```

---

## قواعد لا تُخرَق

- **لا سرّ يُطبع**، ولا قيمة تُنسخ من `credentials.env` إلى أي ملف أو أمر.
- **لا كتابة في العقل بلا باك-أب وسطر ledger** مقابل.
- **الويكي عليه Obsidian + Syncthing نشطان**: أي كتابة جماعية تُشعل مزامنة واسعة — اكتب قليلاً وتحقّق.
- **لا تخمّن رقماً**: كل رقم في `control/` مقيس من ملف فعلي. إن لم تجد المصدر، اكتب «غير معروف».
- عند `HardStop` أو أي إشارة كشف: **توقّف**، لا تُعِد المحاولة في نفس الجلسة.
