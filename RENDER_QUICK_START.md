# ⚡ Déploiement Rapide sur Render.com

## 🚀 En 5 minutes

### 1. Créer un compte
👉 https://render.com → "Get Started" → Connecter GitHub

### 2. Créer un Web Service
- Cliquez sur **"New +"** → **"Web Service"**
- Sélectionnez votre dépôt : `SocialMediaAnalytics`
- Cliquez sur **"Connect"**

### 3. Configurer
**Build Command :**
```bash
pip install -r requirements.txt
```

**Start Command :**
```bash
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

**Plan :** `Free`

### 4. Variables d'environnement
Ajoutez toutes les variables de votre fichier `.env` dans la section "Environment Variables".

**Variables essentielles :**
- `SECRET_KEY`
- `OPENAI_API_KEY`
- `STRIPE_PUBLIC_KEY`
- `STRIPE_SECRET_KEY`
- `DATABASE_URL=sqlite:///social_analytics.db`
- `SMTP_SERVER`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`, `FROM_EMAIL`
- `APP_NAME=Social Media Analytics Pro`

### 5. Déployer
Cliquez sur **"Create Web Service"** et attendez 5-10 minutes.

✅ **C'est tout !** Votre app sera disponible sur `https://votre-app.onrender.com`

---

## 📖 Guide détaillé
Pour plus de détails, consultez : `GUIDE_RENDER_ETAPE_PAR_ETAPE.md`

