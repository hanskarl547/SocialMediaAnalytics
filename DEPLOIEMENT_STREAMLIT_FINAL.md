# 🚀 Déploiement Streamlit Cloud - Guide Final

## ✅ Votre Projet est Prêt !

Votre application Streamlit est prête pour le déploiement sur Streamlit Cloud.

---

## 📋 Déploiement en 3 Étapes

### 1️⃣ Créer un Compte Streamlit Cloud

👉 **https://share.streamlit.io**

- Cliquez sur **"Sign up"** ou **"Continue with GitHub"**
- Autorisez Streamlit à accéder à votre GitHub

---

### 2️⃣ Déployer votre Application

1. Dans Streamlit Cloud Dashboard, cliquez sur **"New app"**

2. Configurez :
   - **Repository** : Sélectionnez `SocialMediaAnalytics` (ou votre repo)
   - **Branch** : `main` (ou `master`)
   - **Main file path** : `app.py`

3. **Advanced settings** (optionnel) :
   - **Python version** : 3.10 ou 3.11

4. Cliquez sur **"Deploy"** 🚀

---

### 3️⃣ Variables d'Environnement (si nécessaire)

Si votre app utilise des variables d'environnement (API keys, secrets) :

1. Settings → **"Secrets"**
2. Ajoutez au format TOML :

```toml
[secrets]
SECRET_KEY = "votre-cle-secrete"
DEMO_MODE = "true"
STRIPE_SECRET_KEY = "sk_test_..."
STRIPE_PUBLISHABLE_KEY = "pk_test_..."
OPENAI_API_KEY = "sk-..."  # Si vous utilisez OpenAI
```

**Dans votre code Streamlit, accédez-y via :**
```python
import streamlit as st

# Accès aux secrets
secret_key = st.secrets["SECRET_KEY"]
demo_mode = st.secrets.get("DEMO_MODE", "true")
```

---

## ✅ Checklist

- [ ] Code sur GitHub
- [ ] `requirements.txt` présent (✅ déjà OK)
- [ ] `app.py` présent (✅ déjà OK)
- [ ] Compte Streamlit Cloud créé
- [ ] Application déployée
- [ ] Variables d'environnement configurées (si nécessaire)
- [ ] Application testée via l'URL fournie

---

## 🎉 Après le Déploiement

Votre application sera disponible sur :
```
https://votre-app-nom.streamlit.app
```

---

## 🔄 Mises à Jour Automatiques

À chaque push sur la branche principale, Streamlit Cloud redéploie automatiquement votre application.

Pour désactiver :
- Settings → **"Auto-redeploy"** → Désactiver

---

## 🐛 Dépannage

### Build échoue

**Vérifiez :**
- ✅ `requirements.txt` est correct
- ✅ Toutes les dépendances sont disponibles sur PyPI
- ✅ Pas d'erreurs dans les logs

### Application ne démarre pas

**Vérifiez les logs :**
1. Dashboard → Votre app → **"Logs"**
2. Cherchez les erreurs
3. Vérifiez les variables d'environnement

### Variables d'environnement

**Utilisez `st.secrets` au lieu de `os.getenv` :**

```python
# ❌ Ne fonctionne pas bien sur Streamlit Cloud
import os
key = os.getenv("SECRET_KEY")

# ✅ Fonctionne sur Streamlit Cloud
import streamlit as st
key = st.secrets["SECRET_KEY"]
```

---

## 🎯 Résumé Rapide

1. **Allez sur** : https://share.streamlit.io
2. **Connectez-vous** avec GitHub
3. **"New app"** → Sélectionnez votre repo → **"Deploy"**
4. **Configurer les secrets** si nécessaire
5. **Tester** l'URL fournie

---

## 🎉 C'est tout !

Streamlit Cloud est gratuit et très simple. Votre application sera en ligne en quelques minutes ! 🚀

**Besoin d'aide ?** Consultez les logs dans le dashboard Streamlit Cloud.
