# 📊 Social Media Analytics Pro

Une plateforme web complète d'analyse des réseaux sociaux avec intelligence artificielle, développée en Python avec Streamlit.

## 🚀 Fonctionnalités

### 🆓 Version Gratuite
- ✅ Authentification sécurisée (email + mot de passe)
- ✅ Import de données (CSV, XLS, XLSX)
- ✅ Statistiques descriptives
- ✅ Tests statistiques de base (Kruskal-Wallis, Spearman, Chi-carré, Wilcoxon)
- ✅ Visualisations interactives
- ✅ Comparaison des plateformes (TikTok, Instagram, Facebook, etc.)
- ✅ Sauvegarde gratuite des projets
- ✅ Interprétations basiques des résultats

### 💎 Version Premium (5€/mois)
- ✨ Tout de la version gratuite +
- ✨ Assistant IA détaillé avec GPT
- ✨ Recommandations personnalisées par plateforme
- ✨ Prédictions avancées avec Machine Learning (Random Forest)
- ✨ Analyses comparatives approfondies
- ✨ Interprétations expertes des tests statistiques
- ✨ Support prioritaire
- ✨ Exports illimités

## 📋 Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

## 🔧 Installation

### 1. Cloner ou télécharger le projet

```bash
cd SocialMediaAnalytics
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Configuration (optionnel)

Copiez le fichier `.env.example` en `.env` et remplissez vos clés API :

```bash
copy .env.example .env
```

Éditez le fichier `.env` avec vos clés :

```
# Clé secrète pour l'application
SECRET_KEY=votre_cle_secrete_unique

# Configuration OpenAI (optionnel, pour l'assistant IA avancé)
OPENAI_API_KEY=sk-...

# Configuration Stripe (pour les paiements réels)
STRIPE_PUBLIC_KEY=pk_...
STRIPE_SECRET_KEY=sk_...
STRIPE_WEBHOOK_SECRET=whsec_...
```

**Note:** L'application fonctionne sans ces clés avec un mode dégradé.

## 🎮 Lancement de l'application

```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse : `http://localhost:8501`

## 📊 Format des données

Votre fichier de données doit contenir les colonnes suivantes (minimum) :

| Colonne | Description | Obligatoire |
|---------|-------------|-------------|
| platform | Nom de la plateforme (TikTok, Instagram, etc.) | ✅ Oui |
| likes | Nombre de likes | ✅ Oui |
| followers | Nombre de followers | Recommandé |
| views | Nombre de vues | Recommandé |

**Colonnes optionnelles :**
- `comments` : Nombre de commentaires
- `shares` : Nombre de partages
- `saves` : Nombre de sauvegardes
- `date` : Date de publication
- `hour` : Heure de publication
- `post_type` : Type de contenu
- etc.

### Exemple de fichier CSV :

```csv
platform,likes,followers,views,comments,shares
TikTok,1250,15000,45000,87,23
Instagram,890,12000,8500,45,12
Facebook,450,8000,5000,32,8
TikTok,3200,15000,95000,156,67
Instagram,1100,12000,12000,78,18
```

## 🧪 Tests Statistiques Disponibles

### 1. Test de Kruskal-Wallis
- **Utilisation** : Comparer 3+ groupes sur une métrique
- **Exemple** : Comparer l'engagement entre TikTok, Instagram et Facebook
- **Interprétation** : p < 0.05 = différence significative entre les groupes

### 2. Corrélation de Spearman
- **Utilisation** : Mesurer la relation entre deux variables
- **Exemple** : Relation entre nombre de followers et likes
- **Interprétation** : 
  - ρ > 0.7 : corrélation forte
  - 0.3 < ρ < 0.7 : corrélation modérée
  - ρ < 0.3 : corrélation faible

### 3. Test du Chi-carré
- **Utilisation** : Tester l'indépendance entre variables catégorielles
- **Exemple** : Association entre plateforme et type de contenu
- **Interprétation** : p < 0.05 = les variables sont liées

### 4. Test de Wilcoxon
- **Utilisation** : Comparer deux échantillons appariés
- **Exemple** : Comparer les performances avant/après une stratégie
- **Interprétation** : p < 0.05 = différence significative

## 🤖 Assistant IA

L'assistant IA utilise OpenAI GPT pour :

1. **Interpréter automatiquement** les résultats des tests statistiques
2. **Générer des recommandations** personnalisées par plateforme
3. **Expliquer les métriques** en langage simple
4. **Fournir des insights actionnables** pour améliorer l'engagement

**Mode gratuit** : Interprétations courtes et basiques
**Mode premium** : Analyses détaillées avec recommandations stratégiques

## 🔮 Prédictions de Likes

Utilisez le Machine Learning pour prédire le nombre de likes :

### Modèles disponibles :
- **Régression Linéaire** (Gratuit) : Rapide et simple
- **Random Forest** (Premium) : Plus précis, gère mieux les relations complexes

### Métriques de qualité :
- **R² Score** : 
  - > 0.7 = Excellent
  - 0.5 - 0.7 = Bon
  - 0.3 - 0.5 = Modéré
  - < 0.3 = Faible
- **RMSE** : Erreur moyenne de prédiction

## 📈 Visualisations

### Types de graphiques :
1. **Comparaison d'engagement** : Barres avec moyennes par plateforme
2. **Distributions** : Histogrammes et box plots
3. **Corrélations** : Heatmap et nuages de points
4. **Évolution temporelle** : Séries chronologiques
5. **Graphique radar** : Comparaison multi-métriques
6. **Top performers** : Classement des meilleurs posts

Tous les graphiques sont **interactifs** (zoom, survol, export).

## 💳 Système de Paiement Premium

### En mode démo :
- Bouton de test pour activer Premium instantanément
- Pas de vraie transaction

### En mode production :
1. Créer un compte Stripe : https://stripe.com
2. Obtenir vos clés API
3. Configurer le webhook
4. Ajouter les clés dans `.env`

Le paiement sera automatiquement traité et le compte Premium activé.

## 💾 Sauvegarde des Projets

- **Gratuit** : Sauvegarde illimitée de vos analyses
- Les projets incluent :
  - Données importées
  - Résultats des tests
  - Configuration des analyses
- Chargez vos anciens projets à tout moment

## 🏗️ Architecture du Projet

```
SocialMediaAnalytics/
│
├── app.py                    # Application principale Streamlit
├── database.py              # Gestion BDD (utilisateurs, paiements, projets)
├── statistical_analysis.py  # Tests statistiques et prédictions
├── ai_assistant.py          # Assistant IA et interprétations
├── visualizations.py        # Graphiques et visualisations
│
├── requirements.txt         # Dépendances Python
├── .env.example            # Template de configuration
├── README.md               # Ce fichier
│
└── social_analytics.db     # Base de données SQLite (créée auto)
```

## 🔐 Sécurité

- Mots de passe hashés avec SHA-256
- Session utilisateur sécurisée avec Streamlit
- Base de données SQLite locale
- Validation des entrées utilisateur

## 🛠️ Technologies Utilisées

- **Frontend** : Streamlit
- **Backend** : Python 3.8+
- **Base de données** : SQLite + SQLAlchemy
- **Analyses** : Pandas, NumPy, SciPy, Statsmodels
- **Machine Learning** : Scikit-learn
- **Visualisations** : Plotly, Seaborn, Matplotlib
- **IA** : OpenAI GPT-3.5
- **Paiements** : Stripe
- **Authentification** : bcrypt, hashlib

## 📝 Guide d'Utilisation Rapide

### 1. Première connexion
- Créez un compte avec votre email
- Connectez-vous avec vos identifiants

### 2. Importer des données
- Allez dans "📤 Importer des données"
- Uploadez votre fichier CSV/Excel
- Prévisualisez et validez

### 3. Lancer des analyses
- Allez dans "📊 Analyses statistiques"
- Choisissez vos tests (Kruskal-Wallis, Spearman, etc.)
- Consultez les résultats

### 4. Consulter l'assistant IA
- Allez dans "🤖 Assistant IA"
- Obtenez des interprétations automatiques
- Consultez les recommandations par plateforme

### 5. Créer des visualisations
- Allez dans "📈 Visualisations"
- Explorez les différents graphiques
- Interagissez avec les visualisations

### 6. Faire des prédictions
- Allez dans "🔮 Prédictions"
- Entraînez un modèle
- Prédisez le nombre de likes

### 7. Sauvegarder votre travail
- Nommez votre projet
- Cliquez sur "💾 Sauvegarder"
- Retrouvez-le dans "💾 Mes projets"

## 🎯 Cas d'Usage

### 1. Influenceur/Créateur de contenu
- Comparez vos performances sur différentes plateformes
- Identifiez les meilleurs moments pour poster
- Prédisez l'engagement de futurs posts

### 2. Social Media Manager
- Analysez les campagnes multi-plateformes
- Générez des rapports automatisés
- Optimisez votre stratégie de contenu

### 3. Agence Marketing
- Comparez plusieurs clients
- Identifiez les tendances
- Fournissez des insights data-driven

### 4. Chercheur/Étudiant
- Analysez des données de réseaux sociaux
- Réalisez des tests statistiques
- Créez des visualisations académiques

## 🆘 Dépannage

### L'application ne démarre pas
```bash
# Vérifier la version de Python
python --version  # Doit être 3.8+

# Réinstaller les dépendances
pip install --upgrade -r requirements.txt
```

### Erreur "Module not found"
```bash
pip install streamlit pandas numpy plotly
```

### La base de données ne se crée pas
- Vérifiez les permissions du dossier
- Supprimez `social_analytics.db` et relancez

### L'assistant IA ne fonctionne pas
- Vérifiez votre clé OpenAI dans `.env`
- L'app fonctionne en mode dégradé sans clé

## 📞 Support

Pour toute question ou problème :
- 📧 Email : support@socialmedialytics.com (exemple)
- 💬 GitHub Issues : [Lien vers repo]
- 📚 Documentation : [Lien vers docs]

## 🔄 Mises à jour futures

- [ ] Export PDF des rapports
- [ ] Comparaison avec benchmarks du secteur
- [ ] Planification de contenu
- [ ] Intégration API directe (TikTok, Instagram)
- [ ] Dashboard multi-utilisateurs
- [ ] Analyse de sentiment
- [ ] Détection de hashtags performants

## 📄 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, le modifier et le distribuer.

## 👨‍💻 Auteur

Développé avec ❤️ pour Christ

---

**Bon courage avec vos analyses ! 🚀📊**

