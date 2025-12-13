@echo off
echo ========================================
echo   RECREER LE DEPOT GITHUB
echo   ET POUSSER LE CODE
echo ========================================
echo.

cd /d "%~dp0"

echo [1/5] Verification de Git...
git --version
if errorlevel 1 (
    echo.
    echo ERREUR: Git n'est pas installe.
    echo Installez Git depuis: https://git-scm.com/download/win
    echo.
    pause
    exit /b 1
)
echo OK - Git est installe
echo.

echo [2/5] Initialisation du depot Git (si necessaire)...
if not exist .git (
    echo Initialisation du depot Git...
    git init
    echo OK - Depot Git initialise
) else (
    echo OK - Depot Git deja initialise
)
echo.

echo [3/5] Ajout de tous les fichiers...
git add .
echo OK - Fichiers ajoutes
echo.

echo [4/5] Creation du commit...
git commit -m "Initial commit - Application Social Media Analytics"
if errorlevel 1 (
    echo.
    echo ATTENTION: Aucun changement a commiter, ou commit deja fait.
    echo Continuons quand meme...
)
echo.

echo [5/5] Configuration du depot distant...
echo.
echo IMPORTANT: Vous devez d'abord creer le depot sur GitHub.com
echo.
echo 1. Allez sur https://github.com/new
echo 2. Nom du depot: SocialMediaAnalytics
echo 3. Choisissez Public ou Private
echo 4. NE COCHEZ PAS "Add a README file"
echo 5. Cliquez sur "Create repository"
echo.
set /p repo_url="Entrez l'URL de votre depot GitHub (ex: https://github.com/hanskarl547/SocialMediaAnalytics.git): "

if "%repo_url%"=="" (
    echo.
    echo ERREUR: URL non fournie. Annulation.
    pause
    exit /b 1
)

echo.
echo Configuration du depot distant...
git remote remove origin 2>nul
git remote add origin "%repo_url%"
echo OK - Depot distant configure
echo.

echo [6/6] Pousser le code vers GitHub...
echo.
echo ATTENTION: Vous devrez entrer vos identifiants GitHub.
echo Si demande, utilisez un Personal Access Token comme mot de passe.
echo.
git branch -M main
git push -u origin main

if errorlevel 1 (
    echo.
    echo ERREUR: Impossible de pousser vers GitHub.
    echo.
    echo Solutions possibles:
    echo 1. Verifiez que le depot existe sur GitHub
    echo 2. Verifiez que vous avez les droits d'ecriture
    echo 3. Utilisez un Personal Access Token comme mot de passe
    echo    (GitHub -^> Settings -^> Developer settings -^> Personal access tokens)
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo   SUCCES!
echo ========================================
echo.
echo Votre code a ete pousse vers GitHub.
echo Vous pouvez maintenant deployer sur Render.com
echo.
pause

