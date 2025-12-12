# 🔧 Résolution : Erreur d'accès à Streamlit Cloud

## ⚠️ Erreur rencontrée

**"You do not have access to this app or it does not exist"**

Cette erreur signifie que Streamlit Cloud ne peut pas trouver votre application ou que vous n'avez pas les permissions nécessaires.

---

## 🔍 Causes possibles

1. **L'application n'a jamais été créée** sur Streamlit Cloud
2. **L'application a été supprimée** ou le lien est incorrect
3. **Problème de compte GitHub** : Le compte utilisé pour créer l'app est différent
4. **L'application a été créée avec un autre compte** Streamlit Cloud

---

## ✅ Solutions

### Solution 1 : Vérifier si l'application existe

1. Allez sur **https://share.streamlit.io/**
2. Connectez-vous avec votre compte GitHub (hanskarl547)
3. Cliquez sur **"My apps"** dans le menu
4. Vérifiez si votre application "SocialMediaAnalytics" apparaît dans la liste

**Si l'application apparaît** :
- Cliquez dessus pour y accéder
- Le problème vient peut-être du lien que vous utilisez

**Si l'application N'APPARAÎT PAS** :
- Passez à la Solution 2 pour créer une nouvelle application

---

### Solution 2 : Créer une nouvelle application (si elle n'existe pas)

#### Étape 1 : Se connecter à Streamlit Cloud

1. Allez sur **https://share.streamlit.io/**
2. Cliquez sur **"Sign in"** (en haut à droite)
3. Cliquez sur **"Continue with GitHub"**
4. Autorisez l'accès à votre compte GitHub (hanskarl547)

#### Étape 2 : Créer une nouvelle application

1. Une fois connecté, cliquez sur le bouton **"New app"** (gros bouton vert)
2. Remplissez le formulaire :
   - **Repository** : Sélectionnez `hanskarl547/SocialMediaAnalytics`
   - **Branch** : `main` (ou `master` si c'est votre branche principale)
   - **Main file path** : `app.py`
   - **App URL** : Laissez le nom par défaut ou choisissez un nom (ex: `social-media-analytics-pro`)
3. Cliquez sur **"Deploy"**

#### Étape 3 : Attendre le déploiement

- ⏱️ Cela prend 2-5 minutes la première fois
- Vous verrez le statut "Deploying..." puis "Running"

#### Étape 4 : Configurer les secrets (IMPORTANT)

Une fois déployée :

1. Cliquez sur **"Settings"** (icône d'engrenage) ou **"Manage app"**
2. Cliquez sur **"Secrets"** dans le menu de gauche
3. Ajoutez vos variables d'environnement au format TOML :

```toml
SECRET_KEY = "générez-une-nouvelle-cle-secrete-ici"
PREMIUM_PRICE = "500"
DATABASE_URL = "sqlite:///social_analytics.db"
APP_NAME = "Social Media Analytics Pro"
```

**Pour générer une nouvelle SECRET_KEY** :
- Exécutez dans PowerShell : `python -c "import secrets; print(secrets.token_hex(32))"`
- Ou allez sur https://randomkeygen.com/

**Clés optionnelles** (si vous les utilisez) :

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
5. L'application redémarre automatiquement

---

### Solution 3 : Vérifier le compte GitHub associé

Si vous avez plusieurs comptes GitHub :

1. Dans Streamlit Cloud, allez dans **"Settings"** (votre profil)
2. Vérifiez quel compte GitHub est connecté
3. Si ce n'est pas le bon compte :
   - Déconnectez-vous
   - Reconnectez-vous avec le bon compte GitHub (hanskarl547)

---

### Solution 4 : Vérifier que le repository est bien sur GitHub

1. Allez sur **https://github.com/hanskarl547/SocialMediaAnalytics**
2. Vérifiez que le repository existe et est accessible
3. Vérifiez que vous avez bien les permissions (Owner ou Admin)
4. Si le repository est privé, assurez-vous que Streamlit Cloud y a accès

---

## 🔗 URL de votre application

Une fois créée, votre application sera accessible à :

- `https://VOTRE-APP-NAME.streamlit.app`
- Ou l'URL affichée dans Streamlit Cloud

**Exemple** : Si vous avez nommé votre app "social-media-analytics-pro", l'URL sera :
- `https://social-media-analytics-pro.streamlit.app`

---

## ✅ Checklist de résolution

- [ ] Je suis connecté à Streamlit Cloud avec le bon compte GitHub
- [ ] Mon repository GitHub est accessible (https://github.com/hanskarl547/SocialMediaAnalytics)
- [ ] J'ai créé une nouvelle application sur Streamlit Cloud (si elle n'existait pas)
- [ ] J'ai configuré les secrets dans Streamlit Cloud
- [ ] L'application est en statut "Running" dans Streamlit Cloud
- [ ] Je peux accéder à l'application via l'URL fournie

---

## 🐛 Si le problème persiste

### Vérifier les logs

1. Dans Streamlit Cloud, cliquez sur votre application
2. Allez dans l'onglet **"Logs"**
3. Vérifiez s'il y a des erreurs
4. Les erreurs courantes :
   - **"Module not found"** : Vérifiez que `requirements.txt` est complet
   - **"Secret not found"** : Vérifiez que les secrets sont bien configurés
   - **"File not found"** : Vérifiez que `app.py` existe dans le repository

### Contacter le support

Si rien ne fonctionne :
1. Allez sur https://discuss.streamlit.io/
2. Créez un nouveau sujet avec votre problème
3. Incluez les logs d'erreur

---

## 📝 Prochaines étapes après résolution

Une fois que votre application fonctionne :

1. **Tester l'application** :
   - Créer un compte
   - Se connecter
   - Importer des données
   - Lancer des analyses

2. **Synchroniser les modifications futures** :
   - Utilisez `SYNCHRONISER.bat` pour pousser vos modifications
   - Ou utilisez GitHub Desktop
   - Streamlit Cloud redéploiera automatiquement

---

**Votre application devrait maintenant être accessible ! 🎉**

