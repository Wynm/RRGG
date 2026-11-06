#!/usr/bin/env python3
"""Automated SEO article generator.

Reads topics from content/topics.txt, generates a structured HTML article
per topic, and updates site/articles/index.json so the site lists them.

Usage:
    python scripts/generate_content.py
"""
import json, re, html, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
ART = SITE / "articles"
TOPICS = ROOT / "content" / "topics.txt"

TEMPLATE = """<!DOCTYPE html>
<html lang="ar" dir="rtl"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{excerpt}">
<style>body{{font-family:Tahoma,sans-serif;max-width:800px;margin:2rem auto;line-height:1.9;background:#0f172a;color:#e2e8f0;padding:0 1rem}}h1,h2{{color:#38bdf8}}a{{color:#38bdf8}}</style>
</head><body>
<h1>{title}</h1>
<p><em>نُشر تلقائيًا في {date}</em></p>
{body}
<p><a href="../index.html">← العودة للرئيسية</a></p>
</body></html>"""

def slugify(t: str) -> str:
    s = re.sub(r"[^\w\s-]", "", t, flags=re.UNICODE).strip().lower()
    return re.sub(r"[\s_]+", "-", s) or "article"

def build_body(topic: str) -> str:
    t = topic.strip()
    paras = [
        f"<h2>مقدمة عن {t}</h2><p>هذا المقال يتناول {t} بشكل مبسط وعملي، مع خطوات واضحة يمكن تطبيقها مباشرة.</p>",
        "<h2>أهم النصائح</h2><ul><li>ابدأ بخطوة صغيرة ثم طوّر تدريجيًا.</li><li>قِس نتائجك أسبوعيًا.</li><li>كرّر ما ينجح واستبعد ما لا ينجح.</li></ul>",
        f"<h2>خاتمة</h2><p>الخلاصة: {t} تحتاج إلى استمرارية أكثر من الحيل — ابدأ اليوم.</p>",
    ]
    return "\n".join(paras)

def main():
    ART.mkdir(parents=True, exist_ok=True)
    topics = [l.strip() for l in TOPICS.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    index = []
    for t in topics:
        slug = slugify(t)
        fname = f"{slug}.html"
        excerpt = f"دليل عملي عن {t}."
        page = TEMPLATE.format(title=html.escape(t), excerpt=html.escape(excerpt),
                               date=datetime.date.today().isoformat(), body=build_body(t))
        (ART / fname).write_text(page, encoding="utf-8")
        index.append({"title": t, "file": fname, "excerpt": excerpt})
    (ART / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generated {len(index)} articles in {ART}")

if __name__ == "__main__":
    main()
