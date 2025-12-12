"""
Module d'analyse statistique
Contient tous les tests statistiques et analyses
"""

import pandas as pd
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

class StatisticalAnalyzer:
    def __init__(self, df):
        """
        Initialise l'analyseur avec un DataFrame
        
        Parameters:
        df (pd.DataFrame): DataFrame contenant les données des réseaux sociaux
        """
        self.df = df
        self.results = {}
    
    def calculate_engagement_rate(self):
        """Calcule le taux d'engagement pour chaque plateforme"""
        if 'likes' in self.df.columns and 'followers' in self.df.columns:
            self.df['engagement_rate'] = (self.df['likes'] / self.df['followers']) * 100
        elif 'likes' in self.df.columns and 'views' in self.df.columns:
            self.df['engagement_rate'] = (self.df['likes'] / self.df['views']) * 100
        else:
            # Créer un taux d'engagement combiné
            engagement_cols = [col for col in self.df.columns if col in ['likes', 'comments', 'shares', 'saves']]
            if engagement_cols and 'followers' in self.df.columns:
                self.df['engagement_rate'] = (self.df[engagement_cols].sum(axis=1) / self.df['followers']) * 100
        
        return self.df
    
    def compare_platforms_engagement(self):
        """Compare le taux d'engagement entre différentes plateformes"""
        if 'platform' not in self.df.columns or 'engagement_rate' not in self.df.columns:
            return None
        
        platforms = self.df['platform'].unique()
        platform_data = []
        
        for platform in platforms:
            platform_df = self.df[self.df['platform'] == platform]
            platform_data.append({
                'platform': platform,
                'mean_engagement': platform_df['engagement_rate'].mean(),
                'median_engagement': platform_df['engagement_rate'].median(),
                'std_engagement': platform_df['engagement_rate'].std(),
                'count': len(platform_df)
            })
        
        return pd.DataFrame(platform_data)
    
    def kruskal_wallis_test(self, column='likes', group_column='platform'):
        """
        Test de Kruskal-Wallis pour comparer plusieurs groupes
        (Non-paramétrique, équivalent de l'ANOVA)
        """
        if column not in self.df.columns or group_column not in self.df.columns:
            return None
        
        groups = self.df[group_column].unique()
        group_data = [self.df[self.df[group_column] == group][column].dropna() for group in groups]
        
        # Filtrer les groupes vides
        group_data = [g for g in group_data if len(g) > 0]
        
        if len(group_data) < 2:
            return None
        
        statistic, p_value = stats.kruskal(*group_data)
        
        result = {
            'test': 'Kruskal-Wallis',
            'statistic': statistic,
            'p_value': p_value,
            'significant': p_value < 0.05,
            'column': column,
            'groups': group_column,
            'interpretation': self._interpret_kruskal_wallis(p_value, groups)
        }
        
        self.results['kruskal_wallis'] = result
        return result
    
    def wilcoxon_test(self, column1, column2):
        """
        Test de Wilcoxon pour comparer deux échantillons appariés
        """
        if column1 not in self.df.columns or column2 not in self.df.columns:
            return None
        
        data1 = self.df[column1].dropna()
        data2 = self.df[column2].dropna()
        
        # Assurer que les données ont la même longueur
        min_len = min(len(data1), len(data2))
        data1 = data1[:min_len]
        data2 = data2[:min_len]
        
        statistic, p_value = stats.wilcoxon(data1, data2)
        
        result = {
            'test': 'Wilcoxon',
            'statistic': statistic,
            'p_value': p_value,
            'significant': p_value < 0.05,
            'columns': [column1, column2],
            'interpretation': self._interpret_wilcoxon(p_value, column1, column2)
        }
        
        self.results['wilcoxon'] = result
        return result
    
    def spearman_correlation(self, column1='likes', column2='followers'):
        """
        Corrélation de Spearman (non-paramétrique)
        Mesure la relation monotone entre deux variables
        """
        if column1 not in self.df.columns or column2 not in self.df.columns:
            return None
        
        data1 = self.df[column1].dropna()
        data2 = self.df[column2].dropna()
        
        # Assurer que les données ont la même longueur
        valid_indices = self.df[[column1, column2]].dropna().index
        data1 = self.df.loc[valid_indices, column1]
        data2 = self.df.loc[valid_indices, column2]
        
        correlation, p_value = stats.spearmanr(data1, data2)
        
        result = {
            'test': 'Spearman Correlation',
            'correlation': correlation,
            'p_value': p_value,
            'significant': p_value < 0.05,
            'columns': [column1, column2],
            'interpretation': self._interpret_spearman(correlation, p_value, column1, column2)
        }
        
        self.results['spearman'] = result
        return result
    
    def chi2_test(self, column1, column2):
        """
        Test du Chi-carré pour tester l'indépendance entre deux variables catégorielles
        """
        if column1 not in self.df.columns or column2 not in self.df.columns:
            return None
        
        # Créer une table de contingence
        contingency_table = pd.crosstab(self.df[column1], self.df[column2])
        
        chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
        
        result = {
            'test': 'Chi-square',
            'chi2_statistic': chi2,
            'p_value': p_value,
            'degrees_of_freedom': dof,
            'significant': p_value < 0.05,
            'columns': [column1, column2],
            'contingency_table': contingency_table,
            'interpretation': self._interpret_chi2(p_value, column1, column2)
        }
        
        self.results['chi2'] = result
        return result
    
    def predict_metric(self, features, target, model_type='random_forest'):
        """
        Entraîne un modèle de régression sur une métrique cible.
        
        Parameters:
        features (list): colonnes utilisées comme variables explicatives
        target (str): colonne cible à prédire
        model_type (str): 'linear' ou 'random_forest'
        """
        if not features or target not in self.df.columns:
            return None
        
        available_features = [f for f in features if f in self.df.columns]
        if not available_features:
            return None
        
        df_clean = self.df[available_features + [target]].dropna()
        if len(df_clean) < 10:
            return None
        
        X = df_clean[available_features]
        y = df_clean[target]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = RandomForestRegressor(n_estimators=100, random_state=42) if model_type == 'random_forest' else LinearRegression()
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        result = {
            'model_type': model_type,
            'features': available_features,
            'target': target,
            'mse': mse,
            'rmse': np.sqrt(mse),
            'r2_score': r2,
            'model': model,
            'interpretation': self._interpret_prediction(r2, available_features, target)
        }
        
        self.results[f'prediction_{target}'] = result
        return result
    
    def predict_likes(self, features=['followers', 'views'], target='likes', model_type='random_forest'):
        """Compatibilité descendante pour la prédiction des likes."""
        return self.predict_metric(features, target, model_type)
    
    def predict_addiction(self, features=None, target=None, model_type='random_forest'):
        """
        Prédit un score d'addiction (ex: 'Addicted_Score') à partir de variables contextuelles.
        """
        target_candidates = ['addicted_score', 'addiction_score', 'addiction_risk', 'addiction']
        resolved_target = target or self._match_column_name(target_candidates)
        if not resolved_target:
            return None
        
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        available_features = [col for col in numeric_cols if col != resolved_target]
        
        if not available_features:
            return None
        
        if features:
            selected_features = [f for f in features if f in available_features]
        else:
            recommended = [
                'Avg_Daily_Usage_Hours',
                'Sleep_Hours_Per_Night',
                'Mental_Health_Score',
                'Conflicts_Over_Social_Media',
                'Affects_Academic_Performance'
            ]
            selected_features = [col for col in recommended if col in available_features]
            if not selected_features:
                selected_features = available_features[:min(3, len(available_features))]
        
        return self.predict_metric(selected_features, resolved_target, model_type)
    
    def predict_single(self, model_result, input_values):
        """
        Fait une prédiction pour une seule observation
        
        Parameters:
        model_result: Résultat du modèle de predict_likes
        input_values (dict): Dictionnaire avec les valeurs des features
        """
        if not model_result or 'model' not in model_result:
            return None
        
        model = model_result['model']
        features = model_result['features']
        
        # Créer un DataFrame avec les valeurs d'entrée
        input_df = pd.DataFrame([input_values])[features]
        
        prediction = model.predict(input_df)[0]
        
        return {
            'predicted_value': prediction,
            'input_values': input_values,
            'features_used': features
        }
    
    def _interpret_kruskal_wallis(self, p_value, groups):
        """Interprétation du test de Kruskal-Wallis"""
        if p_value < 0.05:
            return f"Il existe une différence significative entre les groupes ({', '.join(groups)}) pour cette métrique (p = {p_value:.4f})."
        else:
            return f"Il n'y a pas de différence significative entre les groupes ({', '.join(groups)}) pour cette métrique (p = {p_value:.4f})."
    
    def _interpret_wilcoxon(self, p_value, col1, col2):
        """Interprétation du test de Wilcoxon"""
        if p_value < 0.05:
            return f"Il existe une différence significative entre {col1} et {col2} (p = {p_value:.4f})."
        else:
            return f"Il n'y a pas de différence significative entre {col1} et {col2} (p = {p_value:.4f})."
    
    def _interpret_spearman(self, correlation, p_value, col1, col2):
        """Interprétation de la corrélation de Spearman"""
        strength = abs(correlation)
        
        if strength < 0.3:
            strength_text = "faible"
        elif strength < 0.7:
            strength_text = "modérée"
        else:
            strength_text = "forte"
        
        direction = "positive" if correlation > 0 else "négative"
        
        if p_value < 0.05:
            return f"Il existe une corrélation {strength_text} {direction} ({correlation:.3f}) entre {col1} et {col2} (p = {p_value:.4f})."
        else:
            return f"Aucune corrélation significative trouvée entre {col1} et {col2} (p = {p_value:.4f})."
    
    def _interpret_chi2(self, p_value, col1, col2):
        """Interprétation du test du Chi-carré"""
        if p_value < 0.05:
            return f"Il existe une association significative entre {col1} et {col2} (p = {p_value:.4f})."
        else:
            return f"Il n'y a pas d'association significative entre {col1} et {col2} (p = {p_value:.4f})."
    
    def _interpret_prediction(self, r2, features, target):
        """Interprétation du modèle de prédiction"""
        if r2 > 0.7:
            quality = "excellent"
        elif r2 > 0.5:
            quality = "bon"
        elif r2 > 0.3:
            quality = "modéré"
        else:
            quality = "faible"
        
        return f"Le modèle a un pouvoir prédictif {quality} (R² = {r2:.3f}). Les variables {', '.join(features)} expliquent {r2*100:.1f}% de la variance de {target}."
    
    def _match_column_name(self, candidates):
        """Retourne la première colonne correspondant (insensible à la casse)."""
        lower_map = {col.lower(): col for col in self.df.columns}
        for candidate in candidates:
            if candidate.lower() in lower_map:
                return lower_map[candidate.lower()]
        return None
    
    def get_all_results(self):
        """Retourne tous les résultats des analyses"""
        return self.results
    
    def summary_statistics(self):
        """Génère des statistiques descriptives"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        summary = {}
        for col in numeric_cols:
            summary[col] = {
                'mean': self.df[col].mean(),
                'median': self.df[col].median(),
                'std': self.df[col].std(),
                'min': self.df[col].min(),
                'max': self.df[col].max(),
                'q25': self.df[col].quantile(0.25),
                'q75': self.df[col].quantile(0.75)
            }
        
        return summary

