"""
Module de gestion des notifications
Gère l'affichage des notifications dans l'application
"""

import streamlit as st
from datetime import datetime
from typing import Optional, Dict, List
from email_sender import EmailSender

class NotificationManager:
    """Gestionnaire de notifications pour l'application"""
    
    def __init__(self, db, user_id: Optional[int] = None):
        """
        Initialise le gestionnaire de notifications
        
        Parameters:
        db: Instance de la base de données
        user_id: ID de l'utilisateur (optionnel)
        """
        self.db = db
        self.user_id = user_id
        self.email_sender = EmailSender()
    
    def are_notifications_enabled(self) -> bool:
        """Vérifie si les notifications sont activées pour l'utilisateur"""
        if not self.user_id:
            return True  # Par défaut activées si pas d'utilisateur
        
        prefs = self.db.get_user_preferences(self.user_id)
        if prefs:
            return bool(prefs.get('notifications_enabled', True))
        return True
    
    def are_email_notifications_enabled(self) -> bool:
        """Vérifie si les notifications par email sont activées"""
        if not self.user_id:
            return False
        
        prefs = self.db.get_user_preferences(self.user_id)
        if prefs:
            return bool(prefs.get('email_notifications', True))
        return False
    
    def get_user_email(self) -> Optional[str]:
        """Récupère l'email de l'utilisateur"""
        if not self.user_id:
            return None
        
        profile = self.db.get_user_profile(self.user_id)
        if profile:
            return profile.get('email')
        return None
    
    def show_notification(self, title: str, message: str, type: str = "info", 
                         icon: str = "ℹ️", duration: int = 5):
        """
        Affiche une notification dans l'application
        
        Parameters:
        title: Titre de la notification
        message: Message de la notification
        type: Type de notification ('info', 'success', 'warning', 'error')
        icon: Icône à afficher
        duration: Durée d'affichage en secondes
        """
        if not self.are_notifications_enabled():
            return
        
        # Mapper les types aux fonctions Streamlit
        notification_map = {
            'info': st.info,
            'success': st.success,
            'warning': st.warning,
            'error': st.error
        }
        
        notification_func = notification_map.get(type, st.info)
        
        # Afficher la notification avec un style personnalisé
        notification_func(f"{icon} **{title}**\n\n{message}")
        
        # Envoyer par email si activé
        if self.are_email_notifications_enabled() and self.email_sender.is_configured():
            user_email = self.get_user_email()
            if user_email:
                try:
                    self.email_sender.send_notification_email(
                        user_email, title, message, type
                    )
                except Exception as e:
                    # Ne pas bloquer l'application si l'envoi d'email échoue
                    print(f"Erreur lors de l'envoi de l'email: {str(e)}")
    
    def notify_data_imported(self, row_count: int, filename: str):
        """Notification lors de l'import de données"""
        self.show_notification(
            title="Données importées",
            message=f"✅ {row_count:,} lignes importées depuis '{filename}'",
            type="success",
            icon="📤"
        )
    
    def notify_analysis_complete(self, analysis_type: str):
        """Notification lors de la fin d'une analyse"""
        self.show_notification(
            title="Analyse terminée",
            message=f"✅ L'analyse '{analysis_type}' a été complétée avec succès",
            type="success",
            icon="📊"
        )
    
    def notify_project_saved(self, project_name: str):
        """Notification lors de la sauvegarde d'un projet"""
        self.show_notification(
            title="Projet sauvegardé",
            message=f"✅ Le projet '{project_name}' a été sauvegardé avec succès",
            type="success",
            icon="💾"
        )
    
    def notify_project_loaded(self, project_name: str, row_count: int):
        """Notification lors du chargement d'un projet"""
        self.show_notification(
            title="Projet chargé",
            message=f"✅ Projet '{project_name}' chargé ({row_count:,} lignes)",
            type="success",
            icon="📂"
        )
    
    def notify_performance_alert(self, metric: str, value: float, threshold: float, 
                                above: bool = True):
        """
        Notification d'alerte de performance
        
        Parameters:
        metric: Nom de la métrique
        value: Valeur actuelle
        threshold: Seuil d'alerte
        above: True si l'alerte se déclenche au-dessus du seuil, False si en-dessous
        """
        if above and value > threshold:
            self.show_notification(
                title="🚨 Alerte de performance",
                message=f"La métrique '{metric}' ({value:.2f}) dépasse le seuil ({threshold:.2f})",
                type="warning",
                icon="⚠️"
            )
        elif not above and value < threshold:
            self.show_notification(
                title="🚨 Alerte de performance",
                message=f"La métrique '{metric}' ({value:.2f}) est en dessous du seuil ({threshold:.2f})",
                type="warning",
                icon="⚠️"
            )
    
    def notify_engagement_drop(self, platform: str, old_rate: float, new_rate: float):
        """Notification de baisse d'engagement"""
        drop_percentage = ((old_rate - new_rate) / old_rate) * 100
        self.show_notification(
            title="📉 Baisse d'engagement détectée",
            message=f"L'engagement sur {platform} a baissé de {drop_percentage:.1f}% "
                   f"({old_rate:.2f}% → {new_rate:.2f}%)",
            type="warning",
            icon="📉"
        )
    
    def notify_achievement(self, achievement_name: str, description: str):
        """Notification de réalisation/badge"""
        self.show_notification(
            title="🏆 Nouvelle réalisation",
            message=f"**{achievement_name}**\n\n{description}",
            type="success",
            icon="🏆"
        )
    
    def notify_reminder(self, message: str):
        """Notification de rappel"""
        self.show_notification(
            title="⏰ Rappel",
            message=message,
            type="info",
            icon="⏰"
        )
    
    def check_and_notify_performance(self, df):
        """
        Vérifie les performances et envoie des notifications si nécessaire
        """
        if df is None or len(df) == 0:
            return
        
        # Vérifier l'engagement moyen
        if 'engagement_rate' in df.columns:
            avg_engagement = df['engagement_rate'].mean()
            if avg_engagement < 2.0:  # Seuil de 2%
                self.show_notification(
                    title="📊 Performance faible",
                    message=f"L'engagement moyen ({avg_engagement:.2f}%) est en dessous de 2%. "
                           "Considérez d'améliorer votre stratégie de contenu.",
                    type="warning",
                    icon="📊"
                )
            elif avg_engagement > 5.0:  # Excellent engagement
                self.show_notification(
                    title="🎉 Excellent engagement",
                    message=f"Félicitations ! Votre engagement moyen ({avg_engagement:.2f}%) est excellent !",
                    type="success",
                    icon="🎉"
                )
        
        # Vérifier les likes moyens
        if 'likes' in df.columns:
            avg_likes = df['likes'].mean()
            if avg_likes > 1000:
                self.show_notification(
                    title="👍 Bonne performance",
                    message=f"Votre moyenne de likes ({avg_likes:,.0f}) est excellente !",
                    type="success",
                    icon="👍"
                )

