"""
Application Streamlit Améliorée avec Design Créatif
Version moderne avec animations et micro-interactions
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuration de la page
st.set_page_config(
    page_title="Social Media Analytics Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styles CSS modernes et créatifs
st.markdown("""
<style>
/* Variables CSS modernes */
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    --success-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    --warning-gradient: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
    
    --shadow-soft: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    --shadow-medium: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    --shadow-large: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    
    --border-radius: 12px;
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Animations d'entrée */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideInLeft {
    from {
        opacity: 0;
        transform: translateX(-30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes pulse {
    0%, 100% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.05);
    }
}

@keyframes shimmer {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

/* Header moderne */
.dashboard-header {
    background: var(--primary-gradient);
    padding: 2rem;
    border-radius: var(--border-radius);
    margin-bottom: 2rem;
    animation: fadeInUp 0.8s ease-out;
    box-shadow: var(--shadow-medium);
}

.dashboard-header h1 {
    color: white;
    text-align: center;
    margin: 0;
    font-size: 2.5rem;
    font-weight: 700;
}

.dashboard-header p {
    color: rgba(255,255,255,0.8);
    text-align: center;
    margin: 0.5rem 0 0 0;
    font-size: 1.1rem;
}

/* Cards modernes avec glassmorphism */
.glass-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-medium);
    transition: var(--transition);
    padding: 1.5rem;
}

.glass-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-large);
    background: rgba(255, 255, 255, 0.15);
}

/* Métriques avec animations */
.metric-card {
    background: white;
    border-radius: var(--border-radius);
    padding: 24px;
    box-shadow: var(--shadow-soft);
    transition: var(--transition);
    animation: fadeInUp 0.6s ease-out;
    border-left: 4px solid transparent;
    background-image: linear-gradient(white, white), var(--primary-gradient);
    background-origin: border-box;
    background-clip: content-box, border-box;
}

.metric-card:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-medium);
}

.metric-value {
    font-size: 2.5rem;
    font-weight: 700;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0.5rem 0;
}

.metric-label {
    color: #64748b;
    font-size: 0.9rem;
    font-weight: 500;
    margin-bottom: 0.5rem;
}

.metric-change {
    font-size: 0.8rem;
    font-weight: 600;
    display: flex;
    align-items: center;
}

.metric-change.positive {
    color: #10b981;
}

.metric-change.negative {
    color: #ef4444;
}

/* Boutons modernes */
.btn-modern {
    position: relative;
    overflow: hidden;
    background: var(--primary-gradient);
    border: none;
    border-radius: var(--border-radius);
    padding: 12px 24px;
    color: white;
    font-weight: 600;
    cursor: pointer;
    transition: var(--transition);
    box-shadow: var(--shadow-soft);
}

.btn-modern::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.5s;
}

.btn-modern:hover::before {
    left: 100%;
}

.btn-modern:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-medium);
}

/* Sidebar moderne */
.sidebar-modern {
    background: linear-gradient(180deg, #1e293b 0%, #334155 100%);
    border-radius: 0 var(--border-radius) var(--border-radius) 0;
    box-shadow: var(--shadow-medium);
    padding: 1rem;
}

.sidebar-item {
    padding: 12px 16px;
    margin: 4px 8px;
    border-radius: 8px;
    transition: var(--transition);
    cursor: pointer;
    color: #94a3b8;
    display: flex;
    align-items: center;
    font-weight: 500;
}

.sidebar-item:hover {
    background: rgba(255, 255, 255, 0.1);
    color: white;
    transform: translateX(4px);
}

.sidebar-item.active {
    background: var(--primary-gradient);
    color: white;
    box-shadow: var(--shadow-soft);
}

.sidebar-icon {
    margin-right: 12px;
    font-size: 1.2rem;
}

/* Progress bars animées */
.progress-bar-modern {
    height: 8px;
    background: rgba(0, 0, 0, 0.1);
    border-radius: 4px;
    overflow: hidden;
    position: relative;
    margin: 1rem 0;
}

.progress-fill {
    height: 100%;
    background: var(--success-gradient);
    border-radius: 4px;
    transition: width 0.8s ease-out;
    position: relative;
}

.progress-fill::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    animation: shimmer 2s infinite;
}

/* Notifications toast */
.toast-success {
    position: fixed;
    top: 20px;
    right: 20px;
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: white;
    padding: 16px 24px;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-large);
    z-index: 1000;
    animation: slideInRight 0.5s ease-out;
}

@keyframes slideInRight {
    from { transform: translateX(100%); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}

/* Loading spinner */
.loading-spinner {
    width: 50px;
    height: 50px;
    border: 4px solid #f3f4f6;
    border-top: 4px solid #667eea;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* Responsive design */
@media (max-width: 768px) {
    .metric-card {
        padding: 16px;
    }
    
    .metric-value {
        font-size: 2rem;
    }
    
    .dashboard-header h1 {
        font-size: 2rem;
    }
}

/* Thème sombre */
.dark-theme {
    --bg-primary: #0f172a;
    --bg-secondary: #1e293b;
    --text-primary: #f1f5f9;
    --text-secondary: #94a3b8;
}

/* Amélioration des composants Streamlit */
.stSelectbox > div > div {
    background-color: white;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-soft);
}

.stButton > button {
    background: var(--primary-gradient);
    color: white;
    border: none;
    border-radius: var(--border-radius);
    padding: 0.75rem 2rem;
    font-weight: 600;
    transition: var(--transition);
    box-shadow: var(--shadow-soft);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-medium);
}

/* Upload section moderne */
.upload-section {
    border: 2px dashed #667eea;
    padding: 2rem;
    border-radius: var(--border-radius);
    text-align: center;
    margin: 1rem 0;
    transition: var(--transition);
    background: rgba(102, 126, 234, 0.05);
}

.upload-section:hover {
    border-color: #4f46e5;
    background: rgba(102, 126, 234, 0.1);
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

def create_modern_header():
    """Crée un header moderne avec animations"""
    st.markdown("""
    <div class="dashboard-header">
        <h1>📊 Social Media Analytics Pro</h1>
        <p>Analysez vos performances avec l'IA • Design moderne • Insights avancés</p>
    </div>
    """, unsafe_allow_html=True)

def create_animated_metrics():
    """Crée des métriques avec animations"""
    
    # Données simulées
    metrics_data = {
        'Engagement': {'value': '12.5%', 'change': '+2.3%', 'icon': '📈', 'positive': True},
        'Followers': {'value': '45.2K', 'change': '+1.2K', 'icon': '👥', 'positive': True},
        'Likes': {'value': '8.7K', 'change': '+456', 'icon': '❤️', 'positive': True},
        'Comments': {'value': '234', 'change': '+23', 'icon': '💬', 'positive': True},
        'Shares': {'value': '89', 'change': '+12', 'icon': '🔄', 'positive': True},
        'Reach': {'value': '156K', 'change': '+8.2K', 'icon': '👁️', 'positive': True}
    }
    
    cols = st.columns(3)
    
    for i, (metric, data) in enumerate(metrics_data.items()):
        with cols[i % 3]:
            change_class = "positive" if data['positive'] else "negative"
            change_symbol = "↗" if data['positive'] else "↘"
            
            st.markdown(f"""
            <div class="metric-card" style="animation-delay: {i * 0.1}s;">
                <div class="metric-label">
                    <span style="font-size: 1.5rem; margin-right: 8px;">{data['icon']}</span>
                    {metric}
                </div>
                <div class="metric-value">{data['value']}</div>
                <div class="metric-change {change_class}">
                    {change_symbol} {data['change']}
                </div>
            </div>
            """, unsafe_allow_html=True)

def create_modern_sidebar():
    """Crée une sidebar moderne"""
    
    # Profil utilisateur
    st.markdown("""
    <div style="text-align: center; padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 1rem;">
        <div style="width: 60px; height: 60px; border-radius: 50%; background: var(--primary-gradient); margin: 0 auto 8px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; box-shadow: var(--shadow-medium);">👤</div>
        <div style="color: white; font-weight: 600;">John Doe</div>
        <div style="color: #94a3b8; font-size: 0.8rem;">Premium User</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Menu de navigation
    menu_items = [
        ("🏠", "Accueil", "home"),
        ("📤", "Importer", "upload"),
        ("📊", "Analyses", "analysis"),
        ("🤖", "Assistant IA", "ai"),
        ("📈", "Graphiques", "charts"),
        ("🔮", "Prédictions", "predictions"),
        ("💾", "Projets", "projects"),
        ("💎", "Premium", "premium")
    ]
    
    st.markdown("### 📋 Navigation")
    
    for icon, label, key in menu_items:
        if st.button(f"{icon} {label}", key=f"nav_{key}"):
            st.session_state.page = key
            st.rerun()

def create_animated_charts():
    """Crée des graphiques avec animations"""
    
    # Données d'exemple
    platforms = ['TikTok', 'Instagram', 'Facebook', 'Twitter', 'YouTube']
    engagement = [12.5, 8.3, 6.7, 4.2, 9.1]
    followers = [45200, 32100, 28900, 15600, 23400]
    
    # Graphique en barres avec animations
    fig = px.bar(
        x=platforms,
        y=engagement,
        color=engagement,
        color_continuous_scale='Viridis',
        title='Engagement par Plateforme',
        labels={'x': 'Plateforme', 'y': 'Taux d\'engagement (%)'}
    )
    
    fig.update_layout(
        title_font_size=20,
        title_font_color='#1f2937',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, sans-serif"),
        transition_duration=500,
        height=400
    )
    
    # Ajouter des annotations
    for i, (platform, eng) in enumerate(zip(platforms, engagement)):
        fig.add_annotation(
            x=platform,
            y=eng,
            text=f"{eng}%",
            showarrow=True,
            arrowhead=2,
            arrowcolor='#667eea',
            font=dict(color='#1f2937', size=12)
        )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Graphique en ligne pour l'évolution
    dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
    evolution_data = np.random.randn(31).cumsum() + 10
    
    fig_line = px.line(
        x=dates,
        y=evolution_data,
        title='Évolution de l\'Engagement (30 derniers jours)',
        labels={'x': 'Date', 'y': 'Engagement (%)'}
    )
    
    fig_line.update_layout(
        title_font_size=20,
        title_font_color='#1f2937',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, sans-serif"),
        height=400
    )
    
    fig_line.update_traces(
        line=dict(color='#667eea', width=3),
        marker=dict(size=6, color='#764ba2')
    )
    
    st.plotly_chart(fig_line, use_container_width=True)

def show_loading_animation():
    """Affiche une animation de chargement moderne"""
    
    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; height: 200px; flex-direction: column;">
        <div class="loading-spinner"></div>
        <div style="margin-top: 1rem; color: #64748b; font-weight: 500;">Analyse en cours...</div>
    </div>
    """, unsafe_allow_html=True)

def show_success_toast(message):
    """Affiche une notification de succès"""
    
    st.markdown(f"""
    <div class="toast-success">
        <div style="display: flex; align-items: center;">
            <span style="margin-right: 8px; font-size: 1.2rem;">✅</span>
            <span>{message}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_upload_section():
    """Crée une section d'upload moderne"""
    
    st.markdown("""
    <div class="upload-section">
        <div style="font-size: 3rem; margin-bottom: 1rem;">📁</div>
        <h3 style="color: #1f2937; margin-bottom: 0.5rem;">Glissez-déposez vos fichiers</h3>
        <p style="color: #64748b; margin-bottom: 1rem;">ou cliquez pour sélectionner</p>
        <p style="color: #9ca3af; font-size: 0.9rem;">Formats supportés: CSV, XLS, XLSX (max 50MB)</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Choisir un fichier",
        type=['csv', 'xlsx', 'xls'],
        help="Sélectionnez votre fichier de données"
    )
    
    if uploaded_file:
        show_success_toast("Fichier uploadé avec succès !")
        
        # Simuler le traitement
        with st.spinner("Traitement en cours..."):
            time.sleep(2)
        
        st.success("✅ Données importées et prêtes pour l'analyse !")

def main():
    """Application principale"""
    
    # Initialiser la session
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    
    # Sidebar
    with st.sidebar:
        create_modern_sidebar()
        
        st.markdown("---")
        
        # Thème switcher
        st.markdown("### 🎨 Thème")
        if st.button("🌙 Mode Sombre"):
            st.markdown("""
            <style>
            .stApp {
                background-color: #0f172a;
                color: #f1f5f9;
            }
            </style>
            """, unsafe_allow_html=True)
        
        if st.button("☀️ Mode Clair"):
            st.markdown("""
            <style>
            .stApp {
                background-color: #ffffff;
                color: #1f2937;
            }
            </style>
            """, unsafe_allow_html=True)
    
    # Contenu principal
    if st.session_state.page == 'home':
        create_modern_header()
        create_animated_metrics()
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📊 Graphiques Interactifs")
            create_animated_charts()
        
        with col2:
            st.markdown("### 📤 Import de Données")
            create_upload_section()
    
    elif st.session_state.page == 'upload':
        create_modern_header()
        st.markdown("### 📤 Import de Données")
        create_upload_section()
    
    elif st.session_state.page == 'analysis':
        create_modern_header()
        st.markdown("### 📊 Analyses Statistiques")
        show_loading_animation()
    
    elif st.session_state.page == 'ai':
        create_modern_header()
        st.markdown("### 🤖 Assistant IA")
        st.info("🧠 Assistant IA avec interprétations approfondies disponible !")
    
    elif st.session_state.page == 'charts':
        create_modern_header()
        st.markdown("### 📈 Visualisations")
        create_animated_charts()
    
    elif st.session_state.page == 'predictions':
        create_modern_header()
        st.markdown("### 🔮 Prédictions IA")
        st.info("🔮 Modèles de prédiction avancés disponibles !")
    
    elif st.session_state.page == 'projects':
        create_modern_header()
        st.markdown("### 💾 Mes Projets")
        st.info("💾 Gestion de projets sauvegardés !")
    
    elif st.session_state.page == 'premium':
        create_modern_header()
        st.markdown("### 💎 Premium")
        st.info("💎 Fonctionnalités premium disponibles !")

if __name__ == "__main__":
    main()


