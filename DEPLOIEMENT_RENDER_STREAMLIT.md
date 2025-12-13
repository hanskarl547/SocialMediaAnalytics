# 🌐 Déploiement Streamlit sur Render

## 🎯 Render.com - Gratuit pour Toujours

Render offre un déploiement gratuit (avec limitations) pour vos applications Streamlit.

---

## 📋 Étapes de Déploiement

### Étape 1 : Créer un compte Render

1. Allez sur **https://render.com**
2. Cliquez sur **"Get Started"**
3. Connectez-vous avec **GitHub**

---

### Étape 2 : Créer un nouveau Web Service

1. Dans le dashboard Render, cliquez sur **"New +"**
2. Sélectionnez **"Web Service"**
3. Connectez votre repository GitHub
4. Sélectionnez votre repository : `SocialMediaAnalytics`

---

### Étape 3 : Configurer le Service

Remplissez les informations :

- **Name** : `social-media-analytics` (ou nom de votre choix)
- **Region** : Choisissez la région la plus proche
- **Branch** : `main` (ou votre branche principale)
- **Root Directory** : Laisser vide (ou `./` si nécessaire)

---

### Étape 4 : Build & Start Commands

#### Build Command :
```bash
pip install -r requirements.txt
```

#### Start Command :
```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

---

### Étape 5 : Variables d'Environnement

Dans Render Dashboard → Votre Service → **Environment** :

Cliquez sur **"Add Environment Variable"** :

| Variable | Valeur | Secret? |
|----------|--------|---------|
| `SECRET_KEY` | *(générez une clé)* | ✅ OUI |
| `DEMO_MODE` | `true` | ❌ NON |

---

### Étape 6 : Déployer

1. Cliquez sur **"Create Web Service"**
2. Render va automatiquement :
   - Installer les dépendances
   - Démarrer votre application
   - Générer une URL

---

## ⚠️ Note Importante - Plan Gratuit

Avec le plan gratuit de Render :
- ⏱️ L'instance se met en **veille** après ~15 minutes d'inactivité
- 🐌 Le **premier démarrage** après inactivité peut prendre ~50 secondes
- ✅ C'est **normal** et n'affecte pas les fonctionnalités

---

## 🔧 Fichier render.yaml (Optionnel)

Créez un fichier `render.yaml` à la racine :

```yaml
services:
  - type: web
    name: social-media-analytics
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
    envVars:
      - key: SECRET_KEY
        generateValue: true
      - key: DEMO_MODE
        value: true
```

---

## ✅ Vérifications Post-Déploiement

### 1. Vérifier les Logs

Dans Render Dashboard → Votre Service → **Logs**

Vous devriez voir :
```
Installing streamlit...
You can now view your Streamlit app in your browser.
```

### 2. Tester l'Application

Ouvrez l'URL fournie par Render :
```
https://votre-app.onrender.com
```

⚠️ Si l'instance était en veille, attendez ~50 secondes.

---

## 🐛 Dépannage

### Problème : Application ne démarre pas

**Vérifiez :**
1. ✅ Build Command correct
2. ✅ Start Command correct
3. ✅ `requirements.txt` présent
4. ✅ `app.py` présent

### Problème : Timeout ou erreur

**Vérifiez les logs** dans Render Dashboard pour voir l'erreur exacte.

### Problème : Variables d'environnement

**Dans votre code :**
```python
import os
secret = os.getenv("SECRET_KEY", "default")
```

---

## 💰 Coûts

- **Gratuit** : Pour toujours (avec limitations)
- Plan payant : À partir de $7/mois (évite la mise en veille)

---

## 📋 Checklist

- [ ] Compte Render créé
- [ ] Web Service créé
- [ ] Build Command : `pip install -r requirements.txt`
- [ ] Start Command : `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
- [ ] Variables d'environnement configurées
- [ ] Déploiement réussi
- [ ] Logs vérifiés
- [ ] Application accessible

---

## 🎉 C'est tout !

Render est gratuit et fiable. Parfait pour les projets à long terme ! 🚀
