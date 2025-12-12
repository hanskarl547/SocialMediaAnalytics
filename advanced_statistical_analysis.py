"""
Module d'Analyse Statistique Avancée
Analyses approfondies et professionnelles pour les réseaux sociaux
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency, fisher_exact
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

class AdvancedStatisticalAnalyzer:
    def __init__(self, df):
        """
        Initialise l'analyseur avancé avec un DataFrame
        
        Parameters:
        df (pd.DataFrame): DataFrame contenant les données des réseaux sociaux
        """
        self.df = df.copy()
        self.results = {}
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        
    def calculate_engagement_rate(self):
        """Calcule le taux d'engagement avec plusieurs méthodes"""
        if 'likes' in self.df.columns and 'followers' in self.df.columns:
            self.df['engagement_rate'] = (self.df['likes'] / self.df['followers']) * 100
        elif 'likes' in self.df.columns and 'views' in self.df.columns:
            self.df['engagement_rate'] = (self.df['likes'] / self.df['views']) * 100
        else:
            engagement_cols = [col for col in self.df.columns if col in ['likes', 'comments', 'shares', 'saves']]
            if engagement_cols and 'followers' in self.df.columns:
                self.df['engagement_rate'] = (self.df[engagement_cols].sum(axis=1) / self.df['followers']) * 100
        
        # Calculer des métriques supplémentaires
        self._calculate_additional_metrics()
        return self.df
    
    def _calculate_additional_metrics(self):
        """Calcule des métriques supplémentaires"""
        # Taux d'engagement par type d'interaction
        if all(col in self.df.columns for col in ['likes', 'comments', 'shares', 'followers']):
            self.df['like_rate'] = (self.df['likes'] / self.df['followers']) * 100
            self.df['comment_rate'] = (self.df['comments'] / self.df['followers']) * 100
            self.df['share_rate'] = (self.df['shares'] / self.df['followers']) * 100
        
        # Ratio commentaires/likes (qualité de l'engagement)
        if all(col in self.df.columns for col in ['likes', 'comments']):
            self.df['comment_like_ratio'] = self.df['comments'] / (self.df['likes'] + 1)
        
        # Score de viralité
        if all(col in self.df.columns for col in ['shares', 'likes', 'comments']):
            self.df['virality_score'] = (self.df['shares'] * 2 + self.df['comments'] * 1.5 + self.df['likes']) / 1000
    
    def advanced_kruskal_wallis_analysis(self, column='engagement_rate', group_column='platform'):
        """
        Analyse avancée de Kruskal-Wallis avec post-hoc et effect size
        """
        if column not in self.df.columns or group_column not in self.df.columns:
            return None
        
        groups = self.df[group_column].unique()
        group_data = [self.df[self.df[group_column] == group][column].dropna() for group in groups]
        group_data = [g for g in group_data if len(g) > 0]
        
        if len(group_data) < 2:
            return None
        
        # Test principal
        statistic, p_value = stats.kruskal(*group_data)
        
        # Effect size (eta-squared)
        n_total = sum(len(g) for g in group_data)
        eta_squared = (statistic - len(groups) + 1) / (n_total - len(groups))
        
        # Post-hoc tests (Mann-Whitney U)
        post_hoc_results = []
        for i in range(len(groups)):
            for j in range(i+1, len(groups)):
                group1_name, group2_name = groups[i], groups[j]
                group1_data, group2_data = group_data[i], group_data[j]
                
                u_stat, u_p_value = stats.mannwhitneyu(group1_data, group2_data, alternative='two-sided')
                
                # Effect size pour Mann-Whitney (r)
                n1, n2 = len(group1_data), len(group2_data)
                r_effect = 1 - (2 * u_stat) / (n1 * n2)
                
                post_hoc_results.append({
                    'group1': group1_name,
                    'group2': group2_name,
                    'u_statistic': u_stat,
                    'p_value': u_p_value,
                    'effect_size_r': abs(r_effect),
                    'significant': u_p_value < 0.05,
                    'mean_diff': group1_data.mean() - group2_data.mean()
                })
        
        # Statistiques descriptives par groupe
        descriptive_stats = []
        for i, group in enumerate(groups):
            data = group_data[i]
            descriptive_stats.append({
                'group': group,
                'n': len(data),
                'mean': data.mean(),
                'median': data.median(),
                'std': data.std(),
                'q25': data.quantile(0.25),
                'q75': data.quantile(0.75),
                'min': data.min(),
                'max': data.max(),
                'skewness': stats.skew(data),
                'kurtosis': stats.kurtosis(data)
            })
        
        result = {
            'test_name': 'Kruskal-Wallis Advanced',
            'statistic': statistic,
            'p_value': p_value,
            'significant': p_value < 0.05,
            'effect_size_eta_squared': eta_squared,
            'groups_compared': len(groups),
            'total_sample_size': n_total,
            'post_hoc_tests': post_hoc_results,
            'descriptive_statistics': descriptive_stats,
            'interpretation': self._advanced_kruskal_interpretation(p_value, eta_squared, post_hoc_results),
            'recommendations': self._generate_kruskal_recommendations(descriptive_stats, post_hoc_results)
        }
        
        self.results['advanced_kruskal_wallis'] = result
        return result
    
    def advanced_spearman_analysis(self, col1, col2):
        """
        Analyse avancée de corrélation de Spearman avec tests de significativité
        """
        if col1 not in self.df.columns or col2 not in self.df.columns:
            return None
        
        # Supprimer les valeurs manquantes
        data = self.df[[col1, col2]].dropna()
        
        if len(data) < 3:
            return None
        
        # Corrélation de Spearman
        correlation, p_value = stats.spearmanr(data[col1], data[col2])
        
        # Test de significativité avec différents seuils
        significance_levels = {
            'highly_significant': p_value < 0.001,
            'very_significant': p_value < 0.01,
            'significant': p_value < 0.05,
            'marginally_significant': p_value < 0.1
        }
        
        # Effect size (coefficient de détermination)
        r_squared = correlation ** 2
        
        # Test de normalité des résidus
        residuals = data[col2] - data[col1] * correlation
        shapiro_stat, shapiro_p = stats.shapiro(residuals)
        
        # Analyse de la force de la corrélation
        strength_interpretation = self._interpret_correlation_strength(abs(correlation))
        
        # Analyse des outliers
        outliers = self._detect_correlation_outliers(data[col1], data[col2])
        
        # Régression non-paramétrique (LOWESS)
        try:
            from statsmodels.nonparametric.smoothers_lowess import lowess
            lowess_result = lowess(data[col2], data[col1], frac=0.3)
        except ImportError:
            lowess_result = None
        
        result = {
            'test_name': 'Spearman Correlation Advanced',
            'correlation_coefficient': correlation,
            'p_value': p_value,
            'r_squared': r_squared,
            'sample_size': len(data),
            'significance_levels': significance_levels,
            'strength_interpretation': strength_interpretation,
            'residual_normality': {
                'shapiro_statistic': shapiro_stat,
                'shapiro_p_value': shapiro_p,
                'normal_residuals': shapiro_p > 0.05
            },
            'outliers': outliers,
            'lowess_trend': lowess_result,
            'interpretation': self._advanced_spearman_interpretation(correlation, p_value, r_squared),
            'recommendations': self._generate_spearman_recommendations(correlation, strength_interpretation)
        }
        
        self.results['advanced_spearman'] = result
        return result
    
    def advanced_chi_square_analysis(self, col1, col2):
        """
        Analyse avancée du test du Chi-carré avec tests supplémentaires
        """
        if col1 not in self.df.columns or col2 not in self.df.columns:
            return None
        
        # Créer la table de contingence
        contingency_table = pd.crosstab(self.df[col1], self.df[col2])
        
        if contingency_table.shape[0] < 2 or contingency_table.shape[1] < 2:
            return None
        
        # Test du Chi-carré
        chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)
        
        # Test de Fisher (pour les petits échantillons)
        fisher_odds_ratio = None
        fisher_p_value = None
        if contingency_table.shape == (2, 2):
            try:
                fisher_odds_ratio, fisher_p_value = fisher_exact(contingency_table)
            except:
                pass
        
        # Effect size (Cramér's V)
        n = contingency_table.sum().sum()
        cramers_v = np.sqrt(chi2_stat / (n * (min(contingency_table.shape) - 1)))
        
        # Test de normalité des résidus
        residuals = (contingency_table - expected) / np.sqrt(expected)
        
        # Analyse des cellules contribuant le plus au Chi-carré
        cell_contributions = (contingency_table - expected) ** 2 / expected
        max_contribution_idx = np.unravel_index(cell_contributions.values.argmax(), cell_contributions.shape)
        
        # Rapport de vraisemblance
        likelihood_ratio = 2 * np.sum(contingency_table * np.log(contingency_table / expected))
        
        result = {
            'test_name': 'Chi-Square Advanced',
            'chi2_statistic': chi2_stat,
            'p_value': p_value,
            'degrees_of_freedom': dof,
            'sample_size': n,
            'contingency_table': contingency_table,
            'expected_frequencies': expected,
            'residuals': residuals,
            'cramers_v': cramers_v,
            'fisher_exact': {
                'odds_ratio': fisher_odds_ratio,
                'p_value': fisher_p_value
            },
            'likelihood_ratio': likelihood_ratio,
            'max_contribution_cell': {
                'row': contingency_table.index[max_contribution_idx[0]],
                'col': contingency_table.columns[max_contribution_idx[1]],
                'contribution': cell_contributions.iloc[max_contribution_idx]
            },
            'interpretation': self._advanced_chi_square_interpretation(chi2_stat, p_value, cramers_v),
            'recommendations': self._generate_chi_square_recommendations(contingency_table, cramers_v)
        }
        
        self.results['advanced_chi_square'] = result
        return result
    
    def advanced_regression_analysis(self, target_col, feature_cols):
        """
        Analyse de régression avancée avec plusieurs modèles
        """
        if target_col not in self.df.columns:
            return None
        
        # Préparer les données
        data = self.df[[target_col] + feature_cols].dropna()
        
        if len(data) < 10:
            return None
        
        X = data[feature_cols]
        y = data[target_col]
        
        # Standardiser les features
        X_scaled = self.scaler.fit_transform(X)
        
        # Diviser en train/test
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
        
        # Modèles à tester
        models = {
            'Linear Regression': LinearRegression(),
            'Ridge Regression': Ridge(alpha=1.0),
            'Lasso Regression': Lasso(alpha=0.1),
            'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
            'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42)
        }
        
        model_results = {}
        
        for name, model in models.items():
            # Entraîner le modèle
            model.fit(X_train, y_train)
            
            # Prédictions
            y_pred_train = model.predict(X_train)
            y_pred_test = model.predict(X_test)
            
            # Métriques
            train_r2 = r2_score(y_train, y_pred_train)
            test_r2 = r2_score(y_test, y_pred_test)
            train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
            test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
            train_mae = mean_absolute_error(y_train, y_pred_train)
            test_mae = mean_absolute_error(y_test, y_pred_test)
            
            # Validation croisée
            cv_scores = cross_val_score(model, X_scaled, y, cv=5, scoring='r2')
            
            # Feature importance (si disponible)
            feature_importance = None
            if hasattr(model, 'feature_importances_'):
                feature_importance = dict(zip(feature_cols, model.feature_importances_))
            elif hasattr(model, 'coef_'):
                feature_importance = dict(zip(feature_cols, model.coef_))
            
            model_results[name] = {
                'train_r2': train_r2,
                'test_r2': test_r2,
                'train_rmse': train_rmse,
                'test_rmse': test_rmse,
                'train_mae': train_mae,
                'test_mae': test_mae,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std(),
                'feature_importance': feature_importance,
                'overfitting': train_r2 - test_r2 > 0.1
            }
        
        # Sélectionner le meilleur modèle
        best_model = max(model_results.keys(), key=lambda x: model_results[x]['test_r2'])
        
        # Analyse des résidus du meilleur modèle
        best_model_obj = models[best_model]
        best_model_obj.fit(X_scaled, y)
        y_pred = best_model_obj.predict(X_scaled)
        residuals = y - y_pred
        
        # Tests de normalité des résidus
        shapiro_stat, shapiro_p = stats.shapiro(residuals)
        
        # Test de Breusch-Pagan pour l'homoscédasticité
        try:
            from statsmodels.stats.diagnostic import het_breuschpagan
            bp_stat, bp_p_value, _, _ = het_breuschpagan(residuals, X_scaled)
        except ImportError:
            bp_stat, bp_p_value = None, None
        
        result = {
            'test_name': 'Advanced Regression Analysis',
            'target_variable': target_col,
            'feature_variables': feature_cols,
            'sample_size': len(data),
            'models_comparison': model_results,
            'best_model': best_model,
            'best_model_performance': model_results[best_model],
            'residual_analysis': {
                'shapiro_statistic': shapiro_stat,
                'shapiro_p_value': shapiro_p,
                'normal_residuals': shapiro_p > 0.05,
                'breusch_pagan_stat': bp_stat,
                'breusch_pagan_p_value': bp_p_value,
                'homoscedastic': bp_p_value > 0.05 if bp_p_value else None
            },
            'interpretation': self._advanced_regression_interpretation(model_results, best_model),
            'recommendations': self._generate_regression_recommendations(model_results, best_model)
        }
        
        self.results['advanced_regression'] = result
        return result
    
    def cluster_analysis(self, columns, n_clusters=None):
        """
        Analyse de clustering pour segmenter les données
        """
        if not all(col in self.df.columns for col in columns):
            return None
        
        # Préparer les données
        data = self.df[columns].dropna()
        
        if len(data) < 10:
            return None
        
        # Standardiser les données
        data_scaled = self.scaler.fit_transform(data)
        
        # Déterminer le nombre optimal de clusters
        if n_clusters is None:
            n_clusters = self._find_optimal_clusters(data_scaled)
        
        # K-means clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(data_scaled)
        
        # Ajouter les clusters au DataFrame
        self.df.loc[data.index, 'cluster'] = clusters
        
        # Analyser les clusters
        cluster_analysis = []
        for i in range(n_clusters):
            cluster_data = data[clusters == i]
            cluster_analysis.append({
                'cluster': i,
                'size': len(cluster_data),
                'percentage': len(cluster_data) / len(data) * 100,
                'centroid': cluster_data.mean().to_dict(),
                'characteristics': self._describe_cluster_characteristics(cluster_data, columns)
            })
        
        # PCA pour visualisation
        pca = PCA(n_components=2)
        data_pca = pca.fit_transform(data_scaled)
        
        result = {
            'test_name': 'Cluster Analysis',
            'variables_used': columns,
            'n_clusters': n_clusters,
            'cluster_analysis': cluster_analysis,
            'pca_components': pca.components_,
            'pca_explained_variance': pca.explained_variance_ratio_,
            'silhouette_score': self._calculate_silhouette_score(data_scaled, clusters),
            'interpretation': self._cluster_interpretation(cluster_analysis),
            'recommendations': self._generate_cluster_recommendations(cluster_analysis)
        }
        
        self.results['cluster_analysis'] = result
        return result
    
    def _find_optimal_clusters(self, data, max_clusters=10):
        """Trouve le nombre optimal de clusters avec la méthode du coude"""
        from sklearn.metrics import silhouette_score
        
        silhouette_scores = []
        for k in range(2, min(max_clusters + 1, len(data))):
            kmeans = KMeans(n_clusters=k, random_state=42)
            clusters = kmeans.fit_predict(data)
            score = silhouette_score(data, clusters)
            silhouette_scores.append(score)
        
        return silhouette_scores.index(max(silhouette_scores)) + 2
    
    def _calculate_silhouette_score(self, data, clusters):
        """Calcule le score de silhouette"""
        try:
            from sklearn.metrics import silhouette_score
            return silhouette_score(data, clusters)
        except:
            return None
    
    def _detect_correlation_outliers(self, x, y):
        """Détecte les outliers dans une corrélation"""
        # Calculer les résidus
        correlation = np.corrcoef(x, y)[0, 1]
        predicted_y = x * correlation
        residuals = y - predicted_y
        
        # Identifier les outliers (règle des 3 sigmas)
        threshold = 3 * residuals.std()
        outliers = abs(residuals) > threshold
        
        return {
            'n_outliers': outliers.sum(),
            'outlier_percentage': outliers.sum() / len(x) * 100,
            'outlier_indices': x[outliers].index.tolist()
        }
    
    def _interpret_correlation_strength(self, abs_corr):
        """Interprète la force de la corrélation"""
        if abs_corr >= 0.9:
            return "Très forte"
        elif abs_corr >= 0.7:
            return "Forte"
        elif abs_corr >= 0.5:
            return "Modérée"
        elif abs_corr >= 0.3:
            return "Faible"
        else:
            return "Très faible"
    
    def _describe_cluster_characteristics(self, cluster_data, columns):
        """Décrit les caractéristiques d'un cluster"""
        characteristics = {}
        for col in columns:
            characteristics[col] = {
                'mean': cluster_data[col].mean(),
                'std': cluster_data[col].std(),
                'median': cluster_data[col].median(),
                'q25': cluster_data[col].quantile(0.25),
                'q75': cluster_data[col].quantile(0.75)
            }
        return characteristics
    
    def _advanced_kruskal_interpretation(self, p_value, eta_squared, post_hoc_results):
        """Interprétation avancée du test de Kruskal-Wallis"""
        interpretation = f"Test de Kruskal-Wallis: "
        
        if p_value < 0.001:
            interpretation += "Différence hautement significative (p < 0.001). "
        elif p_value < 0.01:
            interpretation += "Différence très significative (p < 0.01). "
        elif p_value < 0.05:
            interpretation += "Différence significative (p < 0.05). "
        else:
            interpretation += "Pas de différence significative (p ≥ 0.05). "
        
        # Effect size
        if eta_squared >= 0.14:
            interpretation += "Effet de grande taille (η² ≥ 0.14). "
        elif eta_squared >= 0.06:
            interpretation += "Effet de taille moyenne (η² ≥ 0.06). "
        elif eta_squared >= 0.01:
            interpretation += "Effet de petite taille (η² ≥ 0.01). "
        else:
            interpretation += "Effet négligeable (η² < 0.01). "
        
        # Post-hoc
        significant_pairs = [pair for pair in post_hoc_results if pair['significant']]
        if significant_pairs:
            interpretation += f"Différences significatives détectées entre {len(significant_pairs)} paires de groupes. "
        
        return interpretation
    
    def _advanced_spearman_interpretation(self, correlation, p_value, r_squared):
        """Interprétation avancée de la corrélation de Spearman"""
        interpretation = f"Corrélation de Spearman: "
        
        # Direction
        direction = "positive" if correlation > 0 else "negative"
        interpretation += f"Corrélation {direction} (r = {correlation:.3f}). "
        
        # Significativité
        if p_value < 0.001:
            interpretation += "Hautement significative (p < 0.001). "
        elif p_value < 0.01:
            interpretation += "Très significative (p < 0.01). "
        elif p_value < 0.05:
            interpretation += "Significative (p < 0.05). "
        else:
            interpretation += "Non significative (p ≥ 0.05). "
        
        # Force
        strength = self._interpret_correlation_strength(abs(correlation))
        interpretation += f"Force {strength.lower()}. "
        
        # Variance expliquée
        interpretation += f"Variance expliquée: {r_squared:.1%}. "
        
        return interpretation
    
    def _advanced_chi_square_interpretation(self, chi2_stat, p_value, cramers_v):
        """Interprétation avancée du test du Chi-carré"""
        interpretation = f"Test du Chi-carré: "
        
        if p_value < 0.001:
            interpretation += "Association hautement significative (p < 0.001). "
        elif p_value < 0.01:
            interpretation += "Association très significative (p < 0.01). "
        elif p_value < 0.05:
            interpretation += "Association significative (p < 0.05). "
        else:
            interpretation += "Pas d'association significative (p ≥ 0.05). "
        
        # Effect size
        if cramers_v >= 0.5:
            interpretation += "Association forte (V de Cramér ≥ 0.5). "
        elif cramers_v >= 0.3:
            interpretation += "Association modérée (V de Cramér ≥ 0.3). "
        elif cramers_v >= 0.1:
            interpretation += "Association faible (V de Cramér ≥ 0.1). "
        else:
            interpretation += "Association négligeable (V de Cramér < 0.1). "
        
        return interpretation
    
    def _advanced_regression_interpretation(self, model_results, best_model):
        """Interprétation avancée de la régression"""
        best_performance = model_results[best_model]
        
        interpretation = f"Analyse de régression: Meilleur modèle: {best_model}. "
        
        # Performance
        if best_performance['test_r2'] >= 0.8:
            interpretation += "Excellente prédictibilité (R² ≥ 0.8). "
        elif best_performance['test_r2'] >= 0.6:
            interpretation += "Bonne prédictibilité (R² ≥ 0.6). "
        elif best_performance['test_r2'] >= 0.4:
            interpretation += "Prédictibilité modérée (R² ≥ 0.4). "
        else:
            interpretation += "Faible prédictibilité (R² < 0.4). "
        
        # Overfitting
        if best_performance['overfitting']:
            interpretation += "Attention: Risque de sur-apprentissage détecté. "
        
        # Validation croisée
        if best_performance['cv_mean'] >= 0.7:
            interpretation += "Validation croisée excellente. "
        elif best_performance['cv_mean'] >= 0.5:
            interpretation += "Validation croisée acceptable. "
        else:
            interpretation += "Validation croisée faible. "
        
        return interpretation
    
    def _cluster_interpretation(self, cluster_analysis):
        """Interprétation de l'analyse de clustering"""
        n_clusters = len(cluster_analysis)
        interpretation = f"Analyse de clustering: {n_clusters} segments identifiés. "
        
        # Taille des clusters
        sizes = [cluster['size'] for cluster in cluster_analysis]
        max_size = max(sizes)
        min_size = min(sizes)
        
        if max_size / min_size > 3:
            interpretation += "Segmentation déséquilibrée (ratio > 3:1). "
        else:
            interpretation += "Segmentation équilibrée. "
        
        # Clusters dominants
        dominant_clusters = [c for c in cluster_analysis if c['percentage'] > 30]
        if dominant_clusters:
            interpretation += f"{len(dominant_clusters)} segment(s) dominant(s) (>30%). "
        
        return interpretation
    
    def _generate_kruskal_recommendations(self, descriptive_stats, post_hoc_results):
        """Génère des recommandations basées sur Kruskal-Wallis"""
        recommendations = []
        
        # Trouver le groupe le plus performant
        best_group = max(descriptive_stats, key=lambda x: x['mean'])
        worst_group = min(descriptive_stats, key=lambda x: x['mean'])
        
        recommendations.append(f"Focus sur {best_group['group']}: Groupe le plus performant (moyenne: {best_group['mean']:.2f})")
        recommendations.append(f"Améliorer {worst_group['group']}: Groupe le moins performant (moyenne: {worst_group['mean']:.2f})")
        
        # Recommandations basées sur les post-hoc
        significant_pairs = [pair for pair in post_hoc_results if pair['significant']]
        if significant_pairs:
            recommendations.append(f"Analyser les différences entre {len(significant_pairs)} paires significatives")
        
        return recommendations
    
    def _generate_spearman_recommendations(self, correlation, strength_interpretation):
        """Génère des recommandations basées sur Spearman"""
        recommendations = []
        
        if abs(correlation) >= 0.7:
            recommendations.append("Exploiter cette forte corrélation pour optimiser vos stratégies")
            recommendations.append("Utiliser cette relation pour prédire les performances")
        elif abs(correlation) >= 0.5:
            recommendations.append("Tester cette corrélation modérée avec différents types de contenu")
            recommendations.append("Surveiller cette relation dans le temps")
        else:
            recommendations.append("Chercher d'autres variables explicatives")
            recommendations.append("Analyser les facteurs qualitatifs non mesurés")
        
        return recommendations
    
    def _generate_chi_square_recommendations(self, contingency_table, cramers_v):
        """Génère des recommandations basées sur Chi-carré"""
        recommendations = []
        
        if cramers_v >= 0.3:
            recommendations.append("Association forte détectée - Personnaliser le contenu par catégorie")
            recommendations.append("Exploiter cette relation pour segmenter votre audience")
        elif cramers_v >= 0.1:
            recommendations.append("Association modérée - Tester des stratégies différenciées")
            recommendations.append("Surveiller l'évolution de cette association")
        else:
            recommendations.append("Association faible - Explorer d'autres variables catégorielles")
            recommendations.append("Considérer des approches non-catégorielles")
        
        return recommendations
    
    def _generate_regression_recommendations(self, model_results, best_model):
        """Génère des recommandations basées sur la régression"""
        recommendations = []
        best_performance = model_results[best_model]
        
        if best_performance['test_r2'] >= 0.7:
            recommendations.append("Modèle fiable - Utiliser pour la planification stratégique")
            recommendations.append("Optimiser les variables les plus importantes")
        elif best_performance['test_r2'] >= 0.5:
            recommendations.append("Modèle acceptable - Améliorer avec plus de données")
            recommendations.append("Tester d'autres variables explicatives")
        else:
            recommendations.append("Modèle peu fiable - Revoir l'approche analytique")
            recommendations.append("Considérer des méthodes non-linéaires")
        
        if best_performance['overfitting']:
            recommendations.append("Réduire la complexité du modèle")
            recommendations.append("Augmenter la taille de l'échantillon")
        
        return recommendations
    
    def _generate_cluster_recommendations(self, cluster_analysis):
        """Génère des recommandations basées sur le clustering"""
        recommendations = []
        
        # Recommandations par cluster
        for cluster in cluster_analysis:
            if cluster['percentage'] > 30:
                recommendations.append(f"Segment {cluster['cluster']}: Segment majoritaire ({cluster['percentage']:.1f}%) - Stratégie principale")
            elif cluster['percentage'] > 15:
                recommendations.append(f"Segment {cluster['cluster']}: Segment important ({cluster['percentage']:.1f}%) - Stratégie secondaire")
            else:
                recommendations.append(f"Segment {cluster['cluster']}: Segment niche ({cluster['percentage']:.1f}%) - Approche spécialisée")
        
        return recommendations
    
    def get_comprehensive_report(self):
        """Génère un rapport complet de toutes les analyses"""
        report = {
            'summary': {
                'total_analyses': len(self.results),
                'analyses_performed': list(self.results.keys()),
                'data_shape': self.df.shape,
                'missing_data': self.df.isnull().sum().to_dict()
            },
            'detailed_results': self.results,
            'recommendations': self._generate_overall_recommendations()
        }
        
        return report
    
    def _generate_overall_recommendations(self):
        """Génère des recommandations globales"""
        recommendations = []
        
        # Recommandations basées sur les résultats
        if 'advanced_kruskal_wallis' in self.results:
            kruskal_result = self.results['advanced_kruskal_wallis']
            if kruskal_result['significant']:
                recommendations.append("Différences significatives entre groupes détectées - Personnaliser les stratégies")
        
        if 'advanced_spearman' in self.results:
            spearman_result = self.results['advanced_spearman']
            if abs(spearman_result['correlation_coefficient']) >= 0.7:
                recommendations.append("Forte corrélation détectée - Exploiter cette relation pour l'optimisation")
        
        if 'advanced_regression' in self.results:
            regression_result = self.results['advanced_regression']
            best_r2 = regression_result['best_model_performance']['test_r2']
            if best_r2 >= 0.7:
                recommendations.append("Modèle prédictif fiable - Utiliser pour la planification")
        
        return recommendations


