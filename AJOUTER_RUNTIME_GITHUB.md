# ⚡ Ajouter runtime.txt sur GitHub (Sans Git)

## 🎯 Solution Rapide

Si Git n'est pas installé, vous pouvez ajouter le fichier directement sur GitHub.

---

## 📋 Étapes

### 1. Aller sur votre Repository GitHub

1. Ouvrez votre navigateur
2. Allez sur votre repository GitHub : `https://github.com/VOTRE-USERNAME/SocialMediaAnalytics`
3. Assurez-vous d'être sur la branche `main` (ou `master`)

---

### 2. Créer le fichier runtime.txt

1. Cliquez sur le bouton **"Add file"** (en haut à droite)
2. Sélectionnez **"Create new file"**

---

### 3. Nommer et Contenir le fichier

1. **Nom du fichier** : Tapez `runtime.txt`

2. **Contenu du fichier** : Collez ceci dans l'éditeur :
   ```
   python-3.11.9
   ```

---

### 4. Commiter le fichier

1. En bas de la page, dans la section **"Commit new file"** :
   - **Commit message** : `Add runtime.txt to fix Railway Python version`
   - Laissez **"Commit directly to the main branch"** sélectionné

2. Cliquez sur le bouton vert **"Commit new file"**

---

### 5. Railway Redéploiera Automatiquement

- Railway détectera automatiquement le nouveau fichier
- Le déploiement se relancera
- Cette fois avec Python 3.11.9, le build devrait réussir

---

## ✅ Vérification

1. Attendez quelques secondes
2. Allez sur Railway Dashboard
3. Vérifiez que le nouveau déploiement démarre
4. Regardez les logs : vous devriez voir "Installing Python 3.11.9"

---

## 🎉 C'est tout !

Vous avez ajouté le fichier sans installer Git. Railway devrait maintenant déployer correctement ! 🚀
