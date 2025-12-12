# 🔄 Mettre à jour votre site web déployé

## 📋 Guide rapide pour actualiser votre site Streamlit Cloud

Quand vous modifiez votre code localement, vous devez le pousser vers GitHub pour que Streamlit Cloud le détecte et redéploie automatiquement.

---

## ✅ Méthode 1 : Utiliser GitHub Desktop (Le plus simple)

### Étapes :

1. **Ouvrez GitHub Desktop**
2. **Vérifiez les modifications** :
   - Dans la colonne de gauche, vous verrez tous les fichiers modifiés
   - Les fichiers en vert sont nouveaux ou modifiés
3. **Ajoutez un message de commit** :
   - En bas à gauche, dans la zone "Summary", écrivez un message (ex: "Correction erreur NumPy 2.0")
4. **Cliquez sur "Commit to main"** (ou votre branche)
5. **Cliquez sur "Push origin"** (bouton en haut à droite)
6. **Attendez 2-5 minutes** : Streamlit Cloud va automatiquement détecter les changements et redéployer

---

## ✅ Méthode 2 : Utiliser le script batch (Double-clic)

1. **Double-cliquez sur le fichier** `SYNCHRONISER.bat`
2. **Suivez les instructions** à l'écran
3. **Entrez un message** pour décrire vos modifications (ou appuyez sur Entrée pour le message par défaut)
4. **Attendez** que le script termine
5. **Attendez 2-5 minutes** pour le redéploiement automatique

---

## ✅ Méthode 3 : Utiliser la ligne de commande Git

Si vous avez Git installé en ligne de commande :

```powershell
# 1. Aller dans le dossier du projet
cd "c:\Users\HP\Documents\SocialMediaAnalytics"

# 2. Vérifier les modifications
git status

# 3. Ajouter tous les fichiers modifiés
git add .

# 4. Créer un commit avec un message
git commit -m "Mise à jour de l'application"

# 5. Pousser vers GitHub
git push origin main
```

**Note** : Si vous êtes sur la branche `master` au lieu de `main`, utilisez :
```powershell
git push origin master
```

---

## 🔍 Vérifier que les modifications sont sur GitHub

1. Allez sur : **https://github.com/hanskarl547/SocialMediaAnalytics**
2. Vérifiez la date du dernier commit
3. Si la date correspond à maintenant, vos modifications sont bien sur GitHub ✅

---

## ⏱️ Attendre le redéploiement automatique

Après avoir poussé vers GitHub :

1. **Streamlit Cloud détecte automatiquement** les changements (généralement en 1-2 minutes)
2. **Le redéploiement commence** automatiquement
3. **Cela prend 2-5 minutes** pour terminer

### Comment vérifier le statut :

1. Allez sur **https://share.streamlit.io/**
2. Connectez-vous avec GitHub
3. Cliquez sur **"My apps"**
4. Cliquez sur votre application
5. Vous verrez le statut :
   - **"Deploying..."** = Redéploiement en cours ⏳
   - **"Running"** = Application en ligne ✅
   - **"Error"** = Il y a une erreur ❌

---

## 🔄 Forcer un redéploiement manuel (si nécessaire)

Si Streamlit Cloud ne redéploie pas automatiquement :

1. Allez sur **https://share.streamlit.io/**
2. Cliquez sur **"My apps"**
3. Cliquez sur votre application
4. Cliquez sur le menu **"⋮"** (trois points) en haut à droite
5. Cliquez sur **"Reboot app"** ou **"Redeploy"**

---

## 🧹 Vider le cache du navigateur

Parfois, votre navigateur affiche l'ancienne version. Pour voir les nouvelles modifications :

1. **Appuyez sur `Ctrl + F5`** (Windows) pour forcer le rafraîchissement
2. Ou **appuyez sur `Ctrl + Shift + R`**
3. Ou **ouvrez en navigation privée** (Ctrl + Shift + N)

---

## ✅ Checklist de mise à jour

Avant de vérifier votre site :

- [ ] J'ai sauvegardé mes modifications locales
- [ ] J'ai commité mes modifications (avec GitHub Desktop ou Git)
- [ ] J'ai poussé mes modifications vers GitHub (`git push`)
- [ ] J'ai vérifié que le commit apparaît sur GitHub.com
- [ ] J'ai attendu 2-5 minutes pour le redéploiement
- [ ] J'ai vérifié le statut dans Streamlit Cloud
- [ ] J'ai vidé le cache de mon navigateur (Ctrl + F5)

---

## 🐛 Problèmes courants

### Le site ne se met pas à jour après 5 minutes

**Solutions** :
1. Vérifiez les logs dans Streamlit Cloud (onglet "Logs")
2. Vérifiez qu'il n'y a pas d'erreurs dans le code
3. Forcez un redéploiement manuel (voir ci-dessus)

### Erreur "Everything up-to-date"

**Solution** : Cela signifie que vos modifications sont déjà sur GitHub. Vérifiez sur GitHub.com que le dernier commit correspond bien à vos modifications.

### Erreur "Permission denied"

**Solution** : Vérifiez que vous êtes bien connecté à GitHub. Vous devrez peut-être vous authentifier à nouveau.

### Le site affiche toujours l'ancienne version

**Solutions** :
1. Videz le cache du navigateur (Ctrl + F5)
2. Vérifiez que le redéploiement est terminé dans Streamlit Cloud
3. Attendez quelques minutes de plus

---

## 📝 Exemple de workflow complet

Voici un exemple concret pour mettre à jour votre site après avoir corrigé l'erreur NumPy :

1. **Vous avez modifié** `app.py` pour corriger l'erreur NumPy 2.0
2. **Ouvrez GitHub Desktop**
3. **Vous voyez** `app.py` dans la liste des fichiers modifiés
4. **Écrivez** "Correction erreur NumPy 2.0 - Compatibilité avec NumPy 2.0"
5. **Cliquez** sur "Commit to main"
6. **Cliquez** sur "Push origin"
7. **Attendez** 2-5 minutes
8. **Allez** sur votre site Streamlit Cloud
9. **Vérifiez** que l'erreur est corrigée
10. **Testez** la sauvegarde d'un projet

---

## 💡 Astuce : Automatiser avec un script

Vous pouvez créer un raccourci sur votre bureau vers `SYNCHRONISER.bat` pour mettre à jour votre site en un double-clic !

---

## 🔗 Liens utiles

- **GitHub Repository** : https://github.com/hanskarl547/SocialMediaAnalytics
- **Streamlit Cloud** : https://share.streamlit.io/
- **Votre application** : (URL fournie par Streamlit Cloud)

---

**Votre site sera automatiquement mis à jour après chaque push vers GitHub ! 🚀**

