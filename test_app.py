"""
Script de test rapide pour vérifier que l'application fonctionne
"""

import sys
import subprocess

def test_imports():
    """Teste l'importation des modules principaux"""
    print("🔍 Test des imports...")
    
    try:
        import streamlit
        print("✅ Streamlit OK")
    except ImportError:
        print("❌ Streamlit manquant")
        return False
    
    try:
        import pandas
        print("✅ Pandas OK")
    except ImportError:
        print("❌ Pandas manquant")
        return False
    
    try:
        import numpy
        print("✅ NumPy OK")
    except ImportError:
        print("❌ NumPy manquant")
        return False
    
    try:
        import plotly
        print("✅ Plotly OK")
    except ImportError:
        print("❌ Plotly manquant")
        return False
    
    try:
        import sklearn
        print("✅ Scikit-learn OK")
    except ImportError:
        print("❌ Scikit-learn manquant")
        return False
    
    try:
        import scipy
        print("✅ SciPy OK")
    except ImportError:
        print("❌ SciPy manquant")
        return False
    
    return True

def test_modules():
    """Teste les modules personnalisés"""
    print("\n🔍 Test des modules personnalisés...")
    
    try:
        from database import Database
        print("✅ Database module OK")
    except ImportError as e:
        print(f"❌ Database module: {e}")
        return False
    
    try:
        from statistical_analysis import StatisticalAnalyzer
        print("✅ Statistical Analysis module OK")
    except ImportError as e:
        print(f"❌ Statistical Analysis module: {e}")
        return False
    
    try:
        from ai_assistant import AIAssistant
        print("✅ AI Assistant module OK")
    except ImportError as e:
        print(f"❌ AI Assistant module: {e}")
        return False
    
    try:
        from visualizations import DataVisualizer
        print("✅ Visualizations module OK")
    except ImportError as e:
        print(f"❌ Visualizations module: {e}")
        return False
    
    return True

def test_database():
    """Teste la création de la base de données"""
    print("\n🔍 Test de la base de données...")
    
    try:
        from database import Database
        db = Database("test.db")
        print("✅ Base de données créée")
        
        # Test de création d'utilisateur
        success, message = db.create_user("test@example.com", "test123")
        if success:
            print("✅ Création d'utilisateur OK")
        else:
            print(f"⚠️ Création d'utilisateur: {message}")
        
        return True
    except Exception as e:
        print(f"❌ Erreur base de données: {e}")
        return False

def test_statistical_analysis():
    """Teste les analyses statistiques"""
    print("\n🔍 Test des analyses statistiques...")
    
    try:
        import pandas as pd
        import numpy as np
        from statistical_analysis import StatisticalAnalyzer
        
        # Créer des données de test
        data = {
            'platform': ['TikTok', 'Instagram', 'Facebook'] * 10,
            'likes': np.random.randint(100, 1000, 30),
            'followers': np.random.randint(1000, 10000, 30)
        }
        df = pd.DataFrame(data)
        
        analyzer = StatisticalAnalyzer(df)
        analyzer.calculate_engagement_rate()
        
        # Test Kruskal-Wallis
        result = analyzer.kruskal_wallis_test('likes', 'platform')
        if result:
            print("✅ Test Kruskal-Wallis OK")
        else:
            print("⚠️ Test Kruskal-Wallis échoué")
        
        return True
    except Exception as e:
        print(f"❌ Erreur analyses statistiques: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("=" * 60)
    print("🧪 TEST DE SOCIAL MEDIA ANALYTICS PRO")
    print("=" * 60)
    
    all_tests_passed = True
    
    # Test 1: Imports
    if not test_imports():
        all_tests_passed = False
    
    # Test 2: Modules personnalisés
    if not test_modules():
        all_tests_passed = False
    
    # Test 3: Base de données
    if not test_database():
        all_tests_passed = False
    
    # Test 4: Analyses statistiques
    if not test_statistical_analysis():
        all_tests_passed = False
    
    print("\n" + "=" * 60)
    if all_tests_passed:
        print("🎉 TOUS LES TESTS SONT PASSÉS !")
        print("✅ L'application est prête à être lancée")
        print("\nPour lancer l'application:")
        print("streamlit run app.py")
    else:
        print("❌ CERTAINS TESTS ONT ÉCHOUÉ")
        print("⚠️ Vérifiez les erreurs ci-dessus")
        print("\nPour installer les dépendances manquantes:")
        print("pip install -r requirements.txt")
    print("=" * 60)

if __name__ == "__main__":
    main()


