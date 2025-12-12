# 🚀 Déploiement sur Streamlit Cloud - Guide Étape par Étape

## ✅ Prérequis accomplis

- ✅ Votre code est sur GitHub
- ✅ Repository : `SocialMediaAnalytics`
- ✅ Tous les fichiers sont committés

---

## 📋 Étapes pour déployer sur Streamlit Cloud

### Étape 1 : Aller sur Streamlit Cloud

1. Ouvrez votre navigateur
2. Allez sur : **https://share.streamlit.io/**
3. Cliquez sur **"Sign in"** (en haut à droite)

---

### Étape 2 : Se connecter avec GitHub

1. Cliquez sur **"Continue with GitHub"**
2. Autorisez Streamlit Cloud à accéder à votre compte GitHub
3. Vous serez redirigé vers votre tableau de bord Streamlit Cloud

---

### Étape 3 : Créer une nouvelle application

1. Cliquez sur le bouton **"New app"** (gros bouton vert en haut)
2. Remplissez le formulaire :
   - **Repository** : Sélectionnez `SocialMediaAnalytics` (ou votre nom d'utilisateur/SocialMediaAnalytics)
   - **Branch** : `main`
   - **Main file path** : `app.py`
   - **App URL** : Laissez le nom par défaut ou changez-le (ex: `social-media-analytics-pro`)
3. Cliquez sur **"Deploy"**

---

### Étape 4 : Attendre le déploiement

- Streamlit Cloud va :
  1. Installer les dépendances depuis `requirements.txt`
  2. Lancer votre application
  3. Créer l'URL publique

**⏱️ Cela peut prendre 2-5 minutes la première fois**

---

### Étape 5 : Configurer les secrets (IMPORTANT !)

⚠️ **Votre app ne fonctionnera pas correctement sans les secrets !**

1. Une fois déployée, allez dans **"Settings"** (icône d'engrenage) ou **"Manage app"**
2. Cliquez sur **"Secrets"** dans le menu de gauche
3. Copiez-collez ce modèle et remplissez vos valeurs :

```toml
SECRET_KEY = "générez-une-nouvelle-cle-secrete-ici"
PREMIUM_PRICE = "500"
DATABASE_URL = "sqlite:///social_analytics.db"
APP_NAME = "Social Media Analytics Pro"
```

**Clés optionnelles** (ajoutez seulement si vous les utilisez) :

```toml
# Pour l'assistant IA Premium
OPENAI_API_KEY = "sk-votre_cle_openai_ici"

# Pour les paiements Stripe
STRIPE_PUBLIC_KEY = "pk_votre_cle_publique"
STRIPE_SECRET_KEY = "sk_votre_cle_secrete"
STRIPE_WEBHOOK_SECRET = "whsec_votre_webhook_secret"

# Pour les notifications email
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = "587"
SMTP_USERNAME = "votre.email@gmail.com"
SMTP_PASSWORD = "votre_mot_de_passe"
FROM_EMAIL = "votre.email@gmail.com"
```

4. Cliquez sur **"Save"**
5. L'application redémarre automatiquement avec les nouveaux secrets

---

### Étape 6 : Générer une nouvelle SECRET_KEY

⚠️ **N'utilisez PAS la même SECRET_KEY que votre .env local !**

Générez-en une nouvelle pour la production :

**Option 1 : En ligne de commande**
```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

**Option 2 : En ligne**
- Allez sur : https://randomkeygen.com/
- Utilisez une clé de 64 caractères

---

### Étape 7 : Tester votre application

1. Une fois déployée, votre app sera disponible à :
   - `https://VOTRE-APP-NAME.streamlit.app`
   - Ou cliquez sur l'URL affichée dans Streamlit Cloud

2. **Testez** :
   - ✅ Créer un compte
   - ✅ Se connecter
   - ✅ Importer des données
   - ✅ Lancer des analyses

---

## 🔧 Résolution de problèmes

### L'application ne démarre pas

1. Vérifiez les logs dans Streamlit Cloud (onglet "Logs")
2. Vérifiez que tous les secrets sont configurés
3. Vérifiez que `requirements.txt` est complet

### Erreur "Module not found"

- Vérifiez que toutes les dépendances sont dans `requirements.txt`
- Vérifiez les versions dans `requirements.txt`

### Erreur de base de données

- Sur Streamlit Cloud, SQLite fonctionne mais les données sont temporaires
- Pour une base de données persistante, utilisez PostgreSQL (voir guide avancé)

### Les secrets ne fonctionnent pas

- Vérifiez le format TOML dans la section Secrets
- Vérifiez qu'il n'y a pas d'espaces en trop
- Sauvegardez et attendez le redémarrage automatique

---

## ✅ Checklist de déploiement

- [ ] Compte Streamlit Cloud créé
- [ ] Application déployée depuis GitHub
- [ ] SECRET_KEY générée et configurée
- [ ] Autres secrets configurés (si nécessaire)
- [ ] Application accessible via l'URL
- [ ] Tests fonctionnels effectués

---

## 🎉 Félicitations !

Votre application est maintenant en ligne et accessible partout dans le monde ! 🌍

---

## 📝 Notes importantes

1. **Base de données** : SQLite sur Streamlit Cloud est temporaire. Les données peuvent être perdues lors des redéploiements.

2. **Mises à jour automatiques** : Chaque fois que vous poussez du code sur GitHub, Streamlit Cloud redéploie automatiquement.

3. **Secrets** : Ne partagez JAMAIS vos secrets publiquement. Ils sont stockés de manière sécurisée dans Streamlit Cloud.

4. **Limites gratuites** : Streamlit Cloud gratuit a des limites (utilisation CPU, RAM). Pour plus de ressources, il faut un compte payant.

---

**Bon déploiement ! 🚀**

