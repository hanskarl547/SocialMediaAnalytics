# 🚀 Guide Rapide de Dépannage

## ⚡ Solutions rapides pour les problèmes d'affichage

### 1️⃣ Vider le cache (Solution la plus efficace)

**Windows :**
- Appuyez sur `Ctrl + Shift + Delete`
- Cochez "Images et fichiers en cache"
- Cliquez sur "Effacer les données"
- Rafraîchissez avec `Ctrl + F5`

### 2️⃣ Forcer le rafraîchissement

- `Ctrl + F5` : Recharge la page sans cache
- `Ctrl + Shift + R` : Alternative

### 3️⃣ Vérifier les erreurs

1. Appuyez sur `F12` (outils de développement)
2. Allez dans l'onglet "Console"
3. Regardez les erreurs en rouge
4. Notez-les pour le support si nécessaire

---

## 🔄 Mettre à jour le site déployé

### Méthode simple (GitHub Desktop)

1. Ouvrez **GitHub Desktop**
2. Vérifiez les fichiers modifiés
3. Ajoutez un message de commit
4. Cliquez sur **"Commit to main"**
5. Cliquez sur **"Push origin"**
6. Attendez 2-5 minutes

### Méthode script

Double-cliquez sur **`SYNCHRONISER.bat`**

---

## 🐛 Problèmes spécifiques

### Erreur NumPy 2.0
✅ **Résolu** : Le code a été corrigé pour être compatible avec NumPy 2.0

### Icônes qui ne s'affichent pas
- Videz le cache (voir ci-dessus)
- Vérifiez votre connexion internet
- Testez sur un autre navigateur

### Site ne se met pas à jour
- Vérifiez que vous avez bien poussé vers GitHub
- Allez sur https://share.streamlit.io/ et vérifiez le statut
- Forcez un redéploiement si nécessaire

---

## 📞 Besoin d'aide ?

1. Vérifiez les guides détaillés :
   - `MISE_A_JOUR_SITE.md` : Pour mettre à jour le site
   - `RESOLUTION_PROBLEME_AFFICHAGE.md` : Pour les problèmes d'affichage
   - `RESOLUTION_ERREUR_ACCES.md` : Pour les problèmes d'accès

2. Vérifiez les logs sur Streamlit Cloud

3. Contactez le support sur https://discuss.streamlit.io/

---

**Commencez toujours par vider le cache ! 🎯**

