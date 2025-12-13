# ⚡ Déploiement Streamlit Cloud - Guide Rapide

## 🚀 Déploiement en 3 Étapes

### 1️⃣ Préparer le Code

Assurez-vous d'avoir :
- ✅ Code sur GitHub
- ✅ `requirements.txt` à la racine
- ✅ `app.py` (ou votre fichier principal Streamlit)

### 2️⃣ Créer un Compte

👉 https://share.streamlit.io → **"Continue with GitHub"**

### 3️⃣ Déployer

1. **"New app"**
2. **Repository** : Sélectionnez votre repo
3. **Main file path** : `app.py`
4. **"Deploy"**

---

## ✅ C'est tout !

Votre app sera disponible sur :
```
https://votre-app.streamlit.app
```

---

## 🔐 Variables d'Environnement (si nécessaire)

Settings → **Secrets** → Ajoutez :

```toml
[secrets]
SECRET_KEY = "votre-cle"
DEMO_MODE = "true"
```

---

## 📋 Checklist Express

- [ ] Code sur GitHub
- [ ] `requirements.txt` présent
- [ ] Compte Streamlit Cloud créé
- [ ] App déployée
- [ ] URL testée

---

**Streamlit Cloud est gratuit et très simple !** 🎉
