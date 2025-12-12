@echo off
echo ========================================
echo   SYNCHRONISATION AVEC GITHUB
echo   Pour mettre a jour le site deploye
echo ========================================
echo.

cd /d "%~dp0"

echo [1/4] Verification de l'etat Git...
git status
echo.

echo [2/4] Ajout des modifications...
git add .
echo.

echo [3/4] Creation du commit...
set /p commit_msg="Entrez un message pour ce commit (ou appuyez sur Entree pour utiliser le message par defaut): "
if "%commit_msg%"=="" set commit_msg=Mise a jour de l'application
git commit -m "%commit_msg%"
echo.

echo [4/4] Envoi vers GitHub...
git push origin main
if errorlevel 1 (
    echo.
    echo ERREUR: Impossible de pousser vers GitHub.
    echo Verifiez que vous etes connecte a GitHub.
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo   SUCCES!
echo ========================================
echo.
echo Vos modifications ont ete poussees vers GitHub.
echo Streamlit Cloud va redepoyer automatiquement dans 2-5 minutes.
echo.
echo Pour verifier:
echo 1. Allez sur https://github.com/hanskarl547/SocialMediaAnalytics
echo 2. Allez sur https://share.streamlit.io/
echo 3. Cliquez sur votre application pour voir le statut
echo.
pause

