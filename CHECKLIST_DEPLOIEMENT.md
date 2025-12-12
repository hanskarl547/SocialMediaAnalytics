# ✅ Checklist de Déploiement - Social Media Analytics Pro

## 🔒 Sécurité et Configuration

### 1. Variables d'environnement (.env)
- [ ] **SECRET_KEY** : Générer une clé secrète unique et forte (minimum 32 caractères aléatoires)
  ```python
  # Générer avec: python -c "import secrets; print(secrets.token_hex(32))"
  ```
- [ ] **OPENAI_API_KEY** : Configurer si vous utilisez l'assistant IA Premium
- [ ] **STRIPE_KEYS** : Configurer pour les paiements réels (ou laisser vide pour mode démo)
- [ ] **SMTP_CONFIG** : Configurer pour les notifications par email (optionnel)
- [ ] **DATABASE_URL** : Vérifier que le chemin de la base de données est correct pour la production

### 2. Fichier .env
- [ ] Créer un fichier `.env` à partir de `.env.example` (ne pas commiter le vrai `.env`)
- [ ] Ajouter `.env` au `.gitignore` si vous utilisez Git
- [ ] Vérifier que toutes les valeurs sensibles sont dans `.env` et non hardcodées

## 🗄️ Base de données

### 3. Configuration de la base de données
- [ ] Vérifier que `database.py` utilise bien les variables d'environnement
- [ ] Tester la création/migration de la base de données
- [ ] Vérifier les permissions d'écriture sur le fichier de base de données
- [ ] Pour la production, considérer PostgreSQL au lieu de SQLite si nécessaire

### 4. Initialisation
- [ ] S'assurer que les tables sont créées automatiquement au premier lancement
- [ ] Tester la création d'un utilisateur et la connexion

## 📦 Dépendances

### 5. requirements.txt
- [ ] Vérifier que toutes les dépendances sont listées
- [ ] Tester l'installation avec: `pip install -r requirements.txt`
- [ ] Vérifier les versions pour compatibilité (notamment Streamlit 1.28.1)
- [ ] Considérer l'ajout d'un fichier `requirements-dev.txt` pour les dépendances de développement

## 🐛 Gestion des erreurs

### 6. Try/Except et gestion d'erreurs
- [x] Les imports de fichiers utilisent des try/except
- [x] Les opérations de base de données sont protégées
- [ ] Ajouter des logs pour les erreurs en production
- [ ] Vérifier que les messages d'erreur ne révèlent pas d'informations sensibles

### 7. Chemins de fichiers
- [ ] **LIGNE 1910** : Chemin hardcodé `C:\Users\hansk\Documents\...` - À CORRIGER
  ```python
  # Remplacer par un chemin relatif ou une variable d'environnement
  documents_path = os.getenv('ADDICTION_DATA_PATH', os.path.join(os.path.dirname(__file__), "example_addiction_data.csv"))
  ```
- [ ] Vérifier tous les chemins de fichiers pour qu'ils soient relatifs ou configurables
- [ ] Tester sur différents systèmes d'exploitation si nécessaire

## 🚀 Configuration Streamlit

### 8. Fichier .streamlit/config.toml (à créer)
Créer un fichier `.streamlit/config.toml` avec:
```toml
[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#667eea"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f8f9fa"
textColor = "#1f2937"
font = "sans serif"
```

## 🔍 Points spécifiques à vérifier

### 9. Code à corriger dans app.py

#### Ligne ~1910 - Chemin hardcodé
```python
# AVANT (à corriger):
documents_path = r"C:\Users\hansk\Documents\Students Social Media Addiction.csv"

# APRÈS (corrigé):
documents_path = os.getenv(
    'ADDICTION_DATA_PATH', 
    os.path.join(os.path.dirname(__file__), "example_addiction_data.csv")
)
```

### 10. Validation des données
- [ ] Vérifier que les validations de formulaires fonctionnent
- [ ] Tester avec des données invalides
- [ ] Vérifier les limites de taille de fichiers uploadés

### 11. Performance
- [ ] Tester avec de gros fichiers (1000+ lignes)
- [ ] Vérifier les timeouts potentiels
- [ ] Optimiser les requêtes de base de données si nécessaire

## 📝 Documentation

### 12. README et documentation
- [x] README.md existe et est à jour
- [ ] Ajouter des instructions de déploiement spécifiques
- [ ] Documenter les variables d'environnement requises
- [ ] Ajouter un guide de dépannage

## 🌐 Déploiement

### 13. Préparation pour Streamlit Cloud / Heroku / etc.
- [ ] Créer un fichier `Procfile` si nécessaire:
  ```
  web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
  ```
- [ ] Vérifier que le port est configurable via variable d'environnement
- [ ] Tester le déploiement sur un environnement de staging

### 14. Variables d'environnement sur la plateforme
- [ ] Configurer toutes les variables d'environnement sur la plateforme de déploiement
- [ ] Ne jamais commiter de secrets dans le code
- [ ] Utiliser les secrets management de la plateforme

## ✅ Tests finaux

### 15. Tests fonctionnels
- [ ] Test de création de compte
- [ ] Test de connexion
- [ ] Test d'import de données
- [ ] Test des analyses statistiques
- [ ] Test de l'assistant IA (si configuré)
- [ ] Test de sauvegarde/chargement de projets
- [ ] Test des fonctionnalités Premium

### 16. Tests de sécurité
- [ ] Vérifier que les mots de passe sont hashés (bcrypt)
- [ ] Tester l'injection SQL (si applicable)
- [ ] Vérifier les permissions de fichiers
- [ ] Tester l'authentification

## 🎯 Actions prioritaires AVANT déploiement

1. ✅ **TERMINÉ** : Corriger le chemin hardcodé ligne ~1910 (utilise maintenant os.path.expanduser)
2. ✅ **TERMINÉ** : Générer et configurer SECRET_KEY dans .env
3. ✅ **TERMINÉ** : Créer le fichier .streamlit/config.toml
4. ⚠️ **EN ATTENTE** : Tester l'installation complète sur un environnement propre
5. ⚠️ **RECOMMANDÉ** : Ajouter des logs pour le debugging en production

## 📋 Notes supplémentaires

- L'application utilise SQLite par défaut (bon pour le développement, considérer PostgreSQL pour la production)
- Le mode démo Premium fonctionne sans Stripe
- Les notifications email sont optionnelles
- L'assistant IA nécessite une clé OpenAI pour fonctionner

---

**Date de création** : $(Get-Date -Format "yyyy-MM-dd")
**Dernière mise à jour** : $(Get-Date -Format "yyyy-MM-dd")


