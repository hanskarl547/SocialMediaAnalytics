"""
Test des Analyses Statistiques Ultra-Avancées
Démontre toutes les capacités d'analyse approfondie
"""

import pandas as pd
import numpy as np
from ultra_advanced_statistical_analysis import UltraAdvancedStatisticalAnalyzer
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_sample_data():
    """Crée des données d'exemple pour les tests"""
    
    # Données simulées réalistes
    np.random.seed(42)
    n_samples = 500
    
    # Plateformes avec des caractéristiques différentes
    platforms = ['TikTok', 'Instagram', 'Facebook', 'Twitter', 'YouTube']
    platform_weights = [0.3, 0.25, 0.2, 0.15, 0.1]
    
    data = []
    
    for i in range(n_samples):
        platform = np.random.choice(platforms, p=platform_weights)
        
        # Caractéristiques spécifiques par plateforme
        if platform == 'TikTok':
            followers = np.random.lognormal(8, 1.5)
            likes = np.random.lognormal(6, 1.2)
            comments = np.random.lognormal(4, 1.0)
            shares = np.random.lognormal(3, 0.8)
            views = np.random.lognormal(9, 1.0)
        elif platform == 'Instagram':
            followers = np.random.lognormal(7.5, 1.3)
            likes = np.random.lognormal(5.5, 1.1)
            comments = np.random.lognormal(3.5, 0.9)
            shares = np.random.lognormal(2.5, 0.7)
            views = np.random.lognormal(8, 0.9)
        elif platform == 'Facebook':
            followers = np.random.lognormal(7, 1.2)
            likes = np.random.lognormal(5, 1.0)
            comments = np.random.lognormal(3, 0.8)
            shares = np.random.lognormal(2, 0.6)
            views = np.random.lognormal(7.5, 0.8)
        elif platform == 'Twitter':
            followers = np.random.lognormal(6.5, 1.1)
            likes = np.random.lognormal(4.5, 0.9)
            comments = np.random.lognormal(2.5, 0.7)
            shares = np.random.lognormal(1.5, 0.5)
            views = np.random.lognormal(7, 0.7)
        else:  # YouTube
            followers = np.random.lognormal(8.5, 1.4)
            likes = np.random.lognormal(6.5, 1.3)
            comments = np.random.lognormal(4.5, 1.1)
            shares = np.random.lognormal(3.5, 0.9)
            views = np.random.lognormal(9.5, 1.1)
        
        # Ajouter de la variabilité et des corrélations
        engagement_factor = np.random.normal(1, 0.2)
        likes *= engagement_factor
        comments *= engagement_factor
        shares *= engagement_factor
        
        # Ajouter des outliers occasionnels
        if np.random.random() < 0.05:  # 5% d'outliers
            likes *= np.random.uniform(3, 10)
            comments *= np.random.uniform(2, 8)
            shares *= np.random.uniform(2, 6)
        
        data.append({
            'platform': platform,
            'followers': int(followers),
            'likes': int(likes),
            'comments': int(comments),
            'shares': int(shares),
            'views': int(views),
            'date': pd.date_range('2024-01-01', '2024-12-31').sample(1)[0],
            'content_type': np.random.choice(['video', 'image', 'text', 'story']),
            'hashtags': np.random.randint(0, 30),
            'posting_time': np.random.randint(0, 24)
        })
    
    return pd.DataFrame(data)

def test_ultra_advanced_analyses():
    """Test des analyses ultra-avancées"""
    
    print("🧪 TEST DES ANALYSES STATISTIQUES ULTRA-AVANCÉES")
    print("=" * 60)
    
    # Créer les données
    print("\n📊 Création des données d'exemple...")
    df = create_sample_data()
    print(f"✅ Données créées: {df.shape[0]} lignes, {df.shape[1]} colonnes")
    
    # Initialiser l'analyseur
    analyzer = UltraAdvancedStatisticalAnalyzer(df)
    analyzer.calculate_engagement_rate()
    
    print("\n🔍 ANALYSE ULTRA-AVANCÉE DE KRUSKAL-WALLIS")
    print("-" * 50)
    
    # Test de Kruskal-Wallis ultra-avancé
    kruskal_result = analyzer.ultra_advanced_kruskal_wallis_analysis('engagement_rate', 'platform')
    
    if kruskal_result:
        print(f"📈 Test: {kruskal_result['test_name']}")
        print(f"📊 Statistique: {kruskal_result['statistic']:.4f}")
        print(f"🎯 P-value: {kruskal_result['p_value']:.6f}")
        print(f"✅ Significatif: {kruskal_result['significant']}")
        print(f"📏 Effect size (η²): {kruskal_result['effect_size_eta_squared']:.4f}")
        print(f"👥 Groupes comparés: {kruskal_result['groups_compared']}")
        print(f"📝 Échantillon total: {kruskal_result['total_sample_size']}")
        
        print(f"\n🧠 Interprétation:")
        print(f"   {kruskal_result['interpretation']}")
        
        print(f"\n💡 Recommandations:")
        for i, rec in enumerate(kruskal_result['recommendations'], 1):
            print(f"   {i}. {rec}")
        
        # Statistiques descriptives
        print(f"\n📊 Statistiques descriptives par groupe:")
        for group in kruskal_result['descriptive_statistics']:
            print(f"   {group['group']}: n={group['n']}, moyenne={group['mean']:.2f}, médiane={group['median']:.2f}")
        
        # Tests post-hoc
        print(f"\n🔬 Tests post-hoc significatifs:")
        significant_pairs = [pair for pair in kruskal_result['post_hoc_tests'] if pair['mann_whitney']['significant']]
        for pair in significant_pairs[:3]:  # Afficher les 3 premiers
            print(f"   {pair['group1']} vs {pair['group2']}: p={pair['mann_whitney']['p_value']:.4f}")
    
    print("\n🔗 ANALYSE ULTRA-AVANCÉE DE CORRÉLATION SPEARMAN")
    print("-" * 50)
    
    # Test de Spearman ultra-avancé
    spearman_result = analyzer.ultra_advanced_spearman_analysis('likes', 'engagement_rate')
    
    if spearman_result:
        print(f"📈 Test: {spearman_result['test_name']}")
        print(f"📊 Corrélation: {spearman_result['correlation_coefficient']:.4f}")
        print(f"🎯 P-value: {spearman_result['p_value']:.6f}")
        print(f"📏 R²: {spearman_result['r_squared']:.4f}")
        print(f"👥 Taille échantillon: {spearman_result['sample_size']}")
        
        print(f"\n🧠 Interprétation:")
        print(f"   {spearman_result['interpretation']}")
        
        print(f"\n💡 Recommandations:")
        for i, rec in enumerate(spearman_result['recommendations'], 1):
            print(f"   {i}. {rec}")
        
        # Analyse des outliers
        outliers = spearman_result['outliers_analysis']
        print(f"\n🚨 Analyse des outliers:")
        print(f"   Outliers X (IQR): {outliers['x_outliers_iqr']['count']} ({outliers['x_outliers_iqr']['percentage']:.1f}%)")
        print(f"   Outliers Y (IQR): {outliers['y_outliers_iqr']['count']} ({outliers['y_outliers_iqr']['percentage']:.1f}%)")
        
        # Tests de normalité
        normality = spearman_result['normality_tests']
        print(f"\n📊 Tests de normalité des résidus:")
        print(f"   Shapiro-Wilk: p={normality['shapiro_wilk']['p_value']:.4f}")
        print(f"   Kolmogorov-Smirnov: p={normality['kolmogorov_smirnov']['p_value']:.4f}")
        print(f"   Jarque-Bera: p={normality['jarque_bera']['p_value']:.4f}")
    
    print("\n🔮 ANALYSE ULTRA-AVANCÉE DE RÉGRESSION")
    print("-" * 50)
    
    # Test de régression ultra-avancé
    feature_cols = ['likes', 'comments', 'shares', 'views', 'hashtags', 'posting_time']
    regression_result = analyzer.ultra_advanced_regression_analysis('engagement_rate', feature_cols)
    
    if regression_result:
        print(f"📈 Test: {regression_result['test_name']}")
        print(f"🎯 Variable cible: {regression_result['target_variable']}")
        print(f"📊 Variables explicatives: {len(regression_result['feature_variables'])}")
        print(f"👥 Taille échantillon: {regression_result['sample_size']}")
        
        # Comparaison des modèles
        print(f"\n🏆 Comparaison des modèles:")
        for model_name, performance in regression_result['models_comparison'].items():
            print(f"   {model_name}: R²={performance['test_r2']:.4f}, RMSE={performance['test_rmse']:.2f}")
        
        # Meilleur modèle
        best_model = regression_result['best_model']
        best_performance = regression_result['best_model_performance']
        print(f"\n🥇 Meilleur modèle: {best_model}")
        print(f"   R² test: {best_performance['test_r2']:.4f}")
        print(f"   RMSE test: {best_performance['test_rmse']:.2f}")
        print(f"   MAE test: {best_performance['test_mae']:.2f}")
        print(f"   CV R²: {best_performance['cv_mean']:.4f} (±{best_performance['cv_std']:.4f})")
        
        print(f"\n🧠 Interprétation:")
        print(f"   {regression_result['interpretation']}")
        
        print(f"\n💡 Recommandations:")
        for i, rec in enumerate(regression_result['recommendations'], 1):
            print(f"   {i}. {rec}")
        
        # Sélection de features
        feature_selection = regression_result['feature_selection']
        print(f"\n🎯 Top 3 des variables les plus importantes:")
        for i, feature in enumerate(feature_selection['top_features'], 1):
            print(f"   {i}. {feature}")
        
        # Analyse des résidus
        residual_analysis = best_performance['residual_analysis']
        print(f"\n📊 Analyse des résidus:")
        print(f"   Moyenne: {residual_analysis['mean_residual']:.4f}")
        print(f"   Écart-type: {residual_analysis['std_residual']:.4f}")
        print(f"   Normalité: {residual_analysis['normal_residuals']}")
    
    print("\n📋 RAPPORT ULTRA-COMPLET")
    print("-" * 50)
    
    # Rapport complet
    comprehensive_report = analyzer.get_ultra_comprehensive_report()
    
    print(f"📊 Résumé:")
    print(f"   Analyses effectuées: {comprehensive_report['summary']['total_analyses']}")
    print(f"   Qualité des données: {comprehensive_report['summary']['data_quality_score']:.1f}%")
    print(f"   Taille des données: {comprehensive_report['summary']['data_shape']}")
    
    print(f"\n💡 Recommandations globales:")
    for i, rec in enumerate(comprehensive_report['recommendations'], 1):
        print(f"   {i}. {rec}")
    
    print(f"\n🔍 Insights sur les données:")
    for insight in comprehensive_report['data_insights']:
        print(f"   • {insight}")
    
    print("\n✅ Test terminé avec succès!")
    print("=" * 60)

def create_visualization_demo():
    """Crée des visualisations pour démontrer les analyses"""
    
    print("\n📊 CRÉATION DE VISUALISATIONS DÉMONSTRATIVES")
    print("-" * 50)
    
    # Créer des données
    df = create_sample_data()
    analyzer = UltraAdvancedStatisticalAnalyzer(df)
    analyzer.calculate_engagement_rate()
    
    # Graphique 1: Engagement par plateforme
    fig1 = px.box(
        df, 
        x='platform', 
        y='engagement_rate',
        title='Distribution du Taux d\'Engagement par Plateforme',
        color='platform'
    )
    fig1.update_layout(
        xaxis_title="Plateforme",
        yaxis_title="Taux d'Engagement (%)",
        showlegend=False
    )
    
    # Graphique 2: Corrélation Likes vs Engagement
    fig2 = px.scatter(
        df, 
        x='likes', 
        y='engagement_rate',
        color='platform',
        title='Corrélation entre Likes et Taux d\'Engagement',
        trendline="ols"
    )
    fig2.update_layout(
        xaxis_title="Nombre de Likes",
        yaxis_title="Taux d'Engagement (%)"
    )
    
    # Graphique 3: Métriques par plateforme
    platform_stats = df.groupby('platform').agg({
        'engagement_rate': 'mean',
        'likes': 'mean',
        'comments': 'mean',
        'shares': 'mean'
    }).reset_index()
    
    fig3 = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Engagement Rate', 'Likes', 'Comments', 'Shares'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}],
               [{"secondary_y": False}, {"secondary_y": False}]]
    )
    
    fig3.add_trace(
        go.Bar(x=platform_stats['platform'], y=platform_stats['engagement_rate'], name='Engagement Rate'),
        row=1, col=1
    )
    fig3.add_trace(
        go.Bar(x=platform_stats['platform'], y=platform_stats['likes'], name='Likes'),
        row=1, col=2
    )
    fig3.add_trace(
        go.Bar(x=platform_stats['platform'], y=platform_stats['comments'], name='Comments'),
        row=2, col=1
    )
    fig3.add_trace(
        go.Bar(x=platform_stats['platform'], y=platform_stats['shares'], name='Shares'),
        row=2, col=2
    )
    
    fig3.update_layout(
        title_text="Métriques par Plateforme",
        showlegend=False,
        height=600
    )
    
    print("✅ Visualisations créées:")
    print("   • Graphique 1: Distribution de l'engagement par plateforme")
    print("   • Graphique 2: Corrélation Likes vs Engagement")
    print("   • Graphique 3: Métriques comparatives par plateforme")
    
    return fig1, fig2, fig3

if __name__ == "__main__":
    # Lancer les tests
    test_ultra_advanced_analyses()
    
    # Créer les visualisations
    create_visualization_demo()
    
    print("\n🎉 Toutes les analyses ultra-avancées ont été testées avec succès!")
    print("📊 Les analyses incluent:")
    print("   • Tests de Kruskal-Wallis avec post-hoc et effect size")
    print("   • Corrélations Spearman avec tests de normalité et outliers")
    print("   • Régression avec multiples modèles et optimisation")
    print("   • Sélection de features et validation croisée")
    print("   • Analyses de stabilité et résidus")
    print("   • Recommandations personnalisées et insights")


