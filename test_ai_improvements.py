"""
Test des nouvelles capacités de l'IA améliorée
Démontre les interprétations concrètes et approfondies
"""

import pandas as pd
import numpy as np
from ai_assistant import AIAssistant

def test_ai_interpretations():
    """Test des nouvelles interprétations IA"""
    
    # Créer des données d'exemple
    data = {
        'platform': ['TikTok', 'TikTok', 'Instagram', 'Instagram', 'Facebook', 'Facebook'] * 20,
        'likes': np.random.randint(100, 10000, 120),
        'comments': np.random.randint(10, 500, 120),
        'shares': np.random.randint(5, 200, 120),
        'views': np.random.randint(1000, 50000, 120),
        'followers': np.random.randint(5000, 100000, 120)
    }
    
    df = pd.DataFrame(data)
    
    # Calculer l'engagement
    df['engagement_rate'] = ((df['likes'] + df['comments'] + df['shares']) / df['followers'] * 100)
    
    # Créer des résultats d'analyse simulés
    analysis_results = {
        'kruskal_wallis': {
            'p_value': 0.0234,
            'significant': True,
            'interpretation': 'Différence significative entre les plateformes'
        },
        'spearman': {
            'correlation': 0.756,
            'p_value': 0.0012,
            'interpretation': 'Forte corrélation entre likes et engagement'
        },
        'prediction': {
            'r2_score': 0.678,
            'rmse': 245.6,
            'interpretation': 'Modèle de prédiction fiable'
        }
    }
    
    # Créer une comparaison de plateformes
    platform_comparison = df.groupby('platform')['engagement_rate'].agg(['mean', 'std']).reset_index()
    platform_comparison.columns = ['platform', 'mean_engagement', 'std_engagement']
    
    # Initialiser l'assistant IA
    ai = AIAssistant()
    
    print("🧪 TEST DES NOUVELLES CAPACITÉS IA")
    print("=" * 50)
    
    # Test mode gratuit
    print("\n📊 MODE GRATUIT:")
    print("-" * 30)
    interpretation_free = ai.interpret_results(analysis_results, is_premium=False, platform_comparison=platform_comparison)
    print(interpretation_free)
    
    # Test mode premium
    print("\n💎 MODE PREMIUM:")
    print("-" * 30)
    interpretation_premium = ai.interpret_results(analysis_results, is_premium=True, platform_comparison=platform_comparison)
    print(interpretation_premium)
    
    # Test recommandations de contenu
    print("\n🎯 RECOMMANDATIONS DE CONTENU:")
    print("-" * 30)
    for platform in ['TikTok', 'Instagram', 'Facebook']:
        avg_eng = platform_comparison[platform_comparison['platform'] == platform]['mean_engagement'].iloc[0]
        rec = ai.generate_content_recommendation(platform, avg_eng, is_premium=True)
        print(f"\n{platform}:")
        print(rec)
    
    # Test explication de métriques
    print("\n📈 EXPLICATION DE MÉTRIQUES:")
    print("-" * 30)
    metrics = ['engagement_rate', 'likes', 'reach', 'impressions']
    for metric in metrics:
        explanation = ai.explain_metric(metric, is_premium=True)
        print(f"\n{metric.upper()}:")
        print(explanation)

if __name__ == "__main__":
    test_ai_interpretations()


