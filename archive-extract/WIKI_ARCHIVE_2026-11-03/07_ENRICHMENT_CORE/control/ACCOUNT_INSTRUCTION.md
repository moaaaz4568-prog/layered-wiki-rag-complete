# أعطني رابط حساب إنستقرام وسأستخرج منه المعرفة

دليل تنفيذي بالأوامر الحقيقية الموجودة فعلاً في السكربتات. كل flag هنا مُتحقَّق منه من الكود.

- جذر المشروع: `/root/r/nexus_enrichment` — **نفّذ كل الأوامر من هذا الجذر**.
- المفسّر: `/usr/bin/python3` بالمسار الكامل (وليس `python3` المجرّد؛ الـ `python3` الذي يقع عليه الـ PATH لا يرى مكتبات المشروع). `orchestrate.py` نفسه يثبّت `PYTHON = "/usr/bin/python3"`.
- الأسرار: في `control/credentials.env` فقط. لا تكتب أي كلمة مرور أو توكن في ملفات المشروع ولا في سطر الأوامر.

---

## 0) تحميل الاعتمادات (مرة واحدة في كل جلسة طرفية)

```bash
cd /root/r/nexus_enrichment
set -a; . control/credentials.env; set +a
```

المتغيّرات التي يقرأها الكود فعلاً:

| المتغيّر | من يقرأه | إلزامي؟ |
|---|---|---|
| `IG_USERNAME` | `scripts/login_instagram.py` + بوّابة `orchestrate.py` (`_has_ig_credentials`) | نعم للّوجن |
| `IG_PASSWORD` | نفسه | نعم للّوجن |
| `IG_2FA_CODE` | `scripts/login_instagram.py` (`_handle_two_factor`) | فقط لو الحساب يطلب 2FA |
| `IG_ALIAS` | **لا أحد** — موجود في `credentials.env` لكن لا يقرأه أي كود. الـ alias يأتي من `account_alias` في `config/settings.yaml` أو من `--alias` | لا |
| `KAGGLE_USERNAME` / `KAGGLE_KEY` | مكتبة kaggle نفسها (`read_config_environment` تلتقط أي `KAGGLE_*` من البيئة) | بديل عن `~/.kaggle/kaggle.json` |
| `CHROMIUM_PATH` | `scripts/login_instagram.py` (`_resolve_chromium`) | لا — يقع تلقائياً على `/usr/local/playwright/chromium-*/chrome-linux/chrome` |

لو `IG_USERNAME`/`IG_PASSWORD` غير مضبوطين، السكربت يسأل عبر `input()`/`getpass()` — وفي تشغيل غير تفاعلي يتعلّق حتى المهلة. لذلك `orchestrate.py` يفشل سريعاً بـ **rc=2** بدل التعليق.

اعتماد Kaggle: `~/.kaggle/kaggle.json` موجود ويكفي. تحميل `credentials.env` (الخطوة 0) يصدّر أيضاً `KAGGLE_USERNAME`/`KAGGLE_KEY` وتلتقطهما مكتبة kaggle من البيئة مباشرة — الاثنان مساران صالحان، لا حاجة لنسخ أي قيمة يدوياً.

---

## 1) حدّد حساب المصدر (الرابط الذي أعطيتني إياه)

⚠️ **حسابات المصدر تُكتب في `instruction.yaml` وليس في `config/settings.yaml`.**
`src/config.py` يقرأ `source_accounts` من ملف instruction **حصراً** (`instr.get("source_accounts")`)؛ أي قيمة تضعها في `settings.yaml` تُهمَل بصمت وسيقع الكود على `account_alias` كهدف تصفّح (وهو حسابك أنت، لا الهدف).

عدّل `/root/r/nexus_enrichment/instruction.yaml`:

```yaml
source_accounts:
  - suprava.ss          # الـ username فقط، بلا https:// وبلا @ وبلا / في النهاية

run_mode: capture       # capture | analyze | enrich | full
max_items: 8
max_minutes: 15
resume_run: null
write_mode: auto-write  # قرار المالك المعتمد — كتابة مباشرة في العقل
```

تحويل الرابط إلى قيمة صحيحة: `https://www.instagram.com/suprava.ss/` ← `suprava.ss`.

القيم التي تُقرأ من `config/settings.yaml` (لا من instruction): `account_alias`، `project_root`، `nexus_brain_root`، `browse.*`، `verification.*`، و`mode` (كافتراضي لـ `write_mode`).

تحقّق قبل التشغيل:

```bash
/usr/bin/python3 scripts/orchestrate.py capture --dry-run
```

يطبع `Accounts: [...]` و`Alias: ...` والأمر المزمع دون تنفيذه. لو ظهر `Accounts: (لم تُحدَّد)` فالتعديل لم يُلتقط.

---

## 2) اللوجن وحفظ الجلسة

الجلسة تُحفظ في `state/session/<alias>.json` وتُعاد استخدامها؛ لا تُعِد اللوجن إن كانت صالحة.

```bash
xvfb-run -a /usr/bin/python3 scripts/login_instagram.py --alias fluxa.grow
```

عبر الـ orchestrator (يلفّ `xvfb-run -a` تلقائياً عند غياب `DISPLAY`):

```bash
/usr/bin/python3 scripts/orchestrate.py login_only
```

الـ flags الحقيقية في `login_instagram.py`:

| flag | المعنى |
|---|---|
| `--alias` | **إلزامي**. اسم ملف الجلسة. القيمة الحالية: `fluxa.grow` |
| `--headless` | متصفح بلا واجهة (بديل عن `xvfb-run`؛ أكثر عرضة لكشف إنستقرام) |
| `--session-dir` | مجلد الجلسات (افتراضي `state/session/`) |
| `--timeout` | ثواني انتظار اكتمال الدخول (افتراضي **180**) — تشمل وقت حلّ التحدي يدوياً |

`orchestrate.py login_only` يقبل `--alias` و`--headless` فقط من هذه.

**معيار النجاح** ليس تغيّر الرابط، بل وجود كوكيز `sessionid` + `ds_user_id` فعلياً.

أكواد خروج `login_instagram.py`:

| rc | المعنى | التصرّف |
|---|---|---|
| 0 | نجاح — طبع `✅ تم حفظ الحالة: <path>` | تابع للخطوة 3 |
| 1 | لا اسم مستخدم أو لا كلمة مرور | حمّل `control/credentials.env` (الخطوة 0) |
| 2 | انتهت المهلة بلا `sessionid`/`ds_user_id` — **لم يُحفظ شيء** | راجع الأعطال أدناه |

أعطال شائعة في اللوجن:

- **`⚠️ إنستقرام يطلب تحدياً/تحققاً`** — نقطة تفتيش. النافذة تُترك مفتوحة تحت Xvfb حتى نفاد المهلة؛ في تشغيل بلا شاشة لن يحلّها أحد ← rc=2. زد `--timeout` واحضر جلسة VNC، أو سجّل من متصفح عادي على نفس الـ IP أولاً لتهدئة الحساب.
- **`تنبيه: مطلوب رمز 2FA ولا يوجد إدخال متاح`** — صدّر `IG_2FA_CODE` قبل التشغيل.
- **`تنبيه: لم يتم العثور على زر إرسال`** — تحذير لا فشل؛ السكربت يجرّب `Enter` في حقل كلمة المرور. المهم هو الكوكيز.
- **rc=2 مع كوكيز ناقصة `sessionid`** — كلمة مرور خاطئة، أو إنستقرام رفض الجلسة. الرسالة تسمّي الكوكي المفقود.
- **انهيار Chromium فوراً** — مسار المتصفح. صدّر `CHROMIUM_PATH` لمسار موجود؛ وسائط `--no-sandbox --disable-dev-shm-usage` مضبوطة أصلاً للعمل داخل proot.
- **`HardStop`** — فحص السلامة يعمل على **نص** الصفحة بعد نجاح الدخول فقط، فلو أُطلق فهي إشارة كشف حقيقية: توقّف، لا تُعِد المحاولة فوراً.

تأكيد الجلسة بلا كشف أي قيمة:

```bash
/usr/bin/python3 -c "import sys; sys.path.insert(0,'src'); import session; \
s=session.load_storage_state('fluxa.grow'); \
n={c['name'] for c in (s or {}).get('cookies',[])}; \
print('sessionid:', 'sessionid' in n, '| ds_user_id:', 'ds_user_id' in n)"
```

---

## 3) الالتقاط (المرحلة أ)

```bash
/usr/bin/python3 src/run.py instruction.yaml
```

⚠️ **لا تستخدم `python3 -m src.run`** — وحدات `src/` تستورد بعضها مسطّحاً (`import capture`, `import session`, `from config import ...`)، وتشغيلها كحزمة يرفع `ModuleNotFoundError`. النداء المباشر على المسار `src/run.py` يضع `src/` في `sys.path` فيعمل الاستيراد المسطّح.

أو عبر الـ orchestrator (نفس الأمر بالضبط، من جذر المشروع):

```bash
/usr/bin/python3 scripts/orchestrate.py capture
```

`src/run.py` يقبل: وسيطاً موضعياً واحداً `instruction` (مسار instruction.yaml، اختياري) و`--settings <path>`. **لا يوجد `--dry-run` في `src/run.py`** — الـ `--dry-run` خيار على مستوى `orchestrate.py` فقط (يطبع الأمر ولا ينفّذه).

ما يحدث: تحميل الجلسة (بـ `account_alias`) ← تصفّح `source_accounts` ← التقاط ← dedup ضد `state/seen.sqlite` ← بناء دفعات handoff. ثم **يتوقّف** — بايثون لا يفهم المحتوى.

المخرجات تحت `state/runs/<run_id>/`:

- `handoff/batch_NN.md` — الدفعات المعروضة للتحليل، كل عنصر بـ `item_id` ثابت.
- `report.md` — الحصيلة: المُلتقط، عدد الدفعات، الملاحظات، أي hard stop.

أكواد خروج `src/run.py`:

| rc | المعنى |
|---|---|
| 0 | اكتمل (حتى لو 0 عناصر — راجع `report.md`) |
| 2 | `hard stop` من `safety.py` — توقّف بأمان والجلسة محفوظة |

أعطال شائعة في الالتقاط:

- **`source_accounts فاضية — وقعنا على operator alias كهدف تصفّح`** في `report.md` — عدّلت الملف الخطأ. ارجع للخطوة 1.
- **`account_alias إلزامي (SPEC §2.3)`** (`ValueError`) — `account_alias` مفقود من `config/settings.yaml`.
- **الجلسة `None`** — لا ملف جلسة أو تالف. `load_storage_state` يرجّع `None` بلا انهيار فيفشل التصفّح لاحقاً. أعِد الخطوة 2.
- **`بلغنا سقف الزمن (15 دقيقة)`** / **`بلغنا سقف العناصر (8)`** — ملاحظة طبيعية، أهداف بقيت بلا تصفّح. ارفع `max_items`/`max_minutes` في instruction.
- **rc=124 من الـ orchestrator** — مهلة `_run_cmd` هي **900 ثانية = 15 دقيقة**، ومساوية تماماً لـ `max_minutes: 15`. حافة حقيقية: run يستهلك سقفه الزمني كاملاً قد يُقتل قبل كتابة `report.md`. اجعل `max_minutes` ≤ 12، أو شغّل `src.run` مباشرة بلا orchestrator.
- **0 عناصر مع تكرار التشغيل** — dedup يحجب ما رأيناه سابقاً. للاختبار النظيف: انقل `state/seen.sqlite` مؤقتاً (لا تحذفه).

---

## 4) مزامنة Kaggle (نقل الجلسة للمعالجة الثقيلة)

⚠️ **قيد ترتيب إلزامي:** `scripts/transfer_to_kaggle.py` يجب أن يُشغَّل **مرة أولاً** لإنشاء داتاست `nexus-ig-session` **قبل** أي دفع للكيرنل. الكيرنل يعلن الداتاست في `dataset_sources` داخل `kernel-metadata.json`، وكاغل يرفض الدفع لو الـ slug المُعلَن غير موجود. الترتيب: `transfer_to_kaggle.py` ← ثم دفع الكيرنل (`src/run_kaggle.py` / `kaggle_bridge.push_and_run_kernel`).

```bash
/usr/bin/python3 scripts/transfer_to_kaggle.py \
  --storage-state state/session/fluxa.grow.json \
  --run-id "$(date -u +%Y%m%d_%H%M%S)"
```

أو:

```bash
/usr/bin/python3 scripts/orchestrate.py kaggle_sync
```

الـ orchestrator يبني `--storage-state` تلقائياً من `state/session/<alias>.json` ويولّد `--run-id` من التوقيت، ويتحقق من وجود الملف قبل الاستدعاء.

الـ flags الحقيقية في `transfer_to_kaggle.py`:

| flag | المعنى |
|---|---|
| `--storage-state` | **إلزامي** (`required=True`). بدونه argparse يخرج بـ 2 |
| `--run-id` | افتراضي `"default"`. يدخل في **ملاحظات النسخة** لا في اسم الـ dataset |
| `--dataset-title` | عنوان الـ dataset (افتراضي `"IG Session (private)"`) |
| `--config` | مسار YAML للإعدادات (افتراضي `None` ← يقع على `config/settings.yaml`) |
| `--staging-dir` | مجلد التحضير (افتراضي `state/kaggle/session_transfer`) |

الـ orchestrator يمرّر `--run-id` و`--storage-state` فقط، ويقبل هو `--run-id`, `--alias`, `--storage-state`.

⚠️ **الـ slug ثابت ولا يحمل run_id**: `COOKIES_DATASET_NAME = "nexus-ig-session"` ← الـ dataset هو `<username>/nexus-ig-session` دائماً. هذا مقصود: `kaggle_instagram_knowledge_extractor.py` يقرأ `/kaggle/input/nexus-ig-session/cookies.txt` بمسار حرفي، فاسم متغيّر يكسر الربط. تشغيل ثانٍ ينشئ **نسخة جديدة** (`dataset_create_version`) بملاحظة `session refresh <run_id>`.

الـ dataset يُنشأ **خاصاً دائماً** (`isPrivate: True`, ترخيص `other`) لأن الملف يحمل كوكيز جلسة حيّة. المجلد يحوي أيضاً `cookies.txt` بصيغة Netscape (يولّده `src/cookies_export.py`) — بدونه يعمل المستخرِج مجهولاً ويرجّع صفر عناصر.

أكواد خروج `transfer_to_kaggle.py`:

| rc | المعنى | التصرّف |
|---|---|---|
| 0 | نجاح — يطبع `Dataset URL: https://www.kaggle.com/datasets/<user>/nexus-ig-session` | تابع |
| 2 | `storage_state` مفقود أو JSON فاسد أو فارغ (لا cookies ولا origins)، أو فشل staging، أو flag إلزامي ناقص | أعِد الخطوة 2 |
| 3 | فشل الرفع إلى Kaggle | راجع أدناه |

أعطال شائعة في المزامنة:

- **rc=2 `storage_state فارغ`** — لوجن لم ينتج كوكيز. أعِد الخطوة 2.
- **تحذير `لا يوجد كوكي sessionid في الجلسة`** — ليس فشلاً؛ الرفع يكمل لكن جانب Kaggle سيعمل مجهولاً. أعِد اللوجن قبل دفع الكيرنل.
- **rc=3 مصادقة** — `~/.kaggle/kaggle.json` مفقود أو توكن منتهي. البديل الأنظف: حمّل `control/credentials.env` (الخطوة 0) فتلتقط مكتبة kaggle `KAGGLE_USERNAME`/`KAGGLE_KEY` من البيئة. لا تنسخ أي قيمة سر إلى ملف داخل المشروع.
- **`لم يحدد username في ملف ~/.kaggle/kaggle.json`** — الملف ناقص المفتاح `username` ولا `KAGGLE_USERNAME` في البيئة.
- **rc=3 حصص/شبكة** — أعِد المحاولة بنفس `--run-id` (سيصنع نسخة جديدة، لا تكراراً).

---

## دفع الكيرنل إلى Kaggle

بعد أن ينشئ `scripts/transfer_to_kaggle.py` داتاست `nexus-ig-session` بنجاح (الخطوة 4)، يُدفع كيرنل التفريغ عبر `src/kaggle_bridge.py`. الثوابت مكتوبة في رأس الملف ولا تُمرَّر كـ flags:

| الثابت | القيمة | الدور |
|---|---|---|
| `KAGGLE_USER` | `moazhuman` | مالك الداتاست والكيرنل |
| `DATASET_SLUG` | `nexus-posts` | داتاست المنشورات (`moazhuman/nexus-posts`) — يرفعه `push_dataset(posts.json)` |
| `KERNEL_SLUG` | `nexus-transcribe` | الكيرنل (`moazhuman/nexus-transcribe`) — يرفعه ويشغّله `push_and_run_kernel(notebook)` |

المسار العملي كاملاً هو `src/run_kaggle.py`، وهو يوصل الدوال الأربع بالترتيب:

```bash
/usr/bin/python3 src/run_kaggle.py run_20260731_120000
```

ما ينفّذه بالتفصيل:

1. يجمع `state/runs/<run_id>/posts/*.json` في `posts.json` واحد. لو المجلد فارغ يخرج بـ `{"error": "لا منشورات في posts/ — شغّل harvest أولاً"}` و rc=1.
2. `build_notebook` يبني `state/kaggle/kernel/nexus-transcribe.ipynb` برمجياً من خليتَي `kaggle_transcribe.py` (`INSTALL_CELL` + `PROCESS_CELL`) — **لا تحرّر الـ ipynb يدوياً، فهو يُعاد بناؤه في كل تشغيل**.
3. `push_dataset(posts_json)` — ينشئ `moazhuman/nexus-posts` أول مرة، أو `dataset_create_version` بعدها.
4. `push_and_run_kernel(nb)` — يكتب `kernel-metadata.json` بـ `dataset_sources: ["moazhuman/nexus-posts"]` مع GPU وإنترنت مفعّلين، ثم يدفع فيبدأ التشغيل تلقائياً.
5. `wait_for_kernel()` — استقصاء كل **30 ثانية** بسقف **3600 ثانية**، يتوقّف عند `complete` أو `error` أو `cancel`. عند نفاد السقف يرجّع نصاً يبدأ بـ `timeout بعد 3600s` ولا يرفع استثناءً — فالكيرنل قد يكون ما زال يعمل على Kaggle.
6. `pull_output(dest)` — يسحب المخرجات (`transcripts.json`) إلى `state/runs/<run_id>/transcripts/`.

فحص الحالة وحدها بلا دفع:

```bash
/usr/bin/python3 src/kaggle_bridge.py --status
```

⚠️ **التوكن الحالي يرجع 401 على الرفع — قراءة فقط.** الاستعلام (`datasets status`, `kernels status`) يمرّ، لكن `push_dataset`/`push_and_run_kernel` يفشلان بـ 401 ويرفعان `RuntimeError: فشل Kaggle أثناء <action>` من `_raise_auth_or_error`. الإصلاح توليد توكن جديد ولا شيء أقل:

1. Kaggle → **Settings → API → Create New Token**.
2. ضع القيمة في `control/credentials.env` (`KAGGLE_USERNAME` / `KAGGLE_KEY`) وفي `~/.kaggle/kaggle.json` بصلاحية `chmod 600`.
3. أعِد تحميل الاعتمادات (الخطوة 0) قبل أي دفع.

ملاحظة على مسار المصادقة الفعلي في الكود: `_kaggle()` يقرأ أيضاً `~/.kaggle/access_token` ويصدّره كـ `KAGGLE_API_TOKEN`، لأن Kaggle CLI 2.2.x يطلب التوكن الجديد (`KGAT_...`) لعمليات الرفع/التشغيل ولا يكفيه `kaggle.json` وحده. فلو بقي 401 بعد تحديث `kaggle.json`، فالملف الناقص هو `access_token`.

لا تكتب أي قيمة توكن في ملف داخل المشروع ولا في سطر الأوامر.

---

## 5) الإثراء (المرحلة ب)

بين المرحلتين يوجد **أنا**: أقرأ `state/runs/<run_id>/handoff/batch_NN.md` وأكتب قرارات في `state/runs/<run_id>/decisions/*.json` مربوطة بـ `item_id`.

بعد وجود القرارات، الإثراء **يحتاج `resume_run`** — بدونه `src/run.py` يولّد `run_id` جديداً فارغاً ولن يجد أي قرار.

عدّل `instruction.yaml`:

```yaml
run_mode: enrich
resume_run: run_20260731_120000    # نفس اسم مجلد state/runs/<run_id> — لاحظ بادئة run_
write_mode: auto-write             # الوضع المعتمد من المالك
```

`src/run.py` يولّد `run_id` بالشكل `run_<YYYYmmdd_HHMMSS>` (بادئة `run_`)، فقيمة `resume_run` لازم تحمل نفس البادئة. لاحظ الفرق: `--run-id` في `transfer_to_kaggle.py` بلا بادئة (توقيت خام) لأنه معرّف نسخة داتاست لا مجلد run.

ثم:

```bash
/usr/bin/python3 src/run.py instruction.yaml
```

فرق الوضعين:

- `auto-write` (**الوضع المعتمد الحالي** — مطبَّق في `instruction.yaml:12` و`config/settings.yaml:18`) — بوّابة مساحة قرص ← باك-أب ← ledger ← كتابة ذرّية في العقل. ضماناته: بوابة الجودة `quality_gate` قبل القبول، وباك-أب قبل كل كتابة، وسجل الأدلة `ledger`، و`state/provenance/` للتتبّع والرجوع.
- `drafts-review` — خيار احتياطي للتجارب: الكتابة تذهب إلى `drafts/` و**لا لمس** للعقل في `/sdcard/Nexus_Brain`. استخدمه عند اختبار تغييرات جديدة قبل إطلاقها على العقل.

قيم `run_mode` المقبولة في `src/run.py`: `capture` (المرحلة أ)، `enrich` (المرحلة ب دائماً)، `analyze` (المرحلة ب لو وُجدت قرارات)، `full` (أ ثم ب لو وُجدت قرارات).

المخرجات: `drafts/`، `review/` (تعارضات)، `state/provenance/` (ledger)، و`report.md` محدَّث بأعداد كُتب/عُمّق/مسودات/مراجعة/تُجوهل.

أعطال شائعة في الإثراء:

- **كل الأعداد صفر** — `resume_run` يشير لمجلد بلا `decisions/*.json`.
- **`(quarantined) <source>`** في `report.md` — قرار فشل التحقق البنيوي؛ الملف يُعزل ولا يُطبَّق. أصلح شكل الـ JSON.
- **عناصر في `review/`** — تعارض مع محتوى العقل الحالي: قرار بشري مطلوب، ليس خطأ.
- **`skipped`** — قرارات بـ action=skip، سلوك متوقّع.

---

## 6) السلسلة الكاملة

```bash
/usr/bin/python3 scripts/orchestrate.py full
```

يسلسل `login_only` → `capture` → `kaggle_sync` ويتوقّف عند أول rc≠0 مع `✖ توقف عند خطوة <name> (rc=N)`. **لا يشمل الإثراء** (المرحلة ب) لأنها تحتاجني بينهما.

ملاحظة: `full` يُعيد اللوجن في كل تشغيل حتى لو الجلسة صالحة. للتشغيل اليومي على جلسة قائمة، استخدم `capture` ثم `kaggle_sync` منفصلين.

أكواد خروج `orchestrate.py` الخاصة به (قبل تمرير rc السكربت الفرعي):

| rc | المعنى |
|---|---|
| 0 | نجاح، أو `--dry-run` |
| 2 | لا `account_alias` في `config/settings.yaml` / اعتمادات إنستقرام غائبة / ملف الجلسة مفقود |
| 124 | مهلة 900 ثانية للخطوة |
| 127 | ملف/مفسّر غير موجود |
| غير ذلك | rc الخارج من السكربت الفرعي كما هو |

الـ flags المتاحة على `orchestrate.py`: `mode` موضعي من `login_only|capture|kaggle_sync|full` (افتراضي `full`)، و`--dry-run`, `--instruction`, `--run-id`, `--alias`, `--storage-state`, `--headless`.

---

## بطاقة مرجعية

```bash
cd /root/r/nexus_enrichment
set -a; . control/credentials.env; set +a

# 1. الهدف → instruction.yaml (source_accounts) وليس settings.yaml
/usr/bin/python3 scripts/orchestrate.py capture --dry-run

# 2. لوجن (مرة، ثم أعِد الاستخدام)
xvfb-run -a /usr/bin/python3 scripts/login_instagram.py --alias fluxa.grow

# 3. التقاط
/usr/bin/python3 src/run.py instruction.yaml

# 4. Kaggle — نقل الجلسة أولاً (ينشئ nexus-ig-session)
/usr/bin/python3 scripts/orchestrate.py kaggle_sync

# 4b. دفع الكيرنل ومتابعته وسحب المخرجات (يتطلب توكن رفع صالح — الحالي 401)
/usr/bin/python3 src/run_kaggle.py run_20260731_120000

# 5. إثراء (بعد كتابة decisions/ + ضبط run_mode: enrich و resume_run)
/usr/bin/python3 src/run.py instruction.yaml
```
