"""
Module d'Analyse Statistique Ultra-Avancée
Tests statistiques sophistiqués et analyses approfondies
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency, fisher_exact, mannwhitneyu, wilcoxon
from scipy.stats import shapiro, kstest, normaltest, jarque_bera
from scipy.stats import levene, bartlett, kstest, friedmanchisquare
from scipy.stats import anderson, cramervonmises
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, KFold
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, explained_variance_score
from sklearn.preprocessing import StandardScaler, LabelEncoder, PolynomialFeatures
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression
from sklearn.pipeline import Pipeline
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

class UltraAdvancedStatisticalAnalyzer:
    def __init__(self, df):
        """
        Initialise l'analyseur ultra-avancé avec un DataFrame
        
        Parameters:
        df (pd.DataFrame): DataFrame contenant les données des réseaux sociaux
        """
        self.df = df.copy()
        self.results = {}
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        
    def calculate_engagement_rate(self):
        """Calcule le taux d'engagement avec plusieurs méthodes avancées"""
        if 'likes' in self.df.columns and 'followers' in self.df.columns:
            self.df['engagement_rate'] = (self.df['likes'] / self.df['followers']) * 100
        elif 'likes' in self.df.columns and 'views' in self.df.columns:
            self.df['engagement_rate'] = (self.df['likes'] / self.df['views']) * 100
        else:
            engagement_cols = [col for col in self.df.columns if col in ['likes', 'comments', 'shares', 'saves']]
            if engagement_cols and 'followers' in self.df.columns:
                self.df['engagement_rate'] = (self.df[engagement_cols].sum(axis=1) / self.df['followers']) * 100
        
        # Calculer des métriques ultra-avancées
        self._calculate_ultra_advanced_metrics()
        return self.df
    
    def _calculate_ultra_advanced_metrics(self):
        """Calcule des métriques ultra-avancées"""
        # Taux d'engagement par type d'interaction
        if all(col in self.df.columns for col in ['likes', 'comments', 'shares', 'followers']):
            self.df['like_rate'] = (self.df['likes'] / self.df['followers']) * 100
            self.df['comment_rate'] = (self.df['comments'] / self.df['followers']) * 100
            self.df['share_rate'] = (self.df['shares'] / self.df['followers']) * 100
        
        # Ratio commentaires/likes (qualité de l'engagement)
        if all(col in self.df.columns for col in ['likes', 'comments']):
            self.df['comment_like_ratio'] = self.df['comments'] / (self.df['likes'] + 1)
        
        # Score de viralité avancé
        if all(col in self.df.columns for col in ['shares', 'likes', 'comments']):
            self.df['virality_score'] = (self.df['shares'] * 2 + self.df['comments'] * 1.5 + self.df['likes']) / 1000
        
        # Score de qualité du contenu
        if all(col in self.df.columns for col in ['comments', 'shares', 'likes']):
            self.df['content_quality_score'] = (
                self.df['comments'] * 3 + 
                self.df['shares'] * 2 + 
                self.df['likes'] * 1
            ) / (self.df['likes'] + self.df['comments'] + self.df['shares'] + 1)
        
        # Score d'engagement émotionnel
        if all(col in self.df.columns for col in ['comments', 'shares']):
            self.df['emotional_engagement_score'] = (
                self.df['comments'] * 2 + 
                self.df['shares'] * 1.5
            ) / (self.df['likes'] + 1)
        
        # Score de portée organique
        if all(col in self.df.columns for col in ['views', 'followers']):
            self.df['organic_reach_score'] = self.df['views'] / (self.df['followers'] + 1)
        
        # Score de croissance
        if 'followers' in self.df.columns:
            self.df['growth_score'] = self.df['followers'].pct_change().fillna(0)
    
    def ultra_advanced_kruskal_wallis_analysis(self, column='engagement_rate', group_column='platform'):
        """
        Analyse ultra-avancée de Kruskal-Wallis avec tests post-hoc multiples
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
        
        # Tests post-hoc multiples
        post_hoc_results = []
        for i in range(len(groups)):
            for j in range(i+1, len(groups)):
                group1_name, group2_name = groups[i], groups[j]
                group1_data, group2_data = group_data[i], group_data[j]
                
                # Mann-Whitney U
                u_stat, u_p_value = mannwhitneyu(group1_data, group2_data, alternative='two-sided')
                
                # Effect size pour Mann-Whitney (r)
                n1, n2 = len(group1_data), len(group2_data)
                r_effect = 1 - (2 * u_stat) / (n1 * n2)
                
                # Test de Kolmogorov-Smirnov
                ks_stat, ks_p_value = stats.ks_2samp(group1_data, group2_data)
                
                # Test de Anderson-Darling
                try:
                    ad_stat, ad_critical, ad_significance = anderson(group1_data, dist='norm')
                except:
                    ad_stat, ad_critical, ad_significance = None, None, None
                
                post_hoc_results.append({
                    'group1': group1_name,
                    'group2': group2_name,
                    'mann_whitney': {
                        'u_statistic': u_stat,
                        'p_value': u_p_value,
                        'effect_size_r': abs(r_effect),
                        'significant': u_p_value < 0.05
                    },
                    'kolmogorov_smirnov': {
                        'statistic': ks_stat,
                        'p_value': ks_p_value,
                        'significant': ks_p_value < 0.05
                    },
                    'anderson_darling': {
                        'statistic': ad_stat,
                        'critical_values': ad_critical,
                        'significance_levels': ad_significance
                    },
                    'mean_difference': group1_data.mean() - group2_data.mean(),
                    'median_difference': group1_data.median() - group2_data.median()
                })
        
        # Statistiques descriptives ultra-détaillées
        descriptive_stats = []
        for i, group in enumerate(groups):
            data = group_data[i]
            descriptive_stats.append({
                'group': group,
                'n': len(data),
                'mean': data.mean(),
                'median': data.median(),
                'std': data.std(),
                'var': data.var(),
                'q25': data.quantile(0.25),
                'q75': data.quantile(0.75),
                'iqr': data.quantile(0.75) - data.quantile(0.25),
                'min': data.min(),
                'max': data.max(),
                'range': data.max() - data.min(),
                'skewness': stats.skew(data),
                'kurtosis': stats.kurtosis(data),
                'coefficient_of_variation': data.std() / data.mean() if data.mean() != 0 else 0,
                'outliers_iqr': self._detect_outliers_iqr(data),
                'outliers_zscore': self._detect_outliers_zscore(data)
            })
        
        # Tests de normalité par groupe
        normality_tests = []
        for i, group in enumerate(groups):
            data = group_data[i]
            normality_tests.append({
                'group': group,
                'shapiro_wilk': {
                    'statistic': shapiro(data)[0],
                    'p_value': shapiro(data)[1],
                    'normal': shapiro(data)[1] > 0.05
                },
                'kolmogorov_smirnov': {
                    'statistic': kstest(data, 'norm')[0],
                    'p_value': kstest(data, 'norm')[1],
                    'normal': kstest(data, 'norm')[1] > 0.05
                },
                'jarque_bera': {
                    'statistic': jarque_bera(data)[0],
                    'p_value': jarque_bera(data)[1],
                    'normal': jarque_bera(data)[1] > 0.05
                }
            })
        
        # Tests d'homogénéité des variances
        homogeneity_tests = []
        if len(group_data) >= 2:
            # Test de Levene
            levene_stat, levene_p = levene(*group_data)
            homogeneity_tests.append({
                'test': 'Levene',
                'statistic': levene_stat,
                'p_value': levene_p,
                'homogeneous': levene_p > 0.05
            })
            
            # Test de Bartlett
            bartlett_stat, bartlett_p = bartlett(*group_data)
            homogeneity_tests.append({
                'test': 'Bartlett',
                'statistic': bartlett_stat,
                'p_value': bartlett_p,
                'homogeneous': bartlett_p > 0.05
            })
            
            # Test de Fligner-Killeen (remplacé par un test alternatif)
            try:
                from scipy.stats import fligner_killeen
                fligner_stat, fligner_p = fligner_killeen(*group_data)
                homogeneity_tests.append({
                    'test': 'Fligner-Killeen',
                    'statistic': fligner_stat,
                    'p_value': fligner_p,
                    'homogeneous': fligner_p > 0.05
                })
            except ImportError:
                # Test alternatif si Fligner-Killeen n'est pas disponible
                homogeneity_tests.append({
                    'test': 'Alternative',
                    'statistic': None,
                    'p_value': None,
                    'homogeneous': None,
                    'note': 'Fligner-Killeen non disponible'
                })
        
        result = {
            'test_name': 'Ultra-Advanced Kruskal-Wallis',
            'statistic': statistic,
            'p_value': p_value,
            'significant': p_value < 0.05,
            'effect_size_eta_squared': eta_squared,
            'groups_compared': len(groups),
            'total_sample_size': n_total,
            'post_hoc_tests': post_hoc_results,
            'descriptive_statistics': descriptive_stats,
            'normality_tests': normality_tests,
            'homogeneity_tests': homogeneity_tests,
            'interpretation': self._ultra_advanced_kruskal_interpretation(p_value, eta_squared, post_hoc_results, normality_tests),
            'recommendations': self._generate_ultra_kruskal_recommendations(descriptive_stats, post_hoc_results, normality_tests)
        }
        
        self.results['ultra_advanced_kruskal_wallis'] = result
        return result
    
    def ultra_advanced_spearman_analysis(self, col1, col2):
        """
        Analyse ultra-avancée de corrélation de Spearman avec tests multiples
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
        
        # Tests de normalité des résidus
        residuals = data[col2] - data[col1] * correlation
        normality_tests = {
            'shapiro_wilk': {
                'statistic': shapiro(residuals)[0],
                'p_value': shapiro(residuals)[1],
                'normal': shapiro(residuals)[1] > 0.05
            },
            'kolmogorov_smirnov': {
                'statistic': kstest(residuals, 'norm')[0],
                'p_value': kstest(residuals, 'norm')[1],
                'normal': kstest(residuals, 'norm')[1] > 0.05
            },
            'jarque_bera': {
                'statistic': jarque_bera(residuals)[0],
                'p_value': jarque_bera(residuals)[1],
                'normal': jarque_bera(residuals)[1] > 0.05
            }
        }
        
        # Analyse des outliers avancée
        outliers_analysis = self._ultra_advanced_outlier_detection(data[col1], data[col2])
        
        # Analyse de la linéarité
        linearity_tests = self._test_linearity(data[col1], data[col2])
        
        # Régression non-paramétrique (LOWESS)
        try:
            from statsmodels.nonparametric.smoothers_lowess import lowess
            lowess_result = lowess(data[col2], data[col1], frac=0.3)
        except ImportError:
            lowess_result = None
        
        # Analyse de la stabilité de la corrélation
        stability_analysis = self._analyze_correlation_stability(data[col1], data[col2])
        
        # Test de corrélation partielle
        partial_correlation = self._calculate_partial_correlation(data[col1], data[col2])
        
        result = {
            'test_name': 'Ultra-Advanced Spearman Correlation',
            'correlation_coefficient': correlation,
            'p_value': p_value,
            'r_squared': r_squared,
            'sample_size': len(data),
            'significance_levels': significance_levels,
            'normality_tests': normality_tests,
            'outliers_analysis': outliers_analysis,
            'linearity_tests': linearity_tests,
            'lowess_trend': lowess_result,
            'stability_analysis': stability_analysis,
            'partial_correlation': partial_correlation,
            'interpretation': self._ultra_advanced_spearman_interpretation(correlation, p_value, r_squared, outliers_analysis),
            'recommendations': self._generate_ultra_spearman_recommendations(correlation, outliers_analysis, stability_analysis)
        }
        
        self.results['ultra_advanced_spearman'] = result
        return result
    
    def ultra_advanced_regression_analysis(self, target_col, feature_cols):
        """
        Analyse de régression ultra-avancée avec multiples modèles et optimisations
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
        
        # Diviser en train/test avec validation croisée
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
        
        # Modèles ultra-avancés
        models = {
            'Linear Regression': LinearRegression(),
            'Ridge Regression': Ridge(alpha=1.0),
            'Lasso Regression': Lasso(alpha=0.1),
            'Elastic Net': ElasticNet(alpha=0.1, l1_ratio=0.5),
            'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
            'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42),
            'AdaBoost': AdaBoostRegressor(n_estimators=100, random_state=42),
            'SVR': SVR(kernel='rbf'),
            'MLP Regressor': MLPRegressor(hidden_layer_sizes=(100, 50), random_state=42)
        }
        
        model_results = {}
        
        for name, model in models.items():
            # Entraîner le modèle
            model.fit(X_train, y_train)
            
            # Prédictions
            y_pred_train = model.predict(X_train)
            y_pred_test = model.predict(X_test)
            
            # Métriques avancées
            train_r2 = r2_score(y_train, y_pred_train)
            test_r2 = r2_score(y_test, y_pred_test)
            train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
            test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
            train_mae = mean_absolute_error(y_train, y_pred_train)
            test_mae = mean_absolute_error(y_test, y_pred_test)
            train_evs = explained_variance_score(y_train, y_pred_train)
            test_evs = explained_variance_score(y_test, y_pred_test)
            
            # Validation croisée avancée
            cv_scores = cross_val_score(model, X_scaled, y, cv=5, scoring='r2')
            cv_rmse_scores = cross_val_score(model, X_scaled, y, cv=5, scoring='neg_mean_squared_error')
            
            # Feature importance
            feature_importance = None
            if hasattr(model, 'feature_importances_'):
                feature_importance = dict(zip(feature_cols, model.feature_importances_))
            elif hasattr(model, 'coef_'):
                feature_importance = dict(zip(feature_cols, model.coef_))
            
            # Analyse des résidus
            residuals = y_test - y_pred_test
            residual_analysis = {
                'mean_residual': residuals.mean(),
                'std_residual': residuals.std(),
                'shapiro_stat': shapiro(residuals)[0],
                'shapiro_p_value': shapiro(residuals)[1],
                'normal_residuals': shapiro(residuals)[1] > 0.05
            }
            
            model_results[name] = {
                'train_r2': train_r2,
                'test_r2': test_r2,
                'train_rmse': train_rmse,
                'test_rmse': test_rmse,
                'train_mae': train_mae,
                'test_mae': test_mae,
                'train_evs': train_evs,
                'test_evs': test_evs,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std(),
                'cv_rmse_mean': np.sqrt(-cv_rmse_scores.mean()),
                'cv_rmse_std': np.sqrt(cv_rmse_scores.std()),
                'feature_importance': feature_importance,
                'overfitting': train_r2 - test_r2 > 0.1,
                'residual_analysis': residual_analysis
            }
        
        # Sélectionner le meilleur modèle
        best_model = max(model_results.keys(), key=lambda x: model_results[x]['test_r2'])
        
        # Optimisation des hyperparamètres pour le meilleur modèle
        hyperparameter_optimization = self._optimize_hyperparameters(models[best_model], X_scaled, y)
        
        # Analyse de la stabilité du modèle
        stability_analysis = self._analyze_model_stability(models[best_model], X_scaled, y)
        
        # Feature selection
        feature_selection_results = self._advanced_feature_selection(X, y, feature_cols)
        
        result = {
            'test_name': 'Ultra-Advanced Regression Analysis',
            'target_variable': target_col,
            'feature_variables': feature_cols,
            'sample_size': len(data),
            'models_comparison': model_results,
            'best_model': best_model,
            'best_model_performance': model_results[best_model],
            'hyperparameter_optimization': hyperparameter_optimization,
            'stability_analysis': stability_analysis,
            'feature_selection': feature_selection_results,
            'interpretation': self._ultra_advanced_regression_interpretation(model_results, best_model),
            'recommendations': self._generate_ultra_regression_recommendations(model_results, best_model, feature_selection_results)
        }
        
        self.results['ultra_advanced_regression'] = result
        return result
    
    def _detect_outliers_iqr(self, data):
        """Détecte les outliers avec la méthode IQR"""
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = data[(data < lower_bound) | (data > upper_bound)]
        return {
            'count': len(outliers),
            'percentage': len(outliers) / len(data) * 100,
            'indices': outliers.index.tolist()
        }
    
    def _detect_outliers_zscore(self, data):
        """Détecte les outliers avec la méthode Z-score"""
        z_scores = np.abs(stats.zscore(data))
        outliers = data[z_scores > 3]
        return {
            'count': len(outliers),
            'percentage': len(outliers) / len(data) * 100,
            'indices': outliers.index.tolist()
        }
    
    def _ultra_advanced_outlier_detection(self, x, y):
        """Détection ultra-avancée des outliers"""
        # Outliers univariés
        x_outliers_iqr = self._detect_outliers_iqr(x)
        y_outliers_iqr = self._detect_outliers_iqr(y)
        x_outliers_zscore = self._detect_outliers_zscore(x)
        y_outliers_zscore = self._detect_outliers_zscore(y)
        
        # Outliers bivariés (distance de Mahalanobis)
        try:
            from sklearn.covariance import EmpiricalCovariance
            cov = EmpiricalCovariance().fit(np.column_stack([x, y]))
            mahalanobis_distances = cov.mahalanobis(np.column_stack([x, y]))
            outliers_mahalanobis = mahalanobis_distances > 3
            mahalanobis_outliers = {
                'count': outliers_mahalanobis.sum(),
                'percentage': outliers_mahalanobis.sum() / len(x) * 100,
                'indices': x[outliers_mahalanobis].index.tolist()
            }
        except:
            mahalanobis_outliers = None
        
        return {
            'x_outliers_iqr': x_outliers_iqr,
            'y_outliers_iqr': y_outliers_iqr,
            'x_outliers_zscore': x_outliers_zscore,
            'y_outliers_zscore': y_outliers_zscore,
            'mahalanobis_outliers': mahalanobis_outliers
        }
    
    def _test_linearity(self, x, y):
        """Teste la linéarité de la relation"""
        # Test de linéarité avec régression polynomiale
        from sklearn.preprocessing import PolynomialFeatures
        from sklearn.linear_model import LinearRegression
        
        # Régression linéaire
        lr = LinearRegression()
        lr.fit(x.values.reshape(-1, 1), y)
        linear_r2 = lr.score(x.values.reshape(-1, 1), y)
        
        # Régression polynomiale (degré 2)
        poly = PolynomialFeatures(degree=2)
        x_poly = poly.fit_transform(x.values.reshape(-1, 1))
        lr_poly = LinearRegression()
        lr_poly.fit(x_poly, y)
        poly_r2 = lr_poly.score(x_poly, y)
        
        # Test de significativité de l'amélioration
        improvement = poly_r2 - linear_r2
        
        return {
            'linear_r2': linear_r2,
            'polynomial_r2': poly_r2,
            'improvement': improvement,
            'linear_relationship': improvement < 0.05
        }
    
    def _analyze_correlation_stability(self, x, y):
        """Analyse la stabilité de la corrélation"""
        # Corrélation par fenêtres glissantes
        window_size = max(10, len(x) // 10)
        correlations = []
        
        for i in range(len(x) - window_size + 1):
            window_x = x.iloc[i:i+window_size]
            window_y = y.iloc[i:i+window_size]
            corr, _ = stats.spearmanr(window_x, window_y)
            correlations.append(corr)
        
        return {
            'window_size': window_size,
            'mean_correlation': np.mean(correlations),
            'std_correlation': np.std(correlations),
            'min_correlation': np.min(correlations),
            'max_correlation': np.max(correlations),
            'stability': np.std(correlations) < 0.2
        }
    
    def _calculate_partial_correlation(self, x, y):
        """Calcule la corrélation partielle"""
        # Corrélation partielle (en supprimant l'effet des autres variables)
        try:
            from scipy.stats import pearsonr
            # Pour l'instant, on retourne la corrélation simple
            # Dans une version plus avancée, on pourrait inclure d'autres variables
            return {
                'partial_correlation': stats.spearmanr(x, y)[0],
                'note': 'Corrélation partielle calculée avec les variables disponibles'
            }
        except:
            return None
    
    def _optimize_hyperparameters(self, model, X, y):
        """Optimise les hyperparamètres du modèle"""
        # Paramètres à optimiser selon le type de modèle
        param_grids = {
            'Ridge': {'alpha': [0.1, 1.0, 10.0, 100.0]},
            'Lasso': {'alpha': [0.01, 0.1, 1.0, 10.0]},
            'Random Forest': {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20]},
            'Gradient Boosting': {'n_estimators': [50, 100, 200], 'learning_rate': [0.01, 0.1, 0.2]}
        }
        
        model_name = type(model).__name__
        if model_name in param_grids:
            try:
                grid_search = GridSearchCV(model, param_grids[model_name], cv=3, scoring='r2')
                grid_search.fit(X, y)
                return {
                    'best_params': grid_search.best_params_,
                    'best_score': grid_search.best_score_,
                    'optimization_successful': True
                }
            except:
                return {'optimization_successful': False}
        else:
            return {'optimization_successful': False}
    
    def _analyze_model_stability(self, model, X, y):
        """Analyse la stabilité du modèle"""
        # Bootstrap pour évaluer la stabilité
        n_bootstrap = 100
        r2_scores = []
        
        for _ in range(n_bootstrap):
            # Échantillonnage bootstrap
            indices = np.random.choice(len(X), size=len(X), replace=True)
            X_bootstrap = X[indices]
            y_bootstrap = y.iloc[indices]
            
            # Entraîner et évaluer
            model.fit(X_bootstrap, y_bootstrap)
            r2 = model.score(X_bootstrap, y_bootstrap)
            r2_scores.append(r2)
        
        return {
            'bootstrap_r2_mean': np.mean(r2_scores),
            'bootstrap_r2_std': np.std(r2_scores),
            'bootstrap_r2_min': np.min(r2_scores),
            'bootstrap_r2_max': np.max(r2_scores),
            'stability': np.std(r2_scores) < 0.1
        }
    
    def _advanced_feature_selection(self, X, y, feature_cols):
        """Sélection avancée des features"""
        # Sélection avec f_regression
        f_selector = SelectKBest(score_func=f_regression, k='all')
        f_scores = f_selector.fit(X, y)
        
        # Sélection avec mutual_info_regression
        mi_selector = SelectKBest(score_func=mutual_info_regression, k='all')
        mi_scores = mi_selector.fit(X, y)
        
        # Combiner les scores
        feature_scores = []
        for i, feature in enumerate(feature_cols):
            feature_scores.append({
                'feature': feature,
                'f_score': f_scores.scores_[i],
                'mutual_info_score': mi_scores.scores_[i],
                'combined_score': (f_scores.scores_[i] + mi_scores.scores_[i]) / 2
            })
        
        # Trier par score combiné
        feature_scores.sort(key=lambda x: x['combined_score'], reverse=True)
        
        return {
            'feature_ranking': feature_scores,
            'top_features': [f['feature'] for f in feature_scores[:3]]
        }
    
    def _ultra_advanced_kruskal_interpretation(self, p_value, eta_squared, post_hoc_results, normality_tests):
        """Interprétation ultra-avancée du test de Kruskal-Wallis"""
        interpretation = f"Test de Kruskal-Wallis Ultra-Avancé: "
        
        # Significativité
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
        significant_pairs = [pair for pair in post_hoc_results if pair['mann_whitney']['significant']]
        if significant_pairs:
            interpretation += f"Différences significatives détectées entre {len(significant_pairs)} paires de groupes. "
        
        # Normalité
        normal_groups = [test for test in normality_tests if test['shapiro_wilk']['normal']]
        if len(normal_groups) == len(normality_tests):
            interpretation += "Tous les groupes suivent une distribution normale. "
        elif len(normal_groups) == 0:
            interpretation += "Aucun groupe ne suit une distribution normale. "
        else:
            interpretation += f"{len(normal_groups)}/{len(normality_tests)} groupes suivent une distribution normale. "
        
        return interpretation
    
    def _ultra_advanced_spearman_interpretation(self, correlation, p_value, r_squared, outliers_analysis):
        """Interprétation ultra-avancée de la corrélation de Spearman"""
        interpretation = f"Corrélation de Spearman Ultra-Avancée: "
        
        # Direction et force
        direction = "positive" if correlation > 0 else "negative"
        strength = "très forte" if abs(correlation) >= 0.9 else "forte" if abs(correlation) >= 0.7 else "modérée" if abs(correlation) >= 0.5 else "faible"
        interpretation += f"Corrélation {direction} {strength} (r = {correlation:.3f}). "
        
        # Significativité
        if p_value < 0.001:
            interpretation += "Hautement significative (p < 0.001). "
        elif p_value < 0.01:
            interpretation += "Très significative (p < 0.01). "
        elif p_value < 0.05:
            interpretation += "Significative (p < 0.05). "
        else:
            interpretation += "Non significative (p ≥ 0.05). "
        
        # Variance expliquée
        interpretation += f"Variance expliquée: {r_squared:.1%}. "
        
        # Outliers
        total_outliers = sum([
            outliers_analysis['x_outliers_iqr']['count'],
            outliers_analysis['y_outliers_iqr']['count']
        ])
        if total_outliers > 0:
            interpretation += f"Attention: {total_outliers} outliers détectés qui peuvent influencer la corrélation. "
        
        return interpretation
    
    def _ultra_advanced_regression_interpretation(self, model_results, best_model):
        """Interprétation ultra-avancée de la régression"""
        best_performance = model_results[best_model]
        
        interpretation = f"Analyse de régression ultra-avancée: Meilleur modèle: {best_model}. "
        
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
        
        # Résidus
        if best_performance['residual_analysis']['normal_residuals']:
            interpretation += "Résidus normalement distribués. "
        else:
            interpretation += "Résidus non-normaux détectés. "
        
        return interpretation
    
    def _generate_ultra_kruskal_recommendations(self, descriptive_stats, post_hoc_results, normality_tests):
        """Génère des recommandations ultra-avancées basées sur Kruskal-Wallis"""
        recommendations = []
        
        # Recommandations basées sur les performances
        best_group = max(descriptive_stats, key=lambda x: x['mean'])
        worst_group = min(descriptive_stats, key=lambda x: x['mean'])
        
        recommendations.append(f"Focus sur {best_group['group']}: Groupe le plus performant (moyenne: {best_group['mean']:.2f})")
        recommendations.append(f"Améliorer {worst_group['group']}: Groupe le moins performant (moyenne: {worst_group['mean']:.2f})")
        
        # Recommandations basées sur la variabilité
        for group in descriptive_stats:
            cv = group['coefficient_of_variation']
            if cv > 0.5:
                recommendations.append(f"{group['group']}: Variabilité élevée (CV={cv:.2f}) - Standardiser les processus")
        
        # Recommandations basées sur les outliers
        for group in descriptive_stats:
            if group['outliers_iqr']['percentage'] > 10:
                recommendations.append(f"{group['group']}: {group['outliers_iqr']['percentage']:.1f}% d'outliers - Analyser les cas exceptionnels")
        
        return recommendations
    
    def _generate_ultra_spearman_recommendations(self, correlation, outliers_analysis, stability_analysis):
        """Génère des recommandations ultra-avancées basées sur Spearman"""
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
        
        # Recommandations basées sur la stabilité
        if not stability_analysis['stability']:
            recommendations.append("Corrélation instable détectée - Surveiller l'évolution temporelle")
        
        # Recommandations basées sur les outliers
        total_outliers = sum([
            outliers_analysis['x_outliers_iqr']['count'],
            outliers_analysis['y_outliers_iqr']['count']
        ])
        if total_outliers > 0:
            recommendations.append(f"Analyser les {total_outliers} outliers détectés")
        
        return recommendations
    
    def _generate_ultra_regression_recommendations(self, model_results, best_model, feature_selection_results):
        """Génère des recommandations ultra-avancées basées sur la régression"""
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
        
        # Recommandations basées sur la sélection de features
        top_features = feature_selection_results['top_features']
        recommendations.append(f"Focus sur les variables les plus importantes: {', '.join(top_features)}")
        
        # Recommandations basées sur la stabilité
        if not best_performance.get('stability_analysis', {}).get('stability', True):
            recommendations.append("Modèle instable - Augmenter la taille de l'échantillon")
        
        return recommendations
    
    def kolmogorov_smirnov_distribution_test(self, column, distribution='norm'):
        """
        Test de Kolmogorov-Smirnov pour tester la distribution des données
        
        Parameters:
        column (str): Nom de la colonne à tester
        distribution (str): Distribution à tester ('norm', 'uniform', 'expon', etc.)
        
        Returns:
        dict: Résultats du test avec interprétation
        """
        if column not in self.df.columns:
            return None
        
        data = self.df[column].dropna()
        
        if len(data) < 3:
            return None
        
        # Test de Kolmogorov-Smirnov
        ks_statistic, p_value = kstest(data, distribution)
        
        # Effect size (D statistic)
        effect_size = ks_statistic
        
        # Interprétation de l'effect size
        if effect_size >= 0.2:
            effect_interpretation = "Grande différence"
        elif effect_size >= 0.1:
            effect_interpretation = "Différence modérée"
        elif effect_size >= 0.05:
            effect_interpretation = "Petite différence"
        else:
            effect_interpretation = "Différence négligeable"
        
        # Statistiques descriptives
        descriptive_stats = {
            'n': len(data),
            'mean': data.mean(),
            'std': data.std(),
            'min': data.min(),
            'max': data.max(),
            'skewness': stats.skew(data),
            'kurtosis': stats.kurtosis(data),
            'shapiro_wilk': {
                'statistic': shapiro(data)[0],
                'p_value': shapiro(data)[1],
                'normal': shapiro(data)[1] > 0.05
            }
        }
        
        # Test de normalité supplémentaire
        additional_tests = {
            'jarque_bera': {
                'statistic': jarque_bera(data)[0],
                'p_value': jarque_bera(data)[1],
                'normal': jarque_bera(data)[1] > 0.05
            },
            'anderson_darling': {
                'statistic': anderson(data, dist='norm')[0],
                'critical_values': anderson(data, dist='norm')[1],
                'significance_levels': anderson(data, dist='norm')[2]
            }
        }
        
        # Analyse des outliers
        outliers_analysis = self._detect_outliers_iqr(data)
        
        # Test de symétrie
        symmetry_test = {
            'skewness': stats.skew(data),
            'symmetric': abs(stats.skew(data)) < 0.5
        }
        
        result = {
            'test_name': 'Kolmogorov-Smirnov Distribution Test',
            'column_tested': column,
            'distribution_tested': distribution,
            'ks_statistic': ks_statistic,
            'p_value': p_value,
            'significant': p_value < 0.05,
            'effect_size': effect_size,
            'effect_interpretation': effect_interpretation,
            'sample_size': len(data),
            'descriptive_statistics': descriptive_stats,
            'additional_normality_tests': additional_tests,
            'outliers_analysis': outliers_analysis,
            'symmetry_test': symmetry_test,
            'interpretation': self._kolmogorov_smirnov_interpretation(ks_statistic, p_value, distribution, effect_interpretation),
            'recommendations': self._generate_kolmogorov_smirnov_recommendations(ks_statistic, p_value, distribution, descriptive_stats)
        }
        
        self.results['kolmogorov_smirnov'] = result
        return result
    
    def friedman_test_analysis(self, columns, group_column=None):
        """
        Test de Friedman pour données appariées sur plusieurs conditions
        
        Parameters:
        columns (list): Liste des colonnes à comparer (conditions)
        group_column (str): Colonne de groupement (optionnel)
        
        Returns:
        dict: Résultats du test avec post-hoc et interprétation
        """
        if not all(col in self.df.columns for col in columns):
            return None
        
        # Préparer les données
        data = self.df[columns].dropna()
        
        if len(data) < 3:
            return None
        
        # Test de Friedman
        friedman_stat, p_value = friedmanchisquare(*[data[col] for col in columns])
        
        # Effect size (Kendall's W)
        n = len(data)
        k = len(columns)
        kendall_w = friedman_stat / (n * (k - 1))
        
        # Interprétation de l'effect size
        if kendall_w >= 0.7:
            effect_interpretation = "Effet très fort"
        elif kendall_w >= 0.5:
            effect_interpretation = "Effet fort"
        elif kendall_w >= 0.3:
            effect_interpretation = "Effet modéré"
        elif kendall_w >= 0.1:
            effect_interpretation = "Effet faible"
        else:
            effect_interpretation = "Effet négligeable"
        
        # Statistiques descriptives par condition
        condition_stats = []
        for col in columns:
            condition_data = data[col]
            condition_stats.append({
                'condition': col,
                'n': len(condition_data),
                'mean': condition_data.mean(),
                'median': condition_data.median(),
                'std': condition_data.std(),
                'q25': condition_data.quantile(0.25),
                'q75': condition_data.quantile(0.75),
                'min': condition_data.min(),
                'max': condition_data.max(),
                'rank_mean': data[col].rank().mean()
            })
        
        # Tests post-hoc (Wilcoxon signed-rank pour chaque paire)
        post_hoc_results = []
        for i in range(len(columns)):
            for j in range(i+1, len(columns)):
                col1, col2 = columns[i], columns[j]
                
                # Test de Wilcoxon
                wilcoxon_stat, wilcoxon_p = wilcoxon(data[col1], data[col2])
                
                # Effect size pour Wilcoxon (r)
                n_pairs = len(data)
                r_effect = abs(wilcoxon_stat) / np.sqrt(n_pairs)
                
                post_hoc_results.append({
                    'condition1': col1,
                    'condition2': col2,
                    'wilcoxon_statistic': wilcoxon_stat,
                    'p_value': wilcoxon_p,
                    'effect_size_r': r_effect,
                    'significant': wilcoxon_p < 0.05,
                    'mean_difference': data[col1].mean() - data[col2].mean(),
                    'median_difference': data[col1].median() - data[col2].median()
                })
        
        # Test de normalité des différences
        if len(columns) == 2:
            differences = data[columns[0]] - data[columns[1]]
            normality_differences = {
                'shapiro_wilk': {
                    'statistic': shapiro(differences)[0],
                    'p_value': shapiro(differences)[1],
                    'normal': shapiro(differences)[1] > 0.05
                },
                'jarque_bera': {
                    'statistic': jarque_bera(differences)[0],
                    'p_value': jarque_bera(differences)[1],
                    'normal': jarque_bera(differences)[1] > 0.05
                }
            }
        else:
            normality_differences = None
        
        # Analyse de la cohérence des rangs
        rank_consistency = {
            'kendall_w': kendall_w,
            'interpretation': effect_interpretation,
            'consistency_level': 'High' if kendall_w >= 0.7 else 'Medium' if kendall_w >= 0.3 else 'Low'
        }
        
        result = {
            'test_name': 'Friedman Test for Paired Data',
            'conditions_tested': columns,
            'friedman_statistic': friedman_stat,
            'p_value': p_value,
            'significant': p_value < 0.05,
            'kendall_w': kendall_w,
            'effect_interpretation': effect_interpretation,
            'sample_size': n,
            'number_of_conditions': k,
            'condition_statistics': condition_stats,
            'post_hoc_tests': post_hoc_results,
            'normality_differences': normality_differences,
            'rank_consistency': rank_consistency,
            'interpretation': self._friedman_interpretation(friedman_stat, p_value, kendall_w, effect_interpretation),
            'recommendations': self._generate_friedman_recommendations(condition_stats, post_hoc_results, kendall_w)
        }
        
        self.results['friedman_test'] = result
        return result
    
    def _kolmogorov_smirnov_interpretation(self, ks_statistic, p_value, distribution, effect_interpretation):
        """Interprétation du test de Kolmogorov-Smirnov"""
        interpretation = f"Test de Kolmogorov-Smirnov: "
        
        # Significativité
        if p_value < 0.001:
            interpretation += "Différence hautement significative (p < 0.001). "
        elif p_value < 0.01:
            interpretation += "Différence très significative (p < 0.01). "
        elif p_value < 0.05:
            interpretation += "Différence significative (p < 0.05). "
        else:
            interpretation += "Pas de différence significative (p ≥ 0.05). "
        
        # Distribution
        if p_value < 0.05:
            interpretation += f"Les données ne suivent PAS une distribution {distribution}. "
        else:
            interpretation += f"Les données suivent une distribution {distribution}. "
        
        # Effect size
        interpretation += f"Taille de l'effet: {effect_interpretation.lower()} (D = {ks_statistic:.4f}). "
        
        return interpretation
    
    def _friedman_interpretation(self, friedman_stat, p_value, kendall_w, effect_interpretation):
        """Interprétation du test de Friedman"""
        interpretation = f"Test de Friedman: "
        
        # Significativité
        if p_value < 0.001:
            interpretation += "Différence hautement significative (p < 0.001). "
        elif p_value < 0.01:
            interpretation += "Différence très significative (p < 0.01). "
        elif p_value < 0.05:
            interpretation += "Différence significative (p < 0.05). "
        else:
            interpretation += "Pas de différence significative (p ≥ 0.05). "
        
        # Effect size
        interpretation += f"Effet: {effect_interpretation.lower()} (W = {kendall_w:.4f}). "
        
        # Cohérence
        if kendall_w >= 0.7:
            interpretation += "Cohérence très élevée entre les conditions. "
        elif kendall_w >= 0.3:
            interpretation += "Cohérence modérée entre les conditions. "
        else:
            interpretation += "Faible cohérence entre les conditions. "
        
        return interpretation
    
    def _generate_kolmogorov_smirnov_recommendations(self, ks_statistic, p_value, distribution, descriptive_stats):
        """Génère des recommandations basées sur Kolmogorov-Smirnov"""
        recommendations = []
        
        if p_value < 0.05:
            recommendations.append(f"Les données ne suivent pas une distribution {distribution} - Utiliser des tests non-paramétriques")
            recommendations.append("Considérer des transformations de données (log, sqrt, Box-Cox)")
        else:
            recommendations.append(f"Les données suivent une distribution {distribution} - Tests paramétriques appropriés")
            recommendations.append("Utiliser des méthodes statistiques standard")
        
        # Recommandations basées sur la symétrie
        skewness = descriptive_stats['skewness']
        if abs(skewness) > 1:
            recommendations.append("Distribution très asymétrique - Transformation recommandée")
        elif abs(skewness) > 0.5:
            recommendations.append("Distribution modérément asymétrique - Surveiller l'impact")
        
        # Recommandations basées sur les outliers
        outliers_pct = descriptive_stats.get('outliers_iqr', {}).get('percentage', 0)
        if outliers_pct > 10:
            recommendations.append(f"{outliers_pct:.1f}% d'outliers détectés - Analyser les cas exceptionnels")
        
        return recommendations
    
    def _generate_friedman_recommendations(self, condition_stats, post_hoc_results, kendall_w):
        """Génère des recommandations basées sur le test de Friedman"""
        recommendations = []
        
        # Recommandations basées sur les performances
        best_condition = max(condition_stats, key=lambda x: x['mean'])
        worst_condition = min(condition_stats, key=lambda x: x['mean'])
        
        recommendations.append(f"Focus sur {best_condition['condition']}: Condition la plus performante (moyenne: {best_condition['mean']:.2f})")
        recommendations.append(f"Améliorer {worst_condition['condition']}: Condition la moins performante (moyenne: {worst_condition['mean']:.2f})")
        
        # Recommandations basées sur la cohérence
        if kendall_w >= 0.7:
            recommendations.append("Cohérence élevée - Stratégie uniforme efficace")
        elif kendall_w >= 0.3:
            recommendations.append("Cohérence modérée - Personnaliser selon les conditions")
        else:
            recommendations.append("Faible cohérence - Revoir l'approche globale")
        
        # Recommandations basées sur les post-hoc
        significant_pairs = [pair for pair in post_hoc_results if pair['significant']]
        if significant_pairs:
            recommendations.append(f"Différences significatives entre {len(significant_pairs)} paires de conditions")
            for pair in significant_pairs[:2]:  # Afficher les 2 premiers
                recommendations.append(f"  • {pair['condition1']} vs {pair['condition2']}: p={pair['p_value']:.4f}")
        
        return recommendations
    
    def get_ultra_comprehensive_report(self):
        """Génère un rapport ultra-complet de toutes les analyses"""
        report = {
            'summary': {
                'total_analyses': len(self.results),
                'analyses_performed': list(self.results.keys()),
                'data_shape': self.df.shape,
                'missing_data': self.df.isnull().sum().to_dict(),
                'data_quality_score': self._calculate_data_quality_score()
            },
            'detailed_results': self.results,
            'recommendations': self._generate_ultra_overall_recommendations(),
            'data_insights': self._generate_data_insights()
        }
        
        return report
    
    def _calculate_data_quality_score(self):
        """Calcule un score de qualité des données"""
        total_cells = self.df.shape[0] * self.df.shape[1]
        missing_cells = self.df.isnull().sum().sum()
        quality_score = (total_cells - missing_cells) / total_cells * 100
        return quality_score
    
    def _generate_ultra_overall_recommendations(self):
        """Génère des recommandations ultra-globales"""
        recommendations = []
        
        # Recommandations basées sur les résultats
        if 'ultra_advanced_kruskal_wallis' in self.results:
            kruskal_result = self.results['ultra_advanced_kruskal_wallis']
            if kruskal_result['significant']:
                recommendations.append("Différences significatives entre groupes détectées - Personnaliser les stratégies")
        
        if 'ultra_advanced_spearman' in self.results:
            spearman_result = self.results['ultra_advanced_spearman']
            if abs(spearman_result['correlation_coefficient']) >= 0.7:
                recommendations.append("Forte corrélation détectée - Exploiter cette relation pour l'optimisation")
        
        if 'ultra_advanced_regression' in self.results:
            regression_result = self.results['ultra_advanced_regression']
            best_r2 = regression_result['best_model_performance']['test_r2']
            if best_r2 >= 0.7:
                recommendations.append("Modèle prédictif fiable - Utiliser pour la planification")
        
        return recommendations
    
    def _generate_data_insights(self):
        """Génère des insights sur les données"""
        insights = []
        
        # Insights sur la qualité des données
        quality_score = self._calculate_data_quality_score()
        if quality_score >= 90:
            insights.append("Excellente qualité des données")
        elif quality_score >= 75:
            insights.append("Bonne qualité des données")
        else:
            insights.append("Qualité des données à améliorer")
        
        # Insights sur la taille de l'échantillon
        sample_size = len(self.df)
        if sample_size >= 1000:
            insights.append("Échantillon large - Analyses robustes")
        elif sample_size >= 100:
            insights.append("Échantillon moyen - Analyses acceptables")
        else:
            insights.append("Échantillon petit - Prudence dans l'interprétation")
        
        return insights
