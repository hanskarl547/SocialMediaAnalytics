@echo off
echo ========================================
echo   Social Media Analytics Pro - FIXED
echo ========================================
echo.

echo [1/4] Verification de Python...
python --version
if %errorlevel% neq 0 (
    echo ERREUR: Python n'est pas installe ou pas dans le PATH
    pause
    exit /b 1
)

echo.
echo [2/4] Installation des dependances...
pip install streamlit pandas numpy plotly scipy scikit-learn python-dotenv openai
if %errorlevel% neq 0 (
    echo ERREUR: Echec de l'installation des dependances
    pause
    exit /b 1
)

echo.
echo [3/4] Verification des imports...
python -c "from ai_assistant import AIAssistant; print('✅ AI Assistant: OK')"
python -c "from enhanced_ai_assistant import EnhancedAIAssistant; print('✅ Enhanced AI: OK')"
python -c "from real_world_ai_interpreter import RealWorldAIInterpreter; print('✅ Real World AI: OK')"
python -c "from ultra_advanced_statistical_analysis import UltraAdvancedStatisticalAnalyzer; print('✅ Ultra Advanced Stats: OK')"

echo.
echo [4/4] Demarrage de l'application...
echo.
echo ========================================
echo   Application disponible sur:
echo   http://localhost:8501
echo ========================================
echo.
echo 🎯 FONCTIONNALITES DISPONIBLES:
echo ✅ IA Amelioree avec interpretations reelles
echo ✅ Tests statistiques ultra-avances
echo ✅ Kolmogorov-Smirnov et Friedman
echo ✅ Benchmarks de l'industrie
echo ✅ Recommandations actionables
echo ✅ Mode Premium Demo
echo.
echo Appuyez sur Ctrl+C pour arreter l'application
echo.

streamlit run app.py --server.port 8501 --server.address 0.0.0.0


