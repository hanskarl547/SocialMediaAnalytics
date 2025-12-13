# 🚂 Déploiement Streamlit sur Railway

## 🎯 Railway.app - Simple et Rapide

Railway est excellent pour déployer Streamlit. Configuration minimale requise !

---

## 📋 Étapes de Déploiement

### Étape 1 : Créer un compte Railway

1. Allez sur **https://railway.app**
2. Cliquez sur **"Login"** ou **"Get Started"**
3. Connectez-vous avec **GitHub** (recommandé)

---

### Étape 2 : Créer un nouveau projet

1. Dans le dashboard Railway, cliquez sur **"New Project"**
2. Sélectionnez **"Deploy from GitHub repo"**
3. Autorisez Railway à accéder à votre GitHub si nécessaire
4. Sélectionnez votre repository : `SocialMediaAnalytics`

---

### Étape 3 : Railway détecte automatiquement Streamlit

Railway devrait automatiquement :
- ✅ Détecter que c'est une application Streamlit
- ✅ Installer les dépendances depuis `requirements.txt`
- ✅ Configurer le démarrage

#### ⚠️ Important : Fichier runtime.txt

Si vous avez une erreur Python, créez un fichier `runtime.txt` à la racine :

```
python-3.11.9
```

Ou pour Python 3.10 (plus stable) :
```
python-3.10.13
```

Commitez et pushez ce fichier pour que Railway utilise la bonne version Python.

---

### Étape 4 : Configurer le Start Command (si nécessaire)

Si Railway ne détecte pas automatiquement :

1. Allez dans **Settings** → **Deploy**
2. **Start Command** :
   ```bash
   streamlit run app.py --server.port $PORT --server.address 0.0.0.0
   ```

---

### Étape 5 : Variables d'Environnement

Dans Railway Dashboard → Votre Service → **Variables** :

Ajoutez vos variables si nécessaire :

#### Variables Exemple :

| Variable | Valeur | Cryptée? |
|----------|--------|----------|
| `SECRET_KEY` | *(générez une clé)* | ✅ OUI |
| `DEMO_MODE` | `true` | ❌ NON |
| `OPENAI_API_KEY` | `sk-...` | ✅ OUI |

#### Générer une SECRET_KEY

```python
import secrets
print(secrets.token_urlsafe(32))
```

---

### Étape 6 : Déployer

Railway déploie automatiquement après chaque commit GitHub !

**OU** cliquez manuellement sur **"Deploy"** dans le dashboard.

---

## 🔧 Fichier railway.toml (Optionnel)

Créez un fichier `railway.toml` à la racine pour plus de contrôle :

```toml
[build]
builder = "NIXPACKS"

[deploy]
startCommand = "streamlit run app.py --server.port $PORT --server.address 0.0.0.0"
healthcheckPath = "/"
healthcheckTimeout = 100
restartPolicyType = "ON_FAILURE"
restartPolicyMaxRetries = 10
```

---

## ✅ Vérifications Post-Déploiement

### 1. Vérifier les Logs

Dans Railway Dashboard → Votre Service → **Deployments** → Logs

Vous devriez voir :
```
Collecting streamlit...
Installing collected packages: streamlit...
You can now view your Streamlit app in your browser.
```

### 2. Tester l'Application

Ouvrez l'URL fournie par Railway :
```
https://votre-app.up.railway.app
```

---

## 🐛 Dépannage

### Problème : Railway ne détecte pas Streamlit

**Solution :** Définissez manuellement le Start Command :
```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

### Problème : Application ne démarre pas

**Vérifiez :**
1. ✅ `requirements.txt` est présent
2. ✅ `app.py` est à la racine
3. ✅ Variables d'environnement si nécessaire

### Problème : Variables d'environnement

**Dans votre code Streamlit, utilisez :**
```python
import os
secret_key = os.getenv("SECRET_KEY", "default_value")
```

---

## 💰 Coûts

- **Gratuit** : $5 de crédit par mois
- Suffisant pour tester et petits projets
- Payez seulement si vous dépassez

---

## 📋 Checklist

- [ ] Compte Railway créé
- [ ] Projet créé et connecté à GitHub
- [ ] Start Command configuré (si nécessaire)
- [ ] Variables d'environnement ajoutées (si nécessaire)
- [ ] Déploiement réussi
- [ ] Logs vérifiés
- [ ] Application accessible via l'URL Railway

---

## 🎉 C'est tout !

Railway est très simple pour Streamlit. Votre application sera en ligne rapidement ! 🚀
