# MSG-EXT-02 — أسطر 251–500

> نطاق الاستخراج: `sed -n '251,500p' /workspace/wiki/source-transfers/wiki_all_talk.md` (250 سطراً، OBSERVED بأمر `wc -l`).
> قاعدة المتحدث في الملف: عناوين `## <رقم> — <تاريخ> — moaz|Muse`؛ المتكلّم `moaz` = المستخدم، `Muse` = النموذج (OBSERVED من بنية الملف، موثّق أيضاً في ترويسة الملف سطر 5).
> الأسرار: لا تُطبع أي قيمة سرية. ما ورد مسبقاً في المصدر بعلامة `[محذوف]` يبقى كذلك. `[REDACTED]` عند الحاجة.

---

## ملخص النتائج

- **عدد رسائل المستخدم الكاملة داخل النطاق: 0 (OBSERVED)** — لا يوجد أي عنوان `##` جديد بين السطرين 251 و500 (أمر `awk 'NR>=251 && NR<=500 && /^## /'` أعطى مخرجات فارغة).
- **عدد رسائل المستخدم المشتركة (تتجاوز حدود النطاق): 1 (OBSERVED)** — رسالة المستخدم رقم **15**، وهي قيد التنفيذ منذ السطر 215 وتستمر حتى السطر 701، والنطاق 251–500 يقع كلّه داخل جسمها.
- الأسطر 251–500 كلّها نص بايثنج (جسم سكربت ملصوق داخل الرسالة 15)، وليست نصاً منطوقاً جديداً (OBSERVED بالقراءة المباشرة).

---

## الرسايل المستخرجة

### ملاحظة-1 (المقطع الوحيد المشترك)

| الحقل | القيمة |
|---|---|
| معرّف الرسالة | #15 (ترقيم `wiki_all_talk.md` الداخلي) — رسالة من **moaz** (المستخدم) |
| مرساة السطر | L251 (بداية النطاق؛ الرسالة تبدأ عند L215 وتنتهي عند L701 — OBSERVED بأمر `awk 'NR>=215 …'`) |
| المطابقة | تطابق مباشر مع «الرسالة 15» في ترقيم الملف نفسه (OBSERVED). **لا تطابق** مع أي عنصر مرقّم في `/workspace/wiki/MESSAGES.md` (OBSERVED بمراجعة رأس الملف: عناصره الـ19 طلبات جلسة أخرى بمصادر `analysis-session-01.md`، مختلفة المضمون والمصدر). |
| عنوان الرسالة في المصدر | `## 15 — 2026-10-19 17:24 — moaz` (OBSERVED، السطر 215 خارج النطاق) |

**النص الحرفي (مقتطع من النطاق 251–500، مع الاختصار بعد نحو 400 حرفاً):**

```
يعني السكيلز والادوات والسكربتات والسكربت ده
# ============================================================================
# 🎬  YouTube Transcript Downloader — Multi-Strategy Robust Edition (Colab)
# ============================================================================
import os
os.environ["GITHUB_TOKEN"] = "[محذوف]"

# >>> STEP 1: Auto-install dependencies <<<
import subprocess, sys
def pip_install(*pkgs):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "--upgrade", *pkgs])
pip_install("yt-dlp", "youtube-transcript-api", "requests")

# >>> STEP 2: Run the main downloader <<<
import os, sys, re, time, json, hashlib, random, shutil, glob, urllib.parse, zipfile
import requests
import yt_dlp

COOKIE_FILE      = "/content/cookies.txt"
OUTPUT_DIR       = "/content/transcripts"
ZIP_PATH         = "/content/transcripts_final.zip"
LOG_PATH         = "/content/transcripts/_log.json"

COOKIES_TEXT = r"""
[محذوف: كتلة الكوكيز كاملة]
"

URLS_TO_PROCESS = [
    "https://youtube.com/@yassminkhalid?si=E_fMMoCnLThxzggl",
]

LANG_PREF = ["en", "en-US", "en-GB", "ar", "en-orig", "ar-EG"]
PER_CHANNEL_CAP = None
DELAY_RANGE = (0.5, 1.5)
GITHUB_TOKEN  = os.environ.get("GITHUB_TOKEN", "")
GITHUB_REPO   = "geasas/youtube-transcripts"
GITHUB_BRANCH = "main"
GITHUB_PATH   = "transcripts/transcripts_final.zip"

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

def safe_filename(name, max_len=120):
    name = re.sub(r'[\\/*?\":<>|\n\r\t]', "", name).strip()
    return (name or "video")[:max_len]

def clean_v…[TRUNC]
```

**نهاية الرسالة (خارج النطاق، لكنها مطلوبة لعرض «النص الكامل» للرسالة المشتركة):**

> ` كل ده موجود بالفعل وسكيلز بناء الويكي والتفكير الخ ولا ايه الوضع؟`

- موضع النهاية: السطر 701 تقريباً، قبل عنوان `## 16 — 2026-10-19 17:24 — Muse` عند السطر 702 (OBSERVED بأمر `sed -n '700,706p'`).
- ملاحظة: `…[TRUNC]` يمثل استبدالاً لأجزاء من جسم السكربت بين السطرين ~260 و~700؛ **لم يُحذف أي نص خارج المقتطف** ولم يُخمَّن أي جزء (النص بين العلامتين لم يُنسخ هنا لأنه خارج النطاق المطلوب 251–500، حالته UNKNOWN من هذا الأمر بمفرده لكنه OBSERVED موجود عبر أمر `sed` الجانبي).

---

## محتوى النطاق غير النصي (سياق، للتحقق)

- كل السطور 251–500 = داخل دالة/جدول سكربت بايثنج: `safe_filename`, `clean_vtt`, `load_cookies`, `sapisid_hash`, `try_yt_dlp`, `try_yta`, `try_innertube`, `extract_urls_from_endpoint`, `list_videos_for_url` (OBSERVED بالقراءة المباشرة، الأوامر أدناه).
- **الأسرار:** لا توجد قيمة سرية حرفية داخل 251–500. القيم الحساسة مسبقة الإخفاء في المصدر: `INNERTUBE_API_KEY = "[محذوف]"` (سطر نسبي 156 = L406، OBSERVED). `GITHUB_TOKEN` يُقرأ من متغيّر بيئة (`os.environ.get`) وليس مضمّناً (OBSERVED، L265 نسبي 15). لم يُطبع أي شيء يُعاد تسميته `[REDACTED]` لأنه لا يوجد ما يستدعي ذلك في هذا النطاق.

---

## الأوامر المستخدمة (كلها للقراءة فقط)

1. `sed -n '251,500p' /workspace/wiki/source-transfers/wiki_all_talk.md` — الاستخراج الأساسي.
2. `wc -l` على مخرجات الأمر السابق — تأكيد 250 سطراً.
3. `grep -nE '(^|[^A-Za-z])(user|human|USER|Human|مستخدم|رسالة|message)'` على المدى — نتائج: كلمة وحيدة `"user_agent"` فقط.
4. `awk 'NR>=251 && NR<=500 && /^## / {print NR": "$0}'` — لا عناوين رسائل في النطاق.
5. `grep -cE '^(User|Human|USER|مستخدم)'` على الملف كاملاً = 0.
6. `grep -n '— moaz' … | head` — مواقع رسائل المستخدم؛ و`awk 'NR>=215 … /^## /'` — تحديد نهاية الرسالة 15 (L702).
7. `sed -n '245,255p'` و`sed -n '495,505p'` و`sed -n '700,706p'` — حدود النطاق ونهاية الرسالة 15.
8. `grep -nEi 'token|key|password|secret|cookie|…'` على النطاق — فحص أسرار (لا نتائج حسّاسة، كلها أسماء دوال/متغيّرات).
9. `cat -A` و`head -c 390/400` — التأكد من بداية النص الحرفي حرفياً.
10. `grep -rn "MSG-EXT|user message|مستخدم:" /workspace/wiki/work/*.md` و`head -30 /workspace/wiki/MESSAGES.md` — مطابقة العناصر المرقّمة.

---

## الشذوذات (anomalies)

1. **لا توجد أي رسالة مستخدم «كاملة داخل النطاق»** (OBSERVED): النطاق 251–500 هو متن رسالة واحدة ضخمة (رسالة 15، ~486 سطراً) — سلوك غير معتاد قياساً ببقية الملف حيث الرسائل قصيرة (OBSERVED).
2. **انقطاع الترويسات:** ترويسة الرسالة 15 خارج النطاق (L215)، لذا الربط بها يعتمد على مسافة الرأس الأقرب (OBSERVED من أمر `awk`)؛ احتمال وجود رأس تالف داخل النطاق مستبعد بالقراءة المباشرة لكنه NOT_RUN بأمر `grep '^##'` منفرد داخل النطاق (تم دمجه في الأمر 4 ونتيجته فارغة، إذن OBSERVED).
3. **المطابقة مع `MESSAGES.md`: لا يوجد تطابق** (OBSERVED): القائمة المرقّمة هناك لطلبات جلسة أخرى (`analysis-session-01.md`)، وليست رسائل `wiki_all_talk.md`. لذا المطابقة الوحيدة المتاحة هي ترقيم الملف نفسه.
4. **`…[TRUNC]` إلزامي هنا** لأن الرسالة المشتركة تتجاوز 400 حرفاً؛ الاختصار وسطي ولم يُخمَّن أي نص (PROPOSED أن قراءة كاملة للأسطر 251–500 حرفياً ممكنة بأمر `sed` محفوظ أعلاه).
5. نسبة المحتوى «المنطوق فعلياً» في النطاق: 0% نص مستخدم حواري؛ 100% كود ملصوق داخل رسالة مستخدم (OBSERVED).
