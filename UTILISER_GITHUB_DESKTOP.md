# 🖥️ Utiliser GitHub Desktop pour Ajouter runtime.txt

## ✅ Vous avez GitHub Desktop - Parfait !

C'est la méthode la plus simple pour ajouter le fichier.

---

## 📋 Étapes avec GitHub Desktop

### 1. Ouvrir GitHub Desktop

1. Lancez **GitHub Desktop**
2. Assurez-vous que votre repository `SocialMediaAnalytics` est ouvert
   - Si ce n'est pas le cas, cliquez sur **"File"** → **"Add Local Repository"**
   - Sélectionnez le dossier `C:\Users\HP\Documents\SocialMediaAnalytics`

---

### 2. Vérifier que runtime.txt est présent

1. Dans GitHub Desktop, vous devriez voir `runtime.txt` dans la liste des fichiers modifiés
2. Le fichier devrait apparaître avec une coche ☑️ à côté

**Si le fichier n'apparaît pas :**
- Vérifiez qu'il existe dans `C:\Users\HP\Documents\SocialMediaAnalytics\runtime.txt`
- Si nécessaire, créez-le avec le contenu : `python-3.11.9`

---

### 3. Commiter le fichier

1. En bas à gauche, dans la zone **"Summary"**, tapez :
   ```
   Add runtime.txt to fix Railway Python version
   ```
   
2. Optionnellement, ajoutez une description :
   ```
   Fix Python version issue on Railway by specifying python-3.11.9
   ```

3. Cliquez sur le bouton **"Commit to main"** (ou "Commit to master")

---

### 4. Pousser vers GitHub

1. Cliquez sur le bouton **"Push origin"** (en haut)
   - Ou **"Fetch origin"** puis **"Push"**

2. Attendez que le push se termine
   - Vous verrez un message de confirmation

---

## ✅ Vérification

### Sur GitHub Desktop

Vous devriez voir :
- ✅ "Successfully pushed to origin/main"
- ✅ Le fichier `runtime.txt` n'apparaît plus dans les modifications

### Sur Railway

1. Attendez quelques secondes
2. Allez sur Railway Dashboard
3. Un nouveau déploiement devrait démarrer automatiquement
4. Vérifiez les logs : vous devriez voir "Installing Python 3.11.9"

---

## 🎯 Résumé des Actions

1. ✅ Ouvrir GitHub Desktop
2. ✅ Vérifier que `runtime.txt` est présent (avec le contenu `python-3.11.9`)
3. ✅ Commiter avec le message : "Add runtime.txt to fix Railway Python version"
4. ✅ Pousser vers GitHub
5. ✅ Railway redéploiera automatiquement

---

## 🐛 Si runtime.txt n'apparaît pas dans GitHub Desktop

### Option 1 : Créer le fichier manuellement

1. Ouvrez le fichier dans un éditeur de texte :
   - Chemin : `C:\Users\HP\Documents\SocialMediaAnalytics\runtime.txt`
   
2. Vérifiez qu'il contient :
   ```
   python-3.11.9
   ```
   
3. Sauvegardez le fichier
4. Revenez dans GitHub Desktop
5. Le fichier devrait maintenant apparaître

### Option 2 : Vérifier le contenu

Le fichier `runtime.txt` doit contenir exactement :
```
python-3.11.9
```

Sans espaces supplémentaires, sans ligne vide après.

---

## 🎉 C'est tout !

Une fois poussé, Railway détectera automatiquement le changement et redéploiera avec la bonne version Python. 🚀
