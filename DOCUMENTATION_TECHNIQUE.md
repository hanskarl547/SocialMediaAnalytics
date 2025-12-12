# DOCUMENTATION TECHNIQUE
## Social Media Analytics Pro

---

## TABLE DES MATIÈRES

1. [Architecture](#1-architecture)
2. [Modules et Fonctions](#2-modules-et-fonctions)
3. [Base de Données](#3-base-de-données)
4. [APIs et Intégrations](#4-apis-et-intégrations)
5. [Configuration](#5-configuration)
6. [Déploiement](#6-déploiement)
7. [Maintenance](#7-maintenance)

---

## 1. ARCHITECTURE

### 1.1 Structure du Projet

```
SocialMediaAnalytics/
├── app.py                    # Application principale Streamlit
├── database.py               # Gestion de la base de données SQLite
├── statistical_analysis.py   # Analyses statistiques avancées
├── visualizations.py         # Génération de graphiques interactifs
├── ai_assistant.py           # Assistant IA avec OpenAI
├── country_map.py            # Visualisations géographiques
├── notifications.py           # Système de notifications
├── email_sender.py           # Envoi d'emails SMTP
├── payment_handler.py        # Gestion des paiements Stripe
├── .env                      # Variables d'environnement
├── requirements.txt          # Dépendances Python
└── social_analytics.db       # Base de données SQLite
```

### 1.2 Flux de Données

```
Utilisateur → Interface Streamlit → Modules de traitement → Base de données
                ↓
         Visualisations ← Analyses ← Données importées
                ↓
         Notifications → Email/Interface
```

### 1.3 Technologies Utilisées

- **Streamlit** : Framework web Python
- **SQLite** : Base de données relationnelle
- **Pandas** : Manipulation de données
- **Plotly** : Visualisations interactives
- **OpenAI API** : Intelligence artificielle
- **SMTP** : Envoi d'emails

---

## 2. MODULES ET FONCTIONS

### 2.1 app.py - Application Principale

#### Fonctions Principales

```python
def main()
    Point d'entrée de l'application

def main_app()
    Application principale après authentification

def login_page()
    Page de connexion/inscription

def show_home_page()
    Page d'accueil avec tableau de bord

def show_upload_page()
    Page d'import de données

def show_analysis_page()
    Page d'analyses statistiques

def show_visualizations_page()
    Page de visualisations

def show_projects_page()
    Page de gestion des projets

def show_settings_page()
    Page de paramètres

def apply_user_preferences()
    Application des préférences utilisateur au CSS
```

### 2.2 database.py - Gestion de la Base de Données

#### Classe Database

```python
class Database:
    def __init__(self)
        Initialise la connexion à la base de données
    
    def get_connection(self)
        Retourne une connexion à la base de données
    
    def hash_password(self, password)
        Hash un mot de passe avec SHA-256
    
    def create_user(self, email, password, ...)
        Crée un nouvel utilisateur
    
    def authenticate_user(self, email, password)
        Authentifie un utilisateur
    
    def get_user_profile(self, user_id)
        Récupère le profil d'un utilisateur
    
    def get_user_preferences(self, user_id)
        Récupère les préférences d'un utilisateur
    
    def update_user_preferences(self, user_id, **kwargs)
        Met à jour les préférences
    
    def save_project(self, user_id, project_name, ...)
        Sauvegarde un projet
    
    def load_project(self, user_id, project_name)
        Charge un projet sauvegardé
    
    def delete_project(self, user_id, project_id)
        Supprime un projet
```

### 2.3 statistical_analysis.py - Analyses Statistiques

#### Classe StatisticalAnalyzer

```python
class StatisticalAnalyzer:
    def __init__(self, df)
        Initialise l'analyzer avec un DataFrame
    
    def calculate_engagement_rate(self)
        Calcule le taux d'engagement
    
    def descriptive_stats(self, column)
        Statistiques descriptives
    
    def t_test(self, group1, group2)
        Test t de Student
    
    def anova_test(self, groups)
        Test ANOVA
    
    def chi_square_test(self, var1, var2)
        Test du Chi²
    
    def correlation_test(self, var1, var2)
        Test de corrélation
    
    def wilcoxon_test(self, group1, group2)
        Test de Wilcoxon
```

### 2.4 visualizations.py - Visualisations

#### Classe DataVisualizer

```python
class DataVisualizer:
    def __init__(self, df)
        Initialise le visualiseur
    
    def plot_engagement_comparison(self, group_by='platform')
        Graphique de comparaison d'engagement
    
    def plot_likes_distribution(self, group_by='platform')
        Distribution des likes
    
    def plot_correlation_heatmap(self)
        Heatmap de corrélation
    
    def plot_time_series(self, date_column, metric, ...)
        Graphique temporel
    
    def plot_scatter_with_regression(self, x_col, y_col, ...)
        Scatter plot avec régression
    
    def plot_metric_distribution_histogram(self, metric)
        Histogramme de distribution
```

### 2.5 ai_assistant.py - Assistant IA

#### Classe AIAssistant

```python
class AIAssistant:
    def __init__(self)
        Initialise l'assistant IA
    
    def interpret_results(self, results)
        Interprète les résultats d'analyse
    
    def generate_insights(self, df, analysis_type)
        Génère des insights
    
    def compare_platforms(self, platform_data)
        Compare les plateformes
```

### 2.6 notifications.py - Notifications

#### Classe NotificationManager

```python
class NotificationManager:
    def __init__(self, db, user_id)
        Initialise le gestionnaire
    
    def show_notification(self, title, message, ...)
        Affiche une notification
    
    def notify_data_imported(self, row_count, filename)
        Notification d'import
    
    def notify_project_saved(self, project_name)
        Notification de sauvegarde
    
    def check_and_notify_performance(self, df)
        Vérifie et notifie les performances
```

---

## 3. BASE DE DONNÉES

### 3.1 Schéma de la Base de Données

#### Table: users
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    company TEXT,
    phone TEXT,
    job_title TEXT,
    bio TEXT,
    is_premium BOOLEAN DEFAULT 0,
    premium_expires TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
)
```

#### Table: user_preferences
```sql
CREATE TABLE user_preferences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE NOT NULL,
    theme TEXT DEFAULT 'light',
    primary_color TEXT DEFAULT '#667eea',
    secondary_color TEXT DEFAULT '#764ba2',
    accent_color TEXT DEFAULT '#f093fb',
    text_color TEXT DEFAULT '#1f2937',
    background_color TEXT DEFAULT '#ffffff',
    font_family TEXT DEFAULT 'Arial',
    notifications_enabled BOOLEAN DEFAULT 1,
    email_notifications BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
```

#### Table: saved_projects
```sql
CREATE TABLE saved_projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    project_name TEXT NOT NULL,
    data_json TEXT NOT NULL,
    results_json TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
```

### 3.2 Relations

- `users` 1:1 `user_preferences`
- `users` 1:N `saved_projects`

---

## 4. APIs ET INTÉGRATIONS

### 4.1 OpenAI API

#### Configuration
```python
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
```

#### Utilisation
- Génération d'insights
- Interprétation des analyses
- Recommandations personnalisées

### 4.2 SMTP (Email)

#### Configuration
```python
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT'))
SMTP_USERNAME = os.getenv('SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
```

#### Utilisation
- Envoi de notifications par email
- Format HTML avec design personnalisé

### 4.3 Stripe (Paiements)

#### Configuration
```python
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
```

#### Utilisation
- Gestion des abonnements Premium
- Webhooks de paiement

---

## 5. CONFIGURATION

### 5.1 Variables d'Environnement (.env)

```env
# Clé secrète
SECRET_KEY=votre_cle_secrete

# OpenAI
OPENAI_API_KEY=votre_cle_api_openai

# Stripe
STRIPE_PUBLIC_KEY=votre_cle_publique
STRIPE_SECRET_KEY=votre_cle_secrete

# SMTP
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=votre.email@gmail.com
SMTP_PASSWORD=votre_mot_de_passe
FROM_EMAIL=votre.email@gmail.com

# Application
APP_NAME=Social Media Analytics Pro
```

### 5.2 Installation

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app.py
```

---

## 6. DÉPLOIEMENT

### 6.1 Prérequis

- Python 3.10+
- Toutes les dépendances installées
- Fichier .env configuré
- Base de données initialisée

### 6.2 Déploiement Local

```bash
streamlit run app.py
```

### 6.3 Déploiement Cloud (Streamlit Cloud)

1. Créer un compte sur share.streamlit.io
2. Connecter le dépôt GitHub
3. Configurer les variables d'environnement
4. Déployer

---

## 7. MAINTENANCE

### 7.1 Logs

Les erreurs sont loggées dans la console et peuvent être surveillées.

### 7.2 Sauvegarde

- Sauvegarder régulièrement `social_analytics.db`
- Sauvegarder le fichier `.env`

### 7.3 Mises à Jour

```bash
# Mettre à jour les dépendances
pip install --upgrade -r requirements.txt

# Vérifier les versions
pip list
```

---

*Documentation technique - Version 1.0*




