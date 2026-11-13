# 📁 أرشيف محادثات OpenCode المتعلقة بنظام الويكي (05_CONVERSATIONS/opencode)

**تاريخ الأرشفة:** 2026-11-03  
**الحالة:** مكتمل ومتحقق منه بالكامل (P1)  
**المرجعية:** تقرير الفحص الميداني `OPencode_DB_WIKI_SCAN_REPORT.md` وخطة التنفيذ `WIKI_ARCHIVE_EXECUTION_PLAN.md`

---

## 1. نظرة عامة
يضم هذا المجلد أرشيفاً مستقلاً ونظيفاً لجميع جلسات ومحادثات منصة **OpenCode** التي دارت حول مشروع نظام الويكي.  
تم استخراج البيانات مباشرة من قاعدتي البيانات SQLite بنمط القراءة فقط (`mode=ro`) دون نسخ ملفات `.db` الثقيلة (التي تفوق 1 جيجابايت مجتمعة)، مع تحويل كل جلسة إلى ملف `JSONL` مستقل وعالي الهيكلية.

---

## 2. الهيكل التنظيمي للمجلد

```
05_CONVERSATIONS/opencode/
├── main_db/       # 45 جلسة مستخرجة من قاعدة البيانات النشطة (~/.local/share/opencode/opencode.db)
│   ├── ses_11a2a8c07ffeAKI5a48vUdpNI6.jsonl
│   ├── ses_e6b7fdbd3ffe0ShhsiJlQ7ZVQj.jsonl
│   └── ... (45 ملفاً)
├── backup_db/     # 7 جلسات مستخرجة من قاعدة النسخ الاحتياطي (/root/r/BACKUP_OMINIRUSH_CHAT/opencode.db)
│   ├── ses_ef1bd39ddffe387rt8u0LJBGn9.jsonl
│   ├── ses_ee9cf3076ffeCcSyGP0LOyxdyH.jsonl
│   └── ... (7 ملفات)
├── index.csv      # فهرس جدولي شامل يوثق كل جلسة، عنوانها، تاريخ إنشائها، عدد رسائلها، وحجمها
└── README.md      # هذا الملف التوثيقي
```

---

## 3. معايير الترشيح: النطاق A مقابل النطاق B
تم اعتماد **النطاق A (Scope A: العنوان المطابق)** للأسباب الموثقة في تقرير الفحص:
- **النطاق A:** يركز على الجلسات التي خُصصت بالكامل للويكي (العنوان يحتوي `wiki` أو `ويكي`). يبلغ عددها **52 جلسة** (45 في الرئيسية + 7 في الاحتياطية)، بحجم ناتج **33.6 MB** و **2,750 رسالة** و **8,594 جزءاً**.
- **النطاق B (المستثنى):** يشمل أي جلسة وردت فيها كلمة wiki في مسار ملف داخلي أو خطأ عابر (787 جلسة، بحجم يفوق 130 MB). ثبت بالفحص أن 95% منها ضوضاء ومراجعات لكود عام لا علاقة له بتطوير الويكي.

---

## 4. مقارنة القاعدتين (Main DB vs Backup DB)

| البند | القاعدة الرئيسية (`main_db`) | قاعدة النسخ الاحتياطي (`backup_db`) | الإجمالي الموحد |
|---|---|---|---|
| مسار المصدر | `/root/.local/share/opencode/opencode.db` | `/root/r/BACKUP_OMINIRUSH_CHAT/opencode.db` | — |
| حجم ملف .db الأصلي | 959 MB (لم يُنسخ) | 110 MB (لم يُنسخ) | 1,069 MB |
| عدد الجلسات المطابقة | **45** | **7** | **52** |
| المدى الزمني | 2026-06-20 إلى 2026-11-03 | 2026-10-05 إلى 2026-10-07 | 2026-06 إلى 2026-11 |
| التداخل بين المعرفات | **0** (لا يوجد أي معرف مشترك) | **0** | **0** تعارض |
| إجمالي الرسائل | 2,607 رسالة | 143 رسالة | **2,750** رسالة |
| إجمالي الأجزاء (Parts) | 7,713 جزء | 881 جزء | **8,594** جزء |
| الحجم المستخرج (JSONL) | 24.3 MB | 9.3 MB | **33.6 MB** |

> **قيمة مضافة:** تمثل جلسات `backup_db` فترة حرجة من 5 إلى 7 أكتوبر 2026 ركزت على استكمال الأقسام غير المطالب بها في الويكي (`wiki unclaimed 1-4`) وتدقيق المسودات، وهي غير متوفرة في القاعدة النشطة!

---

## 5. مواصفات بنية ملفات JSONL
يتكون كل سطر في ملفات `JSONL` من كائن JSON متكامل يربط الرسالة بجزئها دون فقدان أي حقل، وفق البنية التالية:

```json
{
  "session_id": "ses_...",
  "title": "عنوان الجلسة",
  "session_time_created": 1777048365921,
  "directory": "/root/r",
  "message_id": "msg_...",
  "message_time_created": 1777048365921,
  "role": "user | assistant",
  "part_id": "prt_...",
  "part_time_created": 1777048366062,
  "part_type": "text | tool | tool_result",
  "part": { ... بيانات الجزء كاملة ... },
  "message": { ... بيانات الرسالة والمودل والتوكنز ... }
}
```

### ضمانات السلامة البرمجية:
1. تم استخدام الربط الخارجي الأيسر (`LEFT JOIN part ON p.message_id = m.id`) لضمان عدم ضياع أي رسالة حتى وإن لم تحتوِ على أجزاء ملحقة (تم حماية 89 رسالة من الضياع).
2. فُتحت القواعد بنمط `file:... ?mode=ro` بنسبة 100% لتجنب أي تضارب مع محرك OpenCode النشط.

---

## 6. كيفية إعادة الاستخراج البرمجي (Reproducibility)
لاستخراج جلسة محددة أو تحديث الأرشيف في أي وقت:

```python
import sqlite3, json

conn = sqlite3.connect('file:/root/.local/share/opencode/opencode.db?mode=ro', uri=True)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute('''
    SELECT s.id AS sid, s.title, s.time_created AS s_time, s.directory,
           m.id AS mid, m.time_created AS m_time, m.data AS mdata,
           p.id AS pid, p.time_created AS p_time, p.data AS pdata
    FROM session s
    JOIN message m ON m.session_id = s.id
    LEFT JOIN part p ON p.message_id = m.id
    WHERE s.id = ?
    ORDER BY m.time_created ASC, p.time_created ASC
''', ('ses_e6b7fdbd3ffe0ShhsiJlQ7ZVQj',))

for r in cursor.fetchall():
    print(r['mid'], r['pid'], json.loads(r['mdata'])['role'])
```
