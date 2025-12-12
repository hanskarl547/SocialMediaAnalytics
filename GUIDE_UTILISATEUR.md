# GUIDE UTILISATEUR
## Social Media Analytics Pro

---

## TABLE DES MATIÈRES

1. [Introduction](#1-introduction)
2. [Installation](#2-installation)
3. [Premiers Pas](#3-premiers-pas)
4. [Fonctionnalités Principales](#4-fonctionnalités-principales)
5. [Guide Détaillé](#5-guide-détaillé)
6. [FAQ](#6-faq)

---

## 1. INTRODUCTION

Bienvenue dans **Social Media Analytics Pro**, une plateforme complète pour l'analyse des données des réseaux sociaux.

### 1.1 Qu'est-ce que Social Media Analytics Pro ?

Une application web qui vous permet de :
- 📊 Analyser vos performances sur les réseaux sociaux
- 📈 Visualiser vos données de manière interactive
- 🤖 Obtenir des insights grâce à l'intelligence artificielle
- 💾 Sauvegarder et gérer vos projets d'analyse
- 🎨 Personnaliser l'interface selon vos préférences

---

## 2. INSTALLATION

### 2.1 Prérequis

- Python 3.10 ou supérieur
- Navigateur web moderne (Chrome, Firefox, Edge)

### 2.2 Installation des Dépendances

```bash
pip install -r requirements.txt
```

### 2.3 Configuration

1. Copiez le fichier `.env.example` en `.env`
2. Remplissez les variables d'environnement nécessaires
3. (Optionnel) Configurez l'API OpenAI pour l'assistant IA
4. (Optionnel) Configurez SMTP pour les notifications par email

### 2.4 Lancement

```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur.

---

## 3. PREMIERS PAS

### 3.1 Créer un Compte

1. Sur la page d'accueil, cliquez sur "📝 Inscription"
2. Remplissez le formulaire :
   - Email (obligatoire)
   - Mot de passe (minimum 6 caractères)
   - Informations optionnelles (nom, prénom, entreprise, etc.)
3. Cliquez sur "📝 Créer mon compte"

### 3.2 Se Connecter

1. Entrez votre email et mot de passe
2. Cliquez sur "🔐 Se connecter"

### 3.3 Importer des Données

1. Allez dans "📤 Importer des données"
2. Cliquez sur "Parcourir les fichiers"
3. Sélectionnez un fichier CSV ou Excel
4. Vérifiez l'aperçu des données
5. Configurez les options de prétraitement si nécessaire
6. Cliquez sur "✅ Valider et utiliser ces données"

---

## 4. FONCTIONNALITÉS PRINCIPALES

### 4.1 Tableau de Bord

La page d'accueil affiche :
- 📊 Vue d'ensemble des performances
- 📈 Métriques clés (données, plateformes, interactions, engagement)
- 🎯 Insights rapides
- 📋 Statistiques détaillées

### 4.2 Analyses Statistiques

Accédez à "📊 Analyses statistiques" pour :
- Calculer des statistiques descriptives
- Effectuer des tests statistiques (t-test, ANOVA, Chi², etc.)
- Analyser les corrélations
- Comparer des groupes

### 4.3 Visualisations

Dans "📈 Visualisations", vous pouvez :
- Comparer les performances par catégorie
- Visualiser les distributions
- Analyser les corrélations
- Examiner les tendances temporelles

### 4.4 Assistant IA

L'assistant IA vous aide à :
- Interpréter vos analyses
- Obtenir des recommandations
- Comparer vos performances
- Identifier des opportunités d'amélioration

### 4.5 Gestion de Projets

Dans "💾 Mes projets" :
- Sauvegardez vos analyses
- Chargez des projets précédents
- Supprimez des projets

### 4.6 Paramètres

Personnalisez votre expérience :
- 🎨 Apparence (thème, couleurs, police)
- 🔔 Notifications
- 👤 Profil utilisateur

---

## 5. GUIDE DÉTAILLÉ

### 5.1 Import de Données

#### Formats Supportés
- CSV (.csv)
- Excel (.xls, .xlsx)

#### Colonnes Recommandées
- `platform` : Nom de la plateforme (TikTok, Instagram, etc.)
- `likes` : Nombre de likes
- `comments` : Nombre de commentaires
- `shares` : Nombre de partages
- `views` : Nombre de vues
- `followers` : Nombre d'abonnés
- `date` : Date du post
- `country` : Pays (pour les cartes géographiques)

#### Options de Prétraitement
- **Calculer l'engagement automatiquement** : Calcule `engagement_rate` à partir de likes, followers, etc.
- **Supprimer les lignes avec valeurs manquantes** : Nettoie les données

### 5.2 Analyses Statistiques

#### Statistiques Descriptives
1. Sélectionnez une métrique dans le menu déroulant
2. Consultez les métriques affichées :
   - Moyenne
   - Médiane
   - Minimum
   - Maximum

#### Tests Statistiques
1. Choisissez le type de test
2. Sélectionnez les variables à comparer
3. Cliquez sur "Lancer le test"
4. Consultez les résultats et l'interprétation

### 5.3 Visualisations

#### Comparaisons
- Sélectionnez une colonne catégorielle pour grouper
- Choisissez une métrique numérique à comparer
- Le graphique s'adapte automatiquement

#### Distributions
- Choisissez une métrique
- Visualisez l'histogramme et le box plot

#### Corrélations
- Consultez la heatmap de corrélation
- Créez des scatter plots avec régression

### 5.4 Sauvegarde de Projets

1. Allez dans "📊 Analyses statistiques"
2. Faites défiler jusqu'à "💾 Sauvegarder ce projet"
3. Entrez un nom descriptif
4. Cliquez sur "💾 Sauvegarder"

### 5.5 Personnalisation

#### Thème
- ☀️ Clair : Fond blanc, texte sombre
- 🌙 Sombre : Fond sombre, texte clair
- 🔄 Automatique : S'adapte au système

#### Couleurs
- Couleur principale
- Couleur secondaire
- Couleur d'accent
- Couleur du texte
- Couleur de fond

#### Police
Choisissez parmi :
- Arial
- Roboto
- Inter
- Open Sans
- Lato
- Montserrat
- Poppins
- Raleway

---

## 6. FAQ

### Q1 : Comment calculer l'engagement automatiquement ?

R : Cochez "Calculer le taux d'engagement automatiquement" lors de l'import. L'application calcule : `(likes + comments + shares) / followers * 100`

### Q2 : Puis-je importer plusieurs fichiers ?

R : Oui, mais chaque import remplace les données précédentes. Utilisez la sauvegarde de projets pour conserver plusieurs analyses.

### Q3 : Les notifications par email fonctionnent-elles ?

R : Oui, si vous configurez SMTP dans le fichier `.env`. Consultez `EMAIL_SETUP.md` pour les instructions.

### Q4 : Comment activer Premium ?

R : Allez dans "💎 Premium" et suivez les instructions. En mode démo, vous pouvez activer Premium gratuitement.

### Q5 : Puis-je exporter mes analyses ?

R : Actuellement, vous pouvez sauvegarder vos projets. L'export PDF/Excel est prévu dans une future version.

### Q6 : Quelle est la taille maximale de fichier ?

R : La limite recommandée est de 50MB. Pour de très gros fichiers, l'application peut être plus lente.

### Q7 : Les données sont-elles sécurisées ?

R : Oui, les mots de passe sont hashés, et chaque utilisateur ne peut accéder qu'à ses propres données.

---

## SUPPORT

Pour toute question ou problème :
- Consultez la documentation technique
- Vérifiez les fichiers de configuration
- Contactez le support si nécessaire

---

*Guide utilisateur - Version 1.0*




