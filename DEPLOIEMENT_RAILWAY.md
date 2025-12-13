# 🚂 Déploiement sur Railway.app

**Railway** est une plateforme moderne et simple, alternative à Heroku.

## ✅ Avantages
- ✅ **Gratuit** avec $5 de crédit par mois
- ✅ **HTTPS automatique**
- ✅ **Déploiement automatique depuis GitHub**
- ✅ **Variables d'environnement sécurisées**
- ✅ **Pas de mise en veille**

## 📋 Prérequis
1. Compte GitHub (vous l'avez déjà)
2. Compte Railway (gratuit) : https://railway.app

## 🔧 Étapes de déploiement

### 1. Créer un compte Railway
- Allez sur https://railway.app
- Cliquez sur "Start a New Project"
- Connectez-vous avec votre compte GitHub

### 2. Créer un nouveau projet
- Cliquez sur **"New Project"**
- Sélectionnez **"Deploy from GitHub repo"**
- Choisissez votre dépôt : `SocialMediaAnalytics`

### 3. Configurer le service
Railway détecte automatiquement que c'est une application Python.

**Railway va automatiquement :**
- Détecter `requirements.txt`
- Installer les dépendances
- Démarrer l'application

### 4. Configurer la commande de démarrage
Dans les **"Settings"** du service :
- **Start Command :**
  ```
  streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
  ```

### 5. Configurer les variables d'environnement
Dans **"Variables"**, ajoutez toutes les variables de votre fichier `.env` :

```
SECRET_KEY=votre_secret_key
OPENAI_API_KEY=votre_openai_key
STRIPE_PUBLIC_KEY=votre_stripe_public_key
STRIPE_SECRET_KEY=votre_stripe_secret_key
STRIPE_WEBHOOK_SECRET=votre_webhook_secret
PREMIUM_PRICE=29.99
DATABASE_URL=sqlite:///database.db
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=votre.email@gmail.com
SMTP_PASSWORD=votre_mot_de_passe
FROM_EMAIL=votre.email@gmail.com
APP_NAME=Social Media Analytics Pro
PORT=8501
```

### 6. Générer un domaine
- Dans **"Settings"** → **"Generate Domain"**
- Railway génère automatiquement une URL HTTPS

### 7. Déployer
- Railway déploie automatiquement à chaque push sur `main`
- Le déploiement prend environ 3-5 minutes

## 💰 Coûts
- **Gratuit** : $5 de crédit par mois (suffisant pour une petite app)
- **Payant** : À partir de $5/mois pour plus de ressources

## 🔄 Mise à jour automatique
Railway déploie automatiquement à chaque push sur la branche `main`.

## 📝 Fichiers nécessaires
Votre projet contient déjà :
- ✅ `requirements.txt` (dépendances)
- ✅ `Procfile` (commande de démarrage)

**Aucun fichier supplémentaire n'est nécessaire !**

