# ✈️ Déploiement Streamlit sur Fly.io

## 🎯 Fly.io - Performance Mondiale

Fly.io offre des performances excellentes avec déploiement rapide.

---

## 📋 Étapes de Déploiement

### Étape 1 : Créer un compte Fly.io

1. Allez sur **https://fly.io**
2. Cliquez sur **"Get Started"**
3. Connectez-vous avec **GitHub** ou créez un compte
4. Installez Fly CLI (optionnel mais recommandé) :
   ```bash
   # Windows PowerShell
   iwr https://fly.io/install.ps1 -useb | iex
   ```

---

### Étape 2 : Créer un fichier fly.toml

Créez un fichier `fly.toml` à la racine de votre projet :

```toml
app = "votre-app-nom-unique"
primary_region = "cdg"  # Choisissez : cdg (Paris), ord (Chicago), etc.

[build]
  builder = "paketobuildpacks/builder:base"

[env]
  PORT = "8080"

[[services]]
  http_checks = []
  internal_port = 8080
  processes = ["app"]
  protocol = "tcp"
  script_checks = []

  [services.concurrency]
    hard_limit = 25
    soft_limit = 20
    type = "connections"

  [[services.ports]]
    force_https = true
    handlers = ["http"]
    port = 80

  [[services.ports]]
    handlers = ["tls", "http"]
    port = 443

  [[services.tcp_checks]]
    grace_period = "1s"
    interval = "15s"
    restart_limit = 0
    timeout = "2s"
```

---

### Étape 3 : Créer un Procfile (Optionnel)

Créez un fichier `Procfile` à la racine :

```
web: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

---

### Étape 4 : Déployer via CLI (Recommandé)

```bash
# Se connecter
fly auth login

# Initialiser (dans le dossier de votre projet)
fly launch

# Déployer
fly deploy
```

---

### Étape 5 : Déployer via Dashboard (Alternative)

1. Connectez votre repository GitHub dans Fly.io Dashboard
2. Créez une nouvelle app
3. Sélectionnez votre repository
4. Configurez les paramètres
5. Déployez

---

### Étape 6 : Variables d'Environnement

Via CLI :
```bash
fly secrets set SECRET_KEY="votre-cle"
fly secrets set DEMO_MODE="true"
```

Via Dashboard :
1. Votre App → **Secrets**
2. Ajoutez vos variables

---

## 🔧 Configuration Avancée

### Modifier fly.toml pour Streamlit

```toml
[build]
  builder = "paketobuildpacks/builder:base"

[env]
  PORT = "8080"

[deploy]
  release_command = "echo 'Deploying...'"

[[services]]
  internal_port = 8080
  protocol = "tcp"

  [[services.ports]]
    handlers = ["http"]
    port = 80
    force_https = true

  [[services.ports]]
    handlers = ["tls", "http"]
    port = 443

  [services.concurrency]
    type = "connections"
    hard_limit = 25
    soft_limit = 20
```

---

## ✅ Vérifications Post-Déploiement

### 1. Vérifier les Logs

```bash
fly logs
```

### 2. Tester l'Application

Ouvrez l'URL fournie :
```
https://votre-app-nom.fly.dev
```

---

## 🐛 Dépannage

### Problème : Build échoue

**Vérifiez :**
1. ✅ `fly.toml` est correct
2. ✅ `requirements.txt` est présent
3. ✅ Pas d'erreurs dans les logs

### Problème : Application ne démarre pas

**Vérifiez les logs :**
```bash
fly logs
```

---

## 💰 Coûts

- **Gratuit** : 3 VMs partagées
- Suffisant pour tester
- Payez seulement si vous dépassez

---

## 📋 Checklist

- [ ] Compte Fly.io créé
- [ ] Fly CLI installé (optionnel)
- [ ] `fly.toml` créé
- [ ] App initialisée avec `fly launch`
- [ ] Secrets configurés
- [ ] Déploiement réussi avec `fly deploy`
- [ ] Application accessible

---

## 🎉 C'est tout !

Fly.io offre de bonnes performances. Parfait pour des applications importantes ! 🚀
