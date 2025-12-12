# 🔧 Guide de Configuration

## Configuration des API et Services Externes

### 1. OpenAI (Assistant IA) 🤖

L'assistant IA utilise l'API OpenAI GPT-3.5 pour générer des interprétations détaillées et des recommandations personnalisées.

#### Obtenir votre clé API OpenAI

1. **Créer un compte OpenAI**
   - Allez sur https://platform.openai.com
   - Créez un compte ou connectez-vous

2. **Générer une clé API**
   - Cliquez sur votre profil (coin supérieur droit)
   - Sélectionnez "View API keys"
   - Cliquez sur "Create new secret key"
   - Copiez la clé (elle commence par `sk-...`)
   - ⚠️ **Important** : Sauvegardez-la immédiatement, vous ne pourrez plus la voir!

3. **Ajouter du crédit**
   - Allez dans "Billing" > "Payment methods"
   - Ajoutez une carte de crédit
   - Rechargez votre compte (5-10$ suffisent pour commencer)

4. **Configurer dans l'application**
   - Ouvrez le fichier `.env`
   - Ajoutez : `OPENAI_API_KEY=sk-votre_cle_ici`
   - Sauvegardez et relancez l'application

#### Coûts estimés

- **GPT-3.5-turbo** : ~$0.002 par 1000 tokens
- Une interprétation premium ≈ 800 tokens = **$0.0016** (~0.0015€)
- Avec 10$, vous pouvez générer environ **6000 interprétations** 🎉

#### Mode sans OpenAI

Si vous ne configurez pas OpenAI, l'application fonctionne avec :
- ✅ Interprétations préprogrammées (mode dégradé)
- ✅ Toutes les analyses statistiques
- ✅ Visualisations
- ❌ Interprétations IA détaillées

---

### 2. Stripe (Paiements Premium) 💳

Stripe permet d'accepter les paiements pour les abonnements Premium.

#### Obtenir vos clés Stripe

1. **Créer un compte Stripe**
   - Allez sur https://stripe.com
   - Créez un compte ou connectez-vous

2. **Récupérer vos clés API (Mode Test)**
   - Connectez-vous au Dashboard Stripe
   - Cliquez sur "Developers" dans le menu
   - Sélectionnez "API keys"
   - Copiez :
     - **Publishable key** (commence par `pk_test_...`)
     - **Secret key** (commence par `sk_test_...`)

3. **Configurer les webhooks**
   - Dans "Developers" > "Webhooks"
   - Cliquez sur "Add endpoint"
   - URL : `https://votre-domaine.com/webhook/stripe`
   - Événements à écouter :
     - `payment_intent.succeeded`
     - `customer.subscription.deleted`
     - `customer.subscription.created`
   - Copiez le **Webhook signing secret** (`whsec_...`)

4. **Configurer dans l'application**
   - Ouvrez le fichier `.env`
   - Ajoutez :
     ```
     STRIPE_PUBLIC_KEY=pk_test_votre_cle
     STRIPE_SECRET_KEY=sk_test_votre_cle
     STRIPE_WEBHOOK_SECRET=whsec_votre_secret
     ```

#### Passer en mode Production

1. Dans le Dashboard Stripe, activez le mode **Live**
2. Récupérez les nouvelles clés (elles commenceront par `pk_live_...` et `sk_live_...`)
3. Mettez à jour le fichier `.env`
4. Complétez la vérification de votre compte Stripe

#### Coûts Stripe

- **Frais par transaction** : 1.4% + 0.25€
- Pour un abonnement à 5€ :
  - Vous recevez : **4.68€**
  - Stripe prélève : **0.32€**

#### Mode sans Stripe

Si vous ne configurez pas Stripe :
- ✅ Mode démo disponible (activation Premium instantanée pour tests)
- ❌ Impossibilité d'accepter de vrais paiements

---

### 3. Configuration de la Base de Données 🗄️

L'application utilise SQLite par défaut (pas de configuration nécessaire).

#### SQLite (Par défaut)

- ✅ **Avantages** :
  - Aucune configuration
  - Fichier local (`social_analytics.db`)
  - Parfait pour débuter

- ⚠️ **Limites** :
  - Non adapté pour 1000+ utilisateurs simultanés
  - Un seul fichier (pas de distribution)

#### Migrer vers PostgreSQL (Production)

Pour une utilisation en production avec beaucoup d'utilisateurs :

1. **Installer PostgreSQL**
   - Windows : https://www.postgresql.org/download/windows/
   - Ou utilisez un service cloud (Heroku, Railway, Supabase)

2. **Créer une base de données**
   ```sql
   CREATE DATABASE social_analytics;
   ```

3. **Modifier le fichier `.env`**
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/social_analytics
   ```

4. **Installer psycopg2**
   ```bash
   pip install psycopg2-binary
   ```

5. **Mettre à jour `database.py`**
   - Remplacez `sqlite3` par `SQLAlchemy` avec PostgreSQL

---

## Variables d'Environnement (.env)

### Fichier `.env` complet (template)

```env
# ============================================
# CONFIGURATION SOCIAL MEDIA ANALYTICS PRO
# ============================================

# Clé secrète de l'application (générez-en une unique)
SECRET_KEY=votre_cle_secrete_aleatoire_ici

# ============================================
# OPENAI API (Assistant IA)
# ============================================
# Obtenir une clé: https://platform.openai.com
OPENAI_API_KEY=sk-...

# ============================================
# STRIPE (Paiements)
# ============================================
# Mode Test
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Mode Production (décommenter quand prêt)
# STRIPE_PUBLIC_KEY=pk_live_...
# STRIPE_SECRET_KEY=sk_live_...
# STRIPE_WEBHOOK_SECRET=whsec_...

# Prix Premium (en centimes, 500 = 5€)
PREMIUM_PRICE=500

# ============================================
# BASE DE DONNÉES
# ============================================
# SQLite (par défaut)
DATABASE_URL=sqlite:///social_analytics.db

# PostgreSQL (production)
# DATABASE_URL=postgresql://user:password@localhost:5432/social_analytics

# ============================================
# AUTRES CONFIGURATIONS
# ============================================
# Environnement (development, production)
ENVIRONMENT=development

# Debug mode
DEBUG=True
```

### Générer une clé secrète sécurisée

#### Avec Python :
```python
import secrets
print(secrets.token_urlsafe(32))
```

#### Ou en ligne de commande :
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## Configuration Streamlit

Le fichier `.streamlit/config.toml` personnalise l'apparence de l'application.

### Thème actuel

```toml
[theme]
primaryColor = "#667eea"        # Couleur principale (violet)
backgroundColor = "#FFFFFF"      # Fond blanc
secondaryBackgroundColor = "#F0F2F6"  # Fond secondaire gris clair
textColor = "#262730"           # Texte noir
font = "sans serif"             # Police
```

### Personnaliser les couleurs

Modifiez `primaryColor` pour changer la couleur principale :

- Bleu : `#4A90E2`
- Vert : `#50C878`
- Rouge : `#E74C3C`
- Orange : `#FF8C42`

### Configuration serveur

```toml
[server]
port = 8501                     # Port de l'application
headless = true                 # Mode sans tête (pour serveur)
enableCORS = false              # CORS
enableXsrfProtection = true     # Protection XSRF
```

---

## Déploiement en Production

### Option 1 : Streamlit Cloud (Gratuit & Simple)

1. **Créer un compte**
   - Allez sur https://streamlit.io/cloud
   - Connectez-vous avec GitHub

2. **Déployer**
   - Poussez votre code sur GitHub
   - Dans Streamlit Cloud : "New app"
   - Sélectionnez votre repo
   - Configurez les secrets (équivalent du `.env`)
   - Cliquez sur "Deploy"

3. **Ajouter les secrets**
   - Dans les paramètres de l'app
   - Ajoutez vos clés API (OpenAI, Stripe)

**Limites gratuites** :
- ✅ 1 app publique gratuite
- ✅ Ressources limitées (mais suffisantes)

---

### Option 2 : Heroku

1. **Installer Heroku CLI**
   ```bash
   heroku login
   ```

2. **Créer un fichier `Procfile`**
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

3. **Créer un fichier `setup.sh`**
   ```bash
   mkdir -p ~/.streamlit/
   echo "[server]
   headless = true
   port = $PORT
   " > ~/.streamlit/config.toml
   ```

4. **Déployer**
   ```bash
   heroku create nom-de-votre-app
   git push heroku main
   heroku config:set OPENAI_API_KEY=sk-...
   heroku config:set STRIPE_SECRET_KEY=sk-...
   ```

**Coûts** :
- Hobby : $7/mois
- Professional : $25-50/mois

---

### Option 3 : VPS (DigitalOcean, AWS, etc.)

1. **Louer un serveur** (à partir de 5$/mois)

2. **Installer les dépendances**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   pip3 install -r requirements.txt
   ```

3. **Lancer l'application**
   ```bash
   streamlit run app.py --server.port=8501
   ```

4. **Configurer un reverse proxy (Nginx)**
   ```nginx
   server {
       listen 80;
       server_name votredomaine.com;
       
       location / {
           proxy_pass http://localhost:8501;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
       }
   }
   ```

5. **SSL avec Let's Encrypt**
   ```bash
   sudo certbot --nginx -d votredomaine.com
   ```

---

## Sécurité - Bonnes Pratiques

### ✅ À FAIRE

1. **Ne jamais commiter le fichier `.env`**
   - Ajoutez `.env` dans `.gitignore`

2. **Utiliser des clés différentes en test et production**
   - Test : `pk_test_...`
   - Production : `pk_live_...`

3. **Changer régulièrement les mots de passe**
   - Base de données
   - Clés API

4. **Activer l'authentification 2FA**
   - Sur votre compte OpenAI
   - Sur votre compte Stripe

5. **Limiter les permissions**
   - Utilisez des clés API avec le minimum de permissions nécessaires

### ❌ À ÉVITER

1. ❌ Partager vos clés API
2. ❌ Commiter `.env` sur GitHub
3. ❌ Utiliser les mêmes mots de passe partout
4. ❌ Laisser DEBUG=True en production

---

## Surveillance et Monitoring

### Logs Streamlit

```bash
streamlit run app.py --logger.level=debug
```

### Monitoring avec Sentry (optionnel)

1. Créez un compte sur https://sentry.io
2. Installez le SDK :
   ```bash
   pip install sentry-sdk
   ```
3. Dans `app.py` :
   ```python
   import sentry_sdk
   sentry_sdk.init("https://your-dsn@sentry.io/project-id")
   ```

---

## FAQ Configuration

### Q : L'app fonctionne sans OpenAI ?
**R :** Oui ! Elle utilisera des interprétations préprogrammées.

### Q : Comment tester Stripe sans carte ?
**R :** Utilisez les cartes de test :
- Succès : `4242 4242 4242 4242`
- Échec : `4000 0000 0000 0002`

### Q : Puis-je changer le prix Premium ?
**R :** Oui, modifiez `PREMIUM_PRICE` dans `.env` (en centimes).

### Q : Comment sauvegarder la base de données ?
**R :** Copiez simplement le fichier `social_analytics.db`.

### Q : L'app peut gérer combien d'utilisateurs ?
**R :** 
- SQLite : ~100 utilisateurs simultanés
- PostgreSQL : 1000+ utilisateurs

---

## Support

Pour toute question sur la configuration :
- 📧 Email : support@exemple.com
- 📚 Documentation : README.md
- 💬 Issues GitHub : [lien]

---

**Bonne configuration ! 🚀**

