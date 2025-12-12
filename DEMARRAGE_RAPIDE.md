# ⚡ Démarrage Rapide - 5 Minutes

## 🎯 Objectif
Avoir votre plateforme d'analyse fonctionnelle en **moins de 5 minutes** !

---

## 📋 Étape 1 : Installation (2 minutes)

### Windows

1. **Ouvrez PowerShell** (Clic droit sur le menu Démarrer > Windows PowerShell)

2. **Naviguez vers le dossier du projet :**
   ```powershell
   cd C:\Users\HP\Desktop\SocialMediaAnalytics
   ```

3. **Lancez l'installation automatique :**
   ```powershell
   .\install.bat
   ```
   
   ⏳ Attendez que l'installation se termine (1-2 minutes)

### Alternative manuelle

Si le script ne fonctionne pas :

```powershell
# Vérifier Python
python --version

# Installer les dépendances
pip install streamlit pandas numpy scikit-learn plotly scipy statsmodels openpyxl
```

---

## 🚀 Étape 2 : Lancement (30 secondes)

### Méthode 1 : Script automatique

Double-cliquez sur `start.bat`

### Méthode 2 : Ligne de commande

```powershell
streamlit run app.py
```

✅ **L'application s'ouvre automatiquement dans votre navigateur !**

URL : http://localhost:8501

---

## 👤 Étape 3 : Créer un compte (1 minute)

1. Sur la page d'accueil, cliquez sur l'onglet **"📝 Inscription"**

2. Entrez :
   - **Email** : votre-email@exemple.com
   - **Mot de passe** : minimum 6 caractères
   - **Confirmer** : même mot de passe

3. Cliquez sur **"S'inscrire"**

4. Revenez à l'onglet **"🔐 Connexion"** et connectez-vous

---

## 📊 Étape 4 : Tester avec des données (1 minute)

### Option A : Charger l'exemple

1. Cliquez sur **"📤 Importer des données"** (menu latéral)

2. Faites défiler vers le bas

3. Cliquez sur **"📥 Charger des données d'exemple"**

✅ Vous avez maintenant 64 posts de différentes plateformes !

### Option B : Importer vos données

1. Préparez un fichier CSV avec ces colonnes :
   ```csv
   platform,likes,followers,views
   TikTok,1250,15000,45000
   Instagram,890,12000,8500
   ```

2. Cliquez sur **"Choisissez un fichier CSV, XLS ou XLSX"**

3. Sélectionnez votre fichier

4. Cliquez sur **"✅ Valider et utiliser ces données"**

---

## 🧪 Étape 5 : Première analyse (30 secondes)

1. Allez dans **"📊 Analyses statistiques"**

2. Cliquez sur l'onglet **"Kruskal-Wallis"**

3. Sélectionnez :
   - **Métrique à comparer** : `engagement_rate`
   - **Grouper par** : `platform`

4. Cliquez sur **"Lancer le test Kruskal-Wallis"**

🎉 **Vous avez votre première analyse statistique !**

---

## 📈 Étape 6 : Visualiser (30 secondes)

1. Allez dans **"📈 Visualisations"**

2. Le premier graphique s'affiche automatiquement !

3. **Interagissez** :
   - Survolez pour voir les valeurs
   - Zoom avec la souris
   - Export en cliquant sur l'icône photo

---

## 🎉 Félicitations !

Vous avez maintenant une plateforme d'analyse fonctionnelle !

### 🎯 Prochaines Étapes

1. **Explorez les autres tests** (Spearman, Chi-carré, Wilcoxon)
2. **Consultez l'Assistant IA** (🤖 Assistant IA)
3. **Faites des prédictions** (🔮 Prédictions)
4. **Sauvegardez votre travail** (💾 Mes projets)

---

## 🆘 Problèmes Courants

### ❌ "Python n'est pas reconnu"

**Solution :**
1. Installez Python depuis https://www.python.org/downloads/
2. ⚠️ **Cochez "Add Python to PATH"** pendant l'installation
3. Redémarrez votre ordinateur
4. Relancez l'installation

---

### ❌ "pip n'est pas reconnu"

**Solution :**
```powershell
python -m pip install --upgrade pip
```

---

### ❌ L'application ne s'ouvre pas dans le navigateur

**Solution :**
Ouvrez manuellement : http://localhost:8501

---

### ❌ Erreur "Port already in use"

**Solution :**
```powershell
streamlit run app.py --server.port=8502
```

---

### ❌ Les graphiques ne s'affichent pas

**Solution :**
```powershell
pip install --upgrade plotly
```
Puis redémarrez l'application.

---

## 💎 Mode Premium (Optionnel)

Pour tester les fonctionnalités Premium :

1. Connectez-vous à votre compte
2. Allez dans **"💎 Premium"**
3. Cliquez sur **"✨ Activer Premium (DEMO)"**
4. Rechargez la page

✨ Vous avez maintenant accès à :
- Assistant IA détaillé
- Prédictions Random Forest
- Recommandations personnalisées

---

## 📚 Documentation Complète

Pour aller plus loin :

- **README.md** : Vue d'ensemble complète
- **GUIDE_UTILISATION.md** : Guide détaillé de chaque fonction
- **CONFIGURATION.md** : Configuration avancée (OpenAI, Stripe)
- **PRESENTATION.md** : Architecture et fonctionnalités techniques

---

## 💬 Support

**Besoin d'aide ?**

1. Consultez la section "🆘 Problèmes Courants" ci-dessus
2. Lisez le GUIDE_UTILISATION.md
3. Contactez le support

---

## 🎓 Tutoriel Vidéo (Suggestion)

Vous pourriez créer un tutoriel vidéo de 5 minutes montrant :

1. Installation (1 min)
2. Création de compte (30s)
3. Import de données (1 min)
4. Première analyse (1 min)
5. Visualisations (1 min)
6. Prédictions (30s)

**Format recommandé :**
- Screencast avec voix off
- Sous-titres en français
- Publier sur YouTube

---

## ⚡ Checklist de Démarrage

- [ ] Python 3.8+ installé
- [ ] Dépendances installées (`install.bat`)
- [ ] Application lancée (`start.bat` ou `streamlit run app.py`)
- [ ] Compte créé
- [ ] Données importées (exemple ou personnelles)
- [ ] Première analyse réalisée
- [ ] Graphiques consultés
- [ ] (Optionnel) Premium activé en mode démo

---

## 🎁 Bonus : Raccourci Bureau

Pour lancer l'app encore plus vite :

1. **Clic droit** sur `start.bat`
2. **Créer un raccourci**
3. **Déplacer** le raccourci sur le Bureau
4. **Renommer** : "Social Media Analytics"
5. **Icône personnalisée** (optionnel) :
   - Clic droit > Propriétés > Changer d'icône
   - Choisissez une icône 📊

Maintenant : **double-clic pour lancer !** 🚀

---

## 🌟 Conseil Pro

**Créez un dossier "Données"** pour organiser vos fichiers CSV :

```
SocialMediaAnalytics/
├── app.py
├── ...
└── Données/
    ├── janvier_2024.csv
    ├── fevrier_2024.csv
    └── instagram_posts.xlsx
```

---

## 🎯 Objectifs Atteints

✅ Application installée et fonctionnelle
✅ Compte créé
✅ Première analyse réalisée
✅ Prêt à analyser vos propres données !

---

**Bon courage avec vos analyses ! 🚀📊**

*Temps total : 5 minutes chrono ⏱️*

