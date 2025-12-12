@echo off
echo ========================================
echo   Social Media Analytics Pro - Streamlit
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
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERREUR: Echec de l'installation des dependances
    pause
    exit /b 1
)

echo.
echo [3/3] Verification du mode demo...
python setup_demo.py
echo.

echo ========================================
echo   Application disponible sur:
echo   http://localhost:8501
echo ========================================
echo.
echo Mode Demo Premium active par defaut!
echo Cliquez sur "Activer Premium Demo" pour tester.
echo.
echo Appuyez sur Ctrl+C pour arreter l'application
echo.

streamlit run app.py --server.port 8501 --server.address 0.0.0.0
