# ✈️ Déploiement sur Fly.io

**Fly.io** est une plateforme moderne avec un plan gratuit généreux.

## ✅ Avantages
- ✅ **Gratuit** (3 apps gratuites)
- ✅ **HTTPS automatique**
- ✅ **Déploiement depuis GitHub**
- ✅ **Pas de mise en veille**
- ✅ **Très rapide**

## 📋 Prérequis
1. Compte GitHub (vous l'avez déjà)
2. Compte Fly.io (gratuit) : https://fly.io
3. Fly CLI installé (optionnel, pour déploiement manuel)

## 🔧 Étapes de déploiement

### Option 1 : Déploiement via GitHub (Recommandé)

#### 1. Créer un compte Fly.io
- Allez sur https://fly.io
- Cliquez sur "Sign Up"
- Connectez-vous avec votre compte GitHub

#### 2. Créer une nouvelle app
- Dans le dashboard, cliquez sur **"New App"**
- Sélectionnez **"Launch App"**
- Connectez votre dépôt GitHub : `SocialMediaAnalytics`

#### 3. Configurer l'application
Fly.io détecte automatiquement Python et utilise `requirements.txt`.

#### 4. Configurer les variables d'environnement
Dans **"Secrets"**, ajoutez toutes les variables de votre fichier `.env`.

#### 5. Déployer
- Fly.io déploie automatiquement
- Vous obtiendrez une URL comme : `https://votre-app.fly.dev`

### Option 2 : Déploiement via CLI (Avancé)

#### 1. Installer Fly CLI
```bash
# Windows (PowerShell)
iwr https://fly.io/install.ps1 -useb | iex
```

#### 2. Se connecter
```bash
fly auth login
```

#### 3. Créer l'application
```bash
fly launch
```

#### 4. Configurer les secrets
```bash
fly secrets set SECRET_KEY="votre_secret_key"
fly secrets set OPENAI_API_KEY="votre_openai_key"
# ... etc pour toutes les variables
```

#### 5. Déployer
```bash
fly deploy
```

## 📝 Créer un fichier fly.toml (optionnel)

Si vous voulez personnaliser la configuration, créez `fly.toml` :

```toml
app = "votre-app-name"
primary_region = "cdg"

[build]

[env]
  PORT = "8501"

[[services]]
  internal_port = 8501
  protocol = "tcp"

  [[services.ports]]
    port = 80
    handlers = ["http"]
    force_https = true

  [[services.ports]]
    port = 443
    handlers = ["tls", "http"]

  [services.concurrency]
    type = "connections"
    hard_limit = 25
    soft_limit = 20

  [[services.http_checks]]
    interval = "10s"
    timeout = "2s"
    grace_period = "5s"
    method = "GET"
    path = "/"
```

## 💰 Coûts
- **Gratuit** : 3 apps gratuites avec 256 MB RAM chacune
- **Payant** : À partir de $1.94/mois pour plus de ressources

## 🔄 Mise à jour automatique
Si vous utilisez GitHub, Fly.io peut déployer automatiquement à chaque push.

## 📝 Fichiers nécessaires
Votre projet contient déjà :
- ✅ `requirements.txt` (dépendances)

**Optionnel :** `fly.toml` pour personnaliser la configuration.

