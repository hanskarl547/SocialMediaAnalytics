# ⚡ Guide Rapide : Recréer le dépôt GitHub

## 🚀 Méthode la plus simple (3 étapes)

### Étape 1 : Créer le dépôt sur GitHub.com

1. **Allez sur** : https://github.com/new
2. **Nom du dépôt** : `SocialMediaAnalytics`
3. **Visibilité** : 
   - ✅ **Public** (pour Render gratuit)
   - ⚠️ **Private** (nécessite Render payant)
4. **NE COCHEZ PAS** :
   - ❌ "Add a README file"
   - ❌ "Add .gitignore"
   - ❌ "Choose a license"
5. **Cliquez sur** : "Create repository"

### Étape 2 : Utiliser le script automatique

1. **Double-cliquez sur** : `RECREER_ET_POUSSER.bat`
2. **Suivez les instructions** dans le terminal
3. **Quand demandé**, entrez l'URL de votre dépôt :
   ```
   https://github.com/hanskarl547/SocialMediaAnalytics.git
   ```
   (Remplacez `hanskarl547` par votre nom d'utilisateur GitHub)

### Étape 3 : Authentification GitHub

Si GitHub demande vos identifiants :
- **Username** : votre nom d'utilisateur GitHub
- **Password** : utilisez un **Personal Access Token** (pas votre mot de passe)

#### Créer un Personal Access Token :
1. GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. **Generate new token (classic)**
3. **Nom** : `Render Deployment`
4. **Cochez** : `repo` (accès complet aux dépôts)
5. **Generate token**
6. **COPIEZ LE TOKEN** (vous ne le reverrez plus !)
7. Utilisez ce token comme mot de passe lors du `git push`

---

## ✅ Vérification

Une fois terminé :
1. Allez sur : https://github.com/hanskarl547/SocialMediaAnalytics
2. Vous devriez voir tous vos fichiers
3. ✅ **Votre dépôt est prêt pour Render !**

---

## 🚀 Ensuite : Déployer sur Render

Une fois le dépôt recréé :
1. Retournez sur Render.com
2. Créez un nouveau "Web Service"
3. Sélectionnez votre dépôt `SocialMediaAnalytics`
4. Suivez le guide : `GUIDE_RENDER_ETAPE_PAR_ETAPE.md`

---

## 💡 Alternative : Utiliser GitHub Desktop

Si vous préférez une interface graphique :

1. **Téléchargez** : https://desktop.github.com
2. **Installez** GitHub Desktop
3. **Connectez-vous** avec votre compte GitHub
4. **File** → **Add Local Repository**
5. Sélectionnez : `C:\Users\HP\Documents\SocialMediaAnalytics`
6. **Publish repository** → Créez le dépôt sur GitHub
7. ✅ **C'est fait !**

