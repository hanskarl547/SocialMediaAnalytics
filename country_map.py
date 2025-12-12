"""
Module de visualisation géographique des données par pays
Affiche les cartes interactives avec taux d'engagement par pays
Utilise Plotly pour une meilleure compatibilité avec Streamlit
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pycountry
import numpy as np
import streamlit as st

class CountryMapVisualizer:
    """
    Classe pour créer des cartes interactives montrant l'engagement par pays
    """
    
    def __init__(self, df):
        """
        Initialise le visualiseur de cartes
        
        Parameters:
        df (pd.DataFrame): DataFrame contenant les données avec une colonne 'country'
        """
        self.df = df
    
    def _normalize_country_name(self, country_name):
        """
        Normalise le nom du pays pour correspondre aux données Natural Earth
        
        Parameters:
        country_name (str): Nom du pays à normaliser
        
        Returns:
        str: Nom normalisé du pays
        """
        if pd.isna(country_name):
            return None
        
        country_name = str(country_name).strip().upper()
        
        # Mapping manuel pour les cas courants
        country_mapping = {
            'USA': 'UNITED STATES OF AMERICA',
            'US': 'UNITED STATES OF AMERICA',
            'UK': 'UNITED KINGDOM',
            'RUSSIA': 'RUSSIAN FEDERATION',
            'SOUTH KOREA': 'KOREA, REPUBLIC OF',
            'NORTH KOREA': "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF",
            'VIETNAM': 'VIET NAM',
        }
        
        if country_name in country_mapping:
            country_name = country_mapping[country_name]
        
        # Essayer de trouver le pays avec pycountry
        try:
            country = pycountry.countries.search_fuzzy(country_name)[0]
            return country.name.upper()
        except:
            return country_name
    
    def calculate_engagement_by_country(self, country_column='country'):
        """
        Calcule le taux d'engagement moyen par pays
        
        Parameters:
        country_column (str): Nom de la colonne contenant les pays
        
        Returns:
        pd.DataFrame: DataFrame avec pays et métriques agrégées
        """
        if country_column not in self.df.columns:
            return None
        
        # Normaliser les noms de pays
        self.df['country_normalized'] = self.df[country_column].apply(
            self._normalize_country_name
        )
        
        # Filtrer les valeurs nulles
        df_with_country = self.df[self.df['country_normalized'].notna()].copy()
        
        if len(df_with_country) == 0:
            return None
        
        # Calculer les métriques par pays
        metrics = {}
        
        if 'engagement_rate' in df_with_country.columns:
            metrics['avg_engagement'] = df_with_country.groupby('country_normalized')['engagement_rate'].mean()
            metrics['median_engagement'] = df_with_country.groupby('country_normalized')['engagement_rate'].median()
        
        if 'likes' in df_with_country.columns:
            metrics['total_likes'] = df_with_country.groupby('country_normalized')['likes'].sum()
            metrics['avg_likes'] = df_with_country.groupby('country_normalized')['likes'].mean()
        
        if 'followers' in df_with_country.columns:
            metrics['avg_followers'] = df_with_country.groupby('country_normalized')['followers'].mean()
        
        if 'comments' in df_with_country.columns:
            metrics['total_comments'] = df_with_country.groupby('country_normalized')['comments'].sum()
        
        if 'views' in df_with_country.columns:
            metrics['total_views'] = df_with_country.groupby('country_normalized')['views'].sum()
        
        # Compter le nombre de posts par pays
        metrics['post_count'] = df_with_country.groupby('country_normalized').size()
        
        # Créer le DataFrame agrégé
        country_stats = pd.DataFrame(metrics)
        country_stats = country_stats.reset_index()
        country_stats.rename(columns={'country_normalized': 'country'}, inplace=True)
        
        return country_stats
    
    def create_interactive_map(self, country_stats, engagement_column='avg_engagement'):
        """
        Crée une carte choroplèthe interactive avec Plotly
        
        Parameters:
        country_stats (pd.DataFrame): Statistiques par pays
        engagement_column (str): Colonne à utiliser pour la couleur
        
        Returns:
        plotly.graph_objects.Figure: Carte interactive Plotly
        """
        if country_stats is None or len(country_stats) == 0:
            return None
        
        # Préparer les données pour Plotly
        plot_data = country_stats.copy()
        
        # Convertir les noms de pays en codes ISO-3 pour Plotly
        plot_data['ISO'] = plot_data['country'].apply(self._get_iso_code)
        
        # Filtrer les pays sans code ISO valide
        plot_data = plot_data[plot_data['ISO'].notna()].copy()
        
        if len(plot_data) == 0:
            return None
        
        # Obtenir les labels pour l'affichage
        metric_labels = {
            'avg_engagement': 'Taux d\'engagement moyen (%)',
            'median_engagement': 'Taux d\'engagement médian (%)',
            'avg_likes': 'Likes moyen',
            'total_likes': 'Total de likes',
            'avg_followers': 'Followers moyen',
            'total_comments': 'Total commentaires',
            'total_views': 'Total vues',
            'post_count': 'Nombre de posts'
        }
        
        metric_label = metric_labels.get(engagement_column, engagement_column)
        
        # Construire hover_data dynamiquement avec seulement les colonnes existantes
        hover_data_dict = {'ISO': False}  # Toujours masquer ISO
        
        # Ajouter seulement les colonnes qui existent dans plot_data
        if 'avg_engagement' in plot_data.columns:
            hover_data_dict['avg_engagement'] = ':.2f'
        if 'median_engagement' in plot_data.columns:
            hover_data_dict['median_engagement'] = ':.2f'
        if 'total_likes' in plot_data.columns:
            hover_data_dict['total_likes'] = ':,'
        if 'avg_likes' in plot_data.columns:
            hover_data_dict['avg_likes'] = ':,.0f'
        if 'post_count' in plot_data.columns:
            hover_data_dict['post_count'] = ':,'
        
        # Créer la carte choroplèthe avec Plotly
        fig = px.choropleth(
            plot_data,
            locations='ISO',
            color=engagement_column,
            hover_name='country',
            hover_data=hover_data_dict,
            color_continuous_scale='Viridis',  # Palette de couleurs moderne
            title=f'Carte mondiale - {metric_label}',
            labels={engagement_column: metric_label}
        )
        
        # Améliorer le style de la carte
        fig.update_geos(
            showframe=False,
            showcoastlines=True,
            projection_type='natural earth',
            bgcolor='rgba(0,0,0,0)',
            coastlinecolor='white',
            landcolor='lightgray'
        )
        
        fig.update_layout(
            height=600,
            margin=dict(l=0, r=0, t=50, b=0),
            title_font_size=20,
            title_x=0.5,
            font=dict(family="Arial", size=12),
            geo=dict(bgcolor='#f0f2f6')
        )
        
        return fig
    
    def _get_iso_code(self, country_name):
        """
        Convertit un nom de pays en code ISO-3 pour Plotly
        
        Parameters:
        country_name (str): Nom du pays
        
        Returns:
        str: Code ISO-3 ou None
        """
        if pd.isna(country_name):
            return None
        
        country_name = str(country_name).strip()
        
        # Mapping manuel pour les cas courants
        iso_mapping = {
            'UNITED STATES OF AMERICA': 'USA',
            'UNITED STATES': 'USA',
            'USA': 'USA',
            'US': 'USA',
            'UNITED KINGDOM': 'GBR',
            'UK': 'GBR',
            'RUSSIA': 'RUS',
            'RUSSIAN FEDERATION': 'RUS',
            'SOUTH KOREA': 'KOR',
            'KOREA, REPUBLIC OF': 'KOR',
            'VIETNAM': 'VNM',
            'VIET NAM': 'VNM',
        }
        
        country_upper = country_name.upper()
        if country_upper in iso_mapping:
            return iso_mapping[country_upper]
        
        # Essayer avec pycountry
        try:
            country = pycountry.countries.search_fuzzy(country_name)[0]
            return country.alpha_3
        except:
            return None
    
    def create_bar_chart(self, country_stats, engagement_column='avg_engagement', top_n=20):
        """
        Crée un graphique en barres horizontal pour les pays
        
        Parameters:
        country_stats (pd.DataFrame): Statistiques par pays
        engagement_column (str): Colonne à utiliser
        top_n (int): Nombre de pays à afficher
        
        Returns:
        plotly.graph_objects.Figure: Graphique en barres
        """
        if country_stats is None or len(country_stats) == 0:
            return None
        
        # Trier et prendre les top N pays
        plot_data = country_stats.nlargest(top_n, engagement_column).copy()
        
        metric_labels = {
            'avg_engagement': 'Taux d\'engagement moyen (%)',
            'median_engagement': 'Taux d\'engagement médian (%)',
            'avg_likes': 'Likes moyen',
            'total_likes': 'Total de likes',
        }
        
        metric_label = metric_labels.get(engagement_column, engagement_column)
        
        # Créer le graphique en barres horizontal
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            y=plot_data['country'],
            x=plot_data[engagement_column],
            orientation='h',
            marker=dict(
                color=plot_data[engagement_column],
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title=metric_label)
            ),
            text=[f"{val:.2f}" if 'engagement' in engagement_column else f"{val:,.0f}" 
                  for val in plot_data[engagement_column]],
            textposition='auto',
            hovertemplate='<b>%{y}</b><br>' + metric_label + ': %{x:.2f}<extra></extra>'
        ))
        
        fig.update_layout(
            title=f'Top {top_n} pays - {metric_label}',
            xaxis_title=metric_label,
            yaxis_title='Pays',
            height=max(400, len(plot_data) * 30),
            margin=dict(l=0, r=0, t=50, b=0),
            template='plotly_white'
        )
        
        return fig
    
    def create_treemap(self, country_stats, engagement_column='avg_engagement', value_column='total_likes'):
        """
        Crée un treemap (carte arborescente) pour visualiser les pays
        
        Parameters:
        country_stats (pd.DataFrame): Statistiques par pays
        engagement_column (str): Colonne pour la couleur
        value_column (str): Colonne pour la taille
        
        Returns:
        plotly.graph_objects.Figure: Treemap
        """
        if country_stats is None or len(country_stats) == 0:
            return None
        
        if value_column not in country_stats.columns:
            value_column = 'post_count' if 'post_count' in country_stats.columns else engagement_column
        
        plot_data = country_stats.copy()
        
        # Construire hover_data dynamiquement avec seulement les colonnes existantes
        hover_data_dict = {}
        
        # Ajouter seulement les colonnes qui existent dans plot_data
        if 'avg_engagement' in plot_data.columns:
            hover_data_dict['avg_engagement'] = ':.2f'
        if 'total_likes' in plot_data.columns:
            hover_data_dict['total_likes'] = ':,'
        if 'post_count' in plot_data.columns:
            hover_data_dict['post_count'] = ':,'
        
        # Créer le treemap
        fig = px.treemap(
            plot_data,
            path=['country'],
            values=value_column,
            color=engagement_column,
            color_continuous_scale='Viridis',
            title='Répartition par pays (taille = valeur, couleur = engagement)',
            hover_data=hover_data_dict if hover_data_dict else None
        )
        
        fig.update_layout(
            height=600,
            margin=dict(l=0, r=0, t=50, b=0),
            title_font_size=18,
            title_x=0.5
        )
        
        return fig
    
    def get_country_list(self):
        """
        Retourne la liste des pays disponibles dans les données
        
        Returns:
        list: Liste des noms de pays
        """
        country_cols = [col for col in self.df.columns 
                       if 'country' in col.lower() or 'pays' in col.lower()]
        
        if country_cols:
            countries = self.df[country_cols[0]].dropna().unique().tolist()
            return sorted(countries)
        
        return []

