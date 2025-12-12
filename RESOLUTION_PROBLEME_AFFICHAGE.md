# 🔧 Résolution : Problème d'affichage "keyboard_double_"

## ⚠️ Problème identifié

Si vous voyez du texte comme "keyboard_double_" ou des icônes qui ne s'affichent pas correctement, cela peut être dû à plusieurs causes.

---

## ✅ Solutions rapides

### Solution 1 : Vider le cache du navigateur

1. **Appuyez sur `Ctrl + Shift + Delete`** (Windows)
2. Cochez **"Images et fichiers en cache"**
3. Cliquez sur **"Effacer les données"**
4. **Rafraîchissez la page** avec `Ctrl + F5`

### Solution 2 : Forcer le rafraîchissement

1. **Appuyez sur `Ctrl + F5`** pour forcer le rechargement
2. Ou **`Ctrl + Shift + R`**

### Solution 3 : Tester en navigation privée

1. **Ouvrez une fenêtre de navigation privée** (`Ctrl + Shift + N`)
2. Allez sur votre site
3. Vérifiez si le problème persiste

---

## 🔍 Vérifier les erreurs dans la console

1. **Appuyez sur `F12`** pour ouvrir les outils de développement
2. Allez dans l'onglet **"Console"**
3. Regardez s'il y a des erreurs en rouge
4. Notez les messages d'erreur

---

## 🐛 Problèmes courants et solutions

### Problème : Icônes Material Icons non chargées

Si vous utilisez Material Icons et qu'elles ne s'affichent pas :

**Solution** : Vérifiez que le lien vers Google Fonts/Material Icons est correct dans votre code.

### Problème : Emojis non affichés

Si les emojis ne s'affichent pas correctement :

**Solution** : 
- Vérifiez que votre navigateur supporte les emojis
- Mettez à jour votre navigateur
- Essayez un autre navigateur (Chrome, Firefox, Edge)

### Problème : CSS non chargé

Si le style de la page est cassé :

**Solution** :
1. Videz le cache (voir Solution 1)
2. Vérifiez votre connexion internet
3. Vérifiez les logs dans Streamlit Cloud

---

## 🔄 Redéployer l'application

Si le problème persiste après avoir vidé le cache :

1. **Poussez vos modifications vers GitHub** (voir `MISE_A_JOUR_SITE.md`)
2. **Forcez un redéploiement** sur Streamlit Cloud :
   - Allez sur https://share.streamlit.io/
   - Cliquez sur votre application
   - Cliquez sur "⋮" (menu) → "Reboot app"

---

## 📝 Informations à collecter

Si le problème persiste, notez :

1. **Quel navigateur** vous utilisez (Chrome, Firefox, Edge, etc.)
2. **La version du navigateur**
3. **Les erreurs dans la console** (F12 → Console)
4. **Où exactement** le problème apparaît (quelle page, quelle section)
5. **Une capture d'écran** du problème

---

## ✅ Checklist de dépannage

- [ ] J'ai vidé le cache du navigateur
- [ ] J'ai forcé le rafraîchissement (Ctrl + F5)
- [ ] J'ai testé en navigation privée
- [ ] J'ai vérifié la console pour les erreurs (F12)
- [ ] J'ai testé sur un autre navigateur
- [ ] J'ai redéployé l'application sur Streamlit Cloud
- [ ] Le problème persiste toujours

---

## 🆘 Si rien ne fonctionne

1. **Vérifiez les logs** dans Streamlit Cloud :
   - Allez sur https://share.streamlit.io/
   - Cliquez sur votre application
   - Allez dans l'onglet "Logs"
   - Cherchez les erreurs

2. **Vérifiez votre code** :
   - Assurez-vous qu'il n'y a pas d'erreurs de syntaxe
   - Vérifiez que tous les imports sont corrects

3. **Contactez le support** :
   - Allez sur https://discuss.streamlit.io/
   - Créez un nouveau sujet avec votre problème
   - Incluez les informations collectées ci-dessus

---

**Essayez d'abord de vider le cache et de forcer le rafraîchissement ! 🚀**

