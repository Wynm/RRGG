# RRGG — Automated Content Hub

مشروع موقع محتوى **fully automated**: artículos تتولد من قائمة مواضيع، والموقع يعرضها تلقائيًا.

## 🚀 التشغيل

```bash
# 1) توليد المقالات
python scripts/generate_content.py

# 2) تشغيل الموقع محليًا
cd site && python -m http.server 8000
# ثم افتح http://localhost:8000
```

## 🔁 الأتمتة (نشر يومي)

Linux/macOS (cron):
```bash
0 8 * * * cd /home/user/RRGG && python scripts/generate_content.py
```

## 💰 الربح (Monetization)

- أضف كود AdSense في `<head>` بعد تفعيل حسابك على موقعك الخاص.
- أو Adsterra: ضع سكربت anuncios في القالب.
- انشر الموقع على GitHub Pages / Netlify / Vercel مجانًا.

## 📈 التطوير

- أضف مواضيع جديدة في `content/topics.txt`.
- طوّر `build_body()` لتوليد محتوى أطول وأدق.
