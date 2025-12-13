"""
Module de gestion de la base de données MySQL/TiDB
Gère les utilisateurs, les abonnements et les sauvegardes de manière persistante.
"""

import os
import json
from datetime import datetime, timedelta
import hashlib
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()

class Database:
    def __init__(self):
        self.db_url = os.getenv('DATABASE_URL')
        if not self.db_url:
            # Fallback pour SQLite sur Streamlit Cloud
            self.db_url = "sqlite:///social_analytics.db"
        
        try:
            self.engine = create_engine(self.db_url, echo=False)
            # Détecter le type de base de données
            self.is_sqlite = 'sqlite' in self.db_url.lower()
            self.init_database()
        except Exception as e:
            print(f"Erreur lors de la connexion à la base de données: {e}")
            # En cas d'échec, revenir à SQLite pour permettre à l'application de démarrer
            self.db_url = "sqlite:///social_analytics.db"
            self.engine = create_engine(self.db_url, echo=False)
            self.is_sqlite = True
            self.init_database()

    def init_database(self):
        """Initialise les tables de la base de données avec syntaxe adaptée"""
        try:
            with self.engine.connect() as connection:
                if self.is_sqlite:
                    # Syntaxe SQLite
                    # Table des utilisateurs
                    connection.execute(text("""
                        CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            email TEXT UNIQUE NOT NULL,
                            password_hash TEXT NOT NULL,
                            first_name TEXT,
                            last_name TEXT,
                            company TEXT,
                            phone TEXT,
                            job_title TEXT,
                            bio TEXT,
                            is_premium INTEGER DEFAULT 0,
                            premium_expires TEXT,
                            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                            last_login TEXT
                        )
                    """))
                    
                    # Table des paiements
                    connection.execute(text("""
                        CREATE TABLE IF NOT EXISTS payments (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            amount REAL NOT NULL,
                            currency TEXT DEFAULT 'EUR',
                            stripe_payment_id TEXT,
                            status TEXT DEFAULT 'pending',
                            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (user_id) REFERENCES users (id)
                        )
                    """))
                    
                    # Table des sauvegardes de travaux
                    connection.execute(text("""
                        CREATE TABLE IF NOT EXISTS saved_projects (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            project_name TEXT NOT NULL,
                            data_json TEXT NOT NULL,
                            results_json TEXT,
                            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (user_id) REFERENCES users (id),
                            UNIQUE(user_id, project_name)
                        )
                    """))
                    
                    # Table des préférences utilisateur
                    connection.execute(text("""
                        CREATE TABLE IF NOT EXISTS user_preferences (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER UNIQUE NOT NULL,
                            theme TEXT DEFAULT 'light',
                            primary_color TEXT DEFAULT '#667eea',
                            secondary_color TEXT DEFAULT '#764ba2',
                            accent_color TEXT DEFAULT '#f093fb',
                            text_color TEXT DEFAULT '#1f2937',
                            background_color TEXT DEFAULT '#ffffff',
                            font_family TEXT DEFAULT 'Arial',
                            language TEXT DEFAULT 'fr',
                            notifications_enabled INTEGER DEFAULT 1,
                            email_notifications INTEGER DEFAULT 1,
                            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (user_id) REFERENCES users (id)
                        )
                    """))
                else:
                    # Syntaxe MySQL/MariaDB
                    # Table des utilisateurs
                    connection.execute(text("""
                        CREATE TABLE IF NOT EXISTS users (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            email VARCHAR(255) UNIQUE NOT NULL,
                            password_hash VARCHAR(255) NOT NULL,
                            first_name VARCHAR(255),
                            last_name VARCHAR(255),
                            company VARCHAR(255),
                            phone VARCHAR(255),
                            job_title VARCHAR(255),
                            bio TEXT,
                            is_premium BOOLEAN DEFAULT FALSE,
                            premium_expires DATETIME,
                            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                            last_login DATETIME
                        )
                    """))
                    
                    # Table des paiements
                    connection.execute(text("""
                        CREATE TABLE IF NOT EXISTS payments (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            user_id INT NOT NULL,
                            amount DECIMAL(10, 2) NOT NULL,
                            currency VARCHAR(10) DEFAULT 'EUR',
                            stripe_payment_id VARCHAR(255),
                            status VARCHAR(50) DEFAULT 'pending',
                            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (user_id) REFERENCES users (id)
                        )
                    """))
                    
                    # Table des sauvegardes de travaux
                    connection.execute(text("""
                        CREATE TABLE IF NOT EXISTS saved_projects (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            user_id INT NOT NULL,
                            project_name VARCHAR(255) NOT NULL,
                            data_json JSON NOT NULL,
                            results_json JSON,
                            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (user_id) REFERENCES users (id),
                            UNIQUE KEY unique_project (user_id, project_name)
                        )
                    """))
                    
                    # Table des préférences utilisateur
                    connection.execute(text("""
                        CREATE TABLE IF NOT EXISTS user_preferences (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            user_id INT UNIQUE NOT NULL,
                            theme VARCHAR(50) DEFAULT 'light',
                            primary_color VARCHAR(50) DEFAULT '#667eea',
                            secondary_color VARCHAR(50) DEFAULT '#764ba2',
                            accent_color VARCHAR(50) DEFAULT '#f093fb',
                            text_color VARCHAR(50) DEFAULT '#1f2937',
                            background_color VARCHAR(50) DEFAULT '#ffffff',
                            font_family VARCHAR(50) DEFAULT 'Arial',
                            language VARCHAR(10) DEFAULT 'fr',
                            notifications_enabled BOOLEAN DEFAULT TRUE,
                            email_notifications BOOLEAN DEFAULT TRUE,
                            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (user_id) REFERENCES users (id)
                        )
                    """))
                
                connection.commit()
        except SQLAlchemyError as e:
            print(f"Erreur lors de l'initialisation de la base de données: {e}")
            raise

    def hash_password(self, password):
        """Hash le mot de passe avec SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def create_user(self, email, password, first_name=None, last_name=None, 
                   company=None, phone=None, job_title=None, bio=None):
        """Crée un nouvel utilisateur"""
        try:
            password_hash = self.hash_password(password)
            with self.engine.connect() as connection:
                result = connection.execute(text("""
                    INSERT INTO users (email, password_hash, first_name, last_name, 
                                     company, phone, job_title, bio)
                    VALUES (:email, :password_hash, :first_name, :last_name, 
                            :company, :phone, :job_title, :bio)
                """), {
                    'email': email,
                    'password_hash': password_hash,
                    'first_name': first_name,
                    'last_name': last_name,
                    'company': company,
                    'phone': phone,
                    'job_title': job_title,
                    'bio': bio
                })
                
                user_id = result.lastrowid
                
                # Créer les préférences par défaut
                connection.execute(text("""
                    INSERT INTO user_preferences (user_id)
                    VALUES (:user_id)
                """), {'user_id': user_id})
                
                connection.commit()
                return True, "Compte créé avec succès!"
        except SQLAlchemyError as e:
            if "Duplicate entry" in str(e) or "UNIQUE constraint failed" in str(e):
                return False, "Cet email est déjà utilisé."
            return False, f"Erreur: {str(e)}"

    def authenticate_user(self, email, password):
        """Authentifie un utilisateur"""
        password_hash = self.hash_password(password)
        with self.engine.connect() as connection:
            result = connection.execute(text("""
                SELECT * FROM users
                WHERE email = :email AND password_hash = :password_hash
            """), {'email': email, 'password_hash': password_hash})
            
            user = result.fetchone()
            
            if user:
                # Mise à jour du dernier login
                if self.is_sqlite:
                    connection.execute(text("""
                        UPDATE users
                        SET last_login = datetime('now')
                        WHERE id = :id
                    """), {'id': user[0]}) # user[0] est l'ID
                else:
                    connection.execute(text("""
                        UPDATE users
                        SET last_login = NOW()
                        WHERE id = :id
                    """), {'id': user[0]}) # user[0] est l'ID
                connection.commit()
                
                # Convertir le résultat en dictionnaire pour la compatibilité
                return dict(user._mapping)
            
            return None

    def check_premium_status(self, user_id):
        """Vérifie si l'utilisateur a un abonnement premium actif"""
        with self.engine.connect() as connection:
            result = connection.execute(text("""
                SELECT is_premium, premium_expires
                FROM users
                WHERE id = :user_id
            """), {'user_id': user_id})
            
            user = result.fetchone()
            
            if not user or not user[0]: # user[0] est is_premium
                return False
            
            # Vérifier si l'abonnement n'a pas expiré
            if user[1]: # user[1] est premium_expires
                expiry = user[1]
                if isinstance(expiry, str):
                    expiry = datetime.strptime(expiry, '%Y-%m-%d %H:%M:%S')
                
                if expiry < datetime.now():
                    self.update_premium_status(user_id, False)
                    return False
            
            return True

    def update_premium_status(self, user_id, is_premium, duration_days=30):
        """Met à jour le statut premium d'un utilisateur"""
        with self.engine.connect() as connection:
            if is_premium:
                expiry = datetime.now() + timedelta(days=duration_days)
                if self.is_sqlite:
                    connection.execute(text("""
                        UPDATE users
                        SET is_premium = 1, premium_expires = :expiry
                        WHERE id = :user_id
                    """), {'expiry': expiry.strftime('%Y-%m-%d %H:%M:%S'), 'user_id': user_id})
                else:
                    connection.execute(text("""
                        UPDATE users
                        SET is_premium = TRUE, premium_expires = :expiry
                        WHERE id = :user_id
                    """), {'expiry': expiry.strftime('%Y-%m-%d %H:%M:%S'), 'user_id': user_id})
            else:
                if self.is_sqlite:
                    connection.execute(text("""
                        UPDATE users
                        SET is_premium = 0, premium_expires = NULL
                        WHERE id = :user_id
                    """), {'user_id': user_id})
                else:
                    connection.execute(text("""
                        UPDATE users
                        SET is_premium = FALSE, premium_expires = NULL
                        WHERE id = :user_id
                    """), {'user_id': user_id})
            connection.commit()

    def record_payment(self, user_id, amount, stripe_payment_id, status='completed'):
        """Enregistre un paiement"""
        with self.engine.connect() as connection:
            connection.execute(text("""
                INSERT INTO payments (user_id, amount, stripe_payment_id, status)
                VALUES (:user_id, :amount, :stripe_payment_id, :status)
            """), {
                'user_id': user_id,
                'amount': amount,
                'stripe_payment_id': stripe_payment_id,
                'status': status
            })
            connection.commit()

    def get_user_preferences(self, user_id):
        """Récupère les préférences utilisateur"""
        with self.engine.connect() as connection:
            result = connection.execute(text("""
                SELECT * FROM user_preferences
                WHERE user_id = :user_id
            """), {'user_id': user_id})
            
            prefs = result.fetchone()
            return dict(prefs._mapping) if prefs else None

    def update_user_preferences(self, user_id, **preferences):
        """Met à jour les préférences utilisateur
        
        Args:
            user_id: ID de l'utilisateur
            **preferences: Paramètres nommés des préférences à mettre à jour
        """
        if not preferences:
            return
        
        # Construction dynamique de la requête UPDATE
        set_clauses = [f"{key} = :{key}" for key in preferences.keys()]
        if self.is_sqlite:
            query = f"UPDATE user_preferences SET {', '.join(set_clauses)}, updated_at = datetime('now') WHERE user_id = :user_id"
        else:
            query = f"UPDATE user_preferences SET {', '.join(set_clauses)}, updated_at = NOW() WHERE user_id = :user_id"
        
        params = dict(preferences)
        params['user_id'] = user_id
        
        with self.engine.connect() as connection:
            connection.execute(text(query), params)
            connection.commit()

    def save_project(self, user_id, project_name, data_dict, results_dict=None):
        """Sauvegarde un projet pour un utilisateur"""
        try:
            data_json = json.dumps(data_dict, default=str)
            results_json = json.dumps(results_dict, default=str) if results_dict else None
            
            with self.engine.connect() as connection:
                # Utiliser INSERT OR REPLACE pour gérer l'upsert (mise à jour ou insertion)
                # Note: La syntaxe exacte dépend du dialecte SQL (MySQL, TiDB, etc.)
                # Pour une compatibilité maximale, on tente un UPDATE puis un INSERT
                
                # 1. Tenter la mise à jour
                if self.is_sqlite:
                    update_query = """
                        UPDATE saved_projects
                        SET data_json = :data_json, results_json = :results_json, updated_at = datetime('now')
                        WHERE user_id = :user_id AND project_name = :project_name
                    """
                else:
                    update_query = """
                        UPDATE saved_projects
                        SET data_json = :data_json, results_json = :results_json, updated_at = NOW()
                        WHERE user_id = :user_id AND project_name = :project_name
                    """
                
                update_result = connection.execute(text(update_query), {
                    'user_id': user_id,
                    'project_name': project_name,
                    'data_json': data_json,
                    'results_json': results_json
                })
                
                if update_result.rowcount == 0:
                    # 2. Si aucune ligne n'a été mise à jour, effectuer l'insertion
                    connection.execute(text("""
                        INSERT INTO saved_projects (user_id, project_name, data_json, results_json)
                        VALUES (:user_id, :project_name, :data_json, :results_json)
                    """), {
                        'user_id': user_id,
                        'project_name': project_name,
                        'data_json': data_json,
                        'results_json': results_json
                    })
                
                connection.commit()
                return True
        except SQLAlchemyError as e:
            print(f"Erreur lors de la sauvegarde du projet: {e}")
            return False

    def load_project(self, user_id, project_name):
        """Charge un projet pour un utilisateur"""
        with self.engine.connect() as connection:
            result = connection.execute(text("""
                SELECT data_json, results_json
                FROM saved_projects
                WHERE user_id = :user_id AND project_name = :project_name
            """), {'user_id': user_id, 'project_name': project_name})
            
            project = result.fetchone()
            
            if project:
                data_dict = json.loads(project[0])
                results_dict = json.loads(project[1]) if project[1] else None
                return data_dict, results_dict
            
            return None, None

    def list_projects(self, user_id):
        """Liste les projets sauvegardés pour un utilisateur"""
        with self.engine.connect() as connection:
            result = connection.execute(text("""
                SELECT project_name, updated_at
                FROM saved_projects
                WHERE user_id = :user_id
                ORDER BY updated_at DESC
            """), {'user_id': user_id})
            
            return [dict(row._mapping) for row in result]

    def delete_project(self, user_id, project_name):
        """Supprime un projet"""
        with self.engine.connect() as connection:
            connection.execute(text("""
                DELETE FROM saved_projects
                WHERE user_id = :user_id AND project_name = :project_name
            """), {'user_id': user_id, 'project_name': project_name})
            connection.commit()
            return True

    def get_user_profile(self, user_id):
        """Récupère le profil complet d'un utilisateur"""
        with self.engine.connect() as connection:
            result = connection.execute(text("""
                SELECT * FROM users
                WHERE id = :user_id
            """), {'user_id': user_id})
            
            user = result.fetchone()
            if user:
                return dict(user._mapping)
            return None

    def update_user_profile(self, user_id, **profile_data):
        """Met à jour le profil utilisateur
        
        Args:
            user_id: ID de l'utilisateur
            **profile_data: Paramètres nommés des données de profil à mettre à jour
        """
        if not profile_data:
            return
        
        # Construction dynamique de la requête UPDATE
        set_clauses = [f"{key} = :{key}" for key in profile_data.keys()]
        query = f"UPDATE users SET {', '.join(set_clauses)} WHERE id = :user_id"
        
        params = dict(profile_data)
        params['user_id'] = user_id
        
        with self.engine.connect() as connection:
            connection.execute(text(query), params)
            connection.commit()

    def get_user_projects(self, user_id):
        """Récupère tous les projets d'un utilisateur"""
        with self.engine.connect() as connection:
            result = connection.execute(text("""
                SELECT id, project_name, created_at, updated_at
                FROM saved_projects
                WHERE user_id = :user_id
                ORDER BY updated_at DESC
            """), {'user_id': user_id})
            
            return [dict(row._mapping) for row in result]

# Note: Ce fichier contient l'implémentation de la base de données
# Les opérations de migration/renommage de fichiers doivent être faites manuellement si nécessaire
