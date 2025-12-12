# 📘 Guide d'Utilisation - Social Media Analytics Pro

## 🎯 Introduction

Bienvenue sur **Social Media Analytics Pro**, votre plateforme complète pour analyser et optimiser vos performances sur les réseaux sociaux !

Cette application vous permet de :
- 📊 Comparer l'engagement sur différentes plateformes
- 🧪 Réaliser des tests statistiques avancés
- 🤖 Obtenir des recommandations IA personnalisées
- 🔮 Prédire le nombre de likes de vos futurs posts
- 📈 Visualiser vos données de manière interactive

---

## 🚀 Démarrage Rapide (5 minutes)

### Étape 1 : Installer l'application

1. Ouvrez PowerShell ou l'Invite de commandes
2. Naviguez vers le dossier du projet :
   ```powershell
   cd C:\Users\HP\Desktop\SocialMediaAnalytics
   ```
3. Installez les dépendances :
   ```powershell
   pip install -r requirements.txt
   ```

### Étape 2 : Lancer l'application

```powershell
streamlit run app.py
```

Votre navigateur s'ouvrira automatiquement à l'adresse `http://localhost:8501`

### Étape 3 : Créer un compte

1. Cliquez sur l'onglet "📝 Inscription"
2. Entrez votre email et un mot de passe (minimum 6 caractères)
3. Cliquez sur "S'inscrire"
4. Revenez à l'onglet "🔐 Connexion" et connectez-vous

### Étape 4 : Importer vos données

1. Dans le menu latéral, cliquez sur "📤 Importer des données"
2. Uploadez votre fichier CSV ou Excel
3. Ou cliquez sur "📥 Charger des données d'exemple" pour tester

### Étape 5 : Lancer votre première analyse

1. Allez dans "📊 Analyses statistiques"
2. Choisissez un test (par exemple : Kruskal-Wallis)
3. Sélectionnez vos variables
4. Cliquez sur "Lancer le test"
5. Consultez les résultats !

---

## 📊 Module 1 : Import et Gestion des Données

### Format des Fichiers Supportés

- ✅ **CSV** : Séparateur virgule ou point-virgule
- ✅ **Excel (.xls)** : Format Excel classique
- ✅ **Excel (.xlsx)** : Format Excel moderne

### Structure Minimale Requise

Votre fichier doit contenir **au minimum** ces colonnes :

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| `platform` | Texte | Nom de la plateforme | TikTok, Instagram, Facebook |
| `likes` | Nombre | Nombre de likes | 1250 |
| `followers` | Nombre | Nombre de followers | 15000 |

### Colonnes Recommandées

Pour des analyses plus riches, ajoutez :

| Colonne | Type | Description |
|---------|------|-------------|
| `views` | Nombre | Nombre de vues |
| `comments` | Nombre | Nombre de commentaires |
| `shares` | Nombre | Nombre de partages |
| `saves` | Nombre | Nombre de sauvegardes |
| `date` | Date | Date de publication (YYYY-MM-DD) |
| `hour` | Nombre | Heure de publication (0-23) |
| `post_type` | Texte | Type de contenu (video, photo, reel, etc.) |

### Exemple de Fichier CSV Valide

```csv
platform,likes,followers,views,comments,shares
TikTok,1250,15000,45000,87,23
Instagram,890,12000,8500,45,12
Facebook,450,8000,5000,32,8
TikTok,3200,15000,95000,156,67
Instagram,1100,12000,12000,78,18
```

### Options de Prétraitement

Lors de l'import, vous pouvez :

1. **Calculer le taux d'engagement automatiquement**
   - Formule : (Likes + Comments + Shares) / Followers × 100
   - Recommandé : ✅ Oui

2. **Supprimer les lignes avec valeurs manquantes**
   - Nettoie les données incomplètes
   - Recommandé : ⚠️ Non (sauf si beaucoup de données manquantes)

---

## 🧪 Module 2 : Analyses Statistiques

### Test 1 : Kruskal-Wallis

**📌 Quand l'utiliser ?**
- Vous voulez comparer **3 plateformes ou plus** sur une métrique
- Par exemple : "Y a-t-il une différence d'engagement entre TikTok, Instagram et Facebook ?"

**🔧 Comment l'utiliser ?**
1. Allez dans "📊 Analyses statistiques" > Onglet "Kruskal-Wallis"
2. **Métrique à comparer** : Choisissez ce que vous voulez analyser (ex: `likes`, `engagement_rate`)
3. **Grouper par** : Choisissez `platform`
4. Cliquez sur "Lancer le test Kruskal-Wallis"

**📖 Interpréter les résultats**

- **P-value < 0.05** ✅ → **Différence significative** entre les plateformes
  - Exemple : "TikTok performe significativement mieux qu'Instagram"
  
- **P-value ≥ 0.05** ℹ️ → **Pas de différence significative**
  - Exemple : "Toutes les plateformes ont des performances similaires"

**💡 Cas d'usage réel**

Un influenceur a ces moyennes de likes :
- TikTok : 3000 likes
- Instagram : 1200 likes  
- Facebook : 600 likes

Le test Kruskal-Wallis avec **p = 0.003** confirme que ces différences ne sont pas dues au hasard. 
👉 **Action** : Concentrer les efforts sur TikTok !

---

### Test 2 : Corrélation de Spearman

**📌 Quand l'utiliser ?**
- Vous voulez savoir si **2 variables sont liées**
- Par exemple : "Plus j'ai de followers, plus j'ai de likes ?"

**🔧 Comment l'utiliser ?**
1. Allez dans l'onglet "Spearman"
2. **Variable 1** : Ex: `followers`
3. **Variable 2** : Ex: `likes`
4. Cliquez sur "Calculer la corrélation"

**📖 Interpréter les résultats**

Le coefficient **ρ (rho)** varie de -1 à +1 :

| Valeur de ρ | Force | Interprétation |
|-------------|-------|----------------|
| 0.7 à 1.0 | Forte positive | Plus X augmente, plus Y augmente fortement |
| 0.3 à 0.7 | Modérée positive | Relation positive mais pas systématique |
| -0.3 à 0.3 | Faible | Peu ou pas de relation |
| -0.7 à -0.3 | Modérée négative | Plus X augmente, plus Y diminue |
| -1.0 à -0.7 | Forte négative | Relation négative forte |

**P-value** :
- < 0.05 : La corrélation est **statistiquement significative**
- ≥ 0.05 : La corrélation pourrait être due au hasard

**💡 Exemple**

Corrélation entre `followers` et `likes` : **ρ = 0.85**, **p = 0.001**

👉 **Interprétation** : Forte corrélation positive et significative.
Plus vous avez de followers, plus vous obtenez de likes.

---

### Test 3 : Chi-carré (χ²)

**📌 Quand l'utiliser ?**
- Vous voulez tester l'indépendance entre **2 variables catégorielles**
- Par exemple : "Le type de contenu (video/photo) est-il lié à la plateforme ?"

**🔧 Comment l'utiliser ?**
1. Allez dans l'onglet "Chi-carré"
2. **Variable 1** : Ex: `platform`
3. **Variable 2** : Ex: `post_type`
4. Cliquez sur "Lancer le test Chi-carré"

**📖 Interpréter les résultats**

- **P-value < 0.05** : Les variables sont **dépendantes** (liées)
- **P-value ≥ 0.05** : Les variables sont **indépendantes** (pas de lien)

**💡 Exemple**

Test entre `platform` et `post_type` : **p = 0.012**

👉 **Interprétation** : Certaines plateformes favorisent certains types de contenu.
Par exemple : TikTok = vidéos courtes, Instagram = photos + reels.

---

### Test 4 : Wilcoxon

**📌 Quand l'utiliser ?**
- Comparer **2 échantillons appariés**
- Par exemple : "Mes likes ont-ils augmenté après avoir changé de stratégie ?"

**🔧 Comment l'utiliser ?**
1. Vos données doivent avoir 2 colonnes comparables (ex: `likes_avant`, `likes_apres`)
2. Allez dans l'onglet "Wilcoxon"
3. Sélectionnez les 2 colonnes
4. Cliquez sur "Lancer le test Wilcoxon"

**📖 Interpréter les résultats**

- **P-value < 0.05** : **Différence significative** entre les deux périodes
- **P-value ≥ 0.05** : Pas de différence significative

---

## 🤖 Module 3 : Assistant IA

### Fonctionnalités de l'Assistant

L'assistant IA vous aide à :

1. **Interpréter automatiquement** tous vos tests statistiques
2. **Obtenir des recommandations** personnalisées par plateforme
3. **Comprendre les métriques** en langage simple

### Mode Gratuit vs Premium

| Fonctionnalité | Gratuit | Premium |
|----------------|---------|---------|
| Interprétation des tests | ✅ Basique (3-4 phrases) | ✅ Détaillée (10-15 phrases) |
| Recommandations | ✅ Génériques | ✅ Personnalisées et stratégiques |
| Explication des métriques | ✅ Définition simple | ✅ Explication complète + exemples |
| Insights actionnables | ❌ | ✅ Oui |

### Comment utiliser l'Assistant

1. **D'abord, lancez des analyses** dans la section "📊 Analyses statistiques"
2. Allez dans "🤖 Assistant IA"
3. L'assistant génère automatiquement une interprétation globale
4. Consultez les **recommandations par plateforme** dans les sections déroulantes
5. Cliquez sur **"Guide des métriques"** pour des explications détaillées

### Exemple d'Interprétation Premium

```
📊 Analyse approfondie de vos performances :

Le test de Kruskal-Wallis révèle une différence significative d'engagement 
entre vos plateformes (p = 0.003). TikTok domine avec un taux d'engagement 
moyen de 6.2%, suivi d'Instagram (4.5%) et Facebook (2.1%).

La corrélation de Spearman montre une relation forte entre le nombre de vues 
et les likes (ρ = 0.87), suggérant que la visibilité est le principal moteur 
de l'engagement.

💡 Recommandations stratégiques :

1. TikTok : Maximisez votre ROI en doublant la fréquence de publication. 
   L'algorithme favorise les créateurs actifs.

2. Instagram : Testez les Reels aux heures de pointe (19h-21h) pour 
   augmenter la visibilité organique.

3. Facebook : Considérez une réduction des efforts ou un pivotement vers 
   du contenu vidéo natif, plus performant sur cette plateforme.
```

---

## 📈 Module 4 : Visualisations

### Types de Graphiques Disponibles

#### 1. Comparaison d'Engagement (Barres)

**📍 Où le trouver ?** Visualisations > Onglet "📊 Comparaisons"

**💡 Utilisation :**
- Compare le taux d'engagement moyen par plateforme
- Les barres d'erreur montrent la variabilité

**🎯 Insight :** Identifiez rapidement quelle plateforme performe le mieux.

---

#### 2. Distribution des Likes (Histogramme + Box Plot)

**📍 Où le trouver ?** Visualisations > Onglet "📈 Distributions"

**💡 Utilisation :**
- **Histogramme** : Montre la répartition des valeurs
- **Box Plot** : Identifie les valeurs extrêmes (outliers)

**🎯 Insight :** Détectez les posts exceptionnels et comprenez la distribution normale.

---

#### 3. Heatmap de Corrélation

**📍 Où le trouver ?** Visualisations > Onglet "🔗 Corrélations"

**💡 Utilisation :**
- Visualise toutes les corrélations entre métriques numériques
- Rouge = corrélation positive, Bleu = corrélation négative

**🎯 Insight :** Découvrez des relations cachées entre vos métriques.

---

#### 4. Nuage de Points avec Régression

**📍 Où le trouver ?** Visualisations > Onglet "🔗 Corrélations"

**💡 Utilisation :**
- Choisissez 2 variables (ex: followers vs likes)
- La ligne de tendance montre la relation

**🎯 Insight :** Visualisez si la relation est linéaire ou non.

---

#### 5. Graphique Radar Multi-Métriques

**📍 Où le trouver ?** Visualisations > Onglet "📊 Comparaisons"

**💡 Utilisation :**
- Compare plusieurs métriques simultanément pour chaque plateforme
- Forme un "polygone" pour chaque plateforme

**🎯 Insight :** Vue d'ensemble pour identifier les forces/faiblesses de chaque plateforme.

---

#### 6. Séries Temporelles

**📍 Où le trouver ?** Visualisations > Onglet "⏱️ Temporel"

**💡 Utilisation :**
- Nécessite une colonne `date` dans vos données
- Montre l'évolution d'une métrique dans le temps

**🎯 Insight :** Identifiez les tendances, saisonnalités, et pics d'activité.

---

### Interactivité des Graphiques

Tous les graphiques sont **interactifs** grâce à Plotly :

- 🔍 **Zoom** : Cliquez-glissez sur une zone
- 👁️ **Survol** : Affichez les valeurs exactes
- 📷 **Export** : Bouton de téléchargement en haut à droite
- 🎨 **Légende** : Cliquez pour masquer/afficher une série

---

## 🔮 Module 5 : Prédictions de Likes

### Qu'est-ce que la Prédiction ?

Le module de prédiction utilise le **Machine Learning** pour prédire le nombre de likes 
qu'un post pourrait obtenir basé sur d'autres variables (followers, views, etc.).

### Étape 1 : Entraîner un Modèle

1. Allez dans "🔮 Prédictions"
2. **Sélectionnez les variables prédictives** (ex: followers, views, comments)
3. **Choisissez le type de modèle** :
   - **Régression Linéaire** (Gratuit) : Simple et rapide
   - **Random Forest** (Premium) : Plus précis pour relations complexes
4. Cliquez sur "🚀 Entraîner le modèle"

### Étape 2 : Évaluer la Qualité du Modèle

Après l'entraînement, consultez :

#### R² Score (Coefficient de détermination)
- **> 0.7** : ✅ **Excellent** - Le modèle prédit très bien
- **0.5 - 0.7** : ✅ **Bon** - Prédictions fiables
- **0.3 - 0.5** : ⚠️ **Modéré** - Utilisable mais imparfait
- **< 0.3** : ❌ **Faible** - Trop d'incertitude

#### RMSE (Root Mean Squared Error)
- Erreur moyenne de prédiction
- **Plus c'est bas, mieux c'est**
- Exemple : RMSE = 200 → En moyenne, le modèle se trompe de ±200 likes

### Étape 3 : Faire une Prédiction

Une fois le modèle entraîné :

1. Entrez les valeurs des variables (ex: 15000 followers, 50000 views)
2. Cliquez sur "🔮 Prédire"
3. Le système affiche le nombre de likes prédit

**💡 Exemple pratique**

Vous planifiez un post TikTok :
- Vous avez **20 000 followers**
- Vous estimez **80 000 vues**
- Vous prévoyez **150 commentaires**

Le modèle prédit : **~3 200 likes** ✨

👉 Vous pouvez maintenant ajuster votre stratégie pour atteindre cet objectif !

---

## 💾 Module 6 : Sauvegarde des Projets

### Pourquoi sauvegarder ?

- 💾 **Conservez vos analyses** pour y revenir plus tard
- 📊 **Comparez** vos performances sur différentes périodes
- 🔄 **Reprenez** votre travail là où vous l'aviez laissé

### Comment sauvegarder ?

1. Après avoir importé vos données, scrollez en bas de la page "📤 Importer des données"
2. Entrez un **nom de projet** (ex: "Janvier 2024")
3. Cliquez sur "💾 Sauvegarder le projet"

### Comment charger un projet sauvegardé ?

1. Allez dans "💾 Mes projets"
2. Cliquez sur "📂 Charger" à côté du projet souhaité
3. Vos données sont restaurées !

---

## 💎 Passer en Premium

### Pourquoi Premium ?

| Vous êtes... | Premium est fait pour vous si... |
|--------------|----------------------------------|
| 🎥 **Créateur de contenu** | Vous voulez maximiser votre engagement avec des insights IA |
| 💼 **Social Media Manager** | Vous gérez plusieurs comptes et besoin d'analyses approfondies |
| 🏢 **Agence** | Vous fournissez des rapports clients avec recommandations |
| 📊 **Data Analyst** | Vous avez besoin de modèles ML avancés (Random Forest) |

### Prix : 5€/mois

**Ce que vous débloquez :**

✅ Assistant IA avec GPT (interprétations détaillées)
✅ Modèles de prédiction Random Forest
✅ Recommandations stratégiques personnalisées
✅ Analyses comparatives avancées
✅ Exports illimités de rapports
✅ Support prioritaire

### Comment souscrire ?

1. Connectez-vous à votre compte
2. Allez dans "💎 Premium" (menu latéral)
3. Cliquez sur "🚀 Souscrire maintenant"
4. **Mode démo** : Cliquez sur "✨ Activer Premium (DEMO)"
5. **Mode production** : Vous serez redirigé vers Stripe pour le paiement

---

## 🛠️ Dépannage

### Problème : L'application ne démarre pas

**Solution 1 : Vérifier Python**
```powershell
python --version
```
Doit afficher Python 3.8 ou supérieur.

**Solution 2 : Réinstaller les dépendances**
```powershell
pip install --upgrade -r requirements.txt
```

---

### Problème : "Module not found: streamlit"

**Solution :**
```powershell
pip install streamlit pandas numpy plotly scipy scikit-learn
```

---

### Problème : Les données ne s'affichent pas

**Vérifications :**
1. ✅ Votre fichier contient-il les colonnes `platform`, `likes`, `followers` ?
2. ✅ Avez-vous cliqué sur "✅ Valider et utiliser ces données" ?
3. ✅ Essayez avec les données d'exemple : "📥 Charger des données d'exemple"

---

### Problème : L'assistant IA ne fonctionne pas

**Cause :** Pas de clé OpenAI configurée

**Solution :** L'app fonctionne en **mode dégradé** avec des interprétations préprogrammées.

Pour activer l'IA complète :
1. Créez un compte sur https://platform.openai.com
2. Générez une clé API
3. Copiez `.env.example` en `.env`
4. Ajoutez votre clé : `OPENAI_API_KEY=sk-...`

---

### Problème : La base de données ne se crée pas

**Solution :**
1. Vérifiez les permissions du dossier
2. Supprimez le fichier `social_analytics.db` s'il existe
3. Relancez l'application

---

## 📞 Besoin d'Aide ?

### Support Communautaire

- 💬 **Forum** : [Lien vers forum]
- 📧 **Email** : support@exemple.com
- 📚 **Documentation complète** : Consultez le README.md

### FAQ Rapide

**Q : Puis-je utiliser l'app hors ligne ?**
R : Oui, sauf l'assistant IA qui nécessite une connexion pour GPT.

**Q : Mes données sont-elles sécurisées ?**
R : Oui, tout est stocké localement sur votre machine (base SQLite).

**Q : Combien de données puis-je importer ?**
R : Pas de limite, mais au-delà de 10 000 lignes, les calculs peuvent être plus lents.

**Q : Puis-je exporter mes graphiques ?**
R : Oui, survolez un graphique et cliquez sur l'icône de téléchargement.

---

## 🎓 Cas d'Usage Avancés

### Cas 1 : Optimiser les Heures de Publication

**Objectif :** Trouver la meilleure heure pour poster

**Méthode :**
1. Assurez-vous d'avoir une colonne `hour` (0-23)
2. Allez dans Visualisations > Temporel
3. Sélectionnez `hour` comme axe X, `engagement_rate` comme métrique
4. Identifiez les pics d'engagement

**Action :** Publiez vos posts importants aux heures de pic !

---

### Cas 2 : Comparer Plusieurs Périodes

**Objectif :** "Mes performances ont-elles augmenté ce mois-ci ?"

**Méthode :**
1. Créez 2 colonnes dans vos données : `likes_janvier`, `likes_fevrier`
2. Utilisez le test de Wilcoxon
3. Si p < 0.05 → Amélioration significative !

---

### Cas 3 : Identifier Votre Meilleur Type de Contenu

**Objectif :** "Vidéos ou photos ?"

**Méthode :**
1. Assurez-vous d'avoir une colonne `post_type`
2. Utilisez Kruskal-Wallis : métrique = `likes`, grouper par = `post_type`
3. Consultez aussi les visualisations pour voir la distribution

---

## 📚 Glossaire des Métriques

| Métrique | Définition | Formule | Bon score |
|----------|-----------|---------|-----------|
| **Engagement Rate** | % d'audience qui interagit | (Likes+Comments+Shares)/Followers×100 | > 3% |
| **Reach** | Nombre de personnes uniques touchées | - | Variable |
| **Impressions** | Nombre total d'affichages | - | 2-3× le reach |
| **CTR** | Taux de clic | Clics / Impressions × 100 | > 2% |
| **Saves** | Nombre de sauvegardes (Instagram) | - | Haut = contenu de qualité |

---

## 🎉 Conseils de Pro

1. **📅 Importez régulièrement** vos données pour suivre l'évolution
2. **🔄 Comparez période par période** pour mesurer vos progrès
3. **🎯 Utilisez les prédictions** pour fixer des objectifs réalistes
4. **📊 Créez des rapports visuels** avec les graphiques pour vos clients/équipe
5. **🤖 Consultez l'IA** pour des recommandations actionnables
6. **💾 Sauvegardez** vos analyses importantes
7. **📈 Testez, analysez, optimisez** : c'est un cycle continu !

---

**Bonne analyse ! 🚀📊**

Pour toute question, consultez le README.md ou contactez le support.

---

*Développé avec ❤️ pour optimiser vos réseaux sociaux*

