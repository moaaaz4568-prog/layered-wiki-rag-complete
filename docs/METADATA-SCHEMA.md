# METADATA-SCHEMA — حقول المقطع والصفحة

> الحالة: REPORTED — من `analysis-wiki-talk-01.md` §4.3–§4.4 + `repo-plan-01.md` §3.2.
> وسم الدليل: OBSERVED = مقاس على القرص، REPORTED = منقول من تقرير، PROPOSED = مقترح مستقبلي، UNKNOWN = لا دليل، NOT_RUN = لم يُشغَّل بعد.

## 1. حقول المقطع الواجبة (مفتاح التتبع)

- **الشخصية (persona):** slug الشخصية مالكة المقطع؛ الفلتر المنظوري إجباري كما Metadata | REPORTED — `analysis-wiki-talk-01.md` §1.8
- **المسار الخام (raw_path):** مسار النص الأصلي في `raw/`؛ الخام للقراءة فقط | REPORTED — `analysis-wiki-talk-01.md` §4.4
- **المسار الويكي (wiki_path):** مسار الصفحة المترجمة/المجمّعة التي ينتمي إليها المقطع | REPORTED — `analysis-wiki-talk-01.md` §4.4
- **العنوان (title):** عنوان الصفحة أو عنوان القسم داخلها | REPORTED — `analysis-wiki-talk-01.md` §4.4
- **معرّف المقطع (chunk_id):** معرف فريد مستقر لكل مقطع داخل الصفحة | REPORTED — `analysis-wiki-talk-01.md` §4.4
- **النوع (type):** عنوان/فقرة/جدول/قائمة — حسب تعريف المقطع الصحيح | REPORTED — `analysis-wiki-talk-01.md` §1.8
- **الموقع (offset):** نطاق محارف أو عنوان داخل الصفحة لاسترجاع الاستشهاد | REPORTED — `analysis-wiki-talk-01.md` §4.4
- **البصمة (sha/chunk_hash):** بصمة المحتوى للكشف عن التعديل | REPORTED — `analysis-wiki-talk-01.md` §4.4
- **حجم البايت (bytes):** حجم الصفحة أو المقطع بالبايت لقياس التوزيع | REPORTED — `analysis-wiki-talk-01.md` §4.4
- **عدد المقاطع (nchunks):** لكل صفحة داخل فهرس manifest.jsonl | REPORTED — `analysis-wiki-talk-01.md` §1.7

## 2. حقول الحالة والحجر

- **تاريخ التحديث (updated_at):** آخر تعديل موثّق على الصفحة | REPORTED — `analysis-wiki-talk-01.md` §4.4
- **حالة الحجر (quarantine_state):** مفتوح/محجور — صفحة متناقضة تُحجر من الاسترجاع حتى حكم إنسان | REPORTED — `analysis-wiki-talk-01.md` §1.11
- **سبب الحجر (quarantine_reason):** سببه إن وُجد، ليُسجَّل القرار البشري | REPORTED — `analysis-wiki-talk-01.md` §4.4
- **المنشأ (provenance):** المصدر الأصلي للمعلومة (قناة/كتاب/فيديو) | REPORTED — `analysis-wiki-talk-01.md` §4.4
- **الوسوم (tags):** وسوم إضافية (ديني/سيرة/تعافي) للتنقل | PROPOSED — `analysis-wiki-talk-01.md` §4.3
- **حالة الترقية (lifecycle):** scratch → research → candidate → canon؛ الترقية بموافقة إنسان فقط | REPORTED — `analysis-wiki-talk-01.md` §2.5

## 3. قياسات شاهدة (OBSERVED)

- 6 ويكيات: 5,896 صفحة، 31.3MB (31,262,266 بايت) | OBSERVED — `analysis-wiki-talk-01.md` §1.7
- هيثم 210 صفحة: 601,084 بايت | OBSERVED — `analysis-wiki-talk-01.md` §1.10
- أصغر 20 صفحة لهيثم: 37,402 بايت، 129 مقطعًا | OBSERVED — `analysis-wiki-talk-01.md` §1.7
- متوسط صفحة هيثم 2,336 بايت مقابل ابن تيمية 10,458 بايت | OBSERVED — `analysis-wiki-talk-01.md` §1.7
- تقسيم الويكيات الست: سيرين 780، تيمية 81، قيم 556، هيثم 210، عماد 1,423، علاء 2,846 | OBSERVED — `analysis-wiki-talk-01.md` §1.7
- أرشيف الويكي: 212MB، 2,713 ملفًا على القرص | OBSERVED — `archive-inventory-01.md` §2
- فهرس الأرشيف الجذري: `MANIFEST.json` (780K) — فهرس آلي لكل ملف (لا يُرفع كاملًا) | OBSERVED — `archive-inventory-01.md` §1
