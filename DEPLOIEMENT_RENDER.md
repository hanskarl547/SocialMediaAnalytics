# 🚀 Déploiement sur Render.com

**Render** est une excellente alternative à Streamlit Cloud, gratuite et simple.

## ✅ Avantages
- ✅ **Gratuit** (avec limitations)
- ✅ **HTTPS automatique**
- ✅ **Déploiement automatique depuis GitHub**
- ✅ **Variables d'environnement sécurisées**
- ✅ **Pas de problème avec les icônes Material**

## 📋 Prérequis
1. Compte GitHub (vous l'avez déjà)
2. Compte Render.com (gratuit) : https://render.com

## 🔧 Étapes de déploiement

### 1. Créer un compte Render
- Allez sur https://render.com
- Cliquez sur "Get Started for Free"
- Connectez-vous avec votre compte GitHub

### 2. Créer un nouveau service
- Dans le dashboard, cliquez sur **"New +"**
- Sélectionnez **"Web Service"**

### 3. Connecter votre dépôt GitHub
- Sélectionnez votre dépôt : `SocialMediaAnalytics`
- Cliquez sur **"Connect"**

### 4. Configurer le service
Remplissez les champs suivants :

**Nom du service :**
```
social-media-analytics
```

**Environnement :**
```
Python 3
```

**Build Command :**
```bash
pip install -r requirements.txt
```

**Start Command :**
```bash
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

**Plan :**
- Sélectionnez **"Free"** (gratuit)

### 5. Configurer les variables d'environnement
Dans la section **"Environment Variables"**, ajoutez toutes les variables de votre fichier `.env` :

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
```

### 6. Déployer
- Cliquez sur **"Create Web Service"**
- Render va automatiquement :
  - Cloner votre dépôt
  - Installer les dépendances
  - Démarrer votre application
- Le déploiement prend environ 5-10 minutes

### 7. Accéder à votre application
- Une fois le déploiement terminé, vous obtiendrez une URL comme :
  ```
  https://social-media-analytics.onrender.com
  ```

## ⚠️ Limitations du plan gratuit
- L'application se met en veille après 15 minutes d'inactivité
- Le premier démarrage après veille peut prendre 30-60 secondes
- 750 heures gratuites par mois

## 💡 Astuce : Éviter la mise en veille
Pour éviter que l'application se mette en veille, vous pouvez :
1. Utiliser un service de monitoring (UptimeRobot) qui ping votre site toutes les 5 minutes
2. Passer au plan payant ($7/mois) pour éviter la mise en veille

## 🔄 Mise à jour automatique
Render déploie automatiquement à chaque push sur la branche `main` de votre dépôt GitHub.

## 📝 Fichiers nécessaires
Votre projet contient déjà :
- ✅ `requirements.txt` (dépendances)
- ✅ `Procfile` (commande de démarrage)

**Aucun fichier supplémentaire n'est nécessaire !**

