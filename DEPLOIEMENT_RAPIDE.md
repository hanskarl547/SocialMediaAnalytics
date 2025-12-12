# ⚡ Déploiement Rapide - En 5 minutes

## 🎯 Déployer sur Streamlit Cloud (Recommandé)

### 1️⃣ Préparer GitHub (2 minutes)

```bash
# Si vous n'avez pas encore initialisé Git
git init
git add .
git commit -m "Ready for deployment"

# Créer un repository sur GitHub, puis :
git remote add origin https://github.com/VOTRE_USERNAME/VOTRE_REPO.git
git branch -M main
git push -u origin main
```

### 2️⃣ Déployer sur Streamlit Cloud (3 minutes)

1. Allez sur **https://share.streamlit.io/**
2. Connectez-vous avec GitHub
3. Cliquez sur **"New app"**
4. Sélectionnez votre repository et branche `main`
5. Fichier principal : `app.py`
6. Cliquez sur **"Deploy"**

### 3️⃣ Configurer les secrets (important!)

Une fois déployé, dans les paramètres de l'app :

1. Allez dans **"Settings" → "Secrets"**
2. Copiez-collez ce modèle et remplissez vos valeurs :

```toml
SECRET_KEY = "02ab56758fa872efdfbe7d0a2978c0b80492cf0cb2fcee1eabe97c32fc9df179"
PREMIUM_PRICE = "500"
DATABASE_URL = "sqlite:///social_analytics.db"
APP_NAME = "Social Media Analytics Pro"
```

**Clés optionnelles** (ajoutez seulement si vous les utilisez) :
```toml
OPENAI_API_KEY = "sk-..."
STRIPE_PUBLIC_KEY = "pk_..."
STRIPE_SECRET_KEY = "sk_..."
STRIPE_WEBHOOK_SECRET = "whsec_..."
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = "587"
SMTP_USERNAME = "votre.email@gmail.com"
SMTP_PASSWORD = "votre_mot_de_passe"
FROM_EMAIL = "votre.email@gmail.com"
```

3. Cliquez sur **"Save"**
4. L'app redémarre automatiquement avec les nouveaux secrets

### 4️⃣ Votre app est en ligne ! 🎉

Votre application sera disponible à : `https://VOTRE-APP-NAME.streamlit.app`

---

## ✅ Checklist rapide

- [ ] Code sur GitHub
- [ ] App déployée sur Streamlit Cloud
- [ ] SECRET_KEY configurée (générez-en une nouvelle si besoin)
- [ ] App testée et fonctionnelle

---

## 🔐 Générer une nouvelle SECRET_KEY

Si vous voulez générer une nouvelle clé secrète :

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copiez le résultat et utilisez-le dans les secrets Streamlit Cloud.

---

## 🐛 Problème ?

- Vérifiez les logs dans Streamlit Cloud (icône "Manage app")
- Vérifiez que tous les secrets sont configurés
- Consultez `GUIDE_DEPLOIEMENT.md` pour plus de détails

---

**C'est tout ! Bon déploiement ! 🚀**

