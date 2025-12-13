# 🚀 Déploiement sur Streamlit Cloud - Guide Complet

## 🎯 Streamlit Cloud

Streamlit Cloud est la plateforme officielle (gratuite) pour héberger vos applications Streamlit.

---

## ✅ Prérequis

1. ✅ Un compte GitHub
2. ✅ Votre code Streamlit sur GitHub
3. ✅ Un compte Streamlit Cloud (gratuit)

---

## 📋 Étapes de Déploiement

### Étape 1 : Préparer votre Repository GitHub

#### 1.1 Vérifier les fichiers nécessaires

Votre projet doit contenir :
- ✅ `app.py` (ou votre fichier Streamlit principal)
- ✅ `requirements.txt` (dépendances Python)
- ✅ `.streamlit/config.toml` (optionnel, pour configuration)

#### 1.2 Vérifier requirements.txt

Assurez-vous que `requirements.txt` contient toutes les dépendances :

```txt
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
scipy>=1.10.0
matplotlib>=3.7.0
seaborn>=0.12.0
scikit-learn>=1.3.0
plotly>=5.17.0
openpyxl>=3.1.0
xlrd>=2.0.0
python-dotenv>=1.0.0
```

**Important :** N'incluez PAS `gunicorn` ou des dépendances Flask - c'est pour Streamlit uniquement !

#### 1.3 Commiter et pousser sur GitHub

```bash
git add .
git commit -m "Ready for Streamlit Cloud deployment"
git push origin main
```

---

### Étape 2 : Créer un compte Streamlit Cloud

1. Allez sur **https://share.streamlit.io**
2. Cliquez sur **"Sign up"** ou **"Continue with GitHub"**
3. Autorisez Streamlit à accéder à votre GitHub

---

### Étape 3 : Déployer votre Application

1. Dans Streamlit Cloud Dashboard, cliquez sur **"New app"**

2. Configurez votre app :
   - **Repository** : Sélectionnez votre repository (`SocialMediaAnalytics`)
   - **Branch** : `main` (ou `master`)
   - **Main file path** : `app.py` (le chemin vers votre fichier Streamlit principal)
   
3. **Advanced settings** (optionnel) :
   - **Python version** : 3.10 ou 3.11 (recommandé)
   - Si vous avez des variables d'environnement, ajoutez-les ici

4. Cliquez sur **"Deploy"**

---

### Étape 4 : Variables d'Environnement (si nécessaire)

Si votre application utilise des variables d'environnement (API keys, secrets, etc.) :

1. Dans Streamlit Cloud Dashboard
2. Sélectionnez votre app
3. Cliquez sur **"⋮" (menu)** → **"Settings"**
4. Section **"Secrets"**
5. Ajoutez vos variables au format TOML :

```toml
[secrets]
SECRET_KEY = "votre-cle-secrete"
DEMO_MODE = "true"
STRIPE_SECRET_KEY = "sk_test_..."
STRIPE_PUBLISHABLE_KEY = "pk_test_..."
```

---

### Étape 5 : Attendre le Déploiement

1. Streamlit Cloud va :
   - Installer les dépendances depuis `requirements.txt`
   - Lancer votre application
   - Générer une URL publique

2. Vous verrez les logs de déploiement en temps réel

3. Une fois terminé, votre app sera disponible sur :
   ```
   https://votre-app-nom.streamlit.app
   ```

---

## 🔧 Configuration Avancée

### Créer un fichier .streamlit/config.toml (Optionnel)

Créez un dossier `.streamlit` et un fichier `config.toml` :

```toml
[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

---

## ✅ Checklist de Déploiement

- [ ] Code commité et pushé sur GitHub
- [ ] `requirements.txt` présent et complet
- [ ] `app.py` (ou fichier principal) présent
- [ ] Compte Streamlit Cloud créé
- [ ] Application déployée via Streamlit Cloud
- [ ] Variables d'environnement configurées (si nécessaire)
- [ ] Application accessible via l'URL fournie
- [ ] Tests de l'application réussis

---

## 🐛 Dépannage

### Problème : Build échoue

**Vérifiez :**
1. ✅ `requirements.txt` est correct et présent
2. ✅ Toutes les dépendances sont disponibles sur PyPI
3. ✅ Pas de conflits de versions

### Problème : Application ne démarre pas

**Vérifiez les logs :**
1. Dans Streamlit Cloud Dashboard
2. Cliquez sur votre app
3. Onglet **"Logs"**
4. Cherchez les erreurs

### Problème : Variables d'environnement

**Vérifiez :**
1. ✅ Variables définies dans "Secrets"
2. ✅ Format TOML correct
3. ✅ Accès dans le code via `st.secrets`

Exemple dans votre code :
```python
import streamlit as st

# Accès aux secrets
secret_key = st.secrets["SECRET_KEY"]
demo_mode = st.secrets.get("DEMO_MODE", "true")
```

---

## 📊 Après le Déploiement

### Monitoring

Streamlit Cloud affiche automatiquement :
- ✅ État de l'application (Running/Error)
- ✅ Logs en temps réel
- ✅ Statistiques d'utilisation

### Mises à jour

Chaque push sur la branche principale déclenche un redéploiement automatique.

Pour désactiver :
1. Settings → **"Auto-redeploy"** → Désactiver

---

## 🎯 Résumé Rapide

1. **Préparer** : Code sur GitHub + `requirements.txt`
2. **Créer compte** : https://share.streamlit.io
3. **Déployer** : "New app" → Sélectionner repo → Déployer
4. **Configurer** : Variables d'environnement si nécessaire
5. **Tester** : Ouvrir l'URL fournie

---

## 🎉 Avantages de Streamlit Cloud

- ✅ **Gratuit** pour les projets publics
- ✅ **Déploiement automatique** à chaque push
- ✅ **URL personnalisée** (`nom-app.streamlit.app`)
- ✅ **Facile à configurer**
- ✅ **Support natif** de Streamlit

---

**Votre application sera en ligne en quelques minutes !** 🚀
