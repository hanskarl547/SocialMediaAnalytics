"""
Module de visualisations
Crée des graphiques interactifs pour l'analyse des données
"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

class DataVisualizer:
    def __init__(self, df):
        """
        Initialise le visualiseur avec un DataFrame
        
        Parameters:
        df (pd.DataFrame): DataFrame contenant les données
        """
        self.df = df
        self.color_palette = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F']
    
    def plot_engagement_comparison(self, group_by='platform'):
        """Graphique de comparaison de l'engagement par plateforme"""
        if group_by not in self.df.columns or 'engagement_rate' not in self.df.columns:
            return None
        
        # Calculer les moyennes par groupe
        engagement_by_group = self.df.groupby(group_by)['engagement_rate'].agg(['mean', 'std', 'count']).reset_index()
        engagement_by_group.columns = [group_by, 'mean_engagement', 'std_engagement', 'count']
        
        # Créer le graphique en barres
        fig = px.bar(
            engagement_by_group,
            x=group_by,
            y='mean_engagement',
            error_y='std_engagement',
            title=f'Taux d\'engagement moyen par {group_by}',
            labels={'mean_engagement': 'Taux d\'engagement (%)', group_by: group_by.capitalize()},
            color=group_by,
            color_discrete_sequence=self.color_palette,
            text='mean_engagement'
        )
        
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(
            height=500,
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        return fig
    
    def plot_likes_distribution(self, group_by='platform'):
        """Distribution des likes par plateforme avec box plot"""
        if 'likes' not in self.df.columns or group_by not in self.df.columns:
            return None
        
        fig = px.box(
            self.df,
            x=group_by,
            y='likes',
            title=f'Distribution des likes par {group_by}',
            labels={'likes': 'Nombre de likes', group_by: group_by.capitalize()},
            color=group_by,
            color_discrete_sequence=self.color_palette
        )
        
        fig.update_layout(
            height=500,
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        return fig
    
    def plot_correlation_heatmap(self):
        """Heatmap des corrélations entre variables numériques"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) < 2:
            return None
        
        # Calculer la matrice de corrélation
        corr_matrix = self.df[numeric_cols].corr()
        
        fig = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale='RdBu',
            zmid=0,
            text=corr_matrix.values,
            texttemplate='%{text:.2f}',
            textfont={"size": 10},
            colorbar=dict(title="Corrélation")
        ))
        
        fig.update_layout(
            title='Matrice de corrélation des métriques',
            height=600,
            width=700,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        return fig
    
    def plot_time_series(self, date_column='date', metric='likes', group_by='platform'):
        """Graphique d'évolution temporelle d'une métrique"""
        if date_column not in self.df.columns or metric not in self.df.columns:
            return None
        
        # Convertir en datetime si nécessaire
        if not pd.api.types.is_datetime64_any_dtype(self.df[date_column]):
            self.df[date_column] = pd.to_datetime(self.df[date_column], errors='coerce')
        
        if group_by in self.df.columns:
            fig = px.line(
                self.df.sort_values(date_column),
                x=date_column,
                y=metric,
                color=group_by,
                title=f'Évolution de {metric} dans le temps',
                labels={metric: metric.capitalize(), date_column: 'Date'},
                color_discrete_sequence=self.color_palette
            )
        else:
            fig = px.line(
                self.df.sort_values(date_column),
                x=date_column,
                y=metric,
                title=f'Évolution de {metric} dans le temps',
                labels={metric: metric.capitalize(), date_column: 'Date'}
            )
        
        fig.update_layout(
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        return fig
    
    def plot_scatter_with_regression(self, x_col, y_col, group_by='platform'):
        """Graphique de dispersion avec ligne de régression"""
        if x_col not in self.df.columns or y_col not in self.df.columns:
            return None
        
        if group_by in self.df.columns:
            fig = px.scatter(
                self.df,
                x=x_col,
                y=y_col,
                color=group_by,
                trendline="ols",
                title=f'Relation entre {x_col} et {y_col}',
                labels={x_col: x_col.capitalize(), y_col: y_col.capitalize()},
                color_discrete_sequence=self.color_palette
            )
        else:
            fig = px.scatter(
                self.df,
                x=x_col,
                y=y_col,
                trendline="ols",
                title=f'Relation entre {x_col} et {y_col}',
                labels={x_col: x_col.capitalize(), y_col: y_col.capitalize()}
            )
        
        fig.update_layout(
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        return fig
    
    def plot_top_performers(self, metric='likes', top_n=10, group_by='platform'):
        """Graphique des meilleurs performances"""
        if metric not in self.df.columns:
            return None
        
        # Obtenir les top N
        top_data = self.df.nlargest(top_n, metric)
        
        # Créer un identifiant unique pour chaque post
        if 'post_id' not in top_data.columns:
            top_data = top_data.copy()
            top_data['post_id'] = range(1, len(top_data) + 1)
        
        color_col = group_by if group_by in top_data.columns else None
        
        fig = px.bar(
            top_data,
            x='post_id',
            y=metric,
            color=color_col,
            title=f'Top {top_n} posts par {metric}',
            labels={metric: metric.capitalize(), 'post_id': 'Post ID'},
            color_discrete_sequence=self.color_palette
        )
        
        fig.update_layout(
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        return fig
    
    def plot_metric_distribution_histogram(self, metric='likes'):
        """Histogramme de distribution d'une métrique"""
        if metric not in self.df.columns:
            return None
        
        fig = px.histogram(
            self.df,
            x=metric,
            nbins=30,
            title=f'Distribution de {metric}',
            labels={metric: metric.capitalize(), 'count': 'Fréquence'},
            color_discrete_sequence=['#4ECDC4']
        )
        
        # Ajouter une ligne de moyenne
        mean_value = self.df[metric].mean()
        fig.add_vline(
            x=mean_value,
            line_dash="dash",
            line_color="red",
            annotation_text=f"Moyenne: {mean_value:.2f}",
            annotation_position="top"
        )
        
        fig.update_layout(
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            showlegend=False
        )
        
        return fig
    
    def plot_platform_comparison_radar(self, platforms=None):
        """Graphique radar pour comparer les plateformes sur plusieurs métriques"""
        if 'platform' not in self.df.columns:
            return None
        
        # Métriques à comparer
        metrics = []
        possible_metrics = ['engagement_rate', 'likes', 'comments', 'shares', 'views']
        
        for metric in possible_metrics:
            if metric in self.df.columns:
                metrics.append(metric)
        
        if len(metrics) < 3:
            return None
        
        if platforms is None:
            platforms = self.df['platform'].unique()[:5]  # Max 5 plateformes
        
        # Normaliser les données (0-100)
        normalized_data = []
        
        for platform in platforms:
            platform_data = self.df[self.df['platform'] == platform]
            values = []
            
            for metric in metrics:
                max_val = self.df[metric].max()
                min_val = self.df[metric].min()
                mean_val = platform_data[metric].mean()
                
                # Normalisation
                if max_val != min_val:
                    normalized = ((mean_val - min_val) / (max_val - min_val)) * 100
                else:
                    normalized = 50
                
                values.append(normalized)
            
            normalized_data.append({
                'platform': platform,
                'values': values + [values[0]]  # Fermer le radar
            })
        
        # Créer le graphique radar
        fig = go.Figure()
        
        for i, data in enumerate(normalized_data):
            fig.add_trace(go.Scatterpolar(
                r=data['values'],
                theta=metrics + [metrics[0]],
                fill='toself',
                name=data['platform'],
                line_color=self.color_palette[i % len(self.color_palette)]
            ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            showlegend=True,
            title='Comparaison multi-métriques des plateformes',
            height=600
        )
        
        return fig
    
    def plot_engagement_by_time(self, time_column='hour', metric='engagement_rate'):
        """Analyse de l'engagement par heure/jour"""
        if time_column not in self.df.columns or metric not in self.df.columns:
            return None
        
        engagement_by_time = self.df.groupby(time_column)[metric].mean().reset_index()
        
        fig = px.line(
            engagement_by_time,
            x=time_column,
            y=metric,
            title=f'{metric.capitalize()} moyen par {time_column}',
            labels={metric: metric.replace('_', ' ').capitalize(), time_column: time_column.capitalize()},
            markers=True
        )
        
        fig.update_traces(line_color='#4ECDC4', marker=dict(size=8))
        
        fig.update_layout(
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        return fig
    
    def create_dashboard(self):
        """Crée un tableau de bord avec plusieurs graphiques"""
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Engagement par plateforme', 'Distribution des likes', 
                          'Top posts', 'Tendance temporelle'),
            specs=[[{'type': 'bar'}, {'type': 'box'}],
                   [{'type': 'bar'}, {'type': 'scatter'}]]
        )
        
        # À implémenter selon les besoins spécifiques
        
        return fig

