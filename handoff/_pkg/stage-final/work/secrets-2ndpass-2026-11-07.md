# تقرير فحص الأسرار — الجولة الثانية (بعد دفع GitHub)

- التاريخ: 2026-11-07
- النطاق: `repo/` (كل الملفات incl. hidden) + `work/*.md` (بدون `.log-*` المخفية) + `config/` + `docs/` + `sources/` + `index/` + `masters/` + `templates/` + `reference/` + `timeline/` + جذر `*.md`
- مستبعد من النطاق (عدّ فقط): `archive-extract/` — معروف بـ 23 إرثاً سابقاً
- النمط: `ghp_[A-Za-z0-9]{20,} | github_pat_[A-Za-z0-9_]{20,} | gh[pousr]_[A-Za-z0-9]{20,} | sk-[A-Za-z0-9]{20,} | AKIA[0-9A-Z]{16} | xox[baprs]- | Bearer [A-Za-z0-9] | AIza[0-9A-Za-z_-]{30} | (password|passwd|api_key|token)\s*[:=]\s*\S+`
- قاعدة الإخراج: لا تُطبع أي قيمة مطابقة إطلاقاً — فقط `file:line` + أول 8 أحرف من المطابقة.

---

## 1) عدد التطابقات لكل شجرة (grep -rEnc — الأوامر موثّقة)

### أمر موحّد استُخدم في كل شجرة
```
grep -rEnc 'ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-|Bearer [A-Za-z0-9]|AIza[0-9A-Za-z_-]{30}|(password|passwd|api_key|token)[[:space:]]*[:=][[:space:]]*\S+' <الشجرة>
```

| الشجرة | المطابقات (قوية*) | المطابقات (كلية) | ملفات غير صفريّة |
|---|---|---|---|
| `repo/` | **0** (exit 1) | 2 | `repo/sources/session-export-index.md:1`، `repo/MESSAGES.md:1` |
| `work/*.md` (بدون `.log-*` المخفية) | **0** (exit 1) | 3 | `analysis-session-01.md:1`، `repo-plan-01.md:1`، `review-2.md:1` |
| `config/ docs/ index/ masters/ templates/ reference/ timeline/` | **0** (exit 1) | 0 | — |
| `sources/` | **0** | 1 | `sources/session-export-index.md:1` |
| جذر `*.md` | **0** (exit 1) | 1 | `MESSAGES.md:1` |
| `archive-extract/` (مستبعد، عدّ فقط) | 2947 مطابقة قوية في 54 ملفاً | 3064 في 79 ملفاً (الكلية = قوية 2947 + generic 242 في 66 ملفاً؛ `grep -rEoc ... \| grep -v ':0$' \| awk -F: '{s+=$NF}...'`) | 79 |

\* «قوية» = أنماط `ghp_ / github_pat_ / gh[pousr]_ / sk- / AKIA / xox / Bearer / AIza`.

**الخلاصة الرقمية: صفر مطابقة قوية في كل النطاق المفحوص** (تأكيد بأمر منفصل للأنماط القوية فقط على الشجرات السبع معاً → `EXIT:1` أي لا توجد أي مطابقة).

---

## 2) تفاصيل التطابقات الـ 7 الكلية (بدون طباعة أي قيمة)

كل التطابقات من فئة `generic` الحرفية فقط: `token :[` أو `password` ككلمة مفتاحية:

1. `repo/sources/session-export-index.md:15` — PREFIX=`token :[` — القيمة بعدها `[REDACTED — مفتاح وصول مودوع، انظر القسم 4]` (مُعتمة)
2. `repo/MESSAGES.md:17` — PREFIX=`token :[` — القيمة بعدها `[REDACTED — مفتاح وصول مودوع، انظر قسم (و)]` (مُعتمة)
3. `sources/session-export-index.md:15` — PREFIX=`token :[` — (مُعتمة، نسخة خارج repo)
4. `MESSAGES.md:17` (جذر) — PREFIX=`token :[` — (مُعتمة)
5. `work/analysis-session-01.md:14` — PREFIX=`token :[` — (مُعتمة)
6. `work/repo-plan-01.md:180` — PREFIX=`password` — نص إجراء: قوالب `credential.helper` مع `$GH_TOKEN` كمتغيّر بيئة (لا قيمة سرّية)
7. `work/review-2.md:11` — PREFIX=`password` — نص قائمة تدقيق `grep ... password=` (لا قيمة سرّية)

**لا توجد أي قيمة PAT/mangled/سcredential حقيقية** — المطابقات الأربع لـ `token :[` كلها تشير إلى نص `:[REDACTED ...]` بعدها مباشرة.

---

## 3) التحقق من موضعات التعطيل الستة في `work/`

الأمر:
```
grep -rEnc 'REDACTED-PAT-40chars-ROTATE-REQUIRED' /workspace/wiki/work/
```
الناتج (OBSERVED):
- `work/.log-analysis-session-b` → **1**
- `work/.log-session-c` → **5**
- المجموع = **6/6 الموضعات ما زالت مُعتمة بالبديل** `[REDACTED-PAT-40chars-ROTATE-REQUIRED]` ✅
- (ملاحظة: `work/repo-plan-01.md:233` يردّد وصف البديل نصياً في سرد العملية — ليس موضعاً سابقاً للمفتاح نفسه.)

---

## 4) الحكم النهائي

### OBSERVED — النطاق المفحوص **نظيف**
- صفر (`0`) مطابقة من الأنماط القوية في: `repo/`، `work/*.md`، `config/`، `docs/`، `sources/`، `index/`، `masters/`، `templates/`، `reference/`، `timeline/`، جذر `*.md`.
- التطابقات السبع الكلية كلها إمّا سرد نصي أو موضعات مُعتمة مسبقاً — لا قيمة سرّية مكشوفة.
- `archive-extract/`: مستبعد عمداً (إرث معروف — عدّ فقط أعلاه؛ لا يدخل في حكم النظافة).

### تحقّق التعطيل
- الموضعات الستة في `work/` ما زالت مُعتمة: **OBSERVED (6/6)**.

### حالة إبطال (Revoke) المفتاح
- **UNKNOWN** — لا يوجد في أي ملف معلومة موثّقة عن ما إذا كان المستخدم أبطل المفتاح من GitHub أم لا، ولا يمكن التحقق من ذلك هنا (لا شبكة، لا git). **على المستخدم تدوير المفتاح يدوياً من GitHub → Settings → Developer settings → Personal access tokens** حتى لو بدى كل شيء نظيفاً: التعطيل في الملفات ≠ إبطال المفتاح على الخادم.

### رموز حالة
- `OBSERVED`: صفر نمط قوي في النطاق؛ 6/6 تعطيلات سليمة.
- `UNKNOWN`: حالة revoke.
- `NOT_RUN`: لم يُجرَّب أي فحص خارجي/شبكي عمداً.
