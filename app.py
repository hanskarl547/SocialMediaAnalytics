"""
Application principale Streamlit
Plateforme d'analyse des réseaux sociaux
"""

import streamlit as st
import pandas as pd
import numpy as np
import os
import sys
from datetime import datetime
from dotenv import load_dotenv
import plotly.express as px

# Configuration Streamlit (doit être fait avant les imports qui utilisent st)
load_dotenv()
st.set_page_config(
    page_title="Social Media Analytics Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Importer les modules personnalisés avec gestion d'erreurs
import_errors = []

try:
    from database import Database
except (ImportError, KeyError, ModuleNotFoundError) as e:
    import_errors.append(f"database: {e}")

try:
    from statistical_analysis import StatisticalAnalyzer
except (ImportError, KeyError, ModuleNotFoundError) as e:
    import_errors.append(f"statistical_analysis: {e}")

try:
    from ai_assistant import AIAssistant
except (ImportError, KeyError, ModuleNotFoundError) as e:
    import_errors.append(f"ai_assistant: {e}")

try:
    from visualizations import DataVisualizer
except (ImportError, KeyError, ModuleNotFoundError) as e:
    import_errors.append(f"visualizations: {e}")

try:
    from country_map import CountryMapVisualizer
except (ImportError, KeyError, ModuleNotFoundError) as e:
    import_errors.append(f"country_map: {e}")

try:
    from notifications import NotificationManager
except (ImportError, KeyError, ModuleNotFoundError) as e:
    import_errors.append(f"notifications: {e}")

# Afficher les erreurs d'import si nécessaire
if import_errors:
    st.error("❌ Erreurs lors du chargement des modules:")
    for error in import_errors:
        st.error(f"  - {error}")
    st.stop()

# 🔹 Charger les polices des icônes Material Icons (OBLIGATOIRE pour les icônes)
st.markdown("""
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet">
""", unsafe_allow_html=True)

# 🔹 Corriger l'affichage des icônes Material Icons
st.markdown("""
<style>
/* Material Icons classique */
.material-icons {
    font-family: 'Material Icons' !important;
    font-weight: normal !important;
    font-style: normal !important;
    font-size: 24px !important;
    line-height: 1 !important;
    letter-spacing: normal !important;
    text-transform: none !important;
    display: inline-block !important;
    white-space: nowrap !important;
    word-wrap: normal !important;
    direction: ltr !important;
    -webkit-font-feature-settings: 'liga' !important;
    -webkit-font-smoothing: antialiased !important;
}

/* Material Symbols Outlined */
.material-symbols-outlined {
    font-family: 'Material Symbols Outlined' !important;
    font-weight: normal !important;
    font-style: normal !important;
}
</style>
""", unsafe_allow_html=True)

# Script JavaScript pour masquer le footer GitHub et le texte "keyboard_double_arrow_right" - EXÉCUTÉ EN PREMIER
st.markdown("""
<script>
(function() {
    // Fonction pour masquer les éléments GitHub - VERSION AGRESSIVE
    function hideGitHubElements() {
        // Masquer tous les footers avec tous les styles possibles
        const footers = document.querySelectorAll('footer, [data-testid="stFooter"], [role="contentinfo"]');
        footers.forEach(function(footer) {
            footer.style.cssText = 'display: none !important; visibility: hidden !important; opacity: 0 !important; height: 0 !important; width: 0 !important; max-height: 0 !important; max-width: 0 !important; padding: 0 !important; margin: 0 !important; overflow: hidden !important; position: absolute !important; left: -9999px !important; top: -9999px !important; z-index: -9999 !important; pointer-events: none !important;';
            // Essayer de supprimer complètement
            try {
                footer.remove();
            } catch(e) {}
        });
        
        // Masquer tous les liens GitHub
        const githubLinks = document.querySelectorAll('a[href*="github"], a[href*="GitHub"], a[href*="streamlit.io"]');
        githubLinks.forEach(function(link) {
            link.style.cssText = 'display: none !important; visibility: hidden !important; opacity: 0 !important; height: 0 !important; width: 0 !important; overflow: hidden !important; position: absolute !important; left: -9999px !important; pointer-events: none !important;';
            try {
                link.remove();
            } catch(e) {}
        });
        
        // Masquer tous les iframes GitHub
        const githubIframes = document.querySelectorAll('iframe[title*="github"], iframe[title*="GitHub"], iframe[src*="github"]');
        githubIframes.forEach(function(iframe) {
            iframe.style.cssText = 'display: none !important; visibility: hidden !important; opacity: 0 !important; height: 0 !important; width: 0 !important; overflow: hidden !important;';
            try {
                iframe.remove();
            } catch(e) {}
        });
        
        // Masquer les éléments avec texte GitHub ou Streamlit
        const allElements = document.querySelectorAll('*');
        allElements.forEach(function(el) {
            const elText = el.textContent || '';
            if (elText.includes('GitHub') || 
                elText.includes('github') ||
                elText.includes('Made with Streamlit') ||
                elText.includes('streamlit')) {
                // Vérifier si c'est dans un footer ou un lien
                let parent = el;
                let isInFooter = false;
                while (parent && parent !== document.body) {
                    if (parent.tagName === 'FOOTER' || 
                        parent.getAttribute('data-testid') === 'stFooter' ||
                        parent.getAttribute('role') === 'contentinfo' ||
                        (parent.tagName === 'A' && parent.href && (parent.href.includes('github') || parent.href.includes('streamlit')))) {
                        isInFooter = true;
                        break;
                    }
                    parent = parent.parentElement;
                }
                if (isInFooter) {
                    el.style.cssText = 'display: none !important; visibility: hidden !important; opacity: 0 !important; height: 0 !important; width: 0 !important; overflow: hidden !important; position: absolute !important; left: -9999px !important; pointer-events: none !important;';
                    try {
                        el.remove();
                    } catch(e) {}
                }
            }
        });
    }
    
    // Exécuter immédiatement
    hideGitHubElements();
    
    // Exécuter après le chargement
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            hideGitHubElements();
            setInterval(hideGitHubElements, 200);
        });
    } else {
        hideGitHubElements();
        setInterval(hideGitHubElements, 200);
    }
    
    // Exécuter avec des délais multiples et fréquents
    [50, 100, 200, 300, 500, 750, 1000, 1500, 2000, 3000, 5000].forEach(function(delay) {
        setTimeout(hideGitHubElements, delay);
    });
    
    // Observer TOUS les changements du DOM pour GitHub avec réaction immédiate
    const githubObserver = new MutationObserver(function(mutations) {
        hideGitHubElements();
    });
    githubObserver.observe(document.body, {
        childList: true,
        subtree: true,
        attributes: true,
        attributeOldValue: true,
        characterData: true
    });
    
    // Exécuter en continu toutes les 100ms pendant 30 secondes
    let githubCount = 0;
    const githubInterval = setInterval(function() {
        hideGitHubElements();
        githubCount++;
        if (githubCount > 300) { // 30 secondes (300 * 100ms)
            clearInterval(githubInterval);
        }
    }, 100);
    
    // Exécuter aussi après un délai plus long pour les éléments chargés très tardivement
    setTimeout(function() {
        const longGithubInterval = setInterval(hideGitHubElements, 500);
        // Arrêter après 5 minutes
        setTimeout(function() {
            clearInterval(longGithubInterval);
        }, 300000); // 5 minutes
    }, 10000); // Démarrer après 10 secondes
    
    // Fonction pour SUPPRIMER COMPLÈTEMENT le texte "keyboard_double_arrow_right"
    function hideKeyboardDoubleArrow() {
        // MÉTHODE 1: SUPPRIMER les nœuds texte directement (LE PLUS EFFICACE)
        const walker = document.createTreeWalker(
            document.body,
            NodeFilter.SHOW_TEXT,
            null,
            false
        );
        
        const nodesToRemove = [];
        let node;
        while (node = walker.nextNode()) {
            if (node.textContent && (node.textContent.includes('keyboard_double_arrow_right') || 
                node.textContent.includes('keyboard_double'))) {
                nodesToRemove.push(node);
            }
        }
        
        // Supprimer les nœuds trouvés
        nodesToRemove.forEach(function(textNode) {
            // Supprimer le texte complètement
            textNode.textContent = '';
            // Si le parent n'a plus de contenu, le supprimer aussi
            if (textNode.parentElement) {
                const parent = textNode.parentElement;
                // Vérifier si le parent n'a plus de contenu utile
                if (!parent.textContent || parent.textContent.trim() === '' || 
                    parent.textContent.includes('keyboard_double')) {
                    parent.style.display = 'none';
                    parent.style.visibility = 'hidden';
                    parent.style.opacity = '0';
                    parent.style.fontSize = '0';
                    parent.style.height = '0';
                    parent.style.width = '0';
                    parent.style.overflow = 'hidden';
                    parent.style.position = 'absolute';
                    parent.style.left = '-9999px';
                    // Essayer de supprimer complètement du DOM si possible
                    if (parent.parentElement && parent.textContent.includes('keyboard_double')) {
                        try {
                            parent.remove();
                        } catch(e) {}
                    }
                }
            }
            // Supprimer le nœud texte du DOM
            try {
                textNode.remove();
            } catch(e) {
                textNode.textContent = '';
            }
        });
        
        // MÉTHODE 2: Remplacer les éléments contenant le texte par un emoji
        const allElements = document.querySelectorAll('*');
        allElements.forEach(function(el) {
            const elText = el.textContent || '';
            if (elText.includes('keyboard_double_arrow_right') || 
                elText.includes('keyboard_double')) {
                // Vérifier si c'est dans la sidebar (pour éviter de casser autre chose)
                const isInSidebar = el.closest('[data-testid="stSidebar"]');
                if (isInSidebar || elText.trim() === 'keyboard_double_arrow_right' || elText.trim().includes('keyboard_double_arrow_right')) {
                    // Remplacer tout le contenu par l'emoji
                    el.textContent = '➡️';
                    el.innerHTML = '➡️';
                    // S'assurer que l'élément est visible
                    el.style.display = '';
                    el.style.visibility = '';
                    el.style.opacity = '';
                    el.style.fontSize = '24px';
                    el.style.color = '';
                }
            }
        });
        
        // MÉTHODE 3: REMPLACER COMPLÈTEMENT LE CONTENU PAR UN EMOJI (dans la sidebar)
        const sidebar = document.querySelector('[data-testid="stSidebar"]');
        if (sidebar) {
            // Parcourir tous les éléments de la sidebar
            const sidebarElements = sidebar.querySelectorAll('*');
            sidebarElements.forEach(function(el) {
                const elText = el.textContent || '';
                if (elText.includes('keyboard_double_arrow_right') || 
                    elText.includes('keyboard_double')) {
                    // Remplacer complètement le contenu par l'emoji
                    el.textContent = '➡️';
                    el.innerHTML = '➡️';
                    // S'assurer que l'élément est visible et stylé correctement
                    el.style.display = '';
                    el.style.visibility = '';
                    el.style.opacity = '';
                    el.style.fontSize = '24px';
                    el.style.color = '';
                    el.style.height = '';
                    el.style.width = '';
                    el.style.overflow = '';
                    el.style.position = '';
                    el.style.left = '';
                }
            });
            
            // Parcourir aussi les nœuds texte directement pour les remplacer
            const walker = document.createTreeWalker(
                sidebar,
                NodeFilter.SHOW_TEXT,
                null,
                false
            );
            
            let node;
            while (node = walker.nextNode()) {
                if (node.textContent && (node.textContent.includes('keyboard_double_arrow_right') || 
                    node.textContent.includes('keyboard_double'))) {
                    // Remplacer le texte directement par l'emoji
                    node.textContent = '➡️';
                    
                    // S'assurer que le parent est visible
                    const parent = node.parentElement;
                    if (parent) {
                        parent.style.display = '';
                        parent.style.visibility = '';
                        parent.style.opacity = '';
                        parent.style.fontSize = '24px';
                        parent.style.color = '';
                    }
                }
            }
        }
    }
    
    // EXÉCUTION TRÈS AGRESSIVE - Supprimer immédiatement et continuellement
    hideKeyboardDoubleArrow();
    
    // Exécuter après le chargement
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            hideKeyboardDoubleArrow();
            // Exécuter très fréquemment
            setInterval(hideKeyboardDoubleArrow, 50);
        });
    } else {
        hideKeyboardDoubleArrow();
        // Exécuter très fréquemment
        setInterval(hideKeyboardDoubleArrow, 50);
    }
    
    // Exécuter avec des délais multiples et fréquents
    [10, 25, 50, 100, 200, 300, 500, 750, 1000, 1500, 2000, 3000, 5000].forEach(function(delay) {
        setTimeout(hideKeyboardDoubleArrow, delay);
    });
    
    // Observer TOUS les changements du DOM avec une réaction immédiate
    const observer = new MutationObserver(function(mutations) {
        // Réagir immédiatement à chaque changement
        hideKeyboardDoubleArrow();
    });
    observer.observe(document.body, {
        childList: true,
        subtree: true,
        characterData: true,
        attributes: true,
        attributeOldValue: true
    });
    
    // Exécuter en continu toutes les 50ms pendant 30 secondes (600 itérations)
    let count = 0;
    const interval = setInterval(function() {
        hideKeyboardDoubleArrow();
        count++;
        if (count > 600) { // 30 secondes (600 * 50ms)
            clearInterval(interval);
        }
    }, 50);
    
    // Exécuter aussi après un délai plus long pour les éléments chargés très tardivement
    setTimeout(function() {
        const longInterval = setInterval(hideKeyboardDoubleArrow, 200);
        // Arrêter après 5 minutes
        setTimeout(function() {
            clearInterval(longInterval);
        }, 300000); // 5 minutes
    }, 10000); // Démarrer après 10 secondes
})();
</script>
""", unsafe_allow_html=True)

# Initialisation
if 'db' not in st.session_state:
    st.session_state.db = Database()

if 'user' not in st.session_state:
    st.session_state.user = None

if 'df' not in st.session_state:
    st.session_state.df = None

if 'analyzer' not in st.session_state:
    st.session_state.analyzer = None

if 'ai_assistant' not in st.session_state:
    st.session_state.ai_assistant = AIAssistant()

def get_notification_manager():
    """Retourne le gestionnaire de notifications pour l'utilisateur actuel"""
    if st.session_state.user:
        return NotificationManager(st.session_state.db, st.session_state.user['id'])
    return NotificationManager(st.session_state.db, None)

def get_user_font_family():
    """Récupère la police préférée de l'utilisateur"""
    try:
        if hasattr(st.session_state, 'user') and st.session_state.user and 'db' in st.session_state:
            prefs = st.session_state.db.get_user_preferences(st.session_state.user['id'])
            if prefs and prefs.get('font_family'):
                return prefs.get('font_family')
    except (AttributeError, KeyError):
        pass
    return 'Arial'  # Police par défaut

def generate_custom_css():
    """Génère le CSS personnalisé avec la police de l'utilisateur"""
    font_family = get_user_font_family()
    
    # Mapping des noms de polices aux imports Google Fonts
    font_imports = {
        'Arial': '',  # Police système, pas d'import nécessaire
        'Roboto': "@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap');",
        'Inter': "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');",
        'Open Sans': "@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700;800&display=swap');",
        'Lato': "@import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700;900&display=swap');",
        'Montserrat': "@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap');",
        'Poppins': "@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');",
        'Raleway': "@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800;900&display=swap');"
    }
    
    # Générer l'import pour la police sélectionnée si nécessaire
    font_import = font_imports.get(font_family, '')
    
    # Préparer le nom de la police pour le CSS (ajouter des guillemets si nécessaire)
    if font_family == 'Arial':
        font_css = 'Arial, sans-serif'
    else:
        font_css = f"'{font_family}', sans-serif"
    
    return f"""
<style>
    {font_import}
    
    /* Import de toutes les polices Google (pour que toutes soient disponibles) */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700;900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800;900&display=swap');
    
    /* ============================================
       SOLUTION ULTIME : MASQUER LE PREMIER ÉLÉMENT DE LA SIDEBAR
       (où apparaît souvent "keyboard_double_arrow_right")
       ============================================ */
    
    /* Masquer UNIQUEMENT le texte "keyboard_double_arrow_right" - Solution simple et sûre */
    /* Le JavaScript gère le masquage visuel du texte sans affecter les menus */
    
    /* Masquer les éléments avec classes/attributs keyboard */
    [class*="keyboard_double"], 
    [class*="keyboard"],
    [data-testid*="keyboard"],
    [id*="keyboard"],
    [aria-label*="keyboard"],
    [title*="keyboard"] {{
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        font-size: 0 !important;
        height: 0 !important;
        width: 0 !important;
        overflow: hidden !important;
        position: absolute !important;
        left: -9999px !important;
        pointer-events: none !important;
    }}
    
    
    /* Style global */
    .main {{
        font-family: {font_css} !important;
        color: #000000 !important;
        background-color: #ffffff !important;
    }}
    
    /* Appliquer la police partout SAUF aux icônes */
    body,
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"],
    .element-container,
    .stMarkdown,
    p, h1, h2, h3, h4, h5, h6,
    div:not([style*="background"]):not([style*="gradient"]),
    span:not(.material-icons):not([style*="background"]):not([style*="gradient"]),
    label,
    .stText {{
        font-family: {font_css} !important;
        color: #1f2937 !important;
    }}
    
    /* ✅ RESTAURATION DES ICÔNES */
    .material-icons,
    span.material-icons,
    i.material-icons {{
        font-family: 'Material Icons' !important;
        font-weight: normal !important;
        font-style: normal !important;
    }}
    
    /* Texte blanc UNIQUEMENT pour les zones avec gradients sombres (violet/rose) */
    div[style*="gradient"][style*="#667eea"] h1, 
    div[style*="gradient"][style*="#667eea"] h2, 
    div[style*="gradient"][style*="#667eea"] h3, 
    div[style*="gradient"][style*="#667eea"] p,
    div[style*="gradient"][style*="#f093fb"] h1,
    div[style*="gradient"][style*="#f093fb"] h2,
    div[style*="gradient"][style*="#f093fb"] h3,
    div[style*="gradient"][style*="#f093fb"] p,
    div[style*="gradient"][style*="#10b981"] h1,
    div[style*="gradient"][style*="#10b981"] h2,
    div[style*="gradient"][style*="#10b981"] h3,
    div[style*="gradient"][style*="#10b981"] p {{
        color: white !important;
        font-family: {font_css} !important;
    }}
    
    /* Texte noir pour les autres zones avec gradients clairs */
    div[style*="gradient"][style*="#f8f9fa"] h1, 
    div[style*="gradient"][style*="#f8f9fa"] h2, 
    div[style*="gradient"][style*="#f8f9fa"] h3, 
    div[style*="gradient"][style*="#f8f9fa"] p,
    div[style*="gradient"][style*="#ffffff"] h1,
    div[style*="gradient"][style*="#ffffff"] h2,
    div[style*="gradient"][style*="#ffffff"] h3,
    div[style*="gradient"][style*="#ffffff"] p {{
        color: #1f2937 !important;
        font-family: {font_css} !important;
    }}
    
    /* Fond blanc pour l'application */
    .stApp, [data-testid="stAppViewContainer"] {{
        background-color: #ffffff !important;
    }}
    
    /* Fond blanc pour le contenu principal */
    .main .block-container {{
        background-color: #ffffff !important;
    }}
    
    /* Texte noir pour les métriques et statistiques */
    .metric-card, .metric-card * {{
        color: #000000 !important;
        font-family: {font_css} !important;
    }}
    
    /* Texte noir pour les tableaux */
    .stDataFrame, table, th, td {{
        color: #000000 !important;
        font-family: {font_css} !important;
    }}
    
    /* Texte noir pour les labels des inputs */
    .stTextInput label, .stTextArea label, 
    .stSelectbox label, .stNumberInput label,
    .stDateInput label, .stTimeInput label {{
        color: #1f2937 !important;
        font-weight: 500 !important;
        font-family: {font_css} !important;
    }}
    
    /* Améliorer le contraste des selectbox et inputs */
    .stSelectbox > div > div {{
        background-color: #ffffff !important;
        color: #1f2937 !important;
        font-family: {font_css} !important;
    }}
    
    .stSelectbox [data-baseweb="select"] {{
        background-color: #ffffff !important;
        color: #1f2937 !important;
        font-family: {font_css} !important;
    }}
    
    .stSelectbox [data-baseweb="select"] > div {{
        color: #1f2937 !important;
        font-family: {font_css} !important;
    }}
    
    /* Texte visible dans les dropdowns */
    div[data-baseweb="select"] > div {{
        color: #1f2937 !important;
        background-color: #ffffff !important;
        font-family: {font_css} !important;
    }}
    
    /* Liste déroulante visible */
    ul[role="listbox"] {{
        background-color: #ffffff !important;
    }}
    
    ul[role="listbox"] li {{
        color: #1f2937 !important;
        background-color: #ffffff !important;
        font-family: {font_css} !important;
    }}
    
    ul[role="listbox"] li:hover {{
        background-color: #f3f4f6 !important;
        color: #1f2937 !important;
    }}
    
    /* Texte noir pour les alertes (sauf les alertes d'erreur) */
    .stAlert {{
        color: #1f2937 !important;
        font-family: {font_css} !important;
    }}
    
    /* Texte noir pour les tabs */
    .stTabs [data-baseweb="tab"] {{
        color: #1f2937 !important;
        font-family: {font_css} !important;
        background-color: #ffffff !important;
    }}
    
    /* Texte noir pour les onglets actifs et inactifs */
    .stTabs [data-baseweb="tab"] > div {{
        color: #1f2937 !important;
        background-color: #ffffff !important;
    }}
    
    /* Texte noir pour le contenu des onglets */
    .stTabs [data-baseweb="tab"] span {{
        color: #1f2937 !important;
    }}
    
    /* Onglets actifs avec fond clair et texte noir */
    .stTabs [data-baseweb="tab"][aria-selected="true"] {{
        color: #1f2937 !important;
        background-color: #f3f4f6 !important;
        border-bottom: 2px solid #667eea !important;
    }}
    
    /* Onglets inactifs avec texte noir */
    .stTabs [data-baseweb="tab"][aria-selected="false"] {{
        color: #1f2937 !important;
        background-color: #ffffff !important;
    }}
    
    /* Forcer le texte en noir pour tous les éléments dans les onglets */
    .stTabs [data-baseweb="tab"] * {{
        color: #1f2937 !important;
    }}
    
    /* Améliorer la visibilité des métriques */
    [data-testid="stMetricValue"] {{
        color: #1f2937 !important;
        font-family: {font_css} !important;
    }}
    
    [data-testid="stMetricLabel"] {{
        color: #6b7280 !important;
        font-family: {font_css} !important;
    }}
    
    /* Texte visible dans tous les conteneurs */
    .element-container, .stMarkdown {{
        color: #1f2937 !important;
        font-family: {font_css} !important;
    }}
    
    /* Masquer le footer GitHub de Streamlit Cloud - VERSION COMPLÈTE POUR MOBILE ET DESKTOP */
    footer[data-testid="stFooter"],
    footer[data-testid="stFooter"] *,
    .stApp footer,
    .stApp footer *,
    div[data-testid="stDecoration"],
    iframe[title*="github"],
    iframe[title*="GitHub"],
    iframe[title*="GitHub"] *,
    a[href*="github.com"],
    a[href*="github.com"] *,
    /* Masquer tous les liens GitHub */
    a[href*="github"],
    /* Masquer les badges "Made with Streamlit" */
    a[href*="streamlit.io"],
    a[href*="streamlit.io"] *,
    /* Masquer les éléments dans le footer */
    footer *,
    [role="contentinfo"],
    [role="contentinfo"] *,
    /* Masquer les éléments avec des classes GitHub */
    [class*="github"],
    [class*="GitHub"],
    [id*="github"],
    [id*="GitHub"],
    /* Masquer les éléments avec des attributs GitHub */
    [aria-label*="github"],
    [aria-label*="GitHub"],
    [title*="github"],
    [title*="GitHub"] {{
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        width: 0 !important;
        opacity: 0 !important;
        position: absolute !important;
        left: -9999px !important;
        overflow: hidden !important;
        pointer-events: none !important;
    }}
    
    /* Masquer spécifiquement sur mobile */
    @media (max-width: 768px) {{
        footer,
        footer *,
        [data-testid="stFooter"],
        [data-testid="stFooter"] *,
        a[href*="github"],
        a[href*="streamlit"],
        iframe[title*="github"],
        iframe[title*="GitHub"],
        [class*="github"],
        [id*="github"] {{
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            width: 0 !important;
            opacity: 0 !important;
            position: absolute !important;
            left: -9999px !important;
            overflow: hidden !important;
            pointer-events: none !important;
        }}
    }}
    
    /* Forcer le texte en noir pour les sections sans gradient sombre */
    .stMarkdown h1:not([style*="color: white"]):not([style*="color:white"]),
    .stMarkdown h2:not([style*="color: white"]):not([style*="color:white"]),
    .stMarkdown h3:not([style*="color: white"]):not([style*="color:white"]),
    .stMarkdown p:not([style*="color: white"]):not([style*="color:white"]),
    .stMarkdown span:not([style*="color: white"]):not([style*="color:white"]),
    .stMarkdown div:not([style*="color: white"]):not([style*="color:white"]) {{
        color: #1f2937 !important;
    }}
    
    /* Exception pour les textes explicitement en blanc dans les gradients sombres (headers uniquement) */
    div[style*="gradient"][style*="#667eea"] h1,
    div[style*="gradient"][style*="#667eea"] h2,
    div[style*="gradient"][style*="#667eea"] h3,
    div[style*="gradient"][style*="#f093fb"] h1,
    div[style*="gradient"][style*="#f093fb"] h2,
    div[style*="gradient"][style*="#f093fb"] h3,
    div[style*="gradient"][style*="#10b981"] h1,
    div[style*="gradient"][style*="#10b981"] h2,
    div[style*="gradient"][style*="#10b981"] h3 {{
        color: white !important;
    }}
    
    /* Forcer le texte en noir pour les boutons et onglets avec gradient */
    button[style*="gradient"],
    .stButton button[style*="gradient"],
    div[style*="gradient"] button,
    div[style*="gradient"] .stTabs *,
    .stTabs [data-baseweb="tab"][style*="gradient"] * {{
        color: #1f2937 !important;
    }}
    
    /* Forcer le texte en noir pour les éléments de navigation avec gradient */
    div[style*="gradient"]:not([style*="color: white"]):not([style*="color:white"]) *:not(h1):not(h2):not(h3):not(p[style*="color: white"]):not(p[style*="color:white"]) {{
        color: #1f2937 !important;
    }}
    
    /* Forcer le fond blanc pour les inputs */
    .stTextInput > div > div > input {{
        background-color: #ffffff !important;
        color: #1f2937 !important;
        font-family: {font_css} !important;
    }}
    
    .stNumberInput > div > div > input {{
        background-color: #ffffff !important;
        color: #1f2937 !important;
        font-family: {font_css} !important;
    }}
    
    /* Animations pour les transitions de pages */
    @keyframes fadeIn {{
        from {{
            opacity: 0;
            transform: translateY(20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    @keyframes slideInLeft {{
        from {{
            opacity: 0;
            transform: translateX(-50px);
        }}
        to {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
    
    @keyframes slideInRight {{
        from {{
            opacity: 0;
            transform: translateX(50px);
        }}
        to {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
    
    @keyframes scaleIn {{
        from {{
            opacity: 0;
            transform: scale(0.9);
        }}
        to {{
            opacity: 1;
            transform: scale(1);
        }}
    }}
    
    @keyframes float {{
        0%, 100% {{
            transform: translateY(0px);
        }}
        50% {{
            transform: translateY(-20px);
        }}
    }}
    
    /* Styles spécifiques pour améliorer la visibilité des composants Streamlit */
    [data-baseweb="select"] {{
        background-color: #ffffff !important;
        font-family: {font_css} !important;
    }}
    
    [data-baseweb="select"] > div {{
        color: #1f2937 !important;
        background-color: #ffffff !important;
        font-family: {font_css} !important;
    }}
    
    /* Popover (liste déroulante) avec fond blanc et texte sombre */
    [data-baseweb="popover"] {{
        background-color: #ffffff !important;
    }}
    
    [data-baseweb="popover"] ul {{
        background-color: #ffffff !important;
    }}
    
    [data-baseweb="popover"] li {{
        color: #1f2937 !important;
        background-color: #ffffff !important;
        font-family: {font_css} !important;
    }}
    
    [data-baseweb="popover"] li:hover {{
        background-color: #f3f4f6 !important;
        color: #1f2937 !important;
    }}
    
    [data-baseweb="popover"] li[aria-selected="true"] {{
        background-color: #e5e7eb !important;
        color: #1f2937 !important;
    }}
    
    /* Inputs avec fond blanc et texte sombre */
    input[type="text"], input[type="number"], input[type="email"], input[type="password"] {{
        background-color: #ffffff !important;
        color: #1f2937 !important;
        border: 1px solid #d1d5db !important;
        caret-color: #1f2937 !important;
        font-family: {font_css} !important;
    }}
    
    input[type="text"]:focus, input[type="number"]:focus, 
    input[type="email"]:focus, input[type="password"]:focus {{
        background-color: #ffffff !important;
        color: #1f2937 !important;
        border-color: #667eea !important;
        caret-color: #667eea !important;
    }}
    
    /* Multiselect avec texte visible */
    [data-baseweb="tag"] {{
        background-color: #e5e7eb !important;
        color: #1f2937 !important;
        font-family: {font_css} !important;
    }}
    
    .page-transition {{
        animation: fadeIn 0.6s ease-out;
    }}
    
    .feature-card {{
        animation: scaleIn 0.5s ease-out;
        animation-fill-mode: both;
    }}
    
    .feature-card:nth-child(1) {{ animation-delay: 0.1s; }}
    .feature-card:nth-child(2) {{ animation-delay: 0.2s; }}
    .feature-card:nth-child(3) {{ animation-delay: 0.3s; }}
    .feature-card:nth-child(4) {{ animation-delay: 0.4s; }}
    
    /* En-tête principal */
    .main-header {{
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        padding: 1.5rem 1rem;
        margin-bottom: 2rem;
        letter-spacing: -1px;
        font-family: {font_css} !important;
    }}
    
    /* Badges */
    .premium-badge {{
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 25px;
        font-weight: 600;
        display: inline-block;
        box-shadow: 0 4px 15px rgba(245, 87, 108, 0.3);
        font-size: 0.85rem;
        font-family: {font_css} !important;
    }}
    
    .free-badge {{
        background: linear-gradient(135deg, #95a5a6 0%, #7f8c8d 100%);
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 25px;
        font-weight: 600;
        display: inline-block;
        font-size: 0.85rem;
        font-family: {font_css} !important;
    }}
    
    /* Cartes de métriques */
    .metric-card {{
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin: 0.5rem 0;
        border: 1px solid rgba(102, 126, 234, 0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    
    .metric-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.15);
    }}
    
    /* Boutons */
    .stButton>button {{
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.85rem 2rem;
        border-radius: 10px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        font-family: {font_css} !important;
    }}
    
    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }}
    
    /* Section d'upload */
    .upload-section {{
        border: 3px dashed #667eea;
        padding: 3rem 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 1.5rem 0;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
        transition: all 0.3s ease;
    }}
    
    .upload-section:hover {{
        border-color: #764ba2;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
    }}
    
    /* Sidebar améliorée */
    .css-1d391kg {{
        background: linear-gradient(180deg, #f8f9fa 0%, #ffffff 100%);
    }}
    
    /* Conteneurs de graphiques */
    .stPlotlyChart {{
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }}
    
    /* Alertes et messages */
    .stAlert {{
        border-radius: 10px;
        border-left: 4px solid;
    }}
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        font-weight: 600;
        font-family: {font_css} !important;
        color: #1f2937 !important;
        background-color: #ffffff !important;
    }}
    
    /* Forcer le texte en noir pour tous les onglets */
    .stTabs [data-baseweb="tab"] > div,
    .stTabs [data-baseweb="tab"] span,
    .stTabs [data-baseweb="tab"] p {{
        color: #1f2937 !important;
    }}
    
    /* Onglets actifs avec fond clair */
    .stTabs [data-baseweb="tab"][aria-selected="true"] {{
        background-color: #f3f4f6 !important;
        color: #1f2937 !important;
        border-bottom: 3px solid #667eea !important;
    }}
    
    /* Onglets inactifs */
    .stTabs [data-baseweb="tab"][aria-selected="false"] {{
        background-color: #ffffff !important;
        color: #1f2937 !important;
    }}
    
    /* Override pour les onglets avec gradient - forcer texte noir */
    .stTabs [data-baseweb="tab"] * {{
        color: #1f2937 !important;
    }}
    
    /* Amélioration des inputs */
    .stTextInput>div>div>input {{
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        transition: border-color 0.3s ease;
        font-family: {font_css} !important;
    }}
    
    .stTextInput>div>div>input:focus {{
        border-color: #667eea;
    }}
    
    /* Scrollbar personnalisée */
    ::-webkit-scrollbar {{
        width: 10px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: #f1f1f1;
        border-radius: 10px;
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }}
    
    /* Page de présentation */
    .landing-hero {{
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        position: relative;
        overflow: hidden;
    }}
    
    .landing-hero::before {{
        content: '';
        position: absolute;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: float 20s ease-in-out infinite;
    }}
    
    .hero-subtitle {{
        font-size: 1.5rem;
        color: rgba(255,255,255,0.95);
        text-align: center;
        margin-bottom: 3rem;
        animation: fadeIn 1.2s ease-out;
        z-index: 1;
        position: relative;
        font-family: {font_css} !important;
    }}
    
    .feature-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        padding: 3rem 0;
    }}
    
    .feature-item {{
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        text-align: center;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        font-family: {font_css} !important;
    }}
    
    .feature-item:hover {{
        transform: translateY(-10px);
        box-shadow: 0 20px 60px rgba(0,0,0,0.2);
        border-color: #667eea;
    }}
    
    .feature-icon {{
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }}
    
    .cta-button {{
        background: white;
        color: #667eea;
        padding: 1rem 3rem;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1.2rem;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        animation: scaleIn 1.5s ease-out;
        z-index: 1;
        position: relative;
        font-family: {font_css} !important;
    }}
    
    .cta-button:hover {{
        transform: scale(1.05);
        box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    }}
    
    .stats-section {{
        background: white;
        padding: 4rem 2rem;
    }}
    
    .stat-item {{
        text-align: center;
        padding: 2rem;
        font-family: {font_css} !important;
    }}
    
    .stat-number {{
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: {font_css} !important;
    }}
    
    /* Transitions de pages */
    .stApp {{
        transition: opacity 0.3s ease-in-out;
    }}
    
    /* Animation pour les éléments de contenu */
    .content-wrapper {{
        animation: fadeIn 0.6s ease-out;
    }}
    
    /* Smooth transitions pour les changements de page */
    [data-testid="stAppViewContainer"] {{
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    
    /* Amélioration des transitions pour les graphiques */
    .element-container {{
        animation: fadeIn 0.5s ease-out;
    }}
    
    /* Transition pour les cartes */
    .card-transition {{
        animation: scaleIn 0.4s ease-out;
    }}
    
    /* Transition pour les boutons */
    .stButton > button {{
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }}
    
    /* Transition pour les inputs */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select {{
        transition: all 0.3s ease !important;
    }}
    
    /* Appliquer la police aux éléments spécifiques */
    input, textarea, select, button {{
        font-family: {font_css} !important;
    }}
</style>
"""
    
    return css

# Générer et appliquer le CSS personnalisé
custom_css = generate_custom_css()
st.markdown(custom_css, unsafe_allow_html=True)

# Script JavaScript pour masquer le texte "keyboard_double_arrow_right"
hide_icon_script = """
<script>
(function() {
    function hideKeyboardDoubleArrow() {
        // Chercher tous les éléments qui contiennent ce texte
        const walker = document.createTreeWalker(
            document.body,
            NodeFilter.SHOW_TEXT,
            null,
            false
        );
        
        let node;
        while (node = walker.nextNode()) {
            if (node.textContent && node.textContent.includes('keyboard_double_arrow_right')) {
                if (node.parentElement) {
                    node.parentElement.style.display = 'none';
                    node.parentElement.style.visibility = 'hidden';
                    node.parentElement.style.opacity = '0';
                    node.parentElement.style.fontSize = '0';
                    node.parentElement.style.height = '0';
                    node.parentElement.style.width = '0';
                    node.parentElement.style.overflow = 'hidden';
                }
            }
        }
    }
    
    // Exécuter immédiatement
    hideKeyboardDoubleArrow();
    
    // Exécuter après le chargement de la page
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', hideKeyboardDoubleArrow);
    } else {
        hideKeyboardDoubleArrow();
    }
    
    // Exécuter après un court délai pour les éléments chargés dynamiquement
    setTimeout(hideKeyboardDoubleArrow, 100);
    setTimeout(hideKeyboardDoubleArrow, 500);
    setTimeout(hideKeyboardDoubleArrow, 1000);
    
    // Observer les changements du DOM
    const observer = new MutationObserver(hideKeyboardDoubleArrow);
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
})();
</script>
"""
st.markdown(hide_icon_script, unsafe_allow_html=True)

def landing_page():
    """Page de présentation professionnelle"""
    # Section Hero
    st.markdown("""
    <div class="landing-hero">
        <h1 class="hero-title">📊 Social Media Analytics Pro</h1>
        <p class="hero-subtitle">Transformez vos données en insights stratégiques avec l'intelligence artificielle</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Section Features
    st.markdown('<h2 class="section-title">✨ Fonctionnalités Puissantes</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="feature-item feature-card">
            <span class="feature-icon">🤖</span>
            <h3>IA Avancée</h3>
            <p>Analyse intelligente de vos données avec des recommandations personnalisées</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-item feature-card">
            <span class="feature-icon">📈</span>
            <h3>Visualisations</h3>
            <p>Graphiques interactifs et cartes géographiques pour une meilleure compréhension</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-item feature-card">
            <span class="feature-icon">🔮</span>
            <h3>Prédictions</h3>
            <p>Anticipez les tendances et optimisez votre stratégie de contenu</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="feature-item feature-card">
            <span class="feature-icon">📊</span>
            <h3>Statistiques</h3>
            <p>Analyses approfondies avec tests statistiques et corrélations</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Section Stats
    st.markdown('<div class="stats-section">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">⭐ Pourquoi Nous Choisir ?</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-item">
            <div class="stat-number">100%</div>
            <h3>Précision</h3>
            <p>Analyses fiables basées sur des algorithmes éprouvés</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-item">
            <div class="stat-number">24/7</div>
            <h3>Disponibilité</h3>
            <p>Accédez à vos données et analyses à tout moment</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-item">
            <div class="stat-number">∞</div>
            <h3>Scalabilité</h3>
            <p>Gérez des volumes de données illimités</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Call to Action
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ Commencer Maintenant", key="landing_cta", use_container_width=True):
            st.session_state.show_landing = False
            st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)

def login_page():
    """Page de connexion/inscription professionnelle"""
    # Header professionnel avec gradient
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 3rem 2rem; border-radius: 20px; margin-bottom: 3rem;
                box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3); text-align: center;">
        <h1 style="color: white; font-size: 3rem; font-weight: 800; margin: 0 0 1rem 0;">
            📊 Social Media Analytics Pro
        </h1>
        <p style="color: rgba(255,255,255,0.95); font-size: 1.4rem; margin: 0; font-weight: 300;">
            Analysez l'engagement de vos réseaux sociaux avec l'IA
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Conteneur principal pour les formulaires
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Carte principale avec ombre
        st.markdown("""
        <div style="background: white; padding: 0; border-radius: 20px;
                    box-shadow: 0 10px 40px rgba(0,0,0,0.1); overflow: hidden;">
        </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["🔐 Connexion", "📝 Inscription"])
        
        with tab1:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
            <div style="text-align: center; margin-bottom: 2rem;">
                <h2 style="color: #1f2937; font-size: 2rem; font-weight: 700; margin: 0;">
                    Accédez à votre espace
                </h2>
                <p style="color: #6b7280; font-size: 1.1rem; margin-top: 0.5rem;">
                    Connectez-vous à votre compte pour accéder à vos analyses
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Formulaire de connexion dans une carte
            with st.container():
                email = st.text_input(
                    "📧 Adresse email",
                    key="login_email",
                    placeholder="votre.email@exemple.com"
                )
                
                password = st.text_input(
                    "🔒 Mot de passe",
                    type="password",
                    key="login_password",
                    placeholder="Entrez votre mot de passe"
                )
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                if st.button(
                    "🔐 Se connecter",
                    key="login_btn",
                    type="primary",
                    use_container_width=True
                ):
                    if email and password:
                        user = st.session_state.db.authenticate_user(email, password)
                        if user:
                            st.session_state.user = user
                            st.markdown("""
                            <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                                        padding: 1.5rem; border-radius: 15px; margin-top: 1rem;
                                        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.3);">
                                <h3 style="color: white; margin: 0; text-align: center;">
                                    ✅ Connexion réussie!
                                </h3>
                            </div>
                            """, unsafe_allow_html=True)
                            st.balloons()
                            st.rerun()
                        else:
                            st.markdown("""
                            <div style="background: #fee2e2; padding: 1.5rem; border-radius: 15px;
                                        border-left: 4px solid #ef4444; margin-top: 1rem;">
                                <p style="color: #991b1b; margin: 0; font-weight: 600;">
                                    ❌ Email ou mot de passe incorrect
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.markdown("""
                        <div style="background: #fef3c7; padding: 1.5rem; border-radius: 15px;
                                    border-left: 4px solid #f59e0b; margin-top: 1rem;">
                            <p style="color: #78350f; margin: 0;">
                                ⚠️ Veuillez remplir tous les champs
                            </p>
                        </div>
                        """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
        
        with tab2:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
            <div style="text-align: center; margin-bottom: 2rem;">
                <h2 style="color: #1f2937; font-size: 2rem; font-weight: 700; margin: 0;">
                    Créez votre compte gratuit
                </h2>
                <p style="color: #6b7280; font-size: 1.1rem; margin-top: 0.5rem;">
                    Rejoignez-nous et commencez à analyser vos performances dès aujourd'hui
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Formulaire d'inscription dans une carte
            with st.container():
                st.markdown("""
                <div style="background: #f8f9fa; padding: 1rem; border-radius: 10px; margin-bottom: 1.5rem;">
                    <p style="color: #6b7280; margin: 0; font-size: 0.9rem;">
                        <strong style="color: #667eea;">*</strong> Champs obligatoires
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("### 👤 Informations personnelles")
                
                col1, col2 = st.columns(2)
                with col1:
                    first_name = st.text_input(
                        "Prénom",
                        key="signup_first_name",
                        placeholder="Jean"
                    )
                with col2:
                    last_name = st.text_input(
                        "Nom",
                        key="signup_last_name",
                        placeholder="Dupont"
                    )
                
                new_email = st.text_input(
                    "📧 Email *",
                    key="signup_email",
                    placeholder="votre.email@exemple.com"
                )
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("### 🏢 Informations professionnelles")
                
                col1, col2 = st.columns(2)
                with col1:
                    company = st.text_input(
                        "Entreprise",
                        key="signup_company",
                        placeholder="Nom de votre entreprise"
                    )
                with col2:
                    job_title = st.text_input(
                        "Poste",
                        key="signup_job_title",
                        placeholder="Votre fonction"
                    )
                
                phone = st.text_input(
                    "📱 Téléphone",
                    key="signup_phone",
                    placeholder="+33 6 12 34 56 78"
                )
                
                bio = st.text_area(
                    "📝 Bio (optionnel)",
                    key="signup_bio",
                    height=100,
                    placeholder="Parlez-nous un peu de vous..."
                )
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("### 🔒 Sécurité")
                
                new_password = st.text_input(
                    "🔒 Mot de passe (min. 6 caractères) *",
                    type="password",
                    key="signup_password",
                    placeholder="Minimum 6 caractères"
                )
                confirm_password = st.text_input(
                    "🔒 Confirmer le mot de passe *",
                    type="password",
                    key="confirm_password",
                    placeholder="Répétez votre mot de passe"
                )
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                if st.button(
                    "✨ Créer mon compte",
                    key="signup_btn",
                    type="primary",
                    use_container_width=True
                ):
                    if new_email and new_password and confirm_password:
                        if len(new_password) < 6:
                            st.markdown("""
                            <div style="background: #fee2e2; padding: 1.5rem; border-radius: 15px;
                                        border-left: 4px solid #ef4444; margin-top: 1rem;">
                                <p style="color: #991b1b; margin: 0; font-weight: 600;">
                                    ❌ Le mot de passe doit contenir au moins 6 caractères
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
                        elif new_password != confirm_password:
                            st.markdown("""
                            <div style="background: #fee2e2; padding: 1.5rem; border-radius: 15px;
                                        border-left: 4px solid #ef4444; margin-top: 1rem;">
                                <p style="color: #991b1b; margin: 0; font-weight: 600;">
                                    ❌ Les mots de passe ne correspondent pas
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            success, message = st.session_state.db.create_user(
                                new_email, new_password,
                                first_name=first_name if first_name else None,
                                last_name=last_name if last_name else None,
                                company=company if company else None,
                                phone=phone if phone else None,
                                job_title=job_title if job_title else None,
                                bio=bio if bio else None
                            )
                            if success:
                                st.markdown(f"""
                                <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                                            padding: 2rem; border-radius: 15px; margin-top: 1rem;
                                            box-shadow: 0 4px 20px rgba(16, 185, 129, 0.3); text-align: center;">
                                    <h3 style="color: white; margin: 0 0 0.5rem 0;">
                                        ✅ {message}
                                    </h3>
                                    <p style="color: rgba(255,255,255,0.9); margin: 0;">
                                        Vous pouvez maintenant vous connecter.
                                    </p>
                                </div>
                                """, unsafe_allow_html=True)
                                st.balloons()
                            else:
                                st.markdown(f"""
                                <div style="background: #fee2e2; padding: 1.5rem; border-radius: 15px;
                                            border-left: 4px solid #ef4444; margin-top: 1rem;">
                                    <p style="color: #991b1b; margin: 0; font-weight: 600;">
                                        ❌ {message}
                                    </p>
                                </div>
                                """, unsafe_allow_html=True)
                    else:
                        st.markdown("""
                        <div style="background: #fef3c7; padding: 1.5rem; border-radius: 15px;
                                    border-left: 4px solid #f59e0b; margin-top: 1rem;">
                            <p style="color: #78350f; margin: 0;">
                                ⚠️ Veuillez remplir tous les champs obligatoires (Email et Mot de passe)
                            </p>
                        </div>
                        """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Section fonctionnalités avec design professionnel
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
                padding: 3rem 2rem; border-radius: 20px; margin-top: 3rem;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08);">
        <h2 style="color: #1f2937; font-size: 2.5rem; font-weight: 700; text-align: center; margin-bottom: 2rem;">
            ✨ Fonctionnalités Premium
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 15px;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.08); height: 100%;">
            <div style="font-size: 3rem; text-align: center; margin-bottom: 1rem;">📊</div>
            <h3 style="color: #1f2937; font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem;">
                Analyses Statistiques
            </h3>
            <ul style="color: #6b7280; line-height: 2; padding-left: 1.5rem;">
                <li>Tests de Kruskal-Wallis</li>
                <li>Corrélation de Spearman</li>
                <li>Test du Chi-carré</li>
                <li>Statistiques descriptives</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 15px;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.08); height: 100%;">
            <div style="font-size: 3rem; text-align: center; margin-bottom: 1rem;">🤖</div>
            <h3 style="color: #1f2937; font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem;">
                Assistant IA
            </h3>
            <ul style="color: #6b7280; line-height: 2; padding-left: 1.5rem;">
                <li>Interprétation automatique</li>
                <li>Recommandations personnalisées</li>
                <li>Insights actionnables</li>
                <li>Conseils par plateforme</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 15px;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.08); height: 100%;">
            <div style="font-size: 3rem; text-align: center; margin-bottom: 1rem;">📈</div>
            <h3 style="color: #1f2937; font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem;">
                Visualisations
            </h3>
            <ul style="color: #6b7280; line-height: 2; padding-left: 1.5rem;">
                <li>Graphiques interactifs</li>
                <li>Comparaisons multi-plateformes</li>
                <li>Prédictions de likes</li>
                <li>Tableaux de bord</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def premium_page():
    """Page d'abonnement premium professionnelle"""
    # Header professionnel
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                padding: 2.5rem 2rem; border-radius: 20px; margin-bottom: 2rem;
                box-shadow: 0 10px 40px rgba(240, 147, 251, 0.3);">
        <h1 style="color: white; font-size: 2.5rem; font-weight: 700; margin: 0;">
            💎 Passez en Premium
        </h1>
        <p style="color: rgba(255,255,255,0.95); font-size: 1.2rem; margin-top: 0.5rem;">
            Débloquez toutes les fonctionnalités avancées
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 15px;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.08);">
            <h3 style="color: #1f2937; margin-bottom: 1.5rem;">✨ Débloquez toutes les fonctionnalités!</h3>
            <div style="color: #6b7280; line-height: 2.5;">
                <p style="margin: 1rem 0;"><strong style="color: #667eea;">✅ Analyses approfondies</strong> - Rapports détaillés avec interprétations complètes</p>
                <p style="margin: 1rem 0;"><strong style="color: #667eea;">✅ Assistant IA illimité</strong> - Recommandations personnalisées et insights professionnels</p>
                <p style="margin: 1rem 0;"><strong style="color: #667eea;">✅ Prédictions avancées</strong> - Modèles ML pour prévoir vos performances</p>
                <p style="margin: 1rem 0;"><strong style="color: #667eea;">✅ Exports illimités</strong> - Téléchargez tous vos rapports et graphiques</p>
                <p style="margin: 1rem 0;"><strong style="color: #667eea;">✅ Support prioritaire</strong> - Assistance rapide pour toutes vos questions</p>
                <p style="margin: 1rem 0;"><strong style="color: #667eea;">✅ Analyses comparatives</strong> - Benchmark avec les moyennes du secteur</p>
                <p style="margin: 1rem 0;"><strong style="color: #667eea;">✅ Alertes personnalisées</strong> - Notifications sur vos performances</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2.5rem 2rem; border-radius: 20px; color: white; text-align: center;
                    box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);'>
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">👑</div>
            <h2 style='color: white; margin: 0; font-size: 1.8rem;'>Premium</h2>
            <h1 style='color: white; font-size: 4rem; font-weight: 800; margin: 0.5rem 0;'>5€</h1>
            <p style='color: rgba(255,255,255,0.9); font-size: 1.1rem; margin: 0;'>par mois</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Vérifier le statut actuel
        is_premium = st.session_state.db.check_premium_status(st.session_state.user['id'])
        
        if is_premium:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                        padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;
                        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.3);">
                <h3 style="color: white; margin: 0;">👑 Vous êtes déjà Premium!</h3>
                <p style="color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0;">
                    Profitez de toutes les fonctionnalités avancées
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            if st.button("💎 Activer Premium maintenant", key="subscribe_btn", use_container_width=True, type="primary"):
                from payment_handler import activate_demo_premium
                success = activate_demo_premium(st.session_state.user['id'])
                if success:
                    st.session_state.user['is_premium'] = True
                    st.success("🎉 Premium activé en mode démo!")
                    st.balloons()
                    st.rerun()
                else:
                    st.error("❌ Erreur lors de l'activation")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Section mode démo
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 15px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 2rem;">
        <h3 style="color: #1f2937; margin-bottom: 1rem;">💳 Mode démo disponible</h3>
        <p style="color: #6b7280; line-height: 1.8;">
            Cette version permet de tester Premium sans paiement. Cliquez sur "Activer Premium maintenant" ci-dessus pour activer toutes les fonctionnalités premium gratuitement.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Section paiement réel (optionnel)
    st.markdown("""
    <div style="background: #f8f9fa; padding: 2rem; border-radius: 15px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08);">
        <h3 style="color: #1f2937; margin-bottom: 1rem;">💳 Paiement réel (optionnel)</h3>
        <p style="color: #6b7280; line-height: 1.8;">
            Pour activer les paiements réels via Stripe:
        </p>
        <ol style="color: #6b7280; line-height: 2;">
            <li>Configurez vos clés Stripe dans le fichier <code>.env</code></li>
            <li>L'intégration Stripe sera automatiquement activée</li>
            <li>Les utilisateurs pourront payer 5€/mois</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Vérifier si Stripe est configuré
    from payment_handler import is_stripe_configured
    if is_stripe_configured():
        st.markdown("""
        <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                    padding: 1rem; border-radius: 10px; margin-top: 1rem;
                    box-shadow: 0 4px 20px rgba(16, 185, 129, 0.3);">
            <p style="color: white; margin: 0; font-weight: 600;">
                ✅ Stripe configuré - Paiements réels disponibles
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: #fef3c7; padding: 1rem; border-radius: 10px; margin-top: 1rem;
                    border-left: 4px solid #f59e0b;">
            <p style="color: #78350f; margin: 0;">
                ℹ️ Stripe non configuré - Mode démo uniquement
            </p>
        </div>
        """, unsafe_allow_html=True)

def apply_user_preferences():
    """Applique les préférences utilisateur au CSS"""
    if st.session_state.user:
        user_id = st.session_state.user['id']
        prefs = st.session_state.db.get_user_preferences(user_id)
        
        if prefs:
            primary_color = prefs.get('primary_color', '#667eea')
            secondary_color = prefs.get('secondary_color', '#764ba2')
            accent_color = prefs.get('accent_color', '#f093fb')
            text_color = prefs.get('text_color', '#1f2937')
            background_color = prefs.get('background_color', '#ffffff')
            font_family = prefs.get('font_family', 'Arial')
            theme = prefs.get('theme', 'light')
            
            # Déterminer les couleurs selon le thème
            if theme == 'dark':
                bg_color = '#1f2937'
                text_color_theme = '#f9fafb'
            elif theme == 'auto':
                # Utiliser la préférence système (par défaut clair)
                bg_color = background_color
                text_color_theme = text_color
            else:  # light
                bg_color = background_color
                text_color_theme = text_color
            
            # Appliquer les couleurs personnalisées
            st.markdown(f"""
            <style>
                /* Police personnalisée */
                * {{
                    font-family: '{font_family}', sans-serif !important;
                }}
                
                /* Couleurs personnalisées */
                .main-header {{
                    background: linear-gradient(135deg, {primary_color} 0%, {secondary_color} 50%, {accent_color} 100%);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    background-clip: text;
                }}
                
                .stButton>button {{
                    background: linear-gradient(135deg, {primary_color} 0%, {secondary_color} 100%);
                }}
                
                .premium-badge {{
                    background: linear-gradient(135deg, {accent_color} 0%, #f5576c 100%);
                }}
                
                /* Application de la couleur de fond */
                [data-testid="stAppViewContainer"] {{
                    background-color: {bg_color} !important;
                }}
                
                .main .block-container {{
                    background-color: {bg_color} !important;
                }}
                
                body, .stApp {{
                    background-color: {bg_color} !important;
                }}
                
                /* Application de la couleur du texte selon le thème */
                body, .stApp, [data-testid="stAppViewContainer"], 
                [data-testid="stHeader"], [data-testid="stSidebar"],
                .element-container, .stMarkdown, p, h1, h2, h3, h4, h5, h6,
                div, span, label, .stText, .stSelectbox label, .stNumberInput label {{
                    color: {text_color_theme} !important;
                }}
                
                .metric-card, .metric-card * {{
                    color: {text_color_theme} !important;
                }}
                
                .stDataFrame, table, th, td {{
                    color: {text_color_theme} !important;
                }}
                
                .stTextInput label, .stTextArea label, 
                .stSelectbox label, .stNumberInput label,
                .stDateInput label, .stTimeInput label {{
                    color: {text_color_theme} !important;
                }}
                
                .stAlert {{
                    color: {text_color_theme} !important;
                }}
                
                .stTabs [data-baseweb="tab"] {{
                    color: {text_color_theme} !important;
                }}
                
                /* Inputs avec fond adaptatif */
                input[type="text"], input[type="number"], input[type="email"], input[type="password"] {{
                    background-color: {bg_color} !important;
                    color: {text_color_theme} !important;
                    caret-color: {primary_color} !important;
                }}
                
                input[type="text"]:focus, input[type="number"]:focus, 
                input[type="email"]:focus, input[type="password"]:focus {{
                    background-color: {bg_color} !important;
                    color: {text_color_theme} !important;
                    caret-color: {primary_color} !important;
                }}
                
                ::-webkit-scrollbar-thumb {{
                    background: linear-gradient(135deg, {primary_color} 0%, {secondary_color} 100%);
                }}
            </style>
            """, unsafe_allow_html=True)

def main_app():
    """Application principale après connexion"""
    # Appliquer les préférences utilisateur
    apply_user_preferences()
    
    # Script JavaScript pour masquer le texte "keyboard_double_arrow_right" - VERSION AGRESSIVE
    st.markdown("""
    <script>
    (function() {
        function hideKeyboardDoubleArrow() {
            // Méthode 1: Parcourir tous les éléments
            const allElements = document.querySelectorAll('*');
            allElements.forEach(function(el) {
                if (el.textContent && (el.textContent.includes('keyboard_double_arrow_right') || 
                    el.textContent.includes('keyboard_double'))) {
                    el.style.cssText = 'display: none !important; visibility: hidden !important; opacity: 0 !important; font-size: 0 !important; height: 0 !important; width: 0 !important; overflow: hidden !important; position: absolute !important; left: -9999px !important;';
                }
            });
            
            // Méthode 2: Chercher dans la sidebar
            const sidebar = document.querySelector('[data-testid="stSidebar"]');
            if (sidebar) {
                const sidebarElements = sidebar.querySelectorAll('*');
                sidebarElements.forEach(function(el) {
                    if (el.textContent && (el.textContent.includes('keyboard_double_arrow_right') || 
                        el.textContent.includes('keyboard_double'))) {
                        el.style.cssText = 'display: none !important; visibility: hidden !important; opacity: 0 !important; font-size: 0 !important; height: 0 !important; width: 0 !important; overflow: hidden !important;';
                        // Supprimer aussi le texte
                        if (el.firstChild && el.firstChild.nodeType === 3) {
                            el.firstChild.textContent = '';
                        }
                    }
                });
            }
            
            // Méthode 3: Parcourir les nœuds texte
            const walker = document.createTreeWalker(
                document.body,
                NodeFilter.SHOW_TEXT,
                null,
                false
            );
            
            let node;
            while (node = walker.nextNode()) {
                if (node.textContent.includes('keyboard_double_arrow_right') || 
                    node.textContent.includes('keyboard_double')) {
                    // Supprimer le texte
                    node.textContent = '';
                    // Masquer le parent
                    if (node.parentElement) {
                        node.parentElement.style.cssText = 'display: none !important; visibility: hidden !important; opacity: 0 !important; font-size: 0 !important; height: 0 !important; width: 0 !important; overflow: hidden !important; position: absolute !important; left: -9999px !important;';
                    }
                }
            }
        }
        
        // Exécuter immédiatement
        hideKeyboardDoubleArrow();
        
        // Exécuter après le chargement
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', function() {
                hideKeyboardDoubleArrow();
                setInterval(hideKeyboardDoubleArrow, 50);
            });
        } else {
            hideKeyboardDoubleArrow();
            setInterval(hideKeyboardDoubleArrow, 50);
        }
        
        // Exécuter avec des délais multiples
        [50, 100, 200, 500, 1000, 2000, 3000, 5000].forEach(function(delay) {
            setTimeout(hideKeyboardDoubleArrow, delay);
        });
        
        // Observer les changements du DOM
        const observer = new MutationObserver(function(mutations) {
            hideKeyboardDoubleArrow();
        });
        observer.observe(document.body, {
            childList: true,
            subtree: true,
            characterData: true,
            attributes: true
        });
        
        // Exécuter en continu pendant 10 secondes
        let count = 0;
        const interval = setInterval(function() {
            hideKeyboardDoubleArrow();
            count++;
            if (count > 200) { // 10 secondes (200 * 50ms)
                clearInterval(interval);
            }
        }, 50);
    })();
    </script>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 👤 Profil")
        profile = st.session_state.db.get_user_profile(st.session_state.user['id'])
        if profile:
            name = ""
            if profile.get('first_name'):
                name += profile.get('first_name', '')
            if profile.get('last_name'):
                name += " " + profile.get('last_name', '')
            if name.strip():
                st.write(f"**{name.strip()}**")
            st.write(f"**Email:** {st.session_state.user['email']}")
        else:
            st.write(f"**Email:** {st.session_state.user['email']}")
        
        # Statut Premium
        is_premium = st.session_state.db.check_premium_status(st.session_state.user['id'])
        
        if is_premium:
            st.markdown('<span class="premium-badge">👑 PREMIUM</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="free-badge">🆓 GRATUIT</span>', unsafe_allow_html=True)
            st.markdown("---")
            if st.button("⬆️ Passer à Premium"):
                st.session_state.page = "premium"
                st.rerun()
        
        # Indicateur de mode démo
        from payment_handler import is_stripe_configured
        if not is_stripe_configured():
            st.markdown("---")
            st.markdown("### 🧪 Mode Démo")
            st.info("💡 Mode démo activé - Premium disponible sans paiement")
            if not is_premium and st.button("✨ Activer Premium Démo"):
                from payment_handler import activate_demo_premium
                success = activate_demo_premium(st.session_state.user['id'])
                if success:
                    st.session_state.user['is_premium'] = True
                    st.success("🎉 Premium démo activé!")
                    st.rerun()
        
        st.markdown("---")
        
        # Menu de navigation
        st.markdown("### 📋 Menu")
        menu_options = {
            "🏠 Accueil": "home",
            "📤 Importer des données": "upload",
            "📊 Analyses statistiques": "analysis",
            "🤖 Assistant IA": "ai_assistant",
            "📈 Visualisations": "visualizations",
            "🗺️ Carte par pays": "country_map",
            "🔮 Prédictions": "predictions",
            "💾 Mes projets": "projects",
            "👤 Mon Profil": "profile",
            "⚙️ Paramètres": "settings",
            "💎 Premium": "premium"
        }
        
        for label, page in menu_options.items():
            if st.button(label, key=f"menu_{page}"):
                st.session_state.page = page
                st.rerun()
        
        st.markdown("---")
        
        if st.button("🚪 Déconnexion"):
            st.session_state.user = None
            st.session_state.df = None
            st.session_state.analyzer = None
            st.rerun()
    
    # Contenu principal
    page = st.session_state.get('page', 'home')
    
    if page == "home":
        show_home_page()
    elif page == "upload":
        show_upload_page()
    elif page == "analysis":
        show_analysis_page()
    elif page == "ai_assistant":
        show_ai_assistant_page()
    elif page == "visualizations":
        show_visualizations_page()
    elif page == "country_map":
        show_country_map_page()
    elif page == "predictions":
        show_predictions_page()
    elif page == "projects":
        show_projects_page()
    elif page == "profile":
        show_profile_page()
    elif page == "settings":
        show_settings_page()
    elif page == "premium":
        premium_page()

def show_home_page():
    """Page d'accueil professionnelle"""
    # Récupérer les informations du profil pour personnaliser
    user_id = st.session_state.user['id']
    profile = st.session_state.db.get_user_profile(user_id)
    is_premium = st.session_state.db.check_premium_status(user_id)
    
    # Vérifier et afficher les notifications de performance si des données sont chargées
    if st.session_state.df is not None and len(st.session_state.df) > 0:
        notif_manager = get_notification_manager()
        # Vérifier les performances une seule fois par session
        if 'performance_checked' not in st.session_state:
            notif_manager.check_and_notify_performance(st.session_state.df)
            st.session_state.performance_checked = True
    
    # Header personnalisé
    if profile and (profile.get('first_name') or profile.get('last_name')):
        name = f"{profile.get('first_name', '')} {profile.get('last_name', '')}".strip()
        welcome_text = f"Bienvenue, {name} 👋"
    else:
        welcome_text = f"Bienvenue, {st.session_state.user.get('email', 'Utilisateur')} 👋"
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2.5rem 2rem; border-radius: 20px; margin-bottom: 2rem;
                box-shadow: 0 10px 40px rgba(102, 126, 234, 0.2);">
        <h1 style="color: white; font-size: 2.5rem; font-weight: 700; margin: 0;">
            {welcome_text}
        </h1>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.2rem; margin-top: 0.5rem;">
            Tableau de bord analytique • {datetime.now().strftime('%d %B %Y')}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Actions rapides
    st.markdown("### ⚡ Actions rapides")
    quick_actions = st.columns(4)
    
    with quick_actions[0]:
        if st.button("📤 Importer des données", use_container_width=True, type="primary"):
            st.session_state.page = "upload"
            st.rerun()
    
    with quick_actions[1]:
        if st.button("📊 Analyser", use_container_width=True):
            st.session_state.page = "analysis"
            st.rerun()
    
    with quick_actions[2]:
        if st.button("🤖 Assistant IA", use_container_width=True):
            st.session_state.page = "ai_assistant"
            st.rerun()
    
    with quick_actions[3]:
        if st.button("📈 Visualisations", use_container_width=True):
            st.session_state.page = "visualizations"
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Statistiques principales
    if st.session_state.df is not None:
        st.markdown("### 📊 Vue d'ensemble des performances")
        
        # Cartes de métriques professionnelles
        metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)
        
        with metrics_col1:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 15px;
                        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);">
                <div style="color: rgba(255,255,255,0.9); font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem;">
                    📁 DONNÉES
                </div>
                <div style="font-size: 2rem; font-weight: 700; color: white;">
                    {len(st.session_state.df):,}
                </div>
                <div style="color: rgba(255,255,255,0.85); font-size: 0.85rem; margin-top: 0.25rem;">
                    Lignes analysées
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with metrics_col2:
            platform_count = st.session_state.df['platform'].nunique() if 'platform' in st.session_state.df.columns else 0
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #764ba2 0%, #f093fb 100%); padding: 1.5rem; border-radius: 15px;
                        box-shadow: 0 4px 20px rgba(118, 75, 162, 0.3);">
                <div style="color: rgba(255,255,255,0.9); font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem;">
                    🌐 PLATEFORMES
                </div>
                <div style="font-size: 2rem; font-weight: 700; color: white;">
                    {platform_count}
                </div>
                <div style="color: rgba(255,255,255,0.85); font-size: 0.85rem; margin-top: 0.25rem;">
                    Réseaux sociaux
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with metrics_col3:
            total_likes = f"{st.session_state.df['likes'].sum():,.0f}" if 'likes' in st.session_state.df.columns else "0"
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 1.5rem; border-radius: 15px;
                        box-shadow: 0 4px 20px rgba(240, 147, 251, 0.3);">
                <div style="color: rgba(255,255,255,0.9); font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem;">
                    ❤️ INTERACTIONS
                </div>
                <div style="font-size: 2rem; font-weight: 700; color: white;">
                    {total_likes}
                </div>
                <div style="color: rgba(255,255,255,0.85); font-size: 0.85rem; margin-top: 0.25rem;">
                    Total de likes
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with metrics_col4:
            avg_engagement = f"{st.session_state.df['engagement_rate'].mean():.2f}%" if 'engagement_rate' in st.session_state.df.columns else "N/A"
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 1.5rem; border-radius: 15px;
                        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.3);">
                <div style="color: rgba(255,255,255,0.9); font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem;">
                    📊 ENGAGEMENT
                </div>
                <div style="font-size: 2rem; font-weight: 700; color: white;">
                    {avg_engagement}
                </div>
                <div style="color: rgba(255,255,255,0.85); font-size: 0.85rem; margin-top: 0.25rem;">
                    Taux moyen
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Graphiques et analyses
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### 📈 Performance par plateforme")
            if 'platform' in st.session_state.df.columns:
                visualizer = DataVisualizer(st.session_state.df)
                fig = visualizer.plot_engagement_comparison()
                if fig:
                    fig.update_layout(
                        height=400,
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(family="Inter", size=12)
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.info("📊 Graphique disponible après import des données")
            else:
                st.info("📊 Aucune donnée de plateforme disponible")
        
        with col2:
            st.markdown("### 🎯 Insights rapides")
            
            # Calculer quelques insights
            insights = []
            
            if 'platform' in st.session_state.df.columns and 'engagement_rate' in st.session_state.df.columns:
                platform_engagement = st.session_state.df.groupby('platform')['engagement_rate'].mean().sort_values(ascending=False)
                if len(platform_engagement) > 0:
                    best_platform = platform_engagement.index[0]
                    best_rate = platform_engagement.iloc[0]
                    insights.append(f"🏆 **{best_platform}** a le meilleur engagement ({best_rate:.2f}%)")
            
            if 'likes' in st.session_state.df.columns:
                total_likes_val = st.session_state.df['likes'].sum()
                avg_likes = st.session_state.df['likes'].mean()
                insights.append(f"📈 Total de **{total_likes_val:,.0f}** likes")
                insights.append(f"📊 Moyenne de **{avg_likes:,.0f}** likes par post")
            
            if len(insights) > 0:
                for insight in insights[:4]:  # Limiter à 4 insights
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1rem; border-radius: 10px;
                                margin-bottom: 0.75rem; box-shadow: 0 2px 8px rgba(102, 126, 234, 0.25);">
                        <p style="margin: 0; color: white; font-size: 0.9rem; line-height: 1.5; font-weight: 500;">
                            {insight}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("💡 Les insights apparaîtront après l'analyse de vos données")
            
            st.markdown("---")
            st.markdown("### 💡 Actions recommandées")
            
            action_buttons = [
                ("📊 Analyses approfondies", "analysis"),
                ("🤖 Conseils IA", "ai_assistant"),
                ("🗺️ Analyse géographique", "country_map"),
            ]
            
            for label, page in action_buttons:
                if st.button(label, key=f"quick_{page}", use_container_width=True):
                    st.session_state.page = page
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Section statistiques détaillées
        st.markdown("### 📋 Statistiques détaillées")
        
        stats_col1, stats_col2, stats_col3 = st.columns(3)
        
        with stats_col1:
            st.markdown("#### 📱 Par plateforme")
            if 'platform' in st.session_state.df.columns:
                platform_stats = st.session_state.df.groupby('platform').agg({
                    'likes': 'sum' if 'likes' in st.session_state.df.columns else 'count',
                    'engagement_rate': 'mean' if 'engagement_rate' in st.session_state.df.columns else lambda x: 0
                }).round(2)
                st.dataframe(platform_stats, use_container_width=True)
            else:
                st.info("Aucune donnée de plateforme")
        
        with stats_col2:
            st.markdown("#### 📅 Dernières activités")
            if 'date' in st.session_state.df.columns:
                recent_data = st.session_state.df.tail(5)[['date', 'platform', 'likes'] if all(c in st.session_state.df.columns for c in ['date', 'platform', 'likes']) else []]
                if len(recent_data) > 0:
                    st.dataframe(recent_data, use_container_width=True)
                else:
                    st.info("Aucune activité récente")
            else:
                st.info("💡 Ajoutez une colonne 'date' pour voir les activités récentes")
        
        with stats_col3:
            st.markdown("#### ⚙️ Statut du compte")
            status_info = []
            status_info.append(f"**Statut:** {'👑 Premium' if is_premium else '🆓 Gratuit'}")
            
            projects = st.session_state.db.get_user_projects(user_id)
            status_info.append(f"**Projets:** {len(projects)} sauvegardés")
            
            if profile and profile.get('created_at'):
                created = profile.get('created_at')[:10] if len(profile.get('created_at', '')) > 10 else profile.get('created_at')
                status_info.append(f"**Membre depuis:** {created}")
            
            for info in status_info:
                st.markdown(f"<div style='padding: 0.5rem 0;'>{info}</div>", unsafe_allow_html=True)
            
            if not is_premium:
                st.markdown("---")
                if st.button("💎 Passer à Premium", use_container_width=True, key="home_premium"):
                    st.session_state.page = "premium"
                    st.rerun()
    
    else:
        # État sans données - Design professionnel
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
                    padding: 3rem 2rem; border-radius: 20px; text-align: center;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin: 2rem 0;">
            <h2 style="color: #1f2937; font-size: 2rem; margin-bottom: 1rem;">
                ✨ Commencez votre analyse
            </h2>
            <p style="color: #6b7280; font-size: 1.1rem; margin-bottom: 2rem;">
                Importez vos données pour découvrir des insights puissants sur vos performances
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📚 Guide de démarrage")
        
        guide_col1, guide_col2, guide_col3 = st.columns(3)
        
        with guide_col1:
            st.markdown("""
            <div style="background: white; padding: 2rem; border-radius: 15px;
                        box-shadow: 0 4px 20px rgba(0,0,0,0.08); height: 100%;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">📤</div>
                <h3 style="color: #1f2937; margin-bottom: 1rem;">1. Importer</h3>
                <p style="color: #6b7280; line-height: 1.6;">
                    Uploadez votre fichier CSV ou Excel contenant vos métriques de réseaux sociaux
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with guide_col2:
            st.markdown("""
            <div style="background: white; padding: 2rem; border-radius: 15px;
                        box-shadow: 0 4px 20px rgba(0,0,0,0.08); height: 100%;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">📊</div>
                <h3 style="color: #1f2937; margin-bottom: 1rem;">2. Analyser</h3>
                <p style="color: #6b7280; line-height: 1.6;">
                    Utilisez nos outils statistiques avancés pour découvrir des patterns cachés
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with guide_col3:
            st.markdown("""
            <div style="background: white; padding: 2rem; border-radius: 15px;
                        box-shadow: 0 4px 20px rgba(0,0,0,0.08); height: 100%;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🤖</div>
                <h3 style="color: #1f2937; margin-bottom: 1rem;">3. Optimiser</h3>
                <p style="color: #6b7280; line-height: 1.6;">
                    Recevez des recommandations IA personnalisées pour améliorer vos performances
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Bouton d'action principal
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📤 Importer mes données maintenant", use_container_width=True, type="primary", key="home_upload_main"):
                st.session_state.page = "upload"
                st.rerun()

def show_upload_page():
    """Page d'importation de données professionnelle"""
    # Header professionnel
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2.5rem 2rem; border-radius: 20px; margin-bottom: 2rem;
                box-shadow: 0 10px 40px rgba(102, 126, 234, 0.2);">
        <h1 style="color: white; font-size: 2.5rem; font-weight: 700; margin: 0;">
            📤 Importer vos données
        </h1>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.2rem; margin-top: 0.5rem;">
            Chargez vos fichiers CSV ou Excel pour commencer l'analyse
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Section format des données
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 15px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 2rem;">
        <h3 style="color: #1f2937; margin-bottom: 1rem;">📋 Format des données attendu</h3>
        <p style="color: #6b7280; line-height: 1.8;">
            Votre fichier doit contenir les colonnes suivantes (au minimum):
        </p>
        <ul style="color: #6b7280; line-height: 2;">
            <li><strong style="color: #667eea;">platform</strong>: Nom de la plateforme (TikTok, Instagram, Facebook, etc.)</li>
            <li><strong style="color: #667eea;">likes</strong>: Nombre de likes</li>
            <li><strong style="color: #667eea;">followers</strong> ou <strong style="color: #667eea;">views</strong>: Pour calculer le taux d'engagement</li>
        </ul>
        <p style="color: #6b7280; margin-top: 1rem;">
            <strong>Colonnes optionnelles:</strong> comments, shares, saves, date, hour, country, etc.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Choisissez un fichier CSV, XLS ou XLSX",
        type=['csv', 'xls', 'xlsx'],
        help="Formats supportés: CSV, Excel (.xls, .xlsx)"
    )
    
    if uploaded_file is not None:
        try:
            # Lire le fichier selon son extension
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            # Carte de succès
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                        padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem;
                        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.3);">
                <h3 style="color: white; margin: 0; font-size: 1.3rem;">
                    ✅ Fichier chargé avec succès!
                </h3>
                <p style="color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0;">
                    {len(df):,} lignes • {len(df.columns)} colonnes détectées
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Aperçu des données dans une carte
            st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 15px;
                        box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 2rem;">
                <h3 style="color: #1f2937; margin-bottom: 1rem;">👁️ Aperçu des données</h3>
            </div>
            """, unsafe_allow_html=True)
            st.dataframe(df.head(10), use_container_width=True)
            
            # Informations sur les colonnes dans des cartes
            st.markdown("<br>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            
            with col1:
                numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
                st.markdown(f"""
                <div style="background: white; padding: 1.5rem; border-radius: 15px;
                            box-shadow: 0 4px 20px rgba(0,0,0,0.08);">
                    <h4 style="color: #667eea; margin-bottom: 1rem;">🔢 Colonnes numériques</h4>
                    <p style="color: #6b7280; line-height: 2;">
                        {', '.join(numeric_cols) if numeric_cols else 'Aucune'}
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                cat_cols = df.select_dtypes(include=['object']).columns.tolist()
                st.markdown(f"""
                <div style="background: white; padding: 1.5rem; border-radius: 15px;
                            box-shadow: 0 4px 20px rgba(0,0,0,0.08);">
                    <h4 style="color: #764ba2; margin-bottom: 1rem;">📝 Colonnes catégorielles</h4>
                    <p style="color: #6b7280; line-height: 2;">
                        {', '.join(cat_cols) if cat_cols else 'Aucune'}
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Options de traitement dans une carte
            st.markdown("""
            <div style="background: white; padding: 2rem; border-radius: 15px;
                        box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 2rem;">
                <h3 style="color: #1f2937; margin-bottom: 1.5rem;">⚙️ Options de prétraitement</h3>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                calculate_engagement = st.checkbox(
                    "Calculer le taux d'engagement automatiquement",
                    value=True,
                    help="Calcule l'engagement à partir des likes, followers, etc."
                )
            
            with col2:
                remove_na = st.checkbox(
                    "Supprimer les lignes avec valeurs manquantes",
                    value=False
                )
            
            if st.button("✅ Valider et utiliser ces données", type="primary"):
                # Prétraitement
                if remove_na:
                    df = df.dropna()
                
                # Calculer l'engagement
                if calculate_engagement:
                    analyzer = StatisticalAnalyzer(df)
                    df = analyzer.calculate_engagement_rate()
                
                # Sauvegarder dans la session
                st.session_state.df = df
                st.session_state.analyzer = StatisticalAnalyzer(df)
                
                # Notification
                notif_manager = get_notification_manager()
                notif_manager.notify_data_imported(len(df), uploaded_file.name)
                
                # Vérifier les performances et notifier si nécessaire
                notif_manager.check_and_notify_performance(df)
                
                st.success("🎉 Données prêtes pour l'analyse!")
                st.balloons()
                
                # Option de sauvegarde
                save_project = st.text_input("Nom du projet (pour sauvegarder)", key="save_project_name")
                if save_project and st.button("💾 Sauvegarder le projet"):
                    st.session_state.db.save_project(
                        st.session_state.user['id'],
                        save_project,
                        {'columns': df.columns.tolist(), 'shape': df.shape}
                    )
                    st.success(f"✅ Projet '{save_project}' sauvegardé!")
        
        except Exception as e:
            st.error(f"❌ Erreur lors de la lecture du fichier: {str(e)}")
    
    # Section exemple de données
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
                padding: 2rem; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.08);">
        <h3 style="color: #1f2937; margin-bottom: 1rem;">📝 Pas de données? Essayez avec un exemple</h3>
        <p style="color: #6b7280; margin-bottom: 1.5rem;">
            Chargez des données d'exemple pour tester toutes les fonctionnalités de l'application
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sélection du type de données d'exemple
    example_type = st.selectbox(
        "Choisissez un jeu de données d'exemple:",
        [
            "📊 Réseaux sociaux classiques (likes, followers, engagement)",
            "🌍 Réseaux sociaux avec pays (pour la carte géographique)",
            "🧠 Addiction aux réseaux sociaux (avec prédiction d'addiction)"
        ],
        key="example_type_select"
    )
    
    if st.button("📥 Charger ces données d'exemple", use_container_width=True, type="primary"):
        try:
            if "Addiction" in example_type:
                # Charger le fichier d'addiction (chercher d'abord localement, puis dans Documents)
                local_path = os.path.join(os.path.dirname(__file__), "example_addiction_data.csv")
                # Utiliser une variable d'environnement ou un chemin relatif au lieu d'un chemin hardcodé
                documents_path = os.getenv(
                    'ADDICTION_DATA_PATH',
                    os.path.join(os.path.expanduser("~"), "Documents", "Students Social Media Addiction.csv")
                )
                
                if os.path.exists(local_path):
                    df = pd.read_csv(local_path)
                    st.success(f"✅ Données d'addiction chargées! ({len(df)} étudiants)")
                elif os.path.exists(documents_path):
                    df = pd.read_csv(documents_path)
                    st.success(f"✅ Données d'addiction chargées! ({len(df)} étudiants)")
                else:
                    # Créer des données d'addiction synthétiques si le fichier n'existe pas
                    st.warning("⚠️ Fichier d'addiction non trouvé. Génération de données synthétiques...")
                    np.random.seed(42)
                    n = 200
                    df = pd.DataFrame({
                        'Student_ID': range(1, n + 1),
                        'Age': np.random.randint(18, 25, n),
                        'Gender': np.random.choice(['Male', 'Female'], n),
                        'Academic_Level': np.random.choice(['High School', 'Undergraduate', 'Graduate'], n),
                        'Country': np.random.choice(['France', 'USA', 'UK', 'Canada', 'Germany', 'Spain'], n),
                        'Avg_Daily_Usage_Hours': np.round(np.random.uniform(1.5, 8.0, n), 1),
                        'Most_Used_Platform': np.random.choice(['Instagram', 'TikTok', 'Facebook', 'Twitter', 'Snapchat'], n),
                        'Affects_Academic_Performance': np.random.choice(['Yes', 'No'], n),
                        'Sleep_Hours_Per_Night': np.round(np.random.uniform(4.0, 9.0, n), 1),
                        'Mental_Health_Score': np.random.randint(3, 10, n),
                        'Relationship_Status': np.random.choice(['Single', 'In Relationship', 'Complicated'], n),
                        'Conflicts_Over_Social_Media': np.random.randint(0, 6, n),
                        'Addicted_Score': np.random.randint(2, 10, n)
                    })
                    st.success(f"✅ Données d'addiction synthétiques générées! ({len(df)} étudiants)")
            
            elif "pays" in example_type.lower() or "géographique" in example_type.lower():
                # Charger le fichier avec pays
                example_path = os.path.join(os.path.dirname(__file__), "example_data_with_countries.csv")
                if os.path.exists(example_path):
                    df = pd.read_csv(example_path)
                    st.success(f"✅ Données avec pays chargées! ({len(df)} lignes)")
                else:
                    # Créer des données avec pays
                    np.random.seed(42)
                    platforms = ['TikTok', 'Instagram', 'Facebook', 'Twitter', 'YouTube']
                    countries = ['France', 'United States', 'Germany', 'Spain', 'Italy', 'United Kingdom', 'Canada', 'Australia']
                    n = 60
                    df = pd.DataFrame({
                        'platform': np.random.choice(platforms, n),
                        'likes': np.random.randint(100, 10000, n),
                        'comments': np.random.randint(10, 500, n),
                        'shares': np.random.randint(5, 200, n),
                        'views': np.random.randint(1000, 50000, n),
                        'followers': np.random.randint(5000, 100000, n),
                        'saves': np.random.randint(5, 150, n),
                        'date': pd.date_range('2024-01-15', periods=n, freq='D').strftime('%Y-%m-%d'),
                        'hour': np.random.randint(10, 22, n),
                        'post_type': np.random.choice(['video', 'reel', 'post', 'photo'], n),
                        'country': np.random.choice(countries, n)
                    })
                    st.success(f"✅ Données avec pays générées! ({len(df)} lignes)")
            
            else:
                # Charger le fichier classique
                example_path = os.path.join(os.path.dirname(__file__), "example_data.csv")
                if os.path.exists(example_path):
                    df = pd.read_csv(example_path)
                    st.success(f"✅ Données classiques chargées! ({len(df)} lignes)")
                else:
                    # Créer des données classiques
                    np.random.seed(42)
                    n = 60
                    df = pd.DataFrame({
                        'platform': np.random.choice(['TikTok', 'Instagram', 'Facebook', 'Twitter', 'YouTube'], n),
                        'likes': np.random.randint(100, 10000, n),
                        'comments': np.random.randint(10, 500, n),
                        'shares': np.random.randint(5, 200, n),
                        'views': np.random.randint(1000, 50000, n),
                        'followers': np.random.randint(5000, 100000, n),
                        'saves': np.random.randint(5, 150, n),
                        'date': pd.date_range('2024-01-15', periods=n, freq='D').strftime('%Y-%m-%d'),
                        'hour': np.random.randint(10, 22, n),
                        'post_type': np.random.choice(['video', 'reel', 'post', 'photo'], n)
                    })
                    st.success(f"✅ Données classiques générées! ({len(df)} lignes)")
            
            # Calculer l'engagement si les colonnes nécessaires existent
            analyzer = StatisticalAnalyzer(df)
            if 'likes' in df.columns and ('followers' in df.columns or 'views' in df.columns):
                df = analyzer.calculate_engagement_rate()
            
            # Sauvegarder dans la session
            st.session_state.df = df
            st.session_state.analyzer = analyzer
            
            st.balloons()
            st.rerun()
            
        except Exception as e:
            st.error(f"❌ Erreur lors du chargement des données d'exemple: {str(e)}")
            st.info("💡 Vérifiez que les fichiers d'exemple existent dans le dossier de l'application.")

def show_analysis_page():
    """Page d'analyses statistiques professionnelle"""
    # Header professionnel
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2.5rem 2rem; border-radius: 20px; margin-bottom: 2rem;
                box-shadow: 0 10px 40px rgba(102, 126, 234, 0.2);">
        <h1 style="color: white; font-size: 2.5rem; font-weight: 700; margin: 0;">
            📊 Analyses Statistiques
        </h1>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.2rem; margin-top: 0.5rem;">
            Tests statistiques avancés pour découvrir des insights dans vos données
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.df is None:
        st.markdown("""
        <div style="background: #fef3c7; padding: 2rem; border-radius: 15px;
                    border-left: 4px solid #f59e0b; margin: 2rem 0;">
            <h3 style="color: #92400e; margin: 0 0 0.5rem 0;">⚠️ Aucune donnée importée</h3>
            <p style="color: #78350f; margin: 0;">
                Veuillez d'abord importer des données depuis la page "📤 Importer des données"
            </p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    df = st.session_state.df
    analyzer = st.session_state.analyzer
    
    # Statistiques descriptives dans une carte
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 15px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 2rem;">
        <h3 style="color: #1f2937; margin-bottom: 1.5rem;">📈 Statistiques descriptives</h3>
    </div>
    """, unsafe_allow_html=True)
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if numeric_cols:
        selected_col = st.selectbox("Choisir une métrique", numeric_cols, key="desc_metric")
        
        # Métriques dans des cartes professionnelles
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        padding: 1.5rem; border-radius: 15px; text-align: center;
                        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);">
                <div style="color: rgba(255,255,255,0.9); font-size: 0.9rem; margin-bottom: 0.5rem;">
                    MOYENNE
                </div>
                <div style="color: white; font-size: 2rem; font-weight: 700;">
                    {df[selected_col].mean():.2f}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #764ba2 0%, #f093fb 100%);
                        padding: 1.5rem; border-radius: 15px; text-align: center;
                        box-shadow: 0 4px 20px rgba(118, 75, 162, 0.3);">
                <div style="color: rgba(255,255,255,0.9); font-size: 0.9rem; margin-bottom: 0.5rem;">
                    MÉDIANE
                </div>
                <div style="color: white; font-size: 2rem; font-weight: 700;">
                    {df[selected_col].median():.2f}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                        padding: 1.5rem; border-radius: 15px; text-align: center;
                        box-shadow: 0 4px 20px rgba(240, 147, 251, 0.3);">
                <div style="color: rgba(255,255,255,0.9); font-size: 0.9rem; margin-bottom: 0.5rem;">
                    MINIMUM
                </div>
                <div style="color: white; font-size: 2rem; font-weight: 700;">
                    {df[selected_col].min():.2f}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                        padding: 1.5rem; border-radius: 15px; text-align: center;
                        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.3);">
                <div style="color: rgba(255,255,255,0.9); font-size: 0.9rem; margin-bottom: 0.5rem;">
                    MAXIMUM
                </div>
                <div style="color: white; font-size: 2rem; font-weight: 700;">
                    {df[selected_col].max():.2f}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tests statistiques dans une carte
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 15px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 2rem;">
        <h3 style="color: #1f2937; margin-bottom: 1.5rem;">🧪 Tests Statistiques Avancés</h3>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Kruskal-Wallis", "Spearman", "Chi-carré", "Wilcoxon"])
    
    with tab1:
        st.markdown("#### Test de Kruskal-Wallis")
        st.info("Compare plusieurs groupes sur une métrique (non-paramétrique)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            kw_column = st.selectbox("Métrique à comparer", numeric_cols, key="kw_col")
        
        with col2:
            cat_cols = df.select_dtypes(include=['object']).columns.tolist()
            if cat_cols:
                kw_group = st.selectbox("Grouper par", cat_cols, key="kw_group")
        
        if st.button("Lancer le test Kruskal-Wallis"):
            result = analyzer.kruskal_wallis_test(kw_column, kw_group)
            
            if result:
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Statistique H", f"{result['statistic']:.4f}")
                with col2:
                    st.metric("P-value", f"{result['p_value']:.4f}")
                
                if result['significant']:
                    st.success("✅ Résultat significatif (p < 0.05)")
                else:
                    st.info("ℹ️ Résultat non significatif (p ≥ 0.05)")
                
                st.write(f"**Interprétation:** {result['interpretation']}")
    
    with tab2:
        st.markdown("#### Corrélation de Spearman")
        st.info("Mesure la relation monotone entre deux variables")
        
        if len(numeric_cols) >= 2:
            col1, col2 = st.columns(2)
            
            with col1:
                spear_col1 = st.selectbox("Variable 1", numeric_cols, key="spear_col1")
            
            with col2:
                spear_col2 = st.selectbox("Variable 2", 
                                         [c for c in numeric_cols if c != spear_col1],
                                         key="spear_col2")
            
            if st.button("Calculer la corrélation"):
                result = analyzer.spearman_correlation(spear_col1, spear_col2)
                
                if result:
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.metric("Coefficient ρ", f"{result['correlation']:.4f}")
                    with col2:
                        st.metric("P-value", f"{result['p_value']:.4f}")
                    
                    if result['significant']:
                        st.success("✅ Corrélation significative (p < 0.05)")
                    else:
                        st.info("ℹ️ Corrélation non significative (p ≥ 0.05)")
                    
                    st.write(f"**Interprétation:** {result['interpretation']}")
    
    with tab3:
        st.markdown("#### Test du Chi-carré")
        st.info("Teste l'indépendance entre deux variables catégorielles")
        
        cat_cols = df.select_dtypes(include=['object']).columns.tolist()
        
        if len(cat_cols) >= 2:
            col1, col2 = st.columns(2)
            
            with col1:
                chi_col1 = st.selectbox("Variable 1", cat_cols, key="chi_col1")
            
            with col2:
                chi_col2 = st.selectbox("Variable 2",
                                       [c for c in cat_cols if c != chi_col1],
                                       key="chi_col2")
            
            if st.button("Lancer le test Chi-carré"):
                result = analyzer.chi2_test(chi_col1, chi_col2)
                
                if result:
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("Statistique χ²", f"{result['chi2_statistic']:.4f}")
                    with col2:
                        st.metric("P-value", f"{result['p_value']:.4f}")
                    with col3:
                        st.metric("DDL", result['degrees_of_freedom'])
                    
                    if result['significant']:
                        st.success("✅ Association significative (p < 0.05)")
                    else:
                        st.info("ℹ️ Association non significative (p ≥ 0.05)")
                    
                    st.write(f"**Interprétation:** {result['interpretation']}")
                    
                    # Table de contingence
                    st.markdown("**Table de contingence:**")
                    st.dataframe(result['contingency_table'])
        else:
            st.warning("⚠️ Besoin d'au moins 2 variables catégorielles")
    
    with tab4:
        st.markdown("#### Test de Wilcoxon")
        st.info("Compare deux échantillons appariés")
        
        if len(numeric_cols) >= 2:
            col1, col2 = st.columns(2)
            
            with col1:
                wilc_col1 = st.selectbox("Échantillon 1", numeric_cols, key="wilc_col1")
            
            with col2:
                wilc_col2 = st.selectbox("Échantillon 2",
                                        [c for c in numeric_cols if c != wilc_col1],
                                        key="wilc_col2")
            
            if st.button("Lancer le test Wilcoxon"):
                result = analyzer.wilcoxon_test(wilc_col1, wilc_col2)
                
                if result:
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.metric("Statistique W", f"{result['statistic']:.4f}")
                    with col2:
                        st.metric("P-value", f"{result['p_value']:.4f}")
                    
                    if result['significant']:
                        st.success("✅ Différence significative (p < 0.05)")
                    else:
                        st.info("ℹ️ Différence non significative (p ≥ 0.05)")
                    
                    st.write(f"**Interprétation:** {result['interpretation']}")
    
    # Section de sauvegarde du projet
    st.markdown("---")
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2rem; border-radius: 15px; margin-top: 3rem;
                box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);">
        <h3 style="color: white; margin: 0 0 1rem 0;">💾 Sauvegarder ce projet</h3>
        <p style="color: rgba(255,255,255,0.9); margin: 0; font-size: 0.95rem;">
            Enregistrez vos données et analyses pour y revenir plus tard
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        project_name = st.text_input(
            "📝 Nom du projet",
            key="save_project_name",
            placeholder="Ex: Analyse TikTok Janvier 2024",
            help="Choisissez un nom descriptif pour retrouver facilement ce projet"
        )
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        save_button = st.button(
            "💾 Sauvegarder",
            key="save_project_btn",
            use_container_width=True,
            type="primary"
        )
    
    if save_button:
        if project_name and project_name.strip():
            try:
                # Vérifier que des données sont disponibles
                if df is None or df.empty:
                    st.warning("⚠️ Aucune donnée à sauvegarder. Veuillez d'abord importer des données.")
                else:
                    # Fonction helper pour convertir les types numpy en types Python natifs
                    def convert_numpy_types(obj):
                        """Convertit les types numpy en types Python natifs pour la sérialisation JSON
                        Compatible avec NumPy 1.x et 2.x"""
                        # Utiliser les classes de base qui fonctionnent dans toutes les versions de NumPy
                        if isinstance(obj, np.integer):
                            return int(obj)
                        elif isinstance(obj, np.floating):
                            return float(obj)
                        elif isinstance(obj, bool):
                            return bool(obj)
                        # Gestion de np.bool_ pour compatibilité (peut ne pas exister en NumPy 2.0+)
                        elif hasattr(np, 'bool_') and isinstance(obj, np.bool_):
                            return bool(obj)
                        elif isinstance(obj, np.ndarray):
                            return obj.tolist()
                        elif isinstance(obj, (pd.Timestamp, datetime)):
                            return str(obj)
                        elif isinstance(obj, dict):
                            return {key: convert_numpy_types(value) for key, value in obj.items()}
                        elif isinstance(obj, (list, tuple)):
                            return [convert_numpy_types(item) for item in obj]
                        elif pd.isna(obj):
                            return None
                        else:
                            return obj
                    
                    # Convertir le DataFrame en dictionnaire et nettoyer les types
                    try:
                        data_dict = df.to_dict('records')
                        data_dict = convert_numpy_types(data_dict)
                    except Exception as e:
                        st.error(f"❌ Erreur lors de la conversion des données: {str(e)}")
                        return
                    
                    # Récupérer les résultats d'analyse si disponibles
                    results_dict = None
                    if analyzer:
                        try:
                            results_dict = analyzer.get_all_results()
                            if results_dict:
                                results_dict = convert_numpy_types(results_dict)
                        except Exception as e:
                            st.warning(f"⚠️ Les résultats d'analyse n'ont pas pu être sauvegardés: {str(e)}")
                            results_dict = None
                    
                    # Sauvegarder le projet
                    try:
                        success = st.session_state.db.save_project(
                            st.session_state.user['id'],
                            project_name.strip(),
                            data_dict,
                            results_dict
                        )
                        
                        if success:
                            # Notification
                            try:
                                notif_manager = get_notification_manager()
                                notif_manager.notify_project_saved(project_name.strip())
                            except:
                                pass  # Ne pas bloquer si la notification échoue
                            
                            st.success(f"✅ Projet '{project_name.strip()}' sauvegardé avec succès!")
                            st.info("💡 Vous pouvez retrouver ce projet dans la section '💾 Mes projets'")
                            st.balloons()
                        else:
                            st.error("❌ Erreur lors de la sauvegarde du projet dans la base de données")
                    except Exception as e:
                        st.error(f"❌ Erreur lors de la sauvegarde dans la base de données: {str(e)}")
                        import traceback
                        st.code(traceback.format_exc())
            except Exception as e:
                st.error(f"❌ Erreur lors de la sauvegarde: {str(e)}")
                import traceback
                st.code(traceback.format_exc())
        else:
            st.warning("⚠️ Veuillez entrer un nom pour votre projet")

def show_ai_assistant_page():
    """Page de l'assistant IA professionnelle"""
    # Header professionnel
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2.5rem 2rem; border-radius: 20px; margin-bottom: 2rem;
                box-shadow: 0 10px 40px rgba(102, 126, 234, 0.2);">
        <h1 style="color: white; font-size: 2.5rem; font-weight: 700; margin: 0;">
            🤖 Assistant IA
        </h1>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.2rem; margin-top: 0.5rem;">
            Interprétations intelligentes et recommandations personnalisées
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    is_premium = st.session_state.db.check_premium_status(st.session_state.user['id'])
    
    if not is_premium:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
                    padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem;
                    border-left: 4px solid #f59e0b; box-shadow: 0 4px 20px rgba(245, 158, 11, 0.2);">
            <h3 style="color: #92400e; margin: 0 0 0.5rem 0;">⚠️ Version gratuite</h3>
            <p style="color: #78350f; margin: 0;">
                Interprétations basiques disponibles. <strong>Passez en Premium</strong> pour des analyses détaillées et des recommandations avancées!
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.session_state.analyzer is None:
        st.markdown("""
        <div style="background: #fef3c7; padding: 2rem; border-radius: 15px;
                    border-left: 4px solid #f59e0b; margin: 2rem 0;">
            <h3 style="color: #92400e; margin: 0 0 0.5rem 0;">⚠️ Aucune analyse disponible</h3>
            <p style="color: #78350f; margin: 0;">
                Veuillez d'abord importer des données et lancer des analyses statistiques
            </p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Section interprétation dans une carte
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 15px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 2rem;">
        <h3 style="color: #1f2937; margin-bottom: 1.5rem;">💬 Interprétation automatique</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Obtenir les résultats d'analyse
    results = st.session_state.analyzer.get_all_results()
    
    if results:
        # Comparaison des plateformes
        platform_comparison = None
        if 'platform' in st.session_state.df.columns:
            platform_comparison = st.session_state.analyzer.compare_platforms_engagement()
        
        # Générer l'interprétation
        interpretation = st.session_state.ai_assistant.interpret_results(
            results,
            is_premium,
            platform_comparison
        )
        
        st.markdown(f"""
        <div style="background: #ffffff; padding: 2rem; border-radius: 15px;
                    border-left: 4px solid #667eea; margin-bottom: 2rem; 
                    box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <div style="color: #1f2937;">
                {interpretation}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: #fef3c7; padding: 1.5rem; border-radius: 15px;
                    border-left: 4px solid #f59e0b;">
            <p style="color: #78350f; margin: 0;">
                ℹ️ Lancez d'abord des tests statistiques pour obtenir des interprétations!
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    addiction_prediction = st.session_state.get('last_addiction_prediction')
    if addiction_prediction:
        addiction_score = addiction_prediction.get('predicted_value')
        addiction_target = addiction_prediction.get('target', 'Addicted_Score')
        addiction_text, addiction_status = st.session_state.ai_assistant.interpret_addiction_score(addiction_score)
        
        badge_color = "#dc2626" if addiction_status == "critique" else "#f97316" if addiction_status == "élevé" else "#16a34a"
        badge_label = "Très élevé" if addiction_status == "critique" else "Élevé" if addiction_status == "élevé" else "Modéré"
        
        st.markdown(f"""
        <div style="background: white; padding: 2rem; border-radius: 15px;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 2rem;">
            <h3 style="color: #1f2937; margin-top: 0;">🧠 Interprétation du score d'addiction</h3>
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <div style="font-size: 2.5rem; font-weight: 700; color: #1e40af; text-shadow: 0 1px 2px rgba(0,0,0,0.1);">{addiction_score:.1f}</div>
                <span style="background: {badge_color}; color: white; padding: 0.35rem 0.9rem; border-radius: 999px; font-weight: 600; box-shadow: 0 2px 4px rgba(0,0,0,0.15);">
                    {badge_label}
                </span>
            </div>
            <p style="color: #374151; margin-bottom: 0.75rem; line-height: 1.6;">{addiction_text}</p>
            <p style="color: #4b5563; font-size: 0.9rem; margin: 0;"><strong style="color: #1f2937;">Variable ciblée:</strong> <span style="color: #6b7280;">{addiction_target}</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Recommandations par plateforme dans une carte
    if 'platform' in st.session_state.df.columns:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 15px;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 2rem;">
            <h3 style="color: #1f2937; margin-bottom: 1.5rem;">📱 Recommandations par plateforme</h3>
        </div>
        """, unsafe_allow_html=True)
        
        platforms = st.session_state.df['platform'].unique()
        
        for platform in platforms:
            with st.expander(f"🎯 {platform}"):
                platform_data = st.session_state.df[st.session_state.df['platform'] == platform]
                avg_engagement = platform_data['engagement_rate'].mean() if 'engagement_rate' in platform_data.columns else 0
                
                recommendation = st.session_state.ai_assistant.generate_content_recommendation(
                    platform,
                    avg_engagement,
                    is_premium
                )
                
                st.write(recommendation)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Explication des métriques dans une carte
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 15px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 2rem;">
        <h3 style="color: #1f2937; margin-bottom: 1.5rem;">📚 Guide des métriques</h3>
    </div>
    """, unsafe_allow_html=True)
    
    metrics_to_explain = ['engagement_rate', 'likes', 'reach', 'impressions']
    
    selected_metric = st.selectbox("Choisir une métrique à expliquer", metrics_to_explain, key="metric_explain")
    
    explanation = st.session_state.ai_assistant.explain_metric(selected_metric, is_premium)
    
    st.markdown(f"""
    <div style="background: #ffffff; padding: 1.5rem; border-radius: 15px;
                border-left: 4px solid #667eea; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <p style="color: #1f2937; margin: 0; line-height: 1.8;">
            {explanation}
        </p>
    </div>
    """, unsafe_allow_html=True)

def show_visualizations_page():
    """Page de visualisations professionnelle"""
    # Header professionnel
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2.5rem 2rem; border-radius: 20px; margin-bottom: 2rem;
                box-shadow: 0 10px 40px rgba(102, 126, 234, 0.2);">
        <h1 style="color: white; font-size: 2.5rem; font-weight: 700; margin: 0;">
            📈 Visualisations
        </h1>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.2rem; margin-top: 0.5rem;">
            Graphiques interactifs et analyses visuelles de vos données
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.df is None:
        st.markdown("""
        <div style="background: #fef3c7; padding: 2rem; border-radius: 15px;
                    border-left: 4px solid #f59e0b; margin: 2rem 0;">
            <h3 style="color: #92400e; margin: 0 0 0.5rem 0;">⚠️ Aucune donnée importée</h3>
            <p style="color: #78350f; margin: 0;">
                Veuillez d'abord importer des données depuis la page "📤 Importer des données"
            </p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    visualizer = DataVisualizer(st.session_state.df)
    
    # Utiliser un conteneur pour éviter les conflits DOM
    with st.container():
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Comparaisons", "📈 Distributions", "🔗 Corrélations", "⏱️ Temporel"])
        
        with tab1:
            st.markdown("### Comparaisons par catégorie")
            
            # Identifier les colonnes catégorielles et numériques
            numeric_cols = st.session_state.df.select_dtypes(include=[np.number]).columns.tolist()
            categorical_cols = st.session_state.df.select_dtypes(include=['object', 'category']).columns.tolist()
            
            if categorical_cols and numeric_cols:
                col1, col2 = st.columns(2)
                
                with col1:
                    group_by_col = st.selectbox(
                        "Grouper par (catégorie)",
                        categorical_cols,
                        key="comparison_group",
                        help="Choisissez une colonne catégorielle pour grouper les données"
                    )
                
                with col2:
                    # Chercher une colonne de métrique appropriée
                    metric_options = numeric_cols
                    if 'engagement_rate' in numeric_cols:
                        default_metric = 'engagement_rate'
                    elif 'likes' in numeric_cols:
                        default_metric = 'likes'
                    elif len(numeric_cols) > 0:
                        default_metric = numeric_cols[0]
                    else:
                        default_metric = None
                    
                    if default_metric:
                        metric_col = st.selectbox(
                            "Métrique à comparer",
                            metric_options,
                            index=metric_options.index(default_metric) if default_metric in metric_options else 0,
                            key="comparison_metric",
                            help="Choisissez une colonne numérique à comparer"
                        )
                        
                        try:
                            # Créer un graphique de comparaison personnalisé
                            comparison_data = st.session_state.df.groupby(group_by_col)[metric_col].agg(['mean', 'std', 'count']).reset_index()
                            comparison_data.columns = [group_by_col, 'mean_value', 'std_value', 'count']
                            
                            fig = px.bar(
                                comparison_data,
                                x=group_by_col,
                                y='mean_value',
                                error_y='std_value',
                                title=f'Comparaison de {metric_col} par {group_by_col}',
                                labels={'mean_value': f'{metric_col} moyen', group_by_col: group_by_col},
                                color=group_by_col,
                                text='mean_value'
                            )
                            
                            fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
                            fig.update_layout(
                                height=500,
                                showlegend=False,
                                plot_bgcolor='rgba(0,0,0,0)',
                                paper_bgcolor='rgba(0,0,0,0)'
                            )
                            
                            st.plotly_chart(fig, use_container_width=True, key="custom_comparison")
                        except Exception as e:
                            st.error(f"Erreur lors de la génération du graphique: {str(e)}")
            else:
                if not categorical_cols:
                    st.info("ℹ️ Aucune colonne catégorielle trouvée. Les comparaisons nécessitent au moins une colonne catégorielle.")
                if not numeric_cols:
                    st.info("ℹ️ Aucune colonne numérique trouvée. Les comparaisons nécessitent au moins une colonne numérique.")
        
        with tab2:
            st.markdown("### Distribution des métriques")
            
            numeric_cols = st.session_state.df.select_dtypes(include=[np.number]).columns.tolist()
            
            if numeric_cols:
                selected_metric = st.selectbox("Choisir une métrique", numeric_cols, key="dist_metric")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    try:
                        fig_hist = visualizer.plot_metric_distribution_histogram(selected_metric)
                        if fig_hist:
                            st.plotly_chart(fig_hist, use_container_width=True, key="histogram_dist")
                    except Exception as e:
                        st.error(f"Erreur lors de la génération de l'histogramme: {str(e)}")
                
                with col2:
                    # Box plot avec sélection de colonne catégorielle
                    categorical_cols = st.session_state.df.select_dtypes(include=['object', 'category']).columns.tolist()
                    
                    if categorical_cols:
                        group_by_box = st.selectbox(
                            "Grouper par (pour box plot)",
                            categorical_cols,
                            key="box_group",
                            help="Choisissez une colonne catégorielle pour le box plot"
                        )
                        
                        try:
                            fig_box = px.box(
                                st.session_state.df,
                                x=group_by_box,
                                y=selected_metric,
                                title=f'Distribution de {selected_metric} par {group_by_box}',
                                labels={selected_metric: selected_metric, group_by_box: group_by_box},
                                color=group_by_box
                            )
                            
                            fig_box.update_layout(
                                height=500,
                                showlegend=False,
                                plot_bgcolor='rgba(0,0,0,0)',
                                paper_bgcolor='rgba(0,0,0,0)'
                            )
                            
                            st.plotly_chart(fig_box, use_container_width=True, key="box_dist")
                        except Exception as e:
                            st.error(f"Erreur lors de la génération du box plot: {str(e)}")
                    else:
                        st.info("ℹ️ Aucune colonne catégorielle trouvée pour le box plot")
            else:
                st.info("ℹ️ Aucune colonne numérique trouvée dans vos données")
        
        with tab3:
            st.markdown("### Corrélations et relations")
            
            # Heatmap
            try:
                fig_heatmap = visualizer.plot_correlation_heatmap()
                if fig_heatmap:
                    st.plotly_chart(fig_heatmap, use_container_width=True, key="correlation_heatmap")
            except Exception as e:
                st.error(f"Erreur lors de la génération de la heatmap: {str(e)}")
            
            # Scatter plot
            numeric_cols = st.session_state.df.select_dtypes(include=[np.number]).columns.tolist()
            categorical_cols = st.session_state.df.select_dtypes(include=['object', 'category']).columns.tolist()
            
            if len(numeric_cols) >= 2:
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    x_col = st.selectbox("Axe X", numeric_cols, key="scatter_x")
                
                with col2:
                    y_col = st.selectbox("Axe Y", [c for c in numeric_cols if c != x_col], key="scatter_y")
                
                with col3:
                    color_by = st.selectbox(
                        "Colorier par (optionnel)",
                        ["Aucun"] + categorical_cols,
                        key="scatter_color",
                        help="Choisissez une colonne catégorielle pour colorier les points"
                    )
                
                try:
                    if color_by != "Aucun" and color_by in st.session_state.df.columns:
                        fig_scatter = px.scatter(
                            st.session_state.df,
                            x=x_col,
                            y=y_col,
                            color=color_by,
                            trendline="ols",
                            title=f'Relation entre {x_col} et {y_col}',
                            labels={x_col: x_col, y_col: y_col}
                        )
                    else:
                        fig_scatter = px.scatter(
                            st.session_state.df,
                            x=x_col,
                            y=y_col,
                            trendline="ols",
                            title=f'Relation entre {x_col} et {y_col}',
                            labels={x_col: x_col, y_col: y_col}
                        )
                    
                    fig_scatter.update_layout(
                        height=500,
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)'
                    )
                    
                    st.plotly_chart(fig_scatter, use_container_width=True, key="scatter_plot")
                except Exception as e:
                    st.error(f"Erreur lors de la génération du scatter plot: {str(e)}")
            else:
                st.info("ℹ️ Au moins 2 colonnes numériques sont nécessaires pour le scatter plot")
        
        with tab4:
            st.markdown("### Analyses temporelles")
            
            date_cols = [col for col in st.session_state.df.columns if 'date' in col.lower() or 'time' in col.lower()]
            
            if date_cols:
                date_col = st.selectbox("Colonne de date", date_cols, key="date_col_select")
                metric_col = st.selectbox("Métrique", 
                                         st.session_state.df.select_dtypes(include=[np.number]).columns.tolist(),
                                         key="time_metric")
                
                try:
                    fig_time = visualizer.plot_time_series(date_col, metric_col)
                    if fig_time:
                        st.plotly_chart(fig_time, use_container_width=True, key="time_series")
                except Exception as e:
                    st.error(f"Erreur lors de la génération de la série temporelle: {str(e)}")
            else:
                st.info("ℹ️ Aucune colonne de date détectée dans vos données")

def show_predictions_page():
    """Page de prédictions professionnelle"""
    # Header professionnel
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2.5rem 2rem; border-radius: 20px; margin-bottom: 2rem;
                box-shadow: 0 10px 40px rgba(102, 126, 234, 0.2);">
        <h1 style="color: white; font-size: 2.5rem; font-weight: 700; margin: 0;">
            🔮 Prédictions de Likes
        </h1>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.2rem; margin-top: 0.5rem;">
            Modèles de machine learning pour prédire les performances futures
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    is_premium = st.session_state.db.check_premium_status(st.session_state.user['id'])
    
    if not is_premium:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
                    padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem;
                    border-left: 4px solid #f59e0b; box-shadow: 0 4px 20px rgba(245, 158, 11, 0.2);">
            <h3 style="color: #92400e; margin: 0 0 0.5rem 0;">⚠️ Fonctionnalité Premium</h3>
            <p style="color: #78350f; margin: 0;">
                Les prédictions basiques sont disponibles. <strong>Passez en Premium</strong> pour accéder aux modèles avancés (Random Forest, etc.)
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.session_state.df is None:
        st.markdown("""
        <div style="background: #fef3c7; padding: 2rem; border-radius: 15px;
                    border-left: 4px solid #f59e0b; margin: 2rem 0;">
            <h3 style="color: #92400e; margin: 0 0 0.5rem 0;">⚠️ Aucune donnée importée</h3>
            <p style="color: #78350f; margin: 0;">
                Veuillez d'abord importer des données depuis la page "📤 Importer des données"
            </p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    analyzer = st.session_state.analyzer
    
    # Section entraînement dans une carte
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 15px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 2rem;">
        <h3 style="color: #1f2937; margin-bottom: 1.5rem;">🎯 Entraîner un modèle de prédiction</h3>
    </div>
    """, unsafe_allow_html=True)
    
    numeric_cols = st.session_state.df.select_dtypes(include=[np.number]).columns.tolist()
    
    # Exclure 'likes' des features
    available_features = [col for col in numeric_cols if col != 'likes']
    likes_available = 'likes' in numeric_cols and len(available_features) >= 1
    
    if not likes_available:
        st.error("❌ La section likes nécessite une colonne 'likes' et au moins une variable numérique supplémentaire.")
    
    if not likes_available:
        selected_features = []
    else:
        # Sélection des features
        selected_features = st.multiselect(
            "Sélectionnez les variables prédictives",
            available_features,
            default=available_features[:min(3, len(available_features))]
        )
        
        model_type = st.selectbox(
            "Type de modèle",
            ["Random Forest (Recommandé)", "Régression Linéaire"] if is_premium else ["Régression Linéaire"]
        )
        
        model_type_code = "random_forest" if "Random Forest" in model_type else "linear"
        
        if st.button("🎯 Entraîner le modèle", type="primary"):
            if selected_features:
                with st.spinner("Entraînement du modèle en cours..."):
                    result = analyzer.predict_likes(selected_features, 'likes', model_type_code)
                    
                    if result:
                        st.success("✅ Modèle entraîné avec succès!")
                        
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.metric("R² Score", f"{result['r2_score']:.4f}")
                        with col2:
                            st.metric("RMSE", f"{result['rmse']:.2f}")
                        with col3:
                            quality = "Excellent" if result['r2_score'] > 0.7 else "Bon" if result['r2_score'] > 0.5 else "Modéré"
                            st.metric("Qualité", quality)
                        
                        st.info(f"**Interprétation:** {result['interpretation']}")
                        
                        # Sauvegarder le modèle dans la session
                        st.session_state.prediction_model = result
                    else:
                        st.error("❌ Impossible d'entraîner le modèle. Vérifiez vos données.")
            else:
                st.warning("⚠️ Veuillez sélectionner au moins une variable prédictive!")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Section prédiction dans une carte
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 15px;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 2rem;">
            <h3 style="color: #1f2937; margin-bottom: 1.5rem;">🎲 Faire une prédiction</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if 'prediction_model' in st.session_state:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                        padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem;
                        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.3);">
                <h3 style="color: white; margin: 0;">✅ Modèle chargé et prêt!</h3>
            </div>
            """, unsafe_allow_html=True)
            
            model = st.session_state.prediction_model
            
            st.markdown("""
            <div style="background: #ffffff; padding: 1.5rem; border-radius: 15px;
                        margin-bottom: 2rem; border-left: 4px solid #667eea;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                <p style="color: #1f2937; margin: 0; font-weight: 600;">
                    Entrez les valeurs pour prédire le nombre de likes:
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            input_values = {}
            
            cols = st.columns(min(3, len(model['features'])))
            
            for i, feature in enumerate(model['features']):
                with cols[i % 3]:
                    # Obtenir min/max de la colonne
                    min_val = float(st.session_state.df[feature].min())
                    max_val = float(st.session_state.df[feature].max())
                    mean_val = float(st.session_state.df[feature].mean())
                    
                    input_values[feature] = st.number_input(
                        f"{feature.capitalize()}",
                        min_value=min_val,
                        max_value=max_val * 2,
                        value=mean_val,
                        key=f"pred_{feature}"
                    )
            
            if st.button("🔮 Prédire", type="primary", use_container_width=True):
                prediction = analyzer.predict_single(model, input_values)
                
                if prediction:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                                padding: 2rem; border-radius: 15px; margin-top: 2rem;
                                box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);">
                        <h3 style="color: white; margin: 0 0 1rem 0;">🎯 Résultat de la prédiction</h3>
                        <div style="background: rgba(255,255,255,0.2); padding: 1.5rem; border-radius: 10px;">
                            <p style="color: white; font-size: 1.2rem; margin: 0;">
                                <strong>Likes prédits:</strong> <span style="font-size: 2rem; font-weight: 700;">{prediction['predicted_value']:.0f}</span>
                            </p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Afficher les valeurs utilisées dans une carte
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown("""
                    <div style="background: white; padding: 1.5rem; border-radius: 15px;
                                box-shadow: 0 4px 20px rgba(0,0,0,0.08);">
                        <h4 style="color: #1f2937; margin-bottom: 1rem;">📊 Valeurs utilisées:</h4>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    for feature, value in prediction['input_values'].items():
                        st.markdown(f"""
                        <div style="background: #ffffff; padding: 0.75rem 1rem; border-radius: 8px;
                                    margin-bottom: 0.5rem; border-left: 3px solid #667eea;
                                    box-shadow: 0 1px 3px rgba(0,0,0,0.08);">
                            <span style="color: #1f2937; font-weight: 600;">{feature}:</span>
                            <span style="color: #4b5563; margin-left: 0.5rem;">{value}</span>
                        </div>
                        """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="background: #fef3c7; padding: 1.5rem; border-radius: 15px;
                        border-left: 4px solid #f59e0b;">
                <p style="color: #78350f; margin: 0;">
                    ℹ️ Entraînez d'abord un modèle ci-dessus pour faire des prédictions!
                </p>
            </div>
            """, unsafe_allow_html=True)

    # Section dédiée à la prédiction de l'addiction
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%);
                padding: 2rem; border-radius: 15px; margin: 2rem 0;
                box-shadow: 0 10px 30px rgba(37, 99, 235, 0.25);">
        <h2 style="color: white; margin: 0 0 0.5rem 0; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">🧠 Prédictions du score d'addiction</h2>
        <p style="color: rgba(255,255,255,0.95); margin: 0; text-shadow: 0 1px 2px rgba(0,0,0,0.1);">Anticipez les profils à risque à partir des habitudes d'usage.</p>
    </div>
    """, unsafe_allow_html=True)
    
    numeric_cols = st.session_state.df.select_dtypes(include=[np.number]).columns.tolist()
    addiction_candidates = ['addicted_score', 'addiction_score', 'addiction_risk', 'addiction']
    addiction_target = next((col for col in numeric_cols if col.lower() in addiction_candidates), None)
    
    if not addiction_target:
        st.info("ℹ️ Ajoutez une colonne numérique comme 'Addicted_Score' pour activer cette fonctionnalité.")
        return
    
    addiction_features = [col for col in numeric_cols if col != addiction_target]
    
    if not addiction_features:
        st.warning("⚠️ Aucun prédicteur disponible pour entraîner un modèle d'addiction.")
        return
    
    recommended_features = [
        'Avg_Daily_Usage_Hours',
        'Sleep_Hours_Per_Night',
        'Mental_Health_Score',
        'Conflicts_Over_Social_Media'
    ]
    default_addiction_features = [col for col in recommended_features if col in addiction_features]
    if not default_addiction_features:
        default_addiction_features = addiction_features[:min(4, len(addiction_features))]
    
    selected_addiction_features = st.multiselect(
        "Variables explicatives (habitudes, santé mentale, conflits...)",
        addiction_features,
        default=default_addiction_features,
        key="addiction_features_select"
    )
    
    addiction_model_type = st.selectbox(
        "Type de modèle (Addiction)",
        ["Random Forest (Recommandé)", "Régression Linéaire"] if is_premium else ["Régression Linéaire"],
        key="addiction_model_type"
    )
    addiction_model_code = "random_forest" if "Random Forest" in addiction_model_type else "linear"
    
    if st.button("🧠 Entraîner le modèle d'addiction", type="primary", key="train_addiction_model"):
        if selected_addiction_features:
            with st.spinner("Analyse des profils et entraînement du modèle..."):
                result = analyzer.predict_metric(selected_addiction_features, addiction_target, addiction_model_code)
            
            if result:
                st.success("✅ Modèle d'addiction entraîné avec succès.")
                st.session_state.addiction_prediction_model = result
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("R² Score", f"{result['r2_score']:.4f}")
                with col2:
                    st.metric("RMSE", f"{result['rmse']:.2f}")
                with col3:
                    quality = "Excellent" if result['r2_score'] > 0.7 else "Bon" if result['r2_score'] > 0.5 else "Modéré"
                    st.metric("Qualité", quality)
                
                st.info(f"🧾 Interprétation: {result['interpretation']}")
            else:
                st.error("❌ Impossible d'entraîner le modèle d'addiction. Vérifiez vos données.")
        else:
            st.warning("⚠️ Sélectionnez au moins une variable explicative pour l'addiction.")
    
    if 'addiction_prediction_model' in st.session_state:
        model = st.session_state.addiction_prediction_model
        st.markdown("""
        <div style="background: #ecfccb; padding: 1.5rem; border-radius: 15px;
                    border-left: 4px solid #65a30d; margin-top: 2rem;">
            <h3 style="margin: 0; color: #365314; font-weight: 600;">✅ Modèle d'addiction prêt pour les prédictions</h3>
        </div>
        """, unsafe_allow_html=True)
        
        input_values = {}
        cols = st.columns(min(3, len(model['features'])))
        for i, feature in enumerate(model['features']):
            with cols[i % 3]:
                min_val = float(st.session_state.df[feature].min())
                max_val = float(st.session_state.df[feature].max())
                mean_val = float(st.session_state.df[feature].mean())
                input_values[feature] = st.number_input(
                    f"{feature}",
                    min_value=min_val,
                    max_value=max_val * 2 if max_val != 0 else mean_val * 2,
                    value=mean_val,
                    key=f"addiction_pred_{feature}"
                )
        
        if st.button("🔍 Prédire le score d'addiction", type="primary", key="predict_addiction_btn"):
            prediction = analyzer.predict_single(model, input_values)
            if prediction:
                st.session_state.last_addiction_prediction = {
                    'predicted_value': float(prediction['predicted_value']),
                    'target': addiction_target,
                    'input_values': prediction['input_values']
                }
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%);
                            padding: 2rem; border-radius: 15px; margin-top: 2rem;
                            box-shadow: 0 10px 30px rgba(37, 99, 235, 0.25);">
                    <h3 style="color: white; margin-top: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">Score d'addiction prédit</h3>
                    <p style="color: white; font-size: 2rem; font-weight: 700; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
                        {prediction['predicted_value']:.1f}
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("#### Variables utilisées")
                for feature, value in prediction['input_values'].items():
                    st.markdown(f"- **{feature}** : {value}")
            else:
                st.error("❌ Impossible de calculer la prédiction. Réessayez avec d'autres valeurs.")
    else:
        st.info("ℹ️ Entraînez d'abord le modèle d'addiction pour accéder aux prédictions.")

def show_projects_page():
    """Page de gestion des projets sauvegardés professionnelle"""
    # Header professionnel
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2.5rem 2rem; border-radius: 20px; margin-bottom: 2rem;
                box-shadow: 0 10px 40px rgba(102, 126, 234, 0.2);">
        <h1 style="color: white; font-size: 2.5rem; font-weight: 700; margin: 0;">
            💾 Mes Projets
        </h1>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.2rem; margin-top: 0.5rem;">
            Gérez et accédez à vos analyses sauvegardées
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Récupérer les projets de l'utilisateur
    projects = st.session_state.db.get_user_projects(st.session_state.user['id'])
    
    if projects:
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 15px;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 2rem;">
            <h3 style="color: #1f2937; margin: 0;">
                📊 Vous avez <strong style="color: #667eea;">{len(projects)}</strong> projet(s) sauvegardé(s)
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        for project in projects:
            created_date = project['created_at'][:10] if len(project.get('created_at', '')) > 10 else project.get('created_at', 'N/A')
            updated_date = project['updated_at'][:10] if len(project.get('updated_at', '')) > 10 else project.get('updated_at', 'N/A')
            
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 15px;
                        box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 1.5rem;
                        border-left: 4px solid #667eea;">
                <h4 style="color: #1f2937; margin: 0 0 1rem 0;">📁 {project['project_name']}</h4>
                <div style="color: #6b7280; font-size: 0.9rem; margin-bottom: 1rem;">
                    <p style="margin: 0.25rem 0;"><strong>Créé:</strong> {created_date}</p>
                    <p style="margin: 0.25rem 0;"><strong>Dernière modification:</strong> {updated_date}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                pass  # Espace pour le design
            
            with col2:
                if st.button("📂 Charger", key=f"load_{project['id']}", use_container_width=True):
                    loaded_project = st.session_state.db.load_project(
                        st.session_state.user['id'],
                        project['project_name']
                    )
                    
                    if loaded_project:
                        try:
                            # Restaurer le DataFrame
                            data_list = loaded_project['data']
                            if data_list:
                                st.session_state.df = pd.DataFrame(data_list)
                                
                                # Recréer l'analyzer avec les données restaurées
                                if st.session_state.df is not None:
                                    st.session_state.analyzer = StatisticalAnalyzer(st.session_state.df)
                                    
                                    # Si des résultats étaient sauvegardés, on peut les restaurer
                                    # (les résultats seront recalculés automatiquement si nécessaire)
                                
                                # Notification
                                notif_manager = get_notification_manager()
                                notif_manager.notify_project_loaded(
                                    project['project_name'],
                                    len(st.session_state.df)
                                )
                                
                                st.success(f"✅ Projet '{project['project_name']}' chargé avec succès!")
                                st.info(f"📊 {len(st.session_state.df)} lignes de données restaurées")
                                st.balloons()
                                st.rerun()
                            else:
                                st.error("❌ Aucune donnée trouvée dans ce projet")
                        except Exception as e:
                            st.error(f"❌ Erreur lors du chargement: {str(e)}")
                    else:
                        st.error("❌ Impossible de charger ce projet")
            
            with col3:
                delete_key = f"delete_{project['id']}"
                if st.button("🗑️ Supprimer", key=delete_key, use_container_width=True, type="secondary"):
                    # Afficher un avertissement et demander confirmation
                    st.warning(f"⚠️ Êtes-vous sûr de vouloir supprimer le projet '{project['project_name']}' ?")
                    
                    confirm_col1, confirm_col2 = st.columns(2)
                    with confirm_col1:
                        if st.button("✅ Oui, supprimer", key=f"confirm_{delete_key}", use_container_width=True):
                            success = st.session_state.db.delete_project(
                                st.session_state.user['id'],
                                project['id']
                            )
                            
                            if success:
                                st.success(f"✅ Projet '{project['project_name']}' supprimé avec succès!")
                                st.balloons()
                                st.rerun()
                            else:
                                st.error("❌ Erreur lors de la suppression du projet")
                    
                    with confirm_col2:
                        if st.button("❌ Annuler", key=f"cancel_{delete_key}", use_container_width=True):
                            st.rerun()
            
            st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
                    padding: 3rem 2rem; border-radius: 20px; text-align: center;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin: 2rem 0;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">📭</div>
            <h2 style="color: #1f2937; font-size: 1.8rem; margin-bottom: 1rem;">
                Aucun projet sauvegardé
            </h2>
            <p style="color: #6b7280; font-size: 1.1rem; margin-bottom: 2rem;">
                Importez des données et sauvegardez votre travail pour le retrouver ici
            </p>
            <div style="display: flex; justify-content: center; gap: 1rem;">
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📤 Importer des données maintenant", use_container_width=True, type="primary"):
                st.session_state.page = "upload"
                st.rerun()

def show_country_map_page():
    """Page d'affichage de la carte par pays professionnelle"""
    # Header professionnel
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2.5rem 2rem; border-radius: 20px; margin-bottom: 2rem;
                box-shadow: 0 10px 40px rgba(102, 126, 234, 0.2);">
        <h1 style="color: white; font-size: 2.5rem; font-weight: 700; margin: 0;">
            🗺️ Carte d'Engagement par Pays
        </h1>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.2rem; margin-top: 0.5rem;">
            Visualisez vos performances géographiques sur une carte interactive
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.df is None:
        st.markdown("""
        <div style="background: #fef3c7; padding: 2rem; border-radius: 15px;
                    border-left: 4px solid #f59e0b; margin: 2rem 0;">
            <h3 style="color: #92400e; margin: 0 0 0.5rem 0;">⚠️ Aucune donnée importée</h3>
            <p style="color: #78350f; margin: 0;">
                Veuillez d'abord importer des données depuis la page "📤 Importer des données"
            </p>
            <p style="color: #78350f; margin: 0.5rem 0 0 0;">
                💡 Votre fichier doit contenir une colonne 'country' ou 'pays' avec les noms des pays.
            </p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    df = st.session_state.df
    
    # Vérifier si une colonne pays existe (inclure "paie" au cas où c'est une faute de frappe)
    country_cols = [col for col in df.columns 
                   if 'country' in col.lower() or 'pays' in col.lower() or col.lower() == 'paie']
    
    if not country_cols:
        st.warning("⚠️ Aucune colonne de pays détectée dans vos données!")
        st.markdown("""
        ### 📝 Comment ajouter des pays à vos données?
        
        Votre fichier Excel/CSV doit contenir une colonne nommée **'country'** ou **'pays'** avec les noms des pays.
        
        **Exemples de noms de pays acceptés:**
        - France, United States, Germany, Spain, Italy
        - USA, UK, Canada, Australia, Japan
        
        **Format recommandé:**
        ```csv
        platform,likes,followers,country
        TikTok,1250,15000,France
        Instagram,890,12000,United States
        Facebook,450,8000,Germany
        ```
        """)
        
        # Option pour ajouter une colonne pays manuellement
        st.markdown("---")
        st.markdown("### ➕ Ajouter une colonne pays manuellement")
        
        if st.checkbox("Je veux ajouter une colonne pays avec des valeurs par défaut"):
            default_country = st.text_input("Nom du pays par défaut", value="France")
            if st.button("Ajouter la colonne"):
                df['country'] = default_country
                st.session_state.df = df
                st.success(f"✅ Colonne 'country' ajoutée avec la valeur '{default_country}'!")
                st.rerun()
        
        return
    
    # Afficher les colonnes disponibles avec un mapping pour corriger "Paie" → "Pays"
    # Créer un mapping pour l'affichage
    country_col_display = {}
    country_col_options = []
    
    for col in country_cols:
        # Normaliser l'affichage : "paie" ou "Paie" devient "Pays"
        if col.lower() == 'paie':
            display_name = "Pays"
        else:
            display_name = col
        country_col_display[display_name] = col
        country_col_options.append(display_name)
    
    # Si une seule option, l'utiliser directement
    if len(country_col_options) == 1:
        selected_display = country_col_options[0]
    else:
        selected_display = st.selectbox(
            "Sélectionner la colonne contenant les pays",
            country_col_options,
            key="country_col_selector"
        )
    
    # Récupérer le nom réel de la colonne
    selected_country_col = country_col_display[selected_display]
    
    # Initialiser le visualiseur de carte
    try:
        map_visualizer = CountryMapVisualizer(df)
        
        # Calculer les statistiques par pays
        with st.spinner("🔄 Calcul des statistiques par pays..."):
            country_stats = map_visualizer.calculate_engagement_by_country(selected_country_col)
        
        if country_stats is None or len(country_stats) == 0:
            st.error("❌ Impossible de calculer les statistiques par pays. Vérifiez que vos noms de pays sont corrects.")
            st.info("💡 Essayez d'utiliser les noms de pays en anglais (ex: 'United States' au lieu de 'USA').")
            
            # Afficher les pays détectés
            if selected_country_col in df.columns:
                unique_countries = df[selected_country_col].dropna().unique()[:10]
                st.markdown("**Pays détectés dans vos données (exemples):**")
                st.write(unique_countries)
            return
        
        # Afficher les statistiques
        st.markdown("### 📊 Statistiques par pays")
        st.dataframe(country_stats, use_container_width=True)
        
        # Options de visualisation
        st.markdown("---")
        st.markdown("### 🎨 Options de visualisation")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Filtrer les métriques disponibles selon les colonnes présentes dans country_stats
            available_metrics = []
            metric_options = {
                'avg_engagement': 'Taux d\'engagement moyen',
                'median_engagement': 'Taux d\'engagement médian',
                'avg_likes': 'Likes moyen',
                'total_likes': 'Total de likes',
                'avg_followers': 'Followers moyen',
                'total_comments': 'Total commentaires',
                'total_views': 'Total vues',
                'post_count': 'Nombre de posts'
            }
            
            # Ne garder que les métriques qui existent dans country_stats
            for metric in metric_options.keys():
                if metric in country_stats.columns:
                    available_metrics.append(metric)
            
            # Si aucune métrique n'est disponible, utiliser post_count par défaut
            if not available_metrics:
                st.error("❌ Aucune métrique disponible dans les données.")
                return
            
            engagement_metric = st.selectbox(
                "Métrique à afficher sur la carte",
                available_metrics,
                format_func=lambda x: metric_options.get(x, x),
                key="engagement_metric"
            )
        
        # Onglets pour différentes visualisations
        st.markdown("---")
        viz_tabs = st.tabs(["🗺️ Carte Choroplèthe", "📊 Graphique en Barres", "🌳 Treemap"])
        
        with viz_tabs[0]:
            st.markdown("### 🗺️ Carte Choroplèthe Mondiale")
            
            with st.spinner("🔄 Génération de la carte..."):
                try:
                    map_fig = map_visualizer.create_interactive_map(
                        country_stats,
                        engagement_column=engagement_metric
                    )
                    
                    if map_fig:
                        st.plotly_chart(map_fig, use_container_width=True)
                        st.success("✅ Carte générée avec succès!")
                        
                        st.info("""
                        💡 **Astuce**: Survolez un pays pour voir les détails. Les couleurs plus foncées indiquent des valeurs plus élevées.
                        """)
                    else:
                        st.warning("⚠️ Impossible de créer la carte choroplèthe. Essayez une autre visualisation ci-dessous.")
                        st.info("💡 La carte nécessite des codes pays valides (ISO-3). Certains noms de pays peuvent ne pas être reconnus.")
                except Exception as e:
                    st.error(f"❌ Erreur lors de la génération de la carte: {str(e)}")
                    st.info("💡 Essayez une des autres visualisations ci-dessous!")
        
        with viz_tabs[1]:
            st.markdown("### 📊 Top Pays par Engagement")
            
            top_n = st.slider("Nombre de pays à afficher", min_value=5, max_value=50, value=15, key="top_countries")
            
            with st.spinner("🔄 Génération du graphique..."):
                try:
                    bar_fig = map_visualizer.create_bar_chart(
                        country_stats,
                        engagement_column=engagement_metric,
                        top_n=top_n
                    )
                    
                    if bar_fig:
                        st.plotly_chart(bar_fig, use_container_width=True)
                        st.success("✅ Graphique généré avec succès!")
                    else:
                        st.error("❌ Impossible de créer le graphique en barres.")
                except Exception as e:
                    st.error(f"❌ Erreur: {str(e)}")
        
        with viz_tabs[2]:
            st.markdown("### 🌳 Treemap - Répartition par Pays")
            
            value_for_size = st.selectbox(
                "Variable pour la taille des rectangles",
                ['total_likes', 'post_count', 'avg_likes'] if any(c in country_stats.columns for c in ['total_likes', 'post_count', 'avg_likes']) 
                else ['post_count'],
                key="treemap_value"
            )
            
            with st.spinner("🔄 Génération du treemap..."):
                try:
                    treemap_fig = map_visualizer.create_treemap(
                        country_stats,
                        engagement_column=engagement_metric,
                        value_column=value_for_size
                    )
                    
                    if treemap_fig:
                        st.plotly_chart(treemap_fig, use_container_width=True)
                        st.success("✅ Treemap généré avec succès!")
                        st.info("💡 La taille des rectangles représente la valeur, la couleur représente l'engagement.")
                    else:
                        st.error("❌ Impossible de créer le treemap.")
                except Exception as e:
                    st.error(f"❌ Erreur: {str(e)}")
    
    except Exception as e:
        st.error(f"❌ Erreur: {str(e)}")
        st.info("💡 Assurez-vous que vos données contiennent une colonne 'country' ou 'pays' avec des noms de pays valides.")

def show_profile_page():
    """Page de profil utilisateur"""
    st.markdown('<h1 class="main-header">👤 Mon Profil</h1>', unsafe_allow_html=True)
    
    user_id = st.session_state.user['id']
    profile = st.session_state.db.get_user_profile(user_id)
    
    if not profile:
        st.error("❌ Impossible de charger le profil")
        st.error(f"User ID: {user_id}")
        return
    
    # Debug: Afficher les données brutes (optionnel, peut être retiré après)
    if st.checkbox("🔍 Mode Debug (afficher les données brutes)", key="debug_profile"):
        st.json(profile)
    
    # Afficher les informations actuelles en lecture seule d'abord
    st.markdown("### 📋 Informations personnelles")
    
    # Section d'affichage des informations
    info_col1, info_col2 = st.columns(2)
    
    with info_col1:
        st.markdown("#### 👤 Identité")
        if profile.get('first_name') or profile.get('last_name'):
            full_name = f"{profile.get('first_name', '')} {profile.get('last_name', '')}".strip()
            st.info(f"**Nom complet:** {full_name if full_name else 'Non renseigné'}")
        else:
            st.info("**Nom complet:** Non renseigné")
        
        st.info(f"**Email:** {profile.get('email', 'N/A')}")
        
        if profile.get('phone'):
            st.info(f"**Téléphone:** {profile.get('phone')}")
        else:
            st.info("**Téléphone:** Non renseigné")
    
    with info_col2:
        st.markdown("#### 🏢 Professionnel")
        if profile.get('company'):
            st.info(f"**Entreprise:** {profile.get('company')}")
        else:
            st.info("**Entreprise:** Non renseigné")
        
        if profile.get('job_title'):
            st.info(f"**Poste:** {profile.get('job_title')}")
        else:
            st.info("**Poste:** Non renseigné")
        
        if profile.get('bio'):
            st.info(f"**Bio:** {profile.get('bio')}")
        else:
            st.info("**Bio:** Non renseigné")
    
    st.markdown("---")
    
    # Formulaire de modification
    st.markdown("### ✏️ Modifier mes informations")
    
    with st.form("profile_form"):
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("Prénom", value=profile.get('first_name') or '', key="edit_first_name")
        with col2:
            last_name = st.text_input("Nom", value=profile.get('last_name') or '', key="edit_last_name")
        
        email = st.text_input("Email", value=profile.get('email', ''), disabled=True, key="edit_email")
        st.caption("ℹ️ L'email ne peut pas être modifié")
        
        col1, col2 = st.columns(2)
        with col1:
            company = st.text_input("Entreprise", value=profile.get('company') or '', key="edit_company")
        with col2:
            job_title = st.text_input("Poste", value=profile.get('job_title') or '', key="edit_job_title")
        
        phone = st.text_input("Téléphone", value=profile.get('phone') or '', key="edit_phone")
        bio = st.text_area("Bio", value=profile.get('bio') or '', height=150, key="edit_bio")
        
        submitted = st.form_submit_button("💾 Enregistrer les modifications", use_container_width=True)
        
        if submitted:
            st.session_state.db.update_user_profile(
                user_id,
                first_name=first_name if first_name else None,
                last_name=last_name if last_name else None,
                company=company if company else None,
                phone=phone if phone else None,
                job_title=job_title if job_title else None,
                bio=bio if bio else None
            )
            # Recharger le profil dans la session
            updated_profile = st.session_state.db.get_user_profile(user_id)
            if updated_profile:
                # Mettre à jour les informations dans st.session_state.user
                st.session_state.user.update({
                    'first_name': updated_profile.get('first_name'),
                    'last_name': updated_profile.get('last_name'),
                    'company': updated_profile.get('company'),
                    'phone': updated_profile.get('phone'),
                    'job_title': updated_profile.get('job_title'),
                    'bio': updated_profile.get('bio')
                })
            st.success("✅ Profil mis à jour avec succès!")
            st.rerun()
    
    st.markdown("---")
    st.markdown("### 📊 Statistiques du compte")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        created_at = profile.get('created_at', 'N/A')
        if created_at and created_at != 'N/A':
            st.metric("📅 Date d'inscription", created_at[:10] if len(created_at) > 10 else created_at)
        else:
            st.metric("📅 Date d'inscription", "N/A")
    
    with col2:
        last_login = profile.get('last_login', 'N/A')
        if last_login and last_login != 'N/A':
            st.metric("🕐 Dernière connexion", last_login[:10] if len(last_login) > 10 else last_login)
        else:
            st.metric("🕐 Dernière connexion", "Première fois")
    
    with col3:
        is_premium = st.session_state.db.check_premium_status(user_id)
        status = "👑 Premium" if is_premium else "🆓 Gratuit"
        st.metric("💎 Statut", status)
    
    with col4:
        projects = st.session_state.db.get_user_projects(user_id)
        st.metric("💾 Projets sauvegardés", len(projects))
    
    st.markdown("---")
    st.markdown("### 💎 Gestion de l'abonnement Premium")
    
    is_premium = st.session_state.db.check_premium_status(user_id)
    
    if is_premium:
        st.success("👑 Vous avez actuellement un abonnement Premium actif")
        
        premium_expires = profile.get('premium_expires')
        if premium_expires:
            st.info(f"⏰ Votre abonnement Premium expire le: {premium_expires[:10] if len(premium_expires) > 10 else premium_expires}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Renouveler Premium (30 jours)", use_container_width=True):
                st.session_state.db.update_premium_status(user_id, True, duration_days=30)
                st.success("✅ Premium renouvelé pour 30 jours supplémentaires!")
                st.rerun()
        
        with col2:
            if st.button("🆓 Revenir en mode Gratuit", use_container_width=True, type="secondary"):
                st.session_state.db.update_premium_status(user_id, False)
                st.success("✅ Vous êtes maintenant en mode Gratuit")
                st.info("💡 Vous pouvez réactiver Premium à tout moment depuis cette page ou la page Premium")
                st.rerun()
    else:
        st.info("🆓 Vous êtes actuellement en mode Gratuit")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("👑 Activer Premium (30 jours)", use_container_width=True):
                st.session_state.db.update_premium_status(user_id, True, duration_days=30)
                st.success("✅ Premium activé pour 30 jours!")
                st.balloons()
                st.rerun()
        
        with col2:
            if st.button("💎 Voir les avantages Premium", use_container_width=True, type="secondary"):
                st.session_state.page = "premium"
                st.rerun()

def show_settings_page():
    """Page de paramètres et personnalisation"""
    st.markdown('<h1 class="main-header">⚙️ Paramètres</h1>', unsafe_allow_html=True)
    
    user_id = st.session_state.user['id']
    prefs = st.session_state.db.get_user_preferences(user_id)
    
    if not prefs:
        st.error("❌ Impossible de charger les préférences")
        return
    
    # Onglets pour différents types de paramètres
    settings_tabs = st.tabs(["🎨 Apparence", "🔔 Notifications"])
    
    with settings_tabs[0]:
        st.markdown("### 🎨 Personnalisation de l'apparence")
        
        with st.form("appearance_form"):
            # Sélection du thème
            theme = st.selectbox(
                "Thème",
                ['light', 'dark', 'auto'],
                index=['light', 'dark', 'auto'].index(prefs.get('theme', 'light')),
                format_func=lambda x: {
                    'light': '☀️ Clair',
                    'dark': '🌙 Sombre',
                    'auto': '🔄 Automatique'
                }.get(x, x)
            )
            
            st.markdown("#### 🎨 Couleurs personnalisées")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                primary_color = st.color_picker(
                    "Couleur principale",
                    value=prefs.get('primary_color', '#667eea')
                )
            with col2:
                secondary_color = st.color_picker(
                    "Couleur secondaire",
                    value=prefs.get('secondary_color', '#764ba2')
                )
            with col3:
                accent_color = st.color_picker(
                    "Couleur d'accent",
                    value=prefs.get('accent_color', '#f093fb')
                )
            
            col1, col2 = st.columns(2)
            with col1:
                text_color = st.color_picker(
                    "Couleur du texte",
                    value=prefs.get('text_color', '#1f2937')
                )
            with col2:
                background_color = st.color_picker(
                    "Couleur de fond",
                    value=prefs.get('background_color', '#ffffff')
                )
            
            # Forme de la police
            font_family = st.selectbox(
                "Forme de la police",
                ['Arial', 'Roboto', 'Inter', 'Open Sans', 'Lato', 'Montserrat', 'Poppins', 'Raleway'],
                index=['Arial', 'Roboto', 'Inter', 'Open Sans', 'Lato', 'Montserrat', 'Poppins', 'Raleway'].index(prefs.get('font_family', 'Arial')) if prefs.get('font_family', 'Arial') in ['Arial', 'Roboto', 'Inter', 'Open Sans', 'Lato', 'Montserrat', 'Poppins', 'Raleway'] else 0,
                format_func=lambda x: x
            )
            
            # Aperçu des couleurs
            st.markdown("#### 👁️ Aperçu")
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {primary_color} 0%, {secondary_color} 50%, {accent_color} 100%);
                        padding: 2rem; border-radius: 15px; color: {text_color}; text-align: center;">
                <h3 style="color: {text_color};">Aperçu de votre thème</h3>
                <p style="color: {text_color};">Ceci est un exemple de texte avec vos couleurs personnalisées</p>
            </div>
            """, unsafe_allow_html=True)
            
            submitted = st.form_submit_button("💾 Enregistrer les préférences", use_container_width=True)
            
            if submitted:
                st.session_state.db.update_user_preferences(
                    user_id,
                    theme=theme,
                    primary_color=primary_color,
                    secondary_color=secondary_color,
                    accent_color=accent_color,
                    text_color=text_color,
                    background_color=background_color,
                    font_family=font_family
                )
                st.success("✅ Préférences d'apparence enregistrées!")
                st.info("💡 Rechargez la page pour voir les changements appliqués.")
                st.rerun()
    
    with settings_tabs[1]:
        st.markdown("### 🔔 Paramètres de notifications")
        
        st.markdown("""
        <div style="background: #f0f9ff; padding: 1.5rem; border-radius: 10px; 
                    border-left: 4px solid #3b82f6; margin-bottom: 2rem;">
            <h4 style="color: #1e40af; margin: 0 0 0.5rem 0;">ℹ️ À propos des notifications</h4>
            <p style="color: #1e3a8a; margin: 0; line-height: 1.6;">
                Les notifications vous alertent sur les événements importants de votre application :
            </p>
            <ul style="color: #1e3a8a; margin: 0.5rem 0 0 0; padding-left: 1.5rem;">
                <li>📤 Import de données réussi</li>
                <li>💾 Sauvegarde et chargement de projets</li>
                <li>📊 Alertes de performance (engagement faible/élevé)</li>
                <li>⚠️ Baisses d'engagement détectées</li>
                <li>🎉 Réalisations et bonnes performances</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("notifications_form"):
            notifications_enabled = st.checkbox(
                "Activer les notifications dans l'application",
                value=bool(prefs.get('notifications_enabled', True)),
                help="Affiche des notifications pour les événements importants"
            )
            
            # Vérifier si l'email est configuré
            from notifications import NotificationManager
            notif_manager = NotificationManager(st.session_state.db, user_id)
            email_configured = notif_manager.email_sender.is_configured()
            
            email_notifications = st.checkbox(
                "Notifications par email",
                value=bool(prefs.get('email_notifications', True)),
                disabled=not notifications_enabled,
                help="Recevez des notifications par email lorsque des événements importants se produisent"
            )
            
            if not email_configured and email_notifications:
                st.markdown("""
                <div style="background: #fef3c7; padding: 1.5rem; border-radius: 10px; 
                            border-left: 4px solid #f59e0b; margin: 1rem 0;">
                    <h4 style="color: #92400e; margin: 0 0 1rem 0;">⚠️ Configuration email requise</h4>
                    <p style="color: #78350f; margin: 0 0 1rem 0;">
                        Pour activer les notifications par email, configurez les paramètres SMTP dans le fichier <code>.env</code> :
                    </p>
                    <div style="background: white; padding: 1rem; border-radius: 5px; margin: 1rem 0;">
                        <pre style="margin: 0; color: #1f2937; font-size: 0.9rem;">
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=votre.email@gmail.com
SMTP_PASSWORD=votre_mot_de_passe_application
FROM_EMAIL=votre.email@gmail.com
APP_NAME=Social Media Analytics Pro
                        </pre>
                    </div>
                    <div style="background: #dbeafe; padding: 1rem; border-radius: 5px; margin-top: 1rem;">
                        <strong style="color: #1e40af;">📧 Pour Gmail :</strong>
                        <ol style="color: #1e3a8a; margin: 0.5rem 0 0 0; padding-left: 1.5rem;">
                            <li>Allez sur <a href="https://myaccount.google.com/" target="_blank" style="color: #3b82f6;">myaccount.google.com</a></li>
                            <li>Sélectionnez <strong>"Sécurité"</strong></li>
                            <li>Activez la <strong>"Validation en deux étapes"</strong> si nécessaire</li>
                            <li>Allez dans <strong>"Mots de passe des applications"</strong></li>
                            <li>Créez un nouveau mot de passe pour <strong>"Mail"</strong></li>
                            <li>Copiez le mot de passe généré (16 caractères) dans <code>SMTP_PASSWORD</code></li>
                        </ol>
                    </div>
                    <p style="color: #78350f; margin: 1rem 0 0 0; font-size: 0.9rem;">
                        💡 <strong>Astuce :</strong> Après avoir modifié le fichier <code>.env</code>, redémarrez l'application pour que les changements prennent effet.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            elif email_configured:
                st.success("✅ Configuration email détectée. Les emails seront envoyés automatiquement.")
            
            if not notifications_enabled:
                st.info("ℹ️ Les notifications sont désactivées. Activez-les pour recevoir des alertes sur vos performances.")
            
            submitted = st.form_submit_button("💾 Enregistrer les préférences", use_container_width=True)
            
            if submitted:
                st.session_state.db.update_user_preferences(
                    user_id,
                    notifications_enabled=1 if notifications_enabled else 0,
                    email_notifications=1 if email_notifications else 0
                )
                st.success("✅ Préférences de notifications enregistrées!")
                st.rerun()
    
    st.markdown("---")
    st.markdown("### 🔄 Réinitialiser les paramètres")
    
    if st.button("🔄 Réinitialiser aux valeurs par défaut", use_container_width=True):
        st.session_state.db.update_user_preferences(
            user_id,
            theme='light',
            primary_color='#667eea',
            secondary_color='#764ba2',
            accent_color='#f093fb',
            text_color='#1f2937',
            background_color='#ffffff',
            font_family='Arial',
            notifications_enabled=1,
            email_notifications=1
        )
        st.success("✅ Paramètres réinitialisés aux valeurs par défaut!")
        st.rerun()

# Application principale
def main():
    # Initialiser show_landing si pas déjà défini
    if 'show_landing' not in st.session_state:
        st.session_state.show_landing = True
    
    # Afficher la page de présentation si nécessaire
    if st.session_state.show_landing and st.session_state.user is None:
        landing_page()
    elif st.session_state.user is None:
        login_page()
    else:
        main_app()

if __name__ == "__main__":
    main()

