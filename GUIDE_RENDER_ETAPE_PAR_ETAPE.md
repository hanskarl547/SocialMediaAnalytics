# 🚀 Guide Étape par Étape : Déploiement sur Render.com

## 📋 Prérequis
- ✅ Votre code est sur GitHub (dépôt : `SocialMediaAnalytics`)
- ✅ Vous avez un compte GitHub
- ⚠️ Vous devez créer un compte Render.com (gratuit)

---

## 🔧 ÉTAPE 1 : Créer un compte Render.com

1. **Allez sur** : https://render.com
2. **Cliquez sur** : "Get Started for Free" (en haut à droite)
3. **Choisissez** : "Sign up with GitHub"
4. **Autorisez** Render à accéder à votre compte GitHub
5. **Vérifiez votre email** (si demandé)

✅ **Vous êtes maintenant connecté à Render !**

---

## 🔧 ÉTAPE 2 : Créer un nouveau service Web

1. **Dans le dashboard Render**, cliquez sur le bouton bleu **"New +"** (en haut à droite)
2. **Sélectionnez** : **"Web Service"**

---

## 🔧 ÉTAPE 3 : Connecter votre dépôt GitHub

1. **Dans la section "Connect a repository"** :
   - Render va lister vos dépôts GitHub
   - **Cherchez et sélectionnez** : `SocialMediaAnalytics` (ou le nom de votre dépôt)
   - Si vous ne voyez pas votre dépôt, cliquez sur **"Configure account"** pour autoriser l'accès

2. **Une fois le dépôt sélectionné**, cliquez sur **"Connect"**

---

## 🔧 ÉTAPE 4 : Configurer le service

Remplissez les champs suivants :

### 📝 Nom du service
```
social-media-analytics
```
*(ou un autre nom de votre choix, en minuscules, avec des tirets)*

### 📝 Environnement
**Sélectionnez** : `Python 3`

### 📝 Région
**Sélectionnez** : `Frankfurt (EU)` ou `Oregon (US)` (selon votre localisation)

### 📝 Branche
**Laissez** : `main` (ou `master` si c'est votre branche principale)

### 📝 Build Command
**Copiez-collez** :
```bash
pip install -r requirements.txt
```

### 📝 Start Command
**Copiez-collez** :
```bash
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

### 📝 Plan
**Sélectionnez** : **"Free"** (gratuit)

⚠️ **Important** : Le plan gratuit met l'application en veille après 15 minutes d'inactivité. Le premier démarrage après veille peut prendre 30-60 secondes.

---

## 🔧 ÉTAPE 5 : Configurer les variables d'environnement

**C'est la partie la plus importante !** Vous devez copier toutes les variables de votre fichier `.env`.

1. **Dans la section "Environment Variables"**, cliquez sur **"Add Environment Variable"**

2. **Ajoutez chaque variable une par une** :

   | Clé | Valeur (exemple) | Description |
   |-----|------------------|-------------|
   | `SECRET_KEY` | `d340d2bedb22644cb50d19c74643b05c0afc81eb5d11486f252fca457bcc520a` | Clé secrète de l'application |
   | `OPENAI_API_KEY` | `sk-...` | Votre clé API OpenAI |
   | `STRIPE_PUBLIC_KEY` | `pk_test_...` | Clé publique Stripe |
   | `STRIPE_SECRET_KEY` | `sk_test_...` | Clé secrète Stripe |
   | `STRIPE_WEBHOOK_SECRET` | `whsec_...` | Secret du webhook Stripe |
   | `PREMIUM_PRICE` | `500` | Prix premium en centimes |
   | `DATABASE_URL` | `sqlite:///social_analytics.db` | URL de la base de données |
   | `SMTP_SERVER` | `smtp.gmail.com` | Serveur SMTP |
   | `SMTP_PORT` | `587` | Port SMTP |
   | `SMTP_USERNAME` | `votre.email@gmail.com` | Email SMTP |
   | `SMTP_PASSWORD` | `votre_mot_de_passe` | Mot de passe SMTP |
   | `FROM_EMAIL` | `votre.email@gmail.com` | Email expéditeur |
   | `APP_NAME` | `Social Media Analytics Pro` | Nom de l'application |

3. **Pour chaque variable** :
   - Cliquez sur **"Add Environment Variable"**
   - Entrez le **nom** (colonne "Clé")
   - Entrez la **valeur** (colonne "Valeur")
   - Cliquez sur **"Save"**

4. **Répétez** pour toutes les variables de votre fichier `.env`

💡 **Astuce** : Vous pouvez copier-coller les valeurs directement depuis votre fichier `.env` local.

---

## 🔧 ÉTAPE 6 : Déployer l'application

1. **Une fois toutes les variables ajoutées**, faites défiler vers le bas
2. **Cliquez sur** : **"Create Web Service"**
3. **Render va maintenant** :
   - Cloner votre dépôt GitHub
   - Installer toutes les dépendances (`pip install -r requirements.txt`)
   - Démarrer votre application Streamlit
   - Générer une URL HTTPS

⏱️ **Le déploiement prend environ 5-10 minutes** (première fois)

---

## 🔧 ÉTAPE 7 : Vérifier le déploiement

1. **Pendant le déploiement**, vous verrez des logs en temps réel
2. **Attendez** que vous voyiez :
   ```
   ✅ Build successful
   ✅ Service is live
   ```
3. **Une fois terminé**, vous verrez une URL comme :
   ```
   https://social-media-analytics.onrender.com
   ```
4. **Cliquez sur l'URL** pour ouvrir votre application dans le navigateur

✅ **Votre application est maintenant en ligne !**

---

## 🔄 Mise à jour automatique

**Render déploie automatiquement** à chaque fois que vous poussez du code sur la branche `main` de GitHub.

**Pour mettre à jour votre application** :
1. Faites vos modifications en local
2. Commitez et poussez vers GitHub :
   ```bash
   git add .
   git commit -m "Mise à jour"
   git push origin main
   ```
3. Render détectera automatiquement les changements et redéploiera

---

## ⚠️ Problèmes courants et solutions

### ❌ Erreur : "Build failed"
**Solution** : Vérifiez les logs de build. Souvent c'est une dépendance manquante dans `requirements.txt`.

### ❌ Erreur : "Application crashed"
**Solution** : 
- Vérifiez que toutes les variables d'environnement sont bien configurées
- Vérifiez les logs dans la section "Logs" de Render
- Vérifiez que le `Start Command` est correct

### ❌ L'application se met en veille
**Solution** : C'est normal avec le plan gratuit. L'application se réveille automatiquement au premier accès (30-60 secondes).

**Pour éviter la mise en veille** :
- Utilisez un service gratuit comme **UptimeRobot** (https://uptimerobot.com) qui ping votre site toutes les 5 minutes
- Ou passez au plan payant ($7/mois)

### ❌ Erreur : "Port already in use"
**Solution** : Vérifiez que votre `Start Command` utilise bien `$PORT` :
```bash
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

---

## 📊 Vérifier les logs

1. **Dans le dashboard Render**, cliquez sur votre service
2. **Onglet "Logs"** : Voir les logs en temps réel
3. **Onglet "Events"** : Voir l'historique des déploiements

---

## ✅ Checklist finale

Avant de déployer, vérifiez que vous avez :

- [x] Un compte Render.com créé
- [x] Votre code sur GitHub
- [x] Le fichier `requirements.txt` à jour
- [x] Le fichier `Procfile` présent
- [x] Toutes les variables d'environnement prêtes
- [x] Le `Start Command` correct

---

## 🎉 Félicitations !

Votre application Streamlit est maintenant déployée sur Render.com !

**Avantages par rapport à Streamlit Cloud** :
- ✅ Pas de problème avec les icônes Material
- ✅ Plus de contrôle sur la configuration
- ✅ Logs détaillés
- ✅ Variables d'environnement sécurisées

---

## 📞 Besoin d'aide ?

Si vous rencontrez un problème :
1. Vérifiez les logs dans Render
2. Vérifiez que toutes les variables d'environnement sont configurées
3. Vérifiez que votre code fonctionne en local (`streamlit run app.py`)

