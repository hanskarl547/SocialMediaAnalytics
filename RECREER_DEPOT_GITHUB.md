# 🔄 Recréer votre dépôt GitHub

## 📋 Étapes pour recréer le dépôt

### Option 1 : Via GitHub.com (Recommandé - Le plus simple)

#### 1. Créer un nouveau dépôt sur GitHub
1. Allez sur https://github.com
2. Cliquez sur le bouton **"+"** en haut à droite
3. Sélectionnez **"New repository"**

#### 2. Configurer le dépôt
- **Repository name** : `SocialMediaAnalytics` (ou un autre nom)
- **Description** : `Application d'analyse des réseaux sociaux`
- **Visibilité** : 
  - ✅ **Public** (recommandé pour Render gratuit)
  - ⚠️ **Private** (nécessite un compte Render payant)
- **NE COCHEZ PAS** "Add a README file" (vous avez déjà vos fichiers)
- **NE COCHEZ PAS** "Add .gitignore" (vous avez déjà un .gitignore)
- **NE COCHEZ PAS** "Choose a license"

#### 3. Créer le dépôt
- Cliquez sur **"Create repository"**

#### 4. GitHub vous donnera des instructions
Vous verrez une page avec des commandes. **IGNOREZ-LES** pour l'instant, nous allons utiliser une méthode plus simple.

---

### Option 2 : Pousser votre code local vers GitHub

#### 1. Ouvrir un terminal dans votre dossier
```powershell
cd "C:\Users\HP\Documents\SocialMediaAnalytics"
```

#### 2. Initialiser Git (si pas déjà fait)
```powershell
git init
```

#### 3. Vérifier l'état
```powershell
git status
```

#### 4. Ajouter tous les fichiers
```powershell
git add .
```

#### 5. Créer le premier commit
```powershell
git commit -m "Initial commit - Application Social Media Analytics"
```

#### 6. Ajouter le dépôt distant GitHub
Remplacez `VOTRE_NOM_UTILISATEUR` par votre nom d'utilisateur GitHub (hanskarl547) :

```powershell
git remote add origin https://github.com/hanskarl547/SocialMediaAnalytics.git
```

#### 7. Pousser le code
```powershell
git branch -M main
git push -u origin main
```

#### 8. Entrer vos identifiants GitHub
- **Username** : votre nom d'utilisateur GitHub
- **Password** : utilisez un **Personal Access Token** (pas votre mot de passe)

💡 **Pour créer un Personal Access Token** :
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token (classic)
3. Cochez `repo` (accès complet aux dépôts)
4. Generate token
5. **COPIEZ LE TOKEN** (vous ne le reverrez plus !)
6. Utilisez ce token comme mot de passe lors du `git push`

---

## ✅ Vérification

Une fois terminé :
1. Allez sur https://github.com/hanskarl547/SocialMediaAnalytics
2. Vous devriez voir tous vos fichiers
3. Votre dépôt est prêt pour Render !

---

## 🚀 Ensuite : Déployer sur Render

Une fois le dépôt recréé, retournez sur Render.com et suivez le guide `GUIDE_RENDER_ETAPE_PAR_ETAPE.md`.

