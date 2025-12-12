"""
Gestionnaire de paiements Stripe
Gère les abonnements premium et les paiements
"""

import stripe
import os
from dotenv import load_dotenv
from database import Database

load_dotenv()

class PaymentHandler:
    def __init__(self):
        """Initialise le gestionnaire de paiements"""
        self.stripe_secret_key = os.getenv('STRIPE_SECRET_KEY', '')
        self.stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY', '')
        self.premium_price = int(os.getenv('PREMIUM_PRICE', 500))  # 5€ en centimes
        
        if self.stripe_secret_key:
            stripe.api_key = self.stripe_secret_key
        
        self.db = Database()
    
    def create_payment_intent(self, user_id, amount=None):
        """
        Crée une intention de paiement Stripe
        
        Parameters:
        user_id (int): ID de l'utilisateur
        amount (int): Montant en centimes (500 = 5€)
        
        Returns:
        dict: Contient client_secret et payment_intent_id
        """
        if not self.stripe_secret_key:
            return {
                'error': 'Stripe non configuré. Utilisez le mode démo.',
                'demo_mode': True
            }
        
        try:
            if amount is None:
                amount = self.premium_price
            
            # Créer l'intention de paiement
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='eur',
                metadata={
                    'user_id': user_id,
                    'subscription_type': 'premium_monthly'
                }
            )
            
            return {
                'client_secret': payment_intent.client_secret,
                'payment_intent_id': payment_intent.id,
                'amount': amount,
                'demo_mode': False
            }
        
        except stripe.error.StripeError as e:
            return {
                'error': str(e),
                'demo_mode': False
            }
    
    def confirm_payment(self, payment_intent_id, user_id):
        """
        Confirme un paiement et active Premium
        
        Parameters:
        payment_intent_id (str): ID de l'intention de paiement
        user_id (int): ID de l'utilisateur
        
        Returns:
        bool: Succès ou échec
        """
        if not self.stripe_secret_key:
            # Mode démo - activer directement Premium
            self.db.update_premium_status(user_id, True, duration_days=30)
            return True
        
        try:
            # Récupérer l'intention de paiement
            payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            
            if payment_intent.status == 'succeeded':
                # Enregistrer le paiement
                self.db.record_payment(
                    user_id,
                    payment_intent.amount / 100,  # Convertir en euros
                    payment_intent_id,
                    'completed'
                )
                
                # Activer Premium
                self.db.update_premium_status(user_id, True, duration_days=30)
                
                return True
            else:
                return False
        
        except stripe.error.StripeError as e:
            print(f"Erreur Stripe: {str(e)}")
            return False
    
    def create_checkout_session(self, user_id, success_url, cancel_url):
        """
        Crée une session Stripe Checkout
        
        Parameters:
        user_id (int): ID de l'utilisateur
        success_url (str): URL de redirection en cas de succès
        cancel_url (str): URL de redirection en cas d'annulation
        
        Returns:
        dict: Contient l'URL de la session Checkout
        """
        if not self.stripe_secret_key:
            return {
                'error': 'Stripe non configuré',
                'demo_mode': True
            }
        
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': 'Social Media Analytics Pro - Premium',
                            'description': 'Abonnement mensuel Premium avec accès complet',
                        },
                        'unit_amount': self.premium_price,
                        'recurring': {
                            'interval': 'month',
                        },
                    },
                    'quantity': 1,
                }],
                mode='subscription',
                success_url=success_url,
                cancel_url=cancel_url,
                metadata={
                    'user_id': user_id
                }
            )
            
            return {
                'checkout_url': session.url,
                'session_id': session.id,
                'demo_mode': False
            }
        
        except stripe.error.StripeError as e:
            return {
                'error': str(e),
                'demo_mode': False
            }
    
    def cancel_subscription(self, subscription_id):
        """
        Annule un abonnement Stripe
        
        Parameters:
        subscription_id (str): ID de l'abonnement Stripe
        
        Returns:
        bool: Succès ou échec
        """
        if not self.stripe_secret_key:
            return False
        
        try:
            stripe.Subscription.delete(subscription_id)
            return True
        
        except stripe.error.StripeError as e:
            print(f"Erreur lors de l'annulation: {str(e)}")
            return False
    
    def handle_webhook(self, payload, sig_header):
        """
        Gère les webhooks Stripe (notifications de paiement)
        
        Parameters:
        payload (bytes): Corps de la requête webhook
        sig_header (str): Signature Stripe pour vérification
        
        Returns:
        dict: Résultat du traitement
        """
        webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET', '')
        
        if not webhook_secret:
            return {'error': 'Webhook secret non configuré'}
        
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, webhook_secret
            )
        
        except ValueError as e:
            return {'error': 'Payload invalide'}
        
        except stripe.error.SignatureVerificationError as e:
            return {'error': 'Signature invalide'}
        
        # Gérer les événements
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            user_id = payment_intent['metadata'].get('user_id')
            
            if user_id:
                self.confirm_payment(payment_intent['id'], int(user_id))
        
        elif event['type'] == 'customer.subscription.deleted':
            subscription = event['data']['object']
            # Désactiver Premium pour l'utilisateur
            # (nécessite de stocker subscription_id dans la BDD)
            pass
        
        return {'success': True}
    
    def get_payment_history(self, user_id):
        """
        Récupère l'historique des paiements d'un utilisateur
        
        Parameters:
        user_id (int): ID de l'utilisateur
        
        Returns:
        list: Liste des paiements
        """
        # Cette fonction nécessiterait une requête à la BDD
        # À implémenter selon les besoins
        pass
    
    def generate_invoice(self, user_id, payment_id):
        """
        Génère une facture pour un paiement
        
        Parameters:
        user_id (int): ID de l'utilisateur
        payment_id (str): ID du paiement
        
        Returns:
        str: Lien vers la facture PDF
        """
        if not self.stripe_secret_key:
            return None
        
        try:
            # Récupérer les informations de paiement
            payment_intent = stripe.PaymentIntent.retrieve(payment_id)
            
            # Stripe génère automatiquement des factures pour les abonnements
            # Pour les paiements uniques, il faudrait créer une facture manuellement
            
            return None
        
        except stripe.error.StripeError as e:
            print(f"Erreur lors de la génération de facture: {str(e)}")
            return None


# Fonction utilitaire pour le mode démo
def activate_demo_premium(user_id):
    """
    Active Premium en mode démo (sans paiement réel)
    
    Parameters:
    user_id (int): ID de l'utilisateur
    
    Returns:
    bool: Succès
    """
    db = Database()
    db.update_premium_status(user_id, True, duration_days=30)
    
    # Enregistrer un paiement fictif
    db.record_payment(user_id, 5.0, 'demo_payment', 'completed')
    
    return True


# Fonction pour vérifier si Stripe est configuré
def is_stripe_configured():
    """
    Vérifie si Stripe est correctement configuré
    
    Returns:
    bool: True si configuré
    """
    load_dotenv()
    secret_key = os.getenv('STRIPE_SECRET_KEY', '')
    public_key = os.getenv('STRIPE_PUBLIC_KEY', '')
    
    # Vérifier que les clés ne sont pas vides et commencent par sk_ et pk_
    return bool(secret_key and public_key and 
                secret_key.startswith('sk_') and 
                public_key.startswith('pk_'))

