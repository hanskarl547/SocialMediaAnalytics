"""
Test des Nouveaux Tests Statistiques Avancés
Kolmogorov-Smirnov et Friedman
"""

import pandas as pd
import numpy as np
from ultra_advanced_statistical_analysis import UltraAdvancedStatisticalAnalyzer
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_sample_data_for_new_tests():
    """Crée des données d'exemple spécifiques pour les nouveaux tests"""
    
    np.random.seed(42)
    n_samples = 200
    
    # Données pour Kolmogorov-Smirnov (test de distribution)
    # Créer des données avec différentes distributions
    normal_data = np.random.normal(100, 15, n_samples)
    uniform_data = np.random.uniform(50, 150, n_samples)
    exponential_data = np.random.exponential(50, n_samples)
    
    # Données pour Friedman (données appariées)
    # Simuler des mesures répétées sur les mêmes sujets
    subjects = list(range(1, 51))  # 50 sujets
    conditions = ['Avant', 'Pendant', 'Après']  # 3 conditions
    
    friedman_data = []
    for subject in subjects:
        # Effet de base du sujet
        base_effect = np.random.normal(50, 10)
        
        # Effet de la condition
        condition_effects = {
            'Avant': base_effect + np.random.normal(-5, 5),
            'Pendant': base_effect + np.random.normal(10, 5),
            'Après': base_effect + np.random.normal(15, 5)
        }
        
        for condition in conditions:
            friedman_data.append({
                'subject_id': subject,
                'condition': condition,
                'score': max(0, condition_effects[condition] + np.random.normal(0, 3))
            })
    
    # Créer les DataFrames
    ks_df = pd.DataFrame({
        'normal_distribution': normal_data,
        'uniform_distribution': uniform_data,
        'exponential_distribution': exponential_data,
        'mixed_distribution': np.concatenate([normal_data[:100], uniform_data[100:]])
    })
    
    friedman_df = pd.DataFrame(friedman_data)
    
    # Pivoter pour Friedman
    friedman_pivot = friedman_df.pivot(index='subject_id', columns='condition', values='score').reset_index()
    
    return ks_df, friedman_pivot

def test_kolmogorov_smirnov():
    """Test du test de Kolmogorov-Smirnov"""
    
    print("🔍 TEST DE KOLMOGOROV-SMIRNOV")
    print("=" * 50)
    
    # Créer les données
    ks_df, _ = create_sample_data_for_new_tests()
    
    # Initialiser l'analyseur
    analyzer = UltraAdvancedStatisticalAnalyzer(ks_df)
    
    # Tester différentes distributions
    distributions_to_test = ['norm', 'uniform', 'expon']
    columns_to_test = ['normal_distribution', 'uniform_distribution', 'exponential_distribution', 'mixed_distribution']
    
    for column in columns_to_test:
        print(f"\n📊 Test de la colonne: {column}")
        print("-" * 30)
        
        for distribution in distributions_to_test:
            result = analyzer.kolmogorov_smirnov_distribution_test(column, distribution)
            
            if result:
                print(f"\n🎯 Distribution testée: {distribution}")
                print(f"   Statistique KS: {result['ks_statistic']:.4f}")
                print(f"   P-value: {result['p_value']:.6f}")
                print(f"   Significatif: {result['significant']}")
                print(f"   Effect size: {result['effect_size']:.4f}")
                print(f"   Interprétation: {result['effect_interpretation']}")
                
                print(f"\n🧠 Interprétation complète:")
                print(f"   {result['interpretation']}")
                
                print(f"\n💡 Recommandations:")
                for i, rec in enumerate(result['recommendations'], 1):
                    print(f"   {i}. {rec}")
                
                # Statistiques descriptives
                desc = result['descriptive_statistics']
                print(f"\n📈 Statistiques descriptives:")
                print(f"   n={desc['n']}, moyenne={desc['mean']:.2f}, écart-type={desc['std']:.2f}")
                print(f"   asymétrie={desc['skewness']:.3f}, kurtosis={desc['kurtosis']:.3f}")
                
                # Tests de normalité supplémentaires
                additional = result['additional_normality_tests']
                print(f"\n🔬 Tests de normalité supplémentaires:")
                print(f"   Jarque-Bera: p={additional['jarque_bera']['p_value']:.4f}")
                print(f"   Anderson-Darling: stat={additional['anderson_darling']['statistic']:.4f}")
                
                # Analyse des outliers
                outliers = result['outliers_analysis']
                print(f"\n🚨 Outliers détectés: {outliers['count']} ({outliers['percentage']:.1f}%)")
                
                print("-" * 50)

def test_friedman():
    """Test du test de Friedman"""
    
    print("\n🔍 TEST DE FRIEDMAN")
    print("=" * 50)
    
    # Créer les données
    _, friedman_df = create_sample_data_for_new_tests()
    
    # Initialiser l'analyseur
    analyzer = UltraAdvancedStatisticalAnalyzer(friedman_df)
    
    # Test de Friedman sur les 3 conditions
    conditions = ['Avant', 'Pendant', 'Après']
    result = analyzer.friedman_test_analysis(conditions)
    
    if result:
        print(f"📊 Test: {result['test_name']}")
        print(f"🎯 Conditions testées: {result['conditions_tested']}")
        print(f"📈 Statistique Friedman: {result['friedman_statistic']:.4f}")
        print(f"🎯 P-value: {result['p_value']:.6f}")
        print(f"✅ Significatif: {result['significant']}")
        print(f"📏 Kendall's W: {result['kendall_w']:.4f}")
        print(f"💪 Effet: {result['effect_interpretation']}")
        print(f"👥 Échantillon: {result['sample_size']} sujets")
        print(f"🔢 Nombre de conditions: {result['number_of_conditions']}")
        
        print(f"\n🧠 Interprétation complète:")
        print(f"   {result['interpretation']}")
        
        print(f"\n💡 Recommandations:")
        for i, rec in enumerate(result['recommendations'], 1):
            print(f"   {i}. {rec}")
        
        # Statistiques par condition
        print(f"\n📊 Statistiques par condition:")
        for condition in result['condition_statistics']:
            print(f"   {condition['condition']}: n={condition['n']}, moyenne={condition['mean']:.2f}, médiane={condition['median']:.2f}")
            print(f"      Q25={condition['q25']:.2f}, Q75={condition['q75']:.2f}, rang moyen={condition['rank_mean']:.2f}")
        
        # Tests post-hoc
        print(f"\n🔬 Tests post-hoc (Wilcoxon):")
        significant_pairs = [pair for pair in result['post_hoc_tests'] if pair['significant']]
        for pair in result['post_hoc_tests']:
            significance = "✅" if pair['significant'] else "❌"
            print(f"   {significance} {pair['condition1']} vs {pair['condition2']}: p={pair['p_value']:.4f}, r={pair['effect_size_r']:.3f}")
        
        # Cohérence des rangs
        consistency = result['rank_consistency']
        print(f"\n🎯 Cohérence des rangs:")
        print(f"   Kendall's W: {consistency['kendall_w']:.4f}")
        print(f"   Niveau: {consistency['consistency_level']}")
        print(f"   Interprétation: {consistency['interpretation']}")
        
        # Test de normalité des différences (si 2 conditions)
        if result['normality_differences']:
            print(f"\n📈 Test de normalité des différences:")
            norm_diff = result['normality_differences']
            print(f"   Shapiro-Wilk: p={norm_diff['shapiro_wilk']['p_value']:.4f}")
            print(f"   Jarque-Bera: p={norm_diff['jarque_bera']['p_value']:.4f}")

def create_visualizations_for_new_tests():
    """Crée des visualisations pour les nouveaux tests"""
    
    print("\n📊 CRÉATION DE VISUALISATIONS POUR LES NOUVEAUX TESTS")
    print("-" * 60)
    
    # Créer les données
    ks_df, friedman_df = create_sample_data_for_new_tests()
    
    # Visualisation 1: Distributions pour Kolmogorov-Smirnov
    fig1 = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Distribution Normale', 'Distribution Uniforme', 
                       'Distribution Exponentielle', 'Distribution Mixte'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}],
               [{"secondary_y": False}, {"secondary_y": False}]]
    )
    
    # Histogrammes
    fig1.add_trace(
        go.Histogram(x=ks_df['normal_distribution'], name='Normale', nbinsx=30),
        row=1, col=1
    )
    fig1.add_trace(
        go.Histogram(x=ks_df['uniform_distribution'], name='Uniforme', nbinsx=30),
        row=1, col=2
    )
    fig1.add_trace(
        go.Histogram(x=ks_df['exponential_distribution'], name='Exponentielle', nbinsx=30),
        row=2, col=1
    )
    fig1.add_trace(
        go.Histogram(x=ks_df['mixed_distribution'], name='Mixte', nbinsx=30),
        row=2, col=2
    )
    
    fig1.update_layout(
        title_text="Distributions pour Test de Kolmogorov-Smirnov",
        showlegend=False,
        height=600
    )
    
    # Visualisation 2: Box plots pour Friedman
    fig2 = px.box(
        friedman_df.melt(id_vars=['subject_id'], value_vars=['Avant', 'Pendant', 'Après'],
                        var_name='Condition', value_name='Score'),
        x='Condition',
        y='Score',
        title='Scores par Condition (Test de Friedman)',
        color='Condition'
    )
    
    # Visualisation 3: Graphique de profil pour Friedman
    profile_data = friedman_df.set_index('subject_id')[['Avant', 'Pendant', 'Après']]
    
    fig3 = go.Figure()
    
    # Ajouter quelques profils individuels
    for i in range(min(10, len(profile_data))):
        fig3.add_trace(go.Scatter(
            x=['Avant', 'Pendant', 'Après'],
            y=profile_data.iloc[i].values,
            mode='lines+markers',
            name=f'Sujet {profile_data.index[i]}',
            opacity=0.6
        ))
    
    # Ajouter la moyenne
    means = profile_data.mean()
    fig3.add_trace(go.Scatter(
        x=['Avant', 'Pendant', 'Après'],
        y=means.values,
        mode='lines+markers',
        name='Moyenne',
        line=dict(width=4, color='red')
    ))
    
    fig3.update_layout(
        title='Profils Individuels et Moyenne (Test de Friedman)',
        xaxis_title='Condition',
        yaxis_title='Score',
        height=500
    )
    
    print("✅ Visualisations créées:")
    print("   • Graphique 1: Histogrammes des distributions (Kolmogorov-Smirnov)")
    print("   • Graphique 2: Box plots par condition (Friedman)")
    print("   • Graphique 3: Profils individuels et moyenne (Friedman)")
    
    return fig1, fig2, fig3

def demonstrate_practical_use_cases():
    """Démontre des cas d'usage pratiques"""
    
    print("\n🎯 CAS D'USAGE PRATIQUES")
    print("=" * 50)
    
    print("\n📊 KOLMOGOROV-SMIRNOV - Cas d'usage:")
    print("   • Vérifier si les données suivent une distribution normale")
    print("   • Valider les hypothèses pour les tests paramétriques")
    print("   • Détecter des distributions anormales dans les données")
    print("   • Choisir les bonnes transformations de données")
    print("   • Optimiser les modèles statistiques")
    
    print("\n🔬 FRIEDMAN - Cas d'usage:")
    print("   • Comparer plusieurs conditions sur les mêmes sujets")
    print("   • Analyser l'efficacité d'un traitement sur plusieurs moments")
    print("   • Comparer différentes stratégies marketing sur la même audience")
    print("   • Évaluer l'évolution des performances dans le temps")
    print("   • Tests A/B/C avec mesures répétées")
    
    print("\n💡 AVANTAGES DE CES TESTS:")
    print("   • Kolmogorov-Smirnov: Non-paramétrique, robuste aux outliers")
    print("   • Friedman: Gère les données appariées, plus puissant que les tests répétés")
    print("   • Tous deux: Effect sizes, post-hoc, recommandations automatiques")
    print("   • Intégration: Avec l'IA pour des interprétations approfondies")

if __name__ == "__main__":
    print("🧪 TEST DES NOUVEAUX TESTS STATISTIQUES AVANCÉS")
    print("=" * 60)
    print("🎯 Tests ajoutés: Kolmogorov-Smirnov et Friedman")
    print("=" * 60)
    
    # Lancer les tests
    test_kolmogorov_smirnov()
    test_friedman()
    
    # Créer les visualisations
    create_visualizations_for_new_tests()
    
    # Démontrer les cas d'usage
    demonstrate_practical_use_cases()
    
    print("\n🎉 Tests des nouveaux tests statistiques terminés!")
    print("📊 Fonctionnalités ajoutées:")
    print("   ✅ Test de Kolmogorov-Smirnov pour les distributions")
    print("   ✅ Test de Friedman pour les données appariées")
    print("   ✅ Effect sizes et interprétations avancées")
    print("   ✅ Tests post-hoc automatiques")
    print("   ✅ Recommandations personnalisées")
    print("   ✅ Visualisations intégrées")
    print("   ✅ Cas d'usage pratiques")


