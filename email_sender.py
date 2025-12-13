"""
Module d'envoi d'emails
Gère l'envoi de notifications par email
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class EmailSender:
    """Gestionnaire d'envoi d'emails"""
    
    def __init__(self):
        """Initialise le gestionnaire d'emails avec la configuration"""
        self.smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', '587'))
        self.smtp_username = os.getenv('SMTP_USERNAME', '')
        self.smtp_password = os.getenv('SMTP_PASSWORD', '')
        self.from_email = os.getenv('FROM_EMAIL', self.smtp_username)
        self.app_name = os.getenv('APP_NAME', 'Social Media Analytics Pro')
    
    def is_configured(self) -> bool:
        """Vérifie si la configuration email est complète"""
        return bool(self.smtp_username and self.smtp_password)
    
    def send_email(self, to_email: str, subject: str, body: str, 
                   html_body: Optional[str] = None) -> bool:
        """
        Envoie un email
        
        Parameters:
        to_email: Adresse email du destinataire
        subject: Sujet de l'email
        body: Corps du message (texte)
        html_body: Corps du message (HTML, optionnel)
        
        Returns:
        bool: True si l'email a été envoyé avec succès, False sinon
        """
        if not self.is_configured():
            return False
        
        try:
            # Créer le message
            msg = MIMEMultipart('alternative')
            msg['From'] = self.from_email
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Ajouter le corps du message
            if html_body:
                part1 = MIMEText(body, 'plain', 'utf-8')
                part2 = MIMEText(html_body, 'html', 'utf-8')
                msg.attach(part1)
                msg.attach(part2)
            else:
                msg.attach(MIMEText(body, 'plain', 'utf-8'))
            
            # Se connecter au serveur SMTP et envoyer
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Sécuriser la connexion
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(msg)
            
            return True
        
        except Exception as e:
            print(f"Erreur lors de l'envoi de l'email: {str(e)}")
            return False
    
    def send_notification_email(self, to_email: str, title: str, message: str, 
                               notification_type: str = "info") -> bool:
        """
        Envoie une notification par email avec un format HTML
        
        Parameters:
        to_email: Adresse email du destinataire
        title: Titre de la notification
        message: Message de la notification
        notification_type: Type de notification ('info', 'success', 'warning', 'error')
        
        Returns:
        bool: True si l'email a été envoyé avec succès
        """
        # Définir les couleurs selon le type
        color_map = {
            'info': '#3b82f6',      # Bleu
            'success': '#10b981',    # Vert
            'warning': '#f59e0b',    # Orange
            'error': '#ef4444'       # Rouge
        }
        
        icon_map = {
            'info': 'ℹ️',
            'success': '✅',
            'warning': '⚠️',
            'error': '❌'
        }
        
        color = color_map.get(notification_type, '#3b82f6')
        icon = icon_map.get(notification_type, 'ℹ️')
        
        # Corps HTML
        html_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .container {{
                    background: #ffffff;
                    border-radius: 10px;
                    padding: 30px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }}
                .header {{
                    background: linear-gradient(135deg, {color} 0%, {color}dd 100%);
                    color: white;
                    padding: 20px;
                    border-radius: 10px 10px 0 0;
                    margin: -30px -30px 20px -30px;
                }}
                .content {{
                    padding: 20px 0;
                }}
                .footer {{
                    margin-top: 30px;
                    padding-top: 20px;
                    border-top: 1px solid #e5e7eb;
                    font-size: 12px;
                    color: #6b7280;
                    text-align: center;
                }}
                .button {{
                    display: inline-block;
                    padding: 12px 24px;
                    background: {color};
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1 style="margin: 0; font-size: 24px;">{icon} {title}</h1>
                </div>
                <div class="content">
                    <p style="font-size: 16px; margin: 0;">{message}</p>
                </div>
                <div class="footer">
                    <p>Cet email a été envoyé automatiquement par {self.app_name}</p>
                    <p>Vous recevez cet email car les notifications par email sont activées dans vos paramètres.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Corps texte simple
        text_body = f"""
{icon} {title}

{message}

---
Cet email a été envoyé automatiquement par {self.app_name}
Vous recevez cet email car les notifications par email sont activées dans vos paramètres.
        """
        
        return self.send_email(to_email, f"{icon} {title} - {self.app_name}", text_body, html_body)






