# SOURCES — فهرس المصادر الخارجية والروابط

> الحالة: REPORTED — من `../../work/analysis-wiki-talk-01.md` §2.1 + §2.5 + `../../work/repo-plan-01.md` §3.2.
> وسم الدليل: OBSERVED = مقاس على القرص، REPORTED = منقول من تقرير، PROPOSED = مقترح مستقبلي، UNKNOWN = لا دليل، NOT_RUN = لم يُشغَّل بعد.

## 1. روابط خارجية مذكورة (من التحليل)

- `https://www.transfernow.net/dl/20261101suwmDHnJ` — ملف السياق الكامل المحدث لكلود (نسخة 9MB) | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.1
- `https://github.com/topoteretes/cognee` — GraphRAG المقترح — بُني عليه التصميم، لكنه ليس الاختيار النهائي (تأجيل) | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.1
- `https://github.com/starmynd-org/infinite-brain-os.git` — نظام تنظيم معرفة MIT (584 ملف، 4.7MB، 228 عقدة) — دراسته ودمج مفاهيمه | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.1
- `https://youtu.be/U7UQlAWCKo8?is=alX8CoRG8Jn9HiZx` — اختبار يوتيوب الثلاثي بدون كوكيز | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.1
- `https://youtu.be/aMOgezEHXUc?si=PSAigQYpvPf-13RI` — فيديو من الثلاثة الأساسية للبحث | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.1
- `https://youtu.be/pvcSMlhNKlo?si=2G1bCkdvW27zFDdz` — فيديو من الثلاثة | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.1
- `https://youtu.be/DTCyvo6cC54?si=A3yb5R7-dm4-q844` — Nate Herk — مستويات Second Brain | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.1
- `https://youtube.com/@dr.haitham_talaat?si=SJb66qJcY4o3oMeR` — قناة هيثم طلعت | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.1
- `https://api.yukino.my/keys` — مفتاح Yukino (موقع) | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.1
- `https://api.hcnsec.cn` — مفتاح hcnsec — داخل JSON `_type: newapi_channel_conn` | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.1
- `https://nlozx-2a04-4e41-14-1e1--d091-1e1.run.pinggy-free.link` — رابط ترمنال pinggy الأول | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.1
- `https://pmbwb-2a04-4e41-10-efc--dd64-efc.free.pinggy.net` — رابط ترمنال جديد | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.1
- `http://127.0.0.1:4416/ping` — PoToken server المحلي في سكربت الكولاب | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.1
- GitHub `geasas/youtube-transcripts` + `transcripts/transcripts_final.zip` — مستودع رفع النصوص في سكربت الكولاب | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.1
- `github:goodnight000/api-anything` — أداة api-anything المحملة عبر `npx -y` | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.1

## 2. ملفات على القرص (جرد مقاس)

- `~/workspace/yt-wiki/` — النظام الموحد الجديد: download → build → index → ask (بحث كلمات) | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.2
- `~/workspace/wiki-project/` — الويكيات القديمة: التعافي 1,418 + السيرة 2,844 = 4,262 صفحة | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.2
- `~/workspace/wiki-rag/` — مشروع RAG الجديد: DESIGN.md + manifest.jsonl + phase0/ + research/ | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.2
- `wiki-rag/research/yt-subs-144/` — خام VTT (47MB) + نصوص TXT نظيفة (7.4MB) + SUMMARY.md | OBSERVED — `../../work/analysis-wiki-talk-01.md` §2.2
- (`~/workspace/your_files/wiki-full-context-for-claude.md` — 9,109,934 بايت و193,619 سطر قبل التحديث — الأرقام REPORTED من `../../work/analysis-wiki-talk-01.md` §2.2) | UNKNOWN — غير موجود على القرص
- (نفس الملف محدَّث: 9,144,870 بايت After Infinite Brain OS — الأرقام REPORTED من `../../work/analysis-wiki-talk-01.md` §2.2) | UNKNOWN — غير موجود على القرص
- (`~/workspace/your_files/wiki-context-concise-for-claude.md` — 27,616 بايت، 265 سطر — الأرقام REPORTED من `../../work/analysis-wiki-talk-01.md` §2.2) | UNKNOWN — غير موجود على القرص
- `~/workspace/subs-dl/` — مشروع الترجمة المحلي: cookies.txt + dl_bounded.sh + smart_batch.py | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.2
- (الجرد المقاس: 33,918 ملف / 13,488 TXT / 6,784 ID فريد) | OBSERVED — `../../work/analysis-wiki-talk-01.md` §2.2

## 3. أدوات خارجية (من التحليل)

- **Cognee** — GraphRAG: كيانات وعلاقات + مخزن متجهات + بحث هجين — مفضّل تحت الاختبار، لكن الاستيراد يفشل (قاعدة بيانات 0 بايت) | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.3
- **ChromaDB** — بديل جاهز لـ Cognee لو اتضح مثقل أو الاستخراج ضعيف | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.3
- **bge-m3** — مضمّن متعدد اللغات 1024 بُعد — مرشّح مشروط بالاختبار الذي لم يثبت بعد على العربية داخل Cognee | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.3
- `intfloat/multilingual-e5-large` — مضمّن بديل يذكره التحليل كـ«الأقرب للعربي» | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.3
- **RAGFlow** — RAG + واجهة — تقيل (محتاج 16GB) غير مناسب لبيئة 7.7GB/2CPU | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.3
- **AnythingLLM** — واجهة RAG — «كونه سيرفر MCP لـ OpenCode مش مثبت» | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.3
- **OKF (Open Knowledge Format)** — عقد تنسيق Open Source — Bundle = مجلد Markdown + type + روابط + index.md | REPORTED — `../../work/analysis-wiki-talk-01.md` §2.3

## 4. نتائج بحثية

- تم تحميل 144 فيديو كاملة: VTT 47MB + TXT 7.4MB | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.9
- إنجليزي: 2,783,968 حرف، 509,906 كلمة، 144 فيديو (المقروء فعليًا 143) | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.9
- أطول نص: محاضرة Karpathy Deep Dive وحدها 215,307 حرف | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.9
- فيديو `DTCyvo6cC54` — 304,801 مشاهدة في 30:59 | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.9
- فيديو `Z8kFhWXKay4` — Karpathy's LLM-Wiki is Bad — 7,048 حرف | OBSERVED — `../../work/analysis-wiki-talk-01.md` §1.9
