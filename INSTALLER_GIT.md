# 🔧 Installer Git sur Windows

## ❌ Problème

Git n'est pas installé ou n'est pas dans votre PATH.

## ✅ Solutions

---

## 🎯 Solution 1 : Installer Git (Recommandé)

### Option A : Installer Git pour Windows

1. **Téléchargez Git** :
   - Allez sur : https://git-scm.com/download/win
   - Téléchargez le fichier `.exe`

2. **Installez Git** :
   - Double-cliquez sur le fichier téléchargé
   - Suivez l'assistant d'installation
   - **Important** : Cochez "Add Git to PATH" pendant l'installation

3. **Redémarrez PowerShell** :
   - Fermez et rouvrez PowerShell
   - Ou exécutez : `refreshenv`

4. **Vérifiez l'installation** :
   ```powershell
   git --version
   ```

---

## 🎯 Solution 2 : Utiliser GitHub Desktop

Si vous préférez une interface graphique :

1. **Téléchargez GitHub Desktop** :
   - https://desktop.github.com/

2. **Installez et configurez** :
   - Connectez-vous avec votre compte GitHub
   - Clonez votre repository

3. **Ajoutez le fichier runtime.txt** :
   - Glissez-déposez le fichier dans GitHub Desktop
   - Ajoutez un message de commit
   - Cliquez sur "Commit to main"
   - Cliquez sur "Push origin"

---

## 🎯 Solution 3 : Ajouter le fichier directement sur GitHub

Si vous ne voulez pas installer Git maintenant :

### Étape 1 : Aller sur GitHub

1. Allez sur votre repository GitHub
2. Cliquez sur **"Add file"** → **"Create new file"**

### Étape 2 : Créer runtime.txt

1. **Nom du fichier** : `runtime.txt`
2. **Contenu** :
   ```
   python-3.11.9
   ```
3. Cliquez sur **"Commit new file"**

---

## ✅ Après l'Installation de Git

Une fois Git installé, vous pourrez utiliser :

```powershell
git add runtime.txt
git commit -m "Add runtime.txt to fix Railway Python version"
git push
```

---

## 🔍 Vérifier que Git est Installé

Après l'installation, dans PowerShell :

```powershell
git --version
```

Vous devriez voir quelque chose comme :
```
git version 2.42.0.windows.1
```

---

## ⚡ Solution Rapide (Sans Installation)

Si vous voulez faire vite, utilisez **Solution 3** (ajouter le fichier directement sur GitHub). C'est la plus rapide si vous n'avez pas besoin de Git pour l'instant.
