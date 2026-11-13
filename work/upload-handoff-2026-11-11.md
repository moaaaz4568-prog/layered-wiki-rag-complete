# upload-handoff — رفع حزمة التسليم إلى مستودع GitHub عام (subagent: UPLOAD)

- التاريخ: 2026-11-11
- النطاق: إنشاء مستودع عام جديد `layered-wiki-rag-handoff` ورفع الحزمة، ثم تزكية كل آثار التوكن.
- لا قيمة سرية في هذا الملف إطلاقاً؛ التوكن يُشار إليه بـ`ghp_…[REDACTED]` فقط.
- كل ما ليس كذلك وسِم صراحة. لا شبكة إلا `github.com`/`api.github.com`.

## [U0] بوابة ما قبل الرفع — أمان المحتوى [OBSERVED]

- `handoff/VERIFY-TARS-2026-11-11.md` §[V7]: **FINAL VERDICT: READY-FOR-UPLOAD** للتصارين، مع مسح أنماط أسرار موسّعة على الشجرتين المستخرجتين = **0 إصابات حية** (§[V5]) [OBSERVED — قراءة الملف].
- مسح خاص بي (فوق أنماط [V5] بإضافة `xox[baprs]-`) على `handoff/*.md` التسعة (8 مرساة + `security-fix-2026-11-10.md`): 4 مطابقات كلها النص الحرفي `xoxb-,` داخل نصوص تعليمات فحص (لا قيم) — فحصت السطر 1262 بعينه: المطابقة الوحيدة `xoxb-` النصية [OBSERVED — `grep -nE …` ثم `sed -n '1262p' … | grep -oE … | uniq -c`].
- `conversation-export.json` غير مرفوع مسطّحاً (داخل التارين فقط)، وبصمته بعد التزكية مثبتة في [V4] [OBSERVED — قراءة VERIFY-TARS].

## [U1] التحقق من التوكن [OBSERVED]

- CMD: `curl -s -H "Authorization: Bearer ghp_…[REDACTED]" https://api.github.com/user | jq -r '.login'`
- الخرج: `moaaaz4568-prog` → التوكن شغّال وصحيح المالك ✓.

## [U2] إنشاء المستودع [OBSERVED]

- CMD: `curl -s -X POST -H "Authorization: Bearer ghp_…[REDACTED]" https://api.github.com/user/repos -d '{"name":"layered-wiki-rag-handoff","private":false,"description":"Handoff package — layered-wiki-rag project continuation (context, memory, conversation export, archives)"}'`
- الخرج (jq): `full_name=moaaaz4568-prog/layered-wiki-rag-handoff`, `html_url=https://github.com/moaaaz4568-prog/layered-wiki-rag-handoff`, **`private=false`** ✓ (أُنشئ جديداً؛ لا 422).

## [U3] التجهيز في /tmp/opencode/gitwork/ [OBSERVED]

- CMD: `mkdir -p /tmp/opencode/gitwork/layered-wiki-rag-handoff && cp -a /workspace/wiki/handoff/_pkg/wiki-handoff-package.tar.gz /workspace/wiki/handoff/_pkg/wiki-handoff-light.tar.gz … && cp -a /workspace/wiki/handoff/*.md …`
- إضافة خارج نص المهمة (لتغطية «security note» المذكورة): `cp -a /workspace/wiki/handoff/_pkg/stage-final/work/security-fix-2026-11-10.md` [OBSERVED — المصدر الوحيد لمطابقة `*security*`].
- `SHA256SUMS.txt` عبر `sha256sum wiki-handoff-*.tar.gz` داخل المجلد [OBSERVED]:
  - `37bf1879064e5887651cfa6cf65133f5e49959e28f2dda1432ad468bde814696  wiki-handoff-light.tar.gz`
  - `7062568d45b4178bde3363f004476886c0a726f2977d73a5f9ebd6e8c4cf63ad  wiki-handoff-package.tar.gz`
- القائمة النهائية (11 ملفاً): CONTEXT.md, HANDOFF.md, MEMORY.md, README.md, REVIEW-PREUPLOAD.md, VERIFY-TARS-2026-11-11.md, WHAT-WAS-DONE.md, conversation-export.md, security-fix-2026-11-10.md, wiki-handoff-light.tar.gz, wiki-handoff-package.tar.gz (+ SHA256SUMS.txt لاحقاً = 12) [OBSERVED — `ls -la`].

## [U4] مستودع git ارتجالي + commit [OBSERVED]

- CMD: `git init -b main && git config user.name … && git config user.email … && git add -A && git commit -m "Handoff package: full project state, conversation export, memory+context files, archive tar"`
- الخرج: `main` فرع جديد، commit **`420467399cada4db5535525dd2c1c865cd2a9b12`** ✓.
- فحص `.git/config`: `grep -c ghp_ .git/config` → **0** (grep_exit=1) قبل أي دفع [OBSERVED].

## [U5] الدفع — المحاولة الأولى فشلت، والبدلية نجحت [OBSERVED]

1. محاولة `http.extraHeader="Authorization: Bearer ghp_…[REDACTED]" push https://github.com/…`:
   - الخرج: `remote: invalid credentials` / `fatal: Authentication failed` → **push_exit=128** [OBSERVED — فشل الاتصال المصادق به عبر الترويسة الإضافية مع git فقط؛ نفس التوكن نجح على api.github.com].
   - ⚠️ تنبيه أمني مسجل: هذا النمط لا يعمل مع git هنا. البدلية (URL مضمّن) تُمرر التوكن مؤقتاً داخل `.git/config` ثم تُزكّى فوراً — انظر [U7].
2. البدلية (الموثقة في المهمة):
   - `git remote add origin "https://ghp_…[REDACTED]@github.com/moaaaz4568-prog/layered-wiki-rag-handoff.git"` (الخرج مُنقّح بـ`sed` لطبع `[REDACTED]` بدل التوكن).
   - `GIT_TERMINAL_PROMPT=0 git push origin main` → `* [new branch] main -> main`، **push_exit=0** ✓.
   - تحذير البعيد الوحيد: `GH001: File wiki-handoff-package.tar.gz is 58.84 MB; larger than recommended 50.00 MB` — تحذير توصية فقط، والملف دون البوابة الصلبة 100MB وتحت سقف الحزمة الموثق في VERIFY-TARS §[V6] (SIZE_GATE_PASS) [OBSERVED].
   - فوراً بعد الدفع: `git remote set-url origin https://github.com/moaaaz4568-prog/layered-wiki-rag-handoff.git` (نظيف) ثم `grep -c ghp_ .git/config` → **0** (grep_exit=1) ✓ [OBSERVED — الدفع نجح والتزكية تمت في نفس الأمر الواحد].

## [U6] التحقق عن بعد [OBSERVED]

- CMD: `GET /repos/moaaaz4568-prog/layered-wiki-rag-handoff` (بترويسة): `private=false`, `visibility=public`, `default_branch=main`, `pushed_at=2026-11-11T07:46:57Z`, `size=0` (حقل حجم GitHub بالكيلوبايت لم يُحدَّث بعد لمستودع جديد — غير مقلق؛ الحجم الحقيقي مثبت عبر `/contents/`) [OBSERVED].
- CMD: `GET /repos/…/contents/` (بترويسة) — **12 ملفاً** كلها `file` مع git_url [OBSERVED]:

| الملف | الحجم (بايت) |
|---|---|
| CONTEXT.md | 28,782 |
| HANDOFF.md | 8,170 |
| MEMORY.md | 21,600 |
| README.md | 15,292 |
| REVIEW-PREUPLOAD.md | 28,323 |
| SHA256SUMS.txt | 186 |
| VERIFY-TARS-2026-11-11.md | 8,864 |
| WHAT-WAS-DONE.md | 26,035 |
| conversation-export.md | 342,272 |
| security-fix-2026-11-10.md | 10,271 |
| wiki-handoff-light.tar.gz | 1,742,327 |
| **wiki-handoff-package.tar.gz** | **61,696,718** ✓ (يطابق المتوقع حرفياً؛ git_url: `…/git/blobs/950d4494677f485f4d84d266566a9ec1a8aef2c2`) |

- CMD: `curl -s -o /dev/null -w "%{http_code}" https://api.github.com/repos/moaaaz4568-prog/layered-wiki-rag-handoff` (**بدون مصادقة**) → **200** → المستودع عام فعلاً ✓ [OBSERVED].
- CMD: `git rev-parse HEAD` و`git ls-remote … main` → كلاهما **`420467399cada4db5535525dd2c1c865cd2a9b12`** → الدفع سليم ✓ [OBSERVED].

## [U7] التزكية — إثباتات [OBSERVED]

- CMD: `rm -rf /tmp/opencode/gitwork` ثم `find /tmp/opencode/gitwork` → `No such file or directory` ✓.
- التوكن الحرفي (القيمة الكاملة، لا النمط العام):
  - `grep -rl "<TOKEN_FULL>" /tmp/opencode/ | wc -l` → **0** ✓
  - `grep -rl "<TOKEN_FULL>" /workspace/wiki --exclude-dir=archive-extract | wc -l` → **0** ✓
  - إضافي أوسع: نفس الفحص على `/workspace/wiki/` كاملة (بدون استثناء) → **0**، وعلى `/tmp/` كاملة → **0** ✓.
- توضيح عدّادات النمط العام `ghp_` (ليست التوكن): `grep -rn "ghp_" /tmp/opencode/ | wc -l` = **76** و`grep -rl "ghp_" /workspace/wiki --exclude-dir=archive-extract | wc -l` = **46** — كلها كلمة النمط الحرفية داخل ملفات مشروع سابقة (وثائق إجراءات الفحص، نسخة جلسات أخرى في `/tmp/opencode/layered-wiki-handoff/`، `ctx-trim.md`…) [OBSERVED — فحصت أسماء الملفات، وصفر منها يطابق قيمة التوكن الكاملة].
- تاريخ الأوامر: جلسة غير تفاعلية (لا `history` يُكتب) — لا أثر للأوامر على القرص [REPORTED — سلوك shell غير التفاعلي].
- الشجرة `work/` في `/workspace/wiki` لم تُلمس إلا بإنشاء هذا الملف [OBSERVED].

## [U8] الحكم النهائي

- المستودع: **https://github.com/moaaaz4568-prog/layered-wiki-rag-handoff** — **عام** (`private=false`، مجهول 200) [OBSERVED].
- الفرع `main` عند `420467399cada4db5535525dd2c1c865cd2a9b12` بـ12 ملفاً بينها التار الكامل 61,696,718 بايت [OBSERVED].
- التوكن: لم يُطبع في أي مخرج، لم يُكتب في أي ملف باقٍ (صفر ملفات يحمل قيمته في /tmp و/workspace/wiki) [OBSERVED].
- ما لم يُنفذ/قيد: فحص أول بايتات التار عبر GET خلق — المهمة نصت أن فحص الحجم كافٍ [NOT_RUN — بإذن نص المهمة].
