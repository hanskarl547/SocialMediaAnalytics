@echo off
echo ================================================
echo    Social Media Analytics Pro
echo    Demarrage de l'application...
echo ================================================
echo.

REM Verifier si Python est installe
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe ou n'est pas dans le PATH
    echo Veuillez installer Python 3.8 ou superieur depuis python.org
    pause
    exit /b 1
)

echo [1/3] Verification de Python... OK
echo.

REM Verifier si les dependances sont installees
pip show streamlit >nul 2>&1
if errorlevel 1 (
    echo [2/3] Installation des dependances...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERREUR: Impossible d'installer les dependances
        pause
        exit /b 1
    )
) else (
    echo [2/3] Dependances... OK
)
echo.

REM Creer le fichier .env s'il n'existe pas
if not exist .env (
    echo [INFO] Creation du fichier .env...
    copy .env.example .env >nul 2>&1
)

echo [3/3] Lancement de l'application...
echo.
echo ================================================
echo    L'application va s'ouvrir dans votre navigateur
echo    URL: http://localhost:8501
echo.
echo    Pour arreter l'application: Ctrl+C
echo ================================================
echo.

REM Lancer Streamlit
streamlit run app.py

pause

