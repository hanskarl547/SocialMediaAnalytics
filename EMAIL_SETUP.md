# Configuration des Notifications par Email

Ce guide vous explique comment configurer les notifications par email dans Social Media Analytics Pro.

## 📧 Configuration SMTP

### Pour Gmail (Recommandé)

1. **Créer un mot de passe d'application** :
   - Allez sur https://myaccount.google.com/
   - Sélectionnez "Sécurité"
   - Activez la "Validation en deux étapes" si ce n'est pas déjà fait
   - Allez dans "Mots de passe des applications"
   - Créez un nouveau mot de passe d'application pour "Mail"
   - Copiez le mot de passe généré (16 caractères)

2. **Configurer le fichier `.env`** :
   ```env
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USERNAME=votre.email@gmail.com
   SMTP_PASSWORD=votre_mot_de_passe_application_16_caracteres
   FROM_EMAIL=votre.email@gmail.com
   APP_NAME=Social Media Analytics Pro
   ```

### Pour Outlook/Hotmail

```env
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
SMTP_USERNAME=votre.email@outlook.com
SMTP_PASSWORD=votre_mot_de_passe
FROM_EMAIL=votre.email@outlook.com
APP_NAME=Social Media Analytics Pro
```

### Pour Yahoo Mail

```env
SMTP_SERVER=smtp.mail.yahoo.com
SMTP_PORT=587
SMTP_USERNAME=votre.email@yahoo.com
SMTP_PASSWORD=votre_mot_de_passe_application
FROM_EMAIL=votre.email@yahoo.com
APP_NAME=Social Media Analytics Pro
```

### Pour un serveur SMTP personnalisé

```env
SMTP_SERVER=votre.serveur.smtp.com
SMTP_PORT=587
SMTP_USERNAME=votre_utilisateur
SMTP_PASSWORD=votre_mot_de_passe
FROM_EMAIL=votre.email@domaine.com
APP_NAME=Social Media Analytics Pro
```

## 🔒 Sécurité

- **Ne partagez jamais** votre fichier `.env` ou vos mots de passe
- Utilisez des **mots de passe d'application** plutôt que votre mot de passe principal
- Le fichier `.env` est déjà dans `.gitignore` pour éviter les fuites

## ✅ Vérification

Une fois configuré :

1. Allez dans **⚙️ Paramètres** → **🔔 Notifications**
2. Activez "Notifications par email"
3. Si la configuration est correcte, vous verrez : "✅ Configuration email détectée"
4. Les notifications seront automatiquement envoyées par email lors des événements importants

## 📬 Types de notifications envoyées par email

- 📤 Import de données réussi
- 💾 Sauvegarde de projet
- 📂 Chargement de projet
- 📊 Alertes de performance (engagement faible/élevé)
- ⚠️ Baisses d'engagement détectées
- 🎉 Réalisations et bonnes performances

## 🐛 Dépannage

### Erreur : "Erreur lors de l'envoi de l'email"

1. Vérifiez que tous les paramètres SMTP sont corrects dans `.env`
2. Pour Gmail, assurez-vous d'utiliser un **mot de passe d'application**, pas votre mot de passe principal
3. Vérifiez que le port SMTP est correct (587 pour TLS)
4. Vérifiez que votre pare-feu/autoroute ne bloque pas les connexions SMTP

### Les emails ne sont pas reçus

1. Vérifiez votre dossier spam/courrier indésirable
2. Vérifiez que "Notifications par email" est activé dans les paramètres
3. Vérifiez que votre adresse email dans votre profil est correcte
4. Testez avec un autre fournisseur email

### Gmail bloque les connexions

- Activez "Accès moins sécurisé" (déconseillé) OU
- Utilisez un mot de passe d'application (recommandé)






