# CONTEXT — عامل إثراء Nexus

مرجع تشغيلي واحد للمشروع. يُقرأ قبل أي جلسة عمل.

---

## 1. الهدف

عامل بحث يقرأ إنستقرام **للقراءة فقط** ويحوّل ما يقرأه إلى معرفة داخل ويكي Nexus Brain في `/sdcard/Nexus_Brain`.

- المخرج النهائي: مفاهيم وتعميقات داخل سلسلة المعرفة (مصادر → مفاهيم → تعميق → masters).
- العامل يعمل أساساً في المرحلتين 1 و2 من السلسلة، ولا يكتب في masters مباشرة.
- **ليس** نظام تواصل خارجي، ولا أوتريتش، ولا رسائل، ولا تعليقات، ولا متابعات.
- **ليس** مجمّع نسخ/لصق: كل إضافة تمر بفهم وتفنيد بأدلة قبل الدمج.
- الفلترة الموضوعية إجبارية: محتوى النساء/المواعدة/الجذب فقط، وما عداه يُهمل.
- الأمر اليومي الواحد: `اقرأ /root/r/nexus_enrichment/instruction.yaml ونفّذ.`

---

## 2. خريطة الملفات

### src/ — النواة

| الملف | الدور |
|---|---|
| `__init__.py` | علامة الحزمة. |
| `analysis_prompts.py` | يبني نص المطالبة لكل منشور ويحدّد الحقول المطلوبة في القرار (decision, concept, claim_type, sources_count, excerpt, body, confidence, verdict, weakness_notes, target_file). |
| `backup.py` | `BackupSet` + `manifest.jsonl` بتجزئة sha256، واسترجاع مطابق بايت-ببايت قبل أي كتابة في الويكي. |
| `browse.py` | تصفح قراءة فقط بحدود بشرية (عدد عناصر، مهلة، تأخير عشوائي)، ويستدعي `safety.raise_if_unsafe` على كل صفحة. |
| `capture.py` | يحوّل الصفحة إلى `RawItem` موحّد مع بصمة فريدة، ويرفض النص القصير غير المفيد. |
| `config.py` | يدمج `instruction.yaml` فوق `config/settings.yaml` ويفرض `account_alias`. |
| `cookies_export.py` | يحوّل `storage_state` إلى `cookies.txt` بصيغة Netscape لـ yt-dlp/gallery-dl؛ مكتبة قياسية فقط، صلاحية 600، ولا يسجّل قيم الكوكيز. |
| `dedup.py` | منع التكرار عبر `state/seen.sqlite`. |
| `enrich.py` | ينفّذ القرارات (new / deepen / conflict) مع نسخة احتياطية وتحقق من السجل، ويحترم وضع `drafts-review` مقابل `auto-write`. |
| `guards.py` | حراس المساحة والذاكرة (300MB حرة، 50k inode، 80MB RAM) و`atomic_write` عبر tmp ثم `os.replace`. |
| `handoff.py` | يبني دفعات `handoff/batch_NN.md` للنموذج ويقرأ `decisions/*.json` الراجعة. |
| `harvest.py` | طلب `web_profile_info` واحد لكل حساب → `runs/<id>/posts/*.json`، ويتوقف فوراً عند 429/401/403. |
| `journal.py` | سجل مرحلتين PENDING/COMMITTED باستئناف آمن بعد الانقطاع. |
| `kaggle_bridge.py` | رفع الداتاست وتشغيل الكيرنل والانتظار وسحب المخرجات (`nexus-posts` / `nexus-transcribe`). |
| `kaggle_transcribe.py` | خلايا التثبيت والمعالجة التي تعمل على GPU كاغل وتنتج `transcripts.json`. |
| `ledger.py` | سجل الإثبات JSONL في `state/provenance/<concept_slug>.jsonl`؛ لا كتابة في الويكي بلا سطر صالح. |
| `login_xvfb.py` | تسجيل دخول داخل Xvfb؛ كلمة المرور من متغيّر البيئة `IG_PASSWORD` فقط. |
| `processed_store.py` | تخزين المعالَج تحت `processed/<account>/<run_id>/`. |
| `processed_to_decisions.py` | يمرّر المعالَج عبر بوابة الجودة ويولّد ملفات القرار؛ المرفوض إلى `review/quality_rejected/`. |
| `production_run.py` | يقود سلسلة الدفعات كاملة مع نقطة توقّف وحفظ عند 429. |
| `quality_gate.py` | عتبة القبول: ثقة ≥ 0.65 وطول اقتباس ≥ 30. |
| `raw_store.py` | تخزين الخام تحت `raw/<account>/<run_id>/`. |
| `run.py` | منسّق الدورة الواحدة بمرحلتيها A و B. |
| `run_kaggle.py` | يبني دفتر `nexus-transcribe.ipynb` برمجياً. |
| `safety.py` | كاشف إشارات الخطر (CAPTCHA / CHALLENGE / CHECKPOINT / ACTION_BLOCK / LOGIN_REDIRECT / RATE_LIMIT) بلا أي اتصال شبكي. |
| `session.py` | يحفظ ويقرأ `storage_state` في `state/session/<alias>.json` مع تنظيف الاسم. |
| `transcripts_ingest.py` | يستقبل النصوص من كاغل إلى raw ثم processed، ويكوّن `combined_text = caption + audio_transcript + ocr_text`. |
| `vision.py` | قراءة الصور فقط (حد 8 صور للمنشور)، حذف المؤقتات، ولا ينزّل فيديو أبداً. |

### scripts/ — نقاط التشغيل

| الملف | الدور |
|---|---|
| `login_instagram.py` | تسجيل دخول يدوي مرة واحدة وحفظ الجلسة؛ ينتظر `sessionid` و`ds_user_id` الحقيقيين، ويحدّد مسار Chromium بنمط glob. |
| `orchestrate.py` | المشغّل الرئيسي بأوضاع `login_only` / `capture` / `kaggle_sync` / `full`، ويدعم `--dry-run`. |
| `transfer_to_kaggle.py` | ينقل الجلسة والمخرجات إلى Kaggle Dataset؛ يتطلب `~/.kaggle/kaggle.json`. |

### ملف مستقل

| الملف | الدور |
|---|---|
| `kaggle_instagram_knowledge_extractor.py` | مستخرج جاهز للصق في كاغل: تنزيل + Whisper + OCR (عربي/إنجليزي) + إزالة تكرار، ولا يحتفظ بأي وسائط بعد المعالجة. |

---

## 3. مسار البيانات الحقيقي

```
1. لوجن يدوي مرة واحدة
   scripts/login_instagram.py  (أو src/login_xvfb.py تحت Xvfb)
        ↓
2. جلسة محفوظة
   state/session/<alias>.json   ← storage_state من Playwright
        ↓
3. تحويل الكوكيز
   src/cookies_export.py → cookies.txt بصيغة Netscape (chmod 600)
        ↓
4. التقاط
   src/harvest.py → runs/<run_id>/posts/*.json
   (طلب واحد لكل حساب، حدود بشرية، توقف فوري عند إشارة خطر)
        ↓
5. رفع إلى كاغل
   src/kaggle_bridge.py / src/run_kaggle.py
   dataset: nexus-posts   kernel: nexus-transcribe
        ↓
6. معالجة على GPU مجاني
   تنزيل الوسائط + Whisper (صوت) + OCR (صور/إطارات) → transcripts.json
        ↓
7. استيعاب النصوص
   src/transcripts_ingest.py
   → raw/<account>/<run_id>/  ثم  processed/<account>/<run_id>/
   combined_text = caption + audio_transcript + ocr_text
        ↓
8. تسليم للنموذج
   src/handoff.py → handoff/batch_NN.md
   النموذج يفهم ويفنّد بأدلة ويعيد decisions/*.json
        ↓
9. بوابة الجودة
   src/quality_gate.py (ثقة ≥ 0.65، اقتباس ≥ 30) عبر src/processed_to_decisions.py
   المرفوض → review/quality_rejected/
        ↓
10. الإثراء
   src/enrich.py: نسخة احتياطية → journal PENDING → كتابة → سجل إثبات → journal COMMITTED
        ↓
11. الوجهة
   /sdcard/Nexus_Brain  (auto-write)  أو  drafts/ للمراجعة (drafts-review)
```

`src/production_run.py` هو ما يقود هذه السلسلة دفعةً بعد دفعة.

قواعد التحقق المتدرّج: ادعاء تكتيكي = مصدر واحد (`single-source`)، ادعاء رقمي = مصدران وإلا `unverified-claim`، وأي تعارض لا يُكتب تلقائياً أبداً بل يذهب إلى `review/`.

---

## 4. القيود الصارمة

| القيد | التفصيل |
|---|---|
| **أفعال خارجية = صفر** | لا لايك، لا تعليق، لا متابعة، لا رسائل، لا نشر. قراءة فقط. أي فعل خارجي خرقٌ للميثاق. |
| **المفسّر** | `/usr/bin/python3` حصراً (Python 3.13). لا بيئة افتراضية ولا مفسّر آخر. |
| **Camoufox ممنوع** | ممنوع تشغيل `camoufox fetch`. المساحة الحرة ~1G فقط والقرص ممتلئ 98% (inodes 98% كذلك). ذِكر Camoufox في بعض docstrings هو انحراف توثيقي لا أكثر. |
| **المتصفح الفعلي** | Playwright Chromium في `/usr/local/playwright/chromium-*/chrome-linux/chrome` (حالياً `chromium-1223`)، يُمرَّر عبر `executable_path`. |
| **توقّف صارم** | عند CAPTCHA أو CHALLENGE أو CHECKPOINT أو ACTION_BLOCK أو LOGIN_REDIRECT أو RATE_LIMIT، أو HTTP 429/401/403 → إيقاف فوري وحفظ نقطة الاستئناف. |
| **حساب فرعي فقط** | لا يُستخدم أي حساب شخصي. الحساب المخصّص وحده. |
| **نسخة احتياطية قبل الكتابة** | لا كتابة في `/sdcard/Nexus_Brain` بلا `BackupSet` قابل للاسترجاع. |
| **سجل إثبات إلزامي** | لا سطر في الويكي بلا سطر مقابل في `state/provenance/`. |
| **محلي 100%** | لا مفاتيح LLM خارجية. النموذج هو جلسة العمل نفسها، وبايثون هو الأطراف والحواس والذاكرة. |
| **حدود بشرية للتصفح** | 8 عناصر، 15 دقيقة، تأخير 3–8 ثوانٍ، وقفة تمرير 4 ثوانٍ. |

---

## 5. حالة الإنجاز

| المرحلة | المحتوى | الحالة |
|---|---|---|
| **M0** | الهيكل والثوابت: `ledger` / `backup` / `guards` / `safety` | ✅ مكتملة |
| **M1** | الحواس: `session` / `browse` / `capture` / `dedup` | ✅ مكتملة |
| **M2** | الجسر: `handoff` / `enrich` / `run` + مسار كاغل | ✅ مكتملة |
| **M3** | تشغيل حقيقي محافظ من البداية للنهاية والتحقق من النتيجة | ⬜ متبقٍ |

- الاختبارات تمرّ عبر `/usr/bin/python3 -m pytest tests/ -q`، والتشخيصات نظيفة، وكل سكربت له `main()` وحارس `__main__`.
- المتبقي عملياً هو M3 فقط: جلسة دخول حقيقية، ثم دورة كاملة بعدد عناصر صغير في وضع `drafts-review`، ثم مراجعة المخرجات قبل تفعيل الكتابة التلقائية.

---

## 6. المفاتيح

**لا تُكتب أي كلمة مرور أو توكن في هذا الملف ولا في أي ملف توثيق.**

- كل الأسرار في `control/credentials.env` وحده، بصلاحية 600، وخارج التتبّع.
- المتغيّرات المتوقّعة هناك: `IG_USERNAME`، `IG_PASSWORD`، وبيانات كاغل.
- مفتاح كاغل يُقرأ من `~/.kaggle/kaggle.json` (صلاحية 600)، لا من ملفات المشروع.
- الكود يقرأ الاعتماديات من متغيّرات البيئة فقط؛ لا تمرّرها في سطر الأوامر ولا تضعها في `settings.yaml`.
- أي توكن يظهر بنص صريح داخل ملفات التوثيق يُعدّ تسريباً ويجب إبطاله واستبداله بمؤشّر إلى `control/credentials.env`.
