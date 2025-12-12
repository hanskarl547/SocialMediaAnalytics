# 🚀 Guide de Déploiement - Social Media Analytics Pro

Ce guide vous aidera à déployer votre application Streamlit sur **Streamlit Cloud** (recommandé et gratuit) ou d'autres plateformes.

## 📋 Prérequis

- Un compte GitHub
- Un compte Streamlit Cloud (gratuit) : https://streamlit.io/cloud
- Votre projet doit être sur GitHub

---

## 🌐 Option 1 : Déploiement sur Streamlit Cloud (Recommandé)

### Étape 1 : Préparer votre projet sur GitHub

1. **Initialiser Git** (si pas déjà fait) :
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Ready for deployment"
   ```

2. **Créer un repository sur GitHub** :
   - Allez sur https://github.com/new
   - Créez un nouveau repository (publique ou privée)
   - Suivez les instructions pour pousser votre code

3. **Pousser votre code** :
   ```bash
   git remote add origin https://github.com/VOTRE_USERNAME/VOTRE_REPO.git
   git branch -M main
   git push -u origin main
   ```

### Étape 2 : Configurer Streamlit Cloud

1. **Connecter votre compte** :
   - Allez sur https://share.streamlit.io/
   - Connectez-vous avec votre compte GitHub

2. **Nouvelle application** :
   - Cliquez sur "New app"
   - Sélectionnez votre repository GitHub
   - Sélectionnez la branche `main`
   - Entrez le chemin du fichier principal : `app.py`

3. **Configurer les secrets** :
   - Cliquez sur "Advanced settings"
   - Cliquez sur "Secrets"
   - Ajoutez vos variables d'environnement dans ce format :

   ```toml
   SECRET_KEY = "votre_cle_secrete_ici"
   OPENAI_API_KEY = "sk-votre_cle_openai"
   STRIPE_PUBLIC_KEY = "pk_votre_cle_publique"
   STRIPE_SECRET_KEY = "sk_votre_cle_secrete"
   STRIPE_WEBHOOK_SECRET = "whsec_votre_webhook_secret"
   PREMIUM_PRICE = "500"
   DATABASE_URL = "sqlite:///social_analytics.db"
   SMTP_SERVER = "smtp.gmail.com"
   SMTP_PORT = "587"
   SMTP_USERNAME = "votre.email@gmail.com"
   SMTP_PASSWORD = "votre_mot_de_passe"
   FROM_EMAIL = "votre.email@gmail.com"
   APP_NAME = "Social Media Analytics Pro"
   ```

### Étape 3 : Déployer

1. Cliquez sur "Deploy"
2. Attendez quelques minutes pendant le déploiement
3. Votre application sera disponible à l'adresse : `https://VOTRE-APP.streamlit.app`

### Étape 4 : Configuration post-déploiement

- ✅ Vérifiez que l'application démarre correctement
- ✅ Testez la création de compte
- ✅ Testez l'import de données
- ✅ Vérifiez les fonctionnalités Premium

---

## 🐳 Option 2 : Déploiement avec Docker

### Créer un Dockerfile

Un fichier `Dockerfile` est déjà créé dans votre projet. Voici comment l'utiliser :

1. **Construire l'image** :
   ```bash
   docker build -t social-media-analytics .
   ```

2. **Lancer le conteneur** :
   ```bash
   docker run -p 8501:8501 -e SECRET_KEY="votre_cle" social-media-analytics
   ```

### Déployer sur Docker Hub / AWS / Google Cloud

- Suivez les instructions de votre plateforme pour déployer une image Docker

---

## ☁️ Option 3 : Déploiement sur Heroku

### Étape 1 : Créer un Procfile

Le fichier `Procfile` doit contenir :
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

### Étape 2 : Créer un fichier setup.sh

```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

### Étape 3 : Mettre à jour requirements.txt

Ajoutez `gunicorn` si nécessaire (mais Streamlit n'en a pas besoin).

### Étape 4 : Déployer sur Heroku

```bash
heroku create votre-app-name
heroku config:set SECRET_KEY="votre_cle"
heroku config:set OPENAI_API_KEY="sk-..."
git push heroku main
```

---

## 🔐 Configuration des Secrets

### Variables obligatoires

- `SECRET_KEY` : Clé secrète pour l'application (générez-en une nouvelle)
  ```python
  python -c "import secrets; print(secrets.token_hex(32))"
  ```

### Variables optionnelles (selon vos besoins)

- `OPENAI_API_KEY` : Pour l'assistant IA Premium
- `STRIPE_*` : Pour les paiements réels (ou mode démo sans)
- `SMTP_*` : Pour les notifications email
- `DATABASE_URL` : Pour utiliser PostgreSQL au lieu de SQLite

### ⚠️ Important pour Streamlit Cloud

Sur Streamlit Cloud, utilisez le fichier `.streamlit/secrets.toml` via l'interface web, PAS un fichier `.env` local.

---

## 📊 Base de données en production

### SQLite (défaut)
- ✅ Simple et fonctionne immédiatement
- ❌ Pas idéal pour la production (limitations de concurrence)
- ⚠️ Les données sont perdues si le conteneur redémarre sur certaines plateformes

### PostgreSQL (recommandé pour production)

1. **Créer une base de données PostgreSQL** (Heroku Postgres, Railway, Supabase, etc.)

2. **Mettre à jour DATABASE_URL** :
   ```toml
   DATABASE_URL = "postgresql://user:password@host:port/dbname"
   ```

3. **Mettre à jour database.py** pour supporter PostgreSQL :
   - SQLAlchemy supporte déjà PostgreSQL automatiquement

---

## ✅ Checklist avant déploiement

- [x] ✅ Vérifier que `.env` est dans `.gitignore`
- [x] ✅ Vérifier que `social_analytics.db` est dans `.gitignore`
- [x] ✅ Tous les chemins hardcodés sont corrigés
- [ ] Générer une nouvelle `SECRET_KEY` pour la production
- [ ] Tester l'installation avec `pip install -r requirements.txt`
- [ ] Vérifier que tous les secrets sont configurés
- [ ] Tester l'application localement une dernière fois
- [ ] Documenter les variables d'environnement nécessaires

---

## 🐛 Dépannage

### L'application ne démarre pas

- Vérifiez les logs dans Streamlit Cloud
- Vérifiez que tous les secrets sont configurés
- Vérifiez que `requirements.txt` est à jour

### Erreur de base de données

- Vérifiez les permissions d'écriture
- Pour SQLite, assurez-vous que le chemin est accessible
- Considérez PostgreSQL pour la production

### Les variables d'environnement ne sont pas chargées

- Sur Streamlit Cloud, utilisez l'interface "Secrets" dans les paramètres
- Vérifiez le format TOML des secrets
- Vérifiez que `python-dotenv` est installé

### Erreur "Module not found"

- Vérifiez que toutes les dépendances sont dans `requirements.txt`
- Vérifiez les versions de Python (3.8+ requis)

---

## 📝 Après le déploiement

1. **Tester toutes les fonctionnalités** :
   - Création de compte
   - Connexion
   - Import de données
   - Analyses statistiques
   - Assistant IA
   - Fonctionnalités Premium

2. **Surveiller les logs** :
   - Vérifiez régulièrement les erreurs
   - Surveillez l'utilisation

3. **Backup régulier** :
   - Exportez la base de données régulièrement
   - Sauvegardez les configurations importantes

---

## 🔗 Ressources utiles

- **Streamlit Cloud** : https://streamlit.io/cloud
- **Documentation Streamlit** : https://docs.streamlit.io
- **GitHub** : https://github.com
- **Heroku** : https://www.heroku.com (alternatif)

---

## 💡 Recommandations

1. **Pour commencer** : Utilisez Streamlit Cloud (gratuit, simple, recommandé)
2. **Pour la production** : Considérez PostgreSQL au lieu de SQLite
3. **Pour la sécurité** : Générez une nouvelle SECRET_KEY pour chaque environnement
4. **Pour les performances** : Surveillez l'utilisation et optimisez si nécessaire

---

**Bon déploiement ! 🚀**

