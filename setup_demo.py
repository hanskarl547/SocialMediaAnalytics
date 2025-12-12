"""
Script de configuration pour le mode demo
Vérifie et configure automatiquement le mode demo premium
"""

import os
from dotenv import load_dotenv

def setup_demo_mode():
    """Configure le mode demo si Stripe n'est pas configuré"""
    load_dotenv()
    
    secret_key = os.getenv('STRIPE_SECRET_KEY', '')
    public_key = os.getenv('STRIPE_PUBLIC_KEY', '')
    
    # Vérifier si Stripe est configuré
    stripe_configured = bool(secret_key and public_key and 
                           secret_key.startswith('sk_') and 
                           public_key.startswith('pk_'))
    
    if not stripe_configured:
        print("🧪 Mode démo activé - Stripe non configuré")
        print("✅ Premium disponible sans paiement")
        return True
    else:
        print("💳 Stripe configuré - Paiements réels disponibles")
        print("ℹ️ Mode démo toujours disponible")
        return False

if __name__ == "__main__":
    setup_demo_mode()

