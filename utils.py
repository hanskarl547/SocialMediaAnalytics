"""
Fonctions utilitaires
Helpers et fonctions communes
"""

import pandas as pd
import numpy as np
from datetime import datetime
import re

def validate_email(email):
    """
    Valide le format d'un email
    
    Parameters:
    email (str): Email à valider
    
    Returns:
    bool: True si valide
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def format_number(number, decimals=0):
    """
    Formate un nombre avec séparateurs de milliers
    
    Parameters:
    number (float): Nombre à formater
    decimals (int): Nombre de décimales
    
    Returns:
    str: Nombre formaté
    """
    if decimals == 0:
        return f"{number:,.0f}".replace(',', ' ')
    else:
        return f"{number:,.{decimals}f}".replace(',', ' ')

def calculate_growth_rate(old_value, new_value):
    """
    Calcule le taux de croissance entre deux valeurs
    
    Parameters:
    old_value (float): Ancienne valeur
    new_value (float): Nouvelle valeur
    
    Returns:
    float: Taux de croissance en %
    """
    if old_value == 0:
        return 0
    return ((new_value - old_value) / old_value) * 100

def classify_engagement(engagement_rate):
    """
    Classifie le taux d'engagement
    
    Parameters:
    engagement_rate (float): Taux d'engagement en %
    
    Returns:
    dict: Classification et emoji
    """
    if engagement_rate >= 10:
        return {'level': 'Exceptionnel', 'emoji': '🏆', 'color': 'gold'}
    elif engagement_rate >= 5:
        return {'level': 'Excellent', 'emoji': '🎉', 'color': 'green'}
    elif engagement_rate >= 3:
        return {'level': 'Bon', 'emoji': '✅', 'color': 'lightgreen'}
    elif engagement_rate >= 1:
        return {'level': 'Moyen', 'emoji': '⚠️', 'color': 'orange'}
    else:
        return {'level': 'Faible', 'emoji': '❌', 'color': 'red'}

def detect_outliers(series, method='iqr', threshold=1.5):
    """
    Détecte les valeurs aberrantes dans une série
    
    Parameters:
    series (pd.Series): Série de données
    method (str): 'iqr' ou 'zscore'
    threshold (float): Seuil de détection
    
    Returns:
    pd.Series: Masque booléen des outliers
    """
    if method == 'iqr':
        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        return (series < lower_bound) | (series > upper_bound)
    
    elif method == 'zscore':
        z_scores = np.abs((series - series.mean()) / series.std())
        return z_scores > threshold
    
    return pd.Series([False] * len(series))

def normalize_platform_name(platform):
    """
    Normalise le nom d'une plateforme
    
    Parameters:
    platform (str): Nom de la plateforme
    
    Returns:
    str: Nom normalisé
    """
    platform_mapping = {
        'tiktok': 'TikTok',
        'tik tok': 'TikTok',
        'instagram': 'Instagram',
        'insta': 'Instagram',
        'facebook': 'Facebook',
        'fb': 'Facebook',
        'youtube': 'YouTube',
        'yt': 'YouTube',
        'twitter': 'Twitter',
        'x': 'Twitter',
        'linkedin': 'LinkedIn',
        'snapchat': 'Snapchat',
        'pinterest': 'Pinterest',
        'twitch': 'Twitch'
    }
    
    platform_lower = platform.lower().strip()
    return platform_mapping.get(platform_lower, platform.title())

def get_platform_emoji(platform):
    """
    Retourne l'emoji correspondant à une plateforme
    
    Parameters:
    platform (str): Nom de la plateforme
    
    Returns:
    str: Emoji
    """
    emoji_mapping = {
        'TikTok': '🎵',
        'Instagram': '📸',
        'Facebook': '👥',
        'YouTube': '🎥',
        'Twitter': '🐦',
        'LinkedIn': '💼',
        'Snapchat': '👻',
        'Pinterest': '📌',
        'Twitch': '🎮'
    }
    
    normalized = normalize_platform_name(platform)
    return emoji_mapping.get(normalized, '📱')

def get_best_posting_times(df, time_column='hour', metric='engagement_rate'):
    """
    Identifie les meilleures heures de publication
    
    Parameters:
    df (pd.DataFrame): DataFrame avec les données
    time_column (str): Colonne contenant l'heure
    metric (str): Métrique à optimiser
    
    Returns:
    list: Top 3 des meilleures heures
    """
    if time_column not in df.columns or metric not in df.columns:
        return []
    
    hourly_avg = df.groupby(time_column)[metric].mean().sort_values(ascending=False)
    
    top_hours = hourly_avg.head(3).index.tolist()
    
    return [f"{hour}h" for hour in top_hours]

def calculate_consistency_score(series):
    """
    Calcule un score de cohérence (faible variance = plus cohérent)
    
    Parameters:
    series (pd.Series): Série de données
    
    Returns:
    float: Score de 0 à 100 (100 = très cohérent)
    """
    if len(series) < 2:
        return 100
    
    cv = (series.std() / series.mean()) * 100 if series.mean() != 0 else 100
    
    # Convertir en score (plus le CV est faible, meilleur le score)
    score = max(0, 100 - cv)
    
    return min(100, score)

def recommend_content_frequency(avg_engagement, platform):
    """
    Recommande une fréquence de publication
    
    Parameters:
    avg_engagement (float): Engagement moyen
    platform (str): Nom de la plateforme
    
    Returns:
    dict: Recommandation de fréquence
    """
    platform_normalized = normalize_platform_name(platform)
    
    # Fréquences de base par plateforme
    base_frequencies = {
        'TikTok': {'min': 1, 'max': 3, 'unit': 'par jour'},
        'Instagram': {'min': 1, 'max': 2, 'unit': 'par jour'},
        'Facebook': {'min': 1, 'max': 2, 'unit': 'par jour'},
        'YouTube': {'min': 2, 'max': 4, 'unit': 'par semaine'},
        'Twitter': {'min': 3, 'max': 10, 'unit': 'par jour'},
        'LinkedIn': {'min': 3, 'max': 5, 'unit': 'par semaine'},
    }
    
    freq = base_frequencies.get(platform_normalized, {'min': 1, 'max': 2, 'unit': 'par jour'})
    
    # Ajuster selon l'engagement
    if avg_engagement > 5:
        recommendation = f"{freq['max']} {freq['unit']}"
        tip = "Votre engagement est excellent! Maintenez ce rythme."
    elif avg_engagement > 3:
        recommendation = f"{freq['min']}-{freq['max']} {freq['unit']}"
        tip = "Bon engagement. Vous pouvez augmenter la fréquence progressivement."
    else:
        recommendation = f"{freq['min']} {freq['unit']}"
        tip = "Concentrez-vous sur la qualité plutôt que la quantité."
    
    return {
        'frequency': recommendation,
        'tip': tip
    }

def create_sample_data(n_rows=50):
    """
    Crée des données d'exemple pour les tests
    
    Parameters:
    n_rows (int): Nombre de lignes à générer
    
    Returns:
    pd.DataFrame: Données d'exemple
    """
    np.random.seed(42)
    
    platforms = ['TikTok', 'Instagram', 'Facebook', 'YouTube', 'Twitter']
    post_types = ['video', 'photo', 'reel', 'story', 'carousel']
    
    data = {
        'platform': np.random.choice(platforms, n_rows),
        'post_type': np.random.choice(post_types, n_rows),
        'likes': np.random.randint(100, 5000, n_rows),
        'comments': np.random.randint(10, 500, n_rows),
        'shares': np.random.randint(5, 200, n_rows),
        'saves': np.random.randint(0, 300, n_rows),
        'views': np.random.randint(1000, 50000, n_rows),
        'followers': np.random.randint(5000, 100000, n_rows),
        'hour': np.random.randint(0, 24, n_rows),
    }
    
    # Générer des dates sur le dernier mois
    dates = pd.date_range(end=datetime.now(), periods=n_rows, freq='D')
    data['date'] = dates
    
    df = pd.DataFrame(data)
    
    # Calculer le taux d'engagement
    df['engagement_rate'] = ((df['likes'] + df['comments'] + df['shares']) / df['followers']) * 100
    
    return df

def clean_data(df, remove_duplicates=True, handle_missing='drop'):
    """
    Nettoie un DataFrame
    
    Parameters:
    df (pd.DataFrame): DataFrame à nettoyer
    remove_duplicates (bool): Supprimer les doublons
    handle_missing (str): 'drop', 'fill_mean', 'fill_median', 'fill_zero'
    
    Returns:
    pd.DataFrame: DataFrame nettoyé
    """
    df_clean = df.copy()
    
    # Supprimer les doublons
    if remove_duplicates:
        df_clean = df_clean.drop_duplicates()
    
    # Gérer les valeurs manquantes
    if handle_missing == 'drop':
        df_clean = df_clean.dropna()
    elif handle_missing == 'fill_mean':
        numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
        df_clean[numeric_cols] = df_clean[numeric_cols].fillna(df_clean[numeric_cols].mean())
    elif handle_missing == 'fill_median':
        numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
        df_clean[numeric_cols] = df_clean[numeric_cols].fillna(df_clean[numeric_cols].median())
    elif handle_missing == 'fill_zero':
        df_clean = df_clean.fillna(0)
    
    return df_clean

def generate_insights(df):
    """
    Génère des insights automatiques à partir des données
    
    Parameters:
    df (pd.DataFrame): DataFrame à analyser
    
    Returns:
    list: Liste d'insights
    """
    insights = []
    
    # Insight sur la meilleure plateforme
    if 'platform' in df.columns and 'engagement_rate' in df.columns:
        best_platform = df.groupby('platform')['engagement_rate'].mean().idxmax()
        best_engagement = df.groupby('platform')['engagement_rate'].mean().max()
        
        insights.append({
            'type': 'platform',
            'icon': '🏆',
            'title': 'Meilleure Plateforme',
            'message': f"{best_platform} domine avec {best_engagement:.2f}% d'engagement moyen",
            'priority': 'high'
        })
    
    # Insight sur la cohérence
    if 'engagement_rate' in df.columns:
        consistency = calculate_consistency_score(df['engagement_rate'])
        
        if consistency > 70:
            insights.append({
                'type': 'consistency',
                'icon': '✅',
                'title': 'Cohérence',
                'message': f"Vos performances sont cohérentes (score: {consistency:.0f}/100)",
                'priority': 'medium'
            })
        else:
            insights.append({
                'type': 'consistency',
                'icon': '⚠️',
                'title': 'Variabilité',
                'message': f"Vos performances varient beaucoup (score: {consistency:.0f}/100)",
                'priority': 'medium'
            })
    
    # Insight sur les outliers
    if 'likes' in df.columns:
        outliers = detect_outliers(df['likes'])
        n_outliers = outliers.sum()
        
        if n_outliers > 0:
            insights.append({
                'type': 'outliers',
                'icon': '⭐',
                'title': 'Posts Exceptionnels',
                'message': f"{n_outliers} post(s) ont des performances exceptionnelles",
                'priority': 'medium'
            })
    
    # Insight sur les meilleures heures
    if 'hour' in df.columns and 'engagement_rate' in df.columns:
        best_hours = get_best_posting_times(df)
        
        if best_hours:
            insights.append({
                'type': 'timing',
                'icon': '⏰',
                'title': 'Meilleurs Horaires',
                'message': f"Publiez à {', '.join(best_hours)} pour plus d'engagement",
                'priority': 'high'
            })
    
    return insights

def export_to_excel(df, filename='export.xlsx', include_summary=True):
    """
    Exporte un DataFrame vers Excel avec plusieurs feuilles
    
    Parameters:
    df (pd.DataFrame): DataFrame à exporter
    filename (str): Nom du fichier
    include_summary (bool): Inclure une feuille de résumé
    
    Returns:
    str: Chemin du fichier créé
    """
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        # Feuille principale
        df.to_excel(writer, sheet_name='Données', index=False)
        
        # Feuille de résumé
        if include_summary and 'platform' in df.columns:
            summary = df.groupby('platform').agg({
                col: ['mean', 'sum', 'count'] 
                for col in df.select_dtypes(include=[np.number]).columns
            })
            summary.to_excel(writer, sheet_name='Résumé')
    
    return filename

