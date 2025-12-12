@echo off
echo ========================================
echo   Social Media Analytics Pro - CREATIVE
echo ========================================
echo.

echo [1/3] Verification de Python...
python --version
if %errorlevel% neq 0 (
    echo ERREUR: Python n'est pas installe ou pas dans le PATH
    pause
    exit /b 1
)

echo.
echo [2/3] Installation des dependances...
pip install streamlit pandas numpy plotly
if %errorlevel% neq 0 (
    echo ERREUR: Echec de l'installation des dependances
    pause
    exit /b 1
)

echo.
echo [3/3] Demarrage de l'application CREATIVE...
echo.
echo ========================================
echo   Application CREATIVE disponible sur:
echo   http://localhost:8501
echo ========================================
echo.
echo 🎨 NOUVELLES FONCTIONNALITES CREATIVES:
echo ✅ Design moderne avec animations
echo ✅ Micro-interactions avancees
echo ✅ Graphiques interactifs
echo ✅ Sidebar moderne
echo ✅ Notifications toast
echo ✅ Thèmes sombres/clair
echo ✅ Responsive design
echo.
echo Appuyez sur Ctrl+C pour arreter l'application
echo.

streamlit run app_creative.py --server.port 8501 --server.address 0.0.0.0


