"""
Module de gestion de la base de données
Gère les utilisateurs, les abonnements et les sauvegardes
"""

import sqlite3
import hashlib
import json
from datetime import datetime, timedelta
import os

class Database:
    def __init__(self, db_name="social_analytics.db"):
        self.db_name = db_name
        self.init_database()
    
    def get_connection(self):
        """Crée une connexion à la base de données"""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_database(self):
        """Initialise les tables de la base de données"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Table des utilisateurs
        cursor.execute('''
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
                is_premium BOOLEAN DEFAULT 0,
                premium_expires TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_login TIMESTAMP
            )
        ''')
        
        # Ajouter les nouvelles colonnes si elles n'existent pas (migration)
        try:
            cursor.execute('ALTER TABLE users ADD COLUMN first_name TEXT')
        except:
            pass
        try:
            cursor.execute('ALTER TABLE users ADD COLUMN last_name TEXT')
        except:
            pass
        try:
            cursor.execute('ALTER TABLE users ADD COLUMN company TEXT')
        except:
            pass
        try:
            cursor.execute('ALTER TABLE users ADD COLUMN phone TEXT')
        except:
            pass
        try:
            cursor.execute('ALTER TABLE users ADD COLUMN job_title TEXT')
        except:
            pass
        try:
            cursor.execute('ALTER TABLE users ADD COLUMN bio TEXT')
        except:
            pass
        
        # Table des paiements
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                currency TEXT DEFAULT 'EUR',
                stripe_payment_id TEXT,
                status TEXT DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Table des sauvegardes de travaux
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS saved_projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                project_name TEXT NOT NULL,
                data_json TEXT NOT NULL,
                results_json TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Table des préférences utilisateur
        cursor.execute('''
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
                notifications_enabled BOOLEAN DEFAULT 1,
                email_notifications BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Migration: Ajouter font_family si la colonne n'existe pas
        try:
            cursor.execute('ALTER TABLE user_preferences ADD COLUMN font_family TEXT DEFAULT "Arial"')
            conn.commit()
        except:
            pass  # La colonne existe déjà
        
        # Migration: Supprimer font_size si elle existe (on ne la supprime pas pour éviter de perdre des données)
        
        conn.commit()
        conn.close()
    
    def hash_password(self, password):
        """Hash le mot de passe avec SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def create_user(self, email, password, first_name=None, last_name=None, 
                   company=None, phone=None, job_title=None, bio=None):
        """Crée un nouvel utilisateur"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            password_hash = self.hash_password(password)
            
            cursor.execute('''
                INSERT INTO users (email, password_hash, first_name, last_name, 
                                 company, phone, job_title, bio)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (email, password_hash, first_name, last_name, 
                  company, phone, job_title, bio))
            
            conn.commit()
            user_id = cursor.lastrowid
            
            # Créer les préférences par défaut
            cursor.execute('''
                INSERT INTO user_preferences (user_id)
                VALUES (?)
            ''', (user_id,))
            conn.commit()
            
            conn.close()
            return True, "Compte créé avec succès!"
        except sqlite3.IntegrityError:
            return False, "Cet email est déjà utilisé."
        except Exception as e:
            return False, f"Erreur: {str(e)}"
    
    def authenticate_user(self, email, password):
        """Authentifie un utilisateur"""
        conn = self.get_connection()
        cursor = conn.cursor()
        password_hash = self.hash_password(password)
        
        cursor.execute('''
            SELECT * FROM users
            WHERE email = ? AND password_hash = ?
        ''', (email, password_hash))
        
        user = cursor.fetchone()
        
        if user:
            # Mise à jour du dernier login
            cursor.execute('''
                UPDATE users
                SET last_login = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (user['id'],))
            conn.commit()
        
        conn.close()
        return dict(user) if user else None
    
    def check_premium_status(self, user_id):
        """Vérifie si l'utilisateur a un abonnement premium actif"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT is_premium, premium_expires
            FROM users
            WHERE id = ?
        ''', (user_id,))
        
        result = cursor.fetchone()
        conn.close()
        
        if not result or not result['is_premium']:
            return False
        
        # Vérifier si l'abonnement n'a pas expiré
        if result['premium_expires']:
            expiry = datetime.strptime(result['premium_expires'], '%Y-%m-%d %H:%M:%S')
            if expiry < datetime.now():
                self.update_premium_status(user_id, False)
                return False
        
        return True
    
    def update_premium_status(self, user_id, is_premium, duration_days=30):
        """Met à jour le statut premium d'un utilisateur"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if is_premium:
            expiry = datetime.now() + timedelta(days=duration_days)
            cursor.execute('''
                UPDATE users
                SET is_premium = 1, premium_expires = ?
                WHERE id = ?
            ''', (expiry.strftime('%Y-%m-%d %H:%M:%S'), user_id))
        else:
            cursor.execute('''
                UPDATE users
                SET is_premium = 0
                WHERE id = ?
            ''', (user_id,))
        
        conn.commit()
        conn.close()
    
    def save_project(self, user_id, project_name, data_dict, results_dict=None):
        """Sauvegarde un projet pour un utilisateur"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        data_json = json.dumps(data_dict)
        results_json = json.dumps(results_dict) if results_dict else None
        
        # Vérifier si un projet avec ce nom existe déjà
        cursor.execute('''
            SELECT id FROM saved_projects
            WHERE user_id = ? AND project_name = ?
        ''', (user_id, project_name))
        
        existing = cursor.fetchone()
        
        if existing:
            # Mise à jour
            cursor.execute('''
                UPDATE saved_projects
                SET data_json = ?, results_json = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (data_json, results_json, existing['id']))
        else:
            # Nouvelle sauvegarde
            cursor.execute('''
                INSERT INTO saved_projects (user_id, project_name, data_json, results_json)
                VALUES (?, ?, ?, ?)
            ''', (user_id, project_name, data_json, results_json))
        
        conn.commit()
        conn.close()
        return True
    
    def load_project(self, user_id, project_name):
        """Charge un projet sauvegardé"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM saved_projects
            WHERE user_id = ? AND project_name = ?
        ''', (user_id, project_name))
        
        project = cursor.fetchone()
        conn.close()
        
        if project:
            return {
                'data': json.loads(project['data_json']),
                'results': json.loads(project['results_json']) if project['results_json'] else None,
                'created_at': project['created_at'],
                'updated_at': project['updated_at']
            }
        return None
    
    def get_user_projects(self, user_id):
        """Récupère tous les projets d'un utilisateur"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, project_name, created_at, updated_at
            FROM saved_projects
            WHERE user_id = ?
            ORDER BY updated_at DESC
        ''', (user_id,))
        
        projects = cursor.fetchall()
        conn.close()
        
        return [dict(p) for p in projects]
    
    def delete_project(self, user_id, project_id):
        """Supprime un projet"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Vérifier que le projet appartient à l'utilisateur
        cursor.execute('''
            SELECT id FROM saved_projects
            WHERE id = ? AND user_id = ?
        ''', (project_id, user_id))
        
        project = cursor.fetchone()
        
        if project:
            cursor.execute('''
                DELETE FROM saved_projects
                WHERE id = ? AND user_id = ?
            ''', (project_id, user_id))
            conn.commit()
            conn.close()
            return True
        else:
            conn.close()
            return False
    
    def record_payment(self, user_id, amount, stripe_payment_id, status='completed'):
        """Enregistre un paiement"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO payments (user_id, amount, stripe_payment_id, status)
            VALUES (?, ?, ?, ?)
        ''', (user_id, amount, stripe_payment_id, status))
        
        conn.commit()
        conn.close()
    
    def update_user_profile(self, user_id, first_name=None, last_name=None,
                           company=None, phone=None, job_title=None, bio=None):
        """Met à jour le profil d'un utilisateur"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        updates = []
        values = []
        
        if first_name is not None:
            updates.append('first_name = ?')
            values.append(first_name)
        if last_name is not None:
            updates.append('last_name = ?')
            values.append(last_name)
        if company is not None:
            updates.append('company = ?')
            values.append(company)
        if phone is not None:
            updates.append('phone = ?')
            values.append(phone)
        if job_title is not None:
            updates.append('job_title = ?')
            values.append(job_title)
        if bio is not None:
            updates.append('bio = ?')
            values.append(bio)
        
        if updates:
            values.append(user_id)
            cursor.execute(f'''
                UPDATE users
                SET {', '.join(updates)}
                WHERE id = ?
            ''', values)
            conn.commit()
        
        conn.close()
        return True
    
    def get_user_profile(self, user_id):
        """Récupère le profil complet d'un utilisateur"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, email, first_name, last_name, company, phone, 
                   job_title, bio, is_premium, premium_expires, 
                   created_at, last_login
            FROM users
            WHERE id = ?
        ''', (user_id,))
        
        user = cursor.fetchone()
        conn.close()
        
        if user:
            # Convertir en dictionnaire et s'assurer que toutes les valeurs sont présentes
            profile_dict = dict(user)
            # S'assurer que les valeurs None sont bien None et non des chaînes vides
            for key in ['first_name', 'last_name', 'company', 'phone', 'job_title', 'bio']:
                if key in profile_dict and profile_dict[key] == '':
                    profile_dict[key] = None
            return profile_dict
        return None
    
    def get_user_preferences(self, user_id):
        """Récupère les préférences d'un utilisateur"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM user_preferences
            WHERE user_id = ?
        ''', (user_id,))
        
        prefs = cursor.fetchone()
        
        if not prefs:
            # Créer des préférences par défaut
            cursor.execute('''
                INSERT INTO user_preferences (user_id)
                VALUES (?)
            ''', (user_id,))
            conn.commit()
            cursor.execute('''
                SELECT * FROM user_preferences
                WHERE user_id = ?
            ''', (user_id,))
            prefs = cursor.fetchone()
        
        conn.close()
        return dict(prefs) if prefs else None
    
    def update_user_preferences(self, user_id, **kwargs):
        """Met à jour les préférences d'un utilisateur"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        allowed_keys = ['theme', 'primary_color', 'secondary_color', 
                       'accent_color', 'text_color', 'background_color',
                       'font_family', 'notifications_enabled',
                       'email_notifications']
        
        updates = []
        values = []
        
        for key, value in kwargs.items():
            if key in allowed_keys:
                updates.append(f'{key} = ?')
                values.append(value)
        
        if updates:
            values.append(user_id)
            cursor.execute(f'''
                UPDATE user_preferences
                SET {', '.join(updates)}, updated_at = CURRENT_TIMESTAMP
                WHERE user_id = ?
            ''', values)
            conn.commit()
        
        conn.close()
        return True

