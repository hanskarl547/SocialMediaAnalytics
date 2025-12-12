# 📦 Guide Complet : Publier votre projet sur GitHub

Ce guide vous explique étape par étape comment publier votre projet Social Media Analytics sur GitHub, puis le déployer.

---

## 🔧 Étape 1 : Installer Git (si pas déjà installé)

### Option A : Installer Git pour Windows

1. **Télécharger Git** :
   - Allez sur : https://git-scm.com/download/win
   - Le téléchargement commence automatiquement

2. **Installer Git** :
   - Double-cliquez sur le fichier téléchargé
   - Suivez l'installation (cliquez "Next" à chaque étape)
   - Gardez les options par défaut
   - À la fin, cochez "Launch Git Bash" et "View Release Notes"
   - Cliquez "Finish"

3. **Vérifier l'installation** :
   - Ouvrez PowerShell ou Git Bash
   - Tapez : `git --version`
   - Vous devriez voir quelque chose comme : `git version 2.xx.x`

### Option B : Utiliser GitHub Desktop (Plus facile pour débutants)

1. **Télécharger GitHub Desktop** :
   - Allez sur : https://desktop.github.com/
   - Téléchargez et installez GitHub Desktop

2. **Configurer votre compte** :
   - Ouvrez GitHub Desktop
   - Connectez-vous avec votre compte GitHub (créez-en un si nécessaire)

---

## 📝 Étape 2 : Créer un compte GitHub (si vous n'en avez pas)

1. Allez sur : **https://github.com/signup**
2. Remplissez le formulaire :
   - Username (nom d'utilisateur)
   - Email
   - Mot de passe
3. Vérifiez votre email
4. C'est fait ! 🎉

---

## 🚀 Étape 3 : Publier votre code sur GitHub

### Méthode 1 : Avec Git en ligne de commande (PowerShell)

Ouvrez PowerShell dans le dossier de votre projet et exécutez ces commandes :

```powershell
# 1. Aller dans le dossier du projet
cd "C:\Users\HP\Documents\SocialMediaAnalytics"

# 2. Initialiser Git (si pas déjà fait)
git init

# 3. Configurer Git avec votre nom et email (à faire une seule fois)
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"

# 4. Ajouter tous les fichiers (sauf ceux dans .gitignore)
git add .

# 5. Créer le premier commit
git commit -m "Initial commit - Social Media Analytics Pro"

# 6. Créer un repository sur GitHub (voir étape suivante)
# Puis connecter votre projet local à GitHub :
git remote add origin https://github.com/VOTRE_USERNAME/VOTRE_REPO_NAME.git

# 7. Renommer la branche en "main" (standard GitHub)
git branch -M main

# 8. Pousser le code sur GitHub
git push -u origin main
```

### Méthode 2 : Avec GitHub Desktop (Plus simple)

1. **Ouvrir GitHub Desktop**
2. **Cliquer sur "File" → "Add Local Repository"**
3. **Sélectionner votre dossier** : `C:\Users\HP\Documents\SocialMediaAnalytics`
4. **Si Git n'est pas initialisé** : GitHub Desktop vous demandera de l'initialiser → Cliquez "Create a Repository"
5. **Remplir les informations** :
   - Name : `SocialMediaAnalytics` (ou le nom que vous voulez)
   - Description : "Application d'analyse des réseaux sociaux avec IA"
   - ❌ NE COCHEZ PAS "Initialize this repository with a README" (vous en avez déjà un)
6. **Cliquer sur "Publish repository"**
7. **Choisir** :
   - ✅ Keep this code private (recommandé au début) OU
   - ❌ Make this code public (pour partager)
8. **Cliquer "Publish repository"**

---

## 🌐 Étape 4 : Créer un nouveau repository sur GitHub (si vous utilisez la ligne de commande)

1. **Allez sur GitHub** : https://github.com
2. **Cliquez sur le "+" en haut à droite** → "New repository"
3. **Remplissez les informations** :
   - Repository name : `SocialMediaAnalytics` (ou un autre nom)
   - Description : "Application d'analyse des réseaux sociaux avec IA"
   - ✅ Public OU ✅ Private (choisissez selon vos préférences)
   - ❌ NE COCHEZ PAS "Add a README file" (vous en avez déjà un)
   - ❌ NE COCHEZ PAS "Add .gitignore" (vous en avez déjà un)
   - ❌ NE COCHEZ PAS "Choose a license" (ou ajoutez-en un si vous voulez)
4. **Cliquez sur "Create repository"**
5. **Copiez l'URL du repository** (elle ressemble à : `https://github.com/VOTRE_USERNAME/SocialMediaAnalytics.git`)

---

## ✅ Étape 5 : Vérifier que tout est sur GitHub

1. Allez sur votre repository GitHub : `https://github.com/VOTRE_USERNAME/SocialMediaAnalytics`
2. Vous devriez voir tous vos fichiers :
   - ✅ `app.py`
   - ✅ `requirements.txt`
   - ✅ `README.md`
   - ✅ `.gitignore`
   - ✅ Etc.
3. **Important** : Vérifiez que ces fichiers NE sont PAS sur GitHub (grâce au .gitignore) :
   - ❌ `.env` (vos secrets)
   - ❌ `social_analytics.db` (votre base de données)
   - ❌ `venv/` (votre environnement virtuel)

---

## 🔐 Étape 6 : Ajouter un fichier README pour GitHub (optionnel mais recommandé)

Si votre README.md est déjà bon, vous pouvez le laisser tel quel. Sinon, vous pouvez le mettre à jour.

---

## 📋 Checklist avant de publier

- [ ] Git est installé
- [ ] Vous avez un compte GitHub
- [ ] Le fichier `.gitignore` est présent (✅ il l'est déjà)
- [ ] Votre fichier `.env` est bien ignoré (ne sera pas publié)
- [ ] Votre base de données `social_analytics.db` est bien ignorée
- [ ] Vous avez testé l'application localement

---

## 🚨 Erreurs courantes et solutions

### Erreur : "git: command not found"
**Solution** : Git n'est pas installé. Installez-le avec la Méthode A de l'Étape 1.

### Erreur : "fatal: not a git repository"
**Solution** : Vous n'êtes pas dans le bon dossier. Utilisez `cd` pour aller dans votre dossier de projet.

### Erreur : "fatal: remote origin already exists"
**Solution** : Vous avez déjà ajouté un remote. Pour le remplacer :
```bash
git remote remove origin
git remote add origin https://github.com/VOTRE_USERNAME/VOTRE_REPO_NAME.git
```

### Erreur : "failed to push some refs"
**Solution** : Votre repository GitHub a peut-être des fichiers que vous n'avez pas localement. Faites :
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Erreur : "permission denied"
**Solution** : GitHub Desktop est plus facile pour l'authentification. Ou configurez SSH keys (plus avancé).

---

## 🎯 Prochaine étape : Déployer sur Streamlit Cloud

Une fois votre code sur GitHub :

1. **Allez sur Streamlit Cloud** : https://share.streamlit.io/
2. **Connectez-vous avec GitHub**
3. **Cliquez sur "New app"**
4. **Sélectionnez votre repository** : `SocialMediaAnalytics`
5. **Branche** : `main`
6. **Fichier principal** : `app.py`
7. **Cliquez sur "Deploy"**

Consultez `DEPLOIEMENT_RAPIDE.md` pour les instructions complètes de déploiement Streamlit Cloud.

---

## 💡 Conseils

- ✅ **Commitez régulièrement** : `git add .` puis `git commit -m "Description des changements"`
- ✅ **Poussez régulièrement** : `git push` pour sauvegarder sur GitHub
- ✅ **Utilisez GitHub Desktop** si vous êtes débutant (plus facile)
- ✅ **Gardez votre `.env` privé** : il ne doit jamais être sur GitHub
- ✅ **Écrivez des messages de commit clairs** : "Ajout fonctionnalité X", "Correction bug Y", etc.

---

**Bon courage ! Une fois sur GitHub, le déploiement sur Streamlit Cloud sera très simple ! 🚀**

