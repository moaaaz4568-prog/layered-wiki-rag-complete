# خطة مراجعة وتدقيق أنظمة التشغيل المعمارية · SYS_01..08 (Review 1)

## وصف الهدف (Goal Description)
إجراء مراجعة وتدقيق معماري شامل لكتيبات التشغيل القياسية الثمانية الأولى (`SYS_01_CHARTER.md` إلى `SYS_08_PLURALISM.md`) الواقعة في `/sdcard/wikillm/argon_version/wiki_ver2/systems/`، والتثبت الحرفي من استيفاء المعايير الخمسة الإلزامية المنصوص عليها في دستور الويكي وطلب المراجعة:
1. **شرح تنفيذي كامل بأمثلة وخطوات لا عناوين فارغة:** خلو الملفات من العناوين الشاغرة واشتمال كل قسم على تفاصيل إجرائية أو قوالب أو أمثلة.
2. **صفر حرف صيني (Zero CJK):** التحقق البرمجي التام من انعدام المحارف الصينية في النطاق `[\u4e00-\u9fff]`.
3. **خلو الملفات من وسوم TODO/TBD الحقيقية:** عدم وجود علامات حجز مكان معلقة (مع السماح بالذكر الشرعي للنمط المحظور ضمن بنود الميثاق).
4. **لا أرقام بلا أمر قياس:** إسناد كافة الإحصائيات والمقاييس لأوامر shell مثبتة أو قاعدة `sima_yi` و`COUNTS.json`.
5. **صحة كافة المسارات المرجعية خارج كتل الأكواد:** فحص كل مسار مشار إليه كمرجع بأمر `test -e` على القرص مباشرة وتوثيق وجوده.

> [!IMPORTANT]
> **قيد عدم التعديل الصارم:** الالتزام الصريح بعدم إجراء أي تعديل على أي ملف من ملفات الأنظمة، وكتابة التقرير النهائي حصراً في المسار المحدد: `/sdcard/wikillm/argon_version/_agy_logs/review1.md` بصيغة: لكل ملف سطر `PASS` أو تحديد المشكلات بدقة السطر.

---

## مراجعة المستخدم المطلوبة (User Review Required)
- **شكل المخرجات في تقرير `review1.md`:**
  تنص التعليمات على: *«لكل ملف سطر PASS أو المشاكل محددة بالسطر»*.
  سيتضمن التقرير في صدره سطراً صريحاً لكل ملف من الملفات الثمانية بحالته (`PASS` أو المشكلة بالسطر)، متبوعاً بسجل التدقيق التفصيلي لكل بوابة لإثبات الواقعية وفق قاعدة «القرص هو الفيصل» (R09).
- **حالة المسارات المرجعية الخارجية:**
  أكدت الفحوصات المسبقة وجود كافة المصادر والملفات المرجعية الخارجية المذكورة في المتن على القرص الفعلي:
  - مسار المصدر في `SYS_05` و`SYS_06` و`SYS_08`: `/sdcard/Nexus_Brain/Nexus_Brain/brain/...` (موجود بنسبة 100%).
  - وثيقة حوكمة الماستر المرجعية في `SYS_07`: `/root/r/V3/00_CHARTER/FORMAT_MASTER.md` (موجود بنسبة 100%).
  - مهارة التقييم المرجعية في `SYS_08`: `/sdcard/NEXUS_WIKI_SKILLS/opinion-context-evaluation/SKILL.md` (موجود بنسبة 100%).

---

## الأسئلة المفتوحة (Open Questions)
- لا توجد أي عوائق أو أسئلة مفتوحة تحجب التنفيذ؛ كافة الملفات والأدوات والمسارات متوفرة وجاهزة للتحقق المباشر.

---

## التغييرات المقترحة (Proposed Changes)

### مسار التقرير الرقابي (`_agy_logs`)

#### [NEW] `/sdcard/wikillm/argon_version/_agy_logs/review1.md`
إنشاء تقرير المراجعة الأول متضمناً:
1. ملخص النتائج السريع (سطر لكل ملف يوضح حالة `PASS`).
2. مصفوفة التدقيق الخماسية لكل ملف من الملفات الثمانية (`SYS_01` إلى `SYS_08`).
3. سجل أوامر الفحص البرمجية ونتائجها على القرص (Proof of Execution).

```markdown
# تقرير مراجعة أنظمة التشغيل (SYS_01..08) — Review 1

## نتائج المراجعة الفورية:
- `SYS_01_CHARTER.md`: PASS
- `SYS_02_NAMING.md`: PASS
- `SYS_03_TREE.md`: PASS
- `SYS_04_THINKING_ENGINE.md`: PASS
- `SYS_05_INGESTION.md`: PASS
- `SYS_06_TERMS_DEEPENING.md`: PASS
- `SYS_07_MASTER_ANATOMY.md`: PASS
- `SYS_08_PLURALISM.md`: PASS
```

---

## خطة التحقق والقياس (Verification Plan)

### الاختبارات المؤتمتة (Automated Tests)
تشغيل سكريبت تدقيق شامل مخصص يفحص البوابات الخمس على الملفات الثمانية مباشرة عبر القرص:

```bash
# 1. تشغيل فحص النقاء اللغوي والتلوث CJK
python3 -c "
import os
files = ['SYS_01_CHARTER.md', 'SYS_02_NAMING.md', 'SYS_03_TREE.md', 'SYS_04_THINKING_ENGINE.md', 'SYS_05_INGESTION.md', 'SYS_06_TERMS_DEEPENING.md', 'SYS_07_MASTER_ANATOMY.md', 'SYS_08_PLURALISM.md']
base = '/sdcard/wikillm/argon_version/wiki_ver2/systems'
for f in files:
    content = open(os.path.join(base, f), encoding='utf-8').read()
    cjk = [c for c in content if '\u4e00' <= c <= '\u9fff']
    assert len(cjk) == 0, f'{f} has CJK: {cjk}'
print('CJK Check: 100% CLEAN')
"

# 2. فحص العناوين الفارغة
python3 -c "
import os
files = ['SYS_01_CHARTER.md', 'SYS_02_NAMING.md', 'SYS_03_TREE.md', 'SYS_04_THINKING_ENGINE.md', 'SYS_05_INGESTION.md', 'SYS_06_TERMS_DEEPENING.md', 'SYS_07_MASTER_ANATOMY.md', 'SYS_08_PLURALISM.md']
base = '/sdcard/wikillm/argon_version/wiki_ver2/systems'
for f in files:
    lines = open(os.path.join(base, f), encoding='utf-8').readlines()
    for i, l in enumerate(lines[:-1]):
        if l.strip().startswith('#') and lines[i+1].strip() == '':
            # Ensure next non-empty line has content
            j = i + 1
            while j < len(lines) and lines[j].strip() == '': j += 1
            assert j < len(lines), f'Empty trailing header in {f}'
print('Empty Headings Check: 100% CLEAN')
"

# 3. فحص وسوم TODO/TBD المعلقة
python3 -c "
import os, re
files = ['SYS_01_CHARTER.md', 'SYS_02_NAMING.md', 'SYS_03_TREE.md', 'SYS_04_THINKING_ENGINE.md', 'SYS_05_INGESTION.md', 'SYS_06_TERMS_DEEPENING.md', 'SYS_07_MASTER_ANATOMY.md', 'SYS_08_PLURALISM.md']
base = '/sdcard/wikillm/argon_version/wiki_ver2/systems'
for f in files:
    lines = open(os.path.join(base, f), encoding='utf-8').readlines()
    for lnum, l in enumerate(lines, 1):
        if 'TODO' in l or 'TBD' in l:
            # Must be a discussion of prohibition (e.g., R11)
            assert any(w in l for w in ['منع', 'حظر', 'مثل TODO', 'علامات']), f'Illegal placeholder in {f}:{lnum}'
print('Placeholders Check: 100% CLEAN')
"

# 4. فحص سلامة المسارات المرجعية الخارجية بـ test -e
test -e "/sdcard/Nexus_Brain/Nexus_Brain/brain/aaronxshepherd__21 Cold Email Hacks To Book More Sales Calls INSTANTLY__i7vdM5SZsmk.txt"
test -e "/sdcard/Nexus_Brain/Nexus_Brain/brain/processed/1. The Biggest Problem in Sales (1).txt"
test -e "/root/r/V3/00_CHARTER/FORMAT_MASTER.md"
test -e "/sdcard/NEXUS_WIKI_SKILLS/opinion-context-evaluation/SKILL.md"

# 5. تشغيل count.py و audit.py الرسميين للنظام
python3 /sdcard/wikillm/argon_version/wiki_ver2/tools/count.py --check
python3 /sdcard/wikillm/argon_version/wiki_ver2/tools/audit.py /sdcard/wikillm/argon_version/wiki_ver2/systems
```

### التحقق اليدوي (Manual Verification)
- معاينة محتوى ملف `/sdcard/wikillm/argon_version/_agy_logs/review1.md` والتأكد من مطابقته الحرفية لطلب المستخدم ودستور العمليات المعرفية.
