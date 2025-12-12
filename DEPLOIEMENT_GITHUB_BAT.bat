@echo off
REM Script pour publier le projet sur GitHub
REM Utilisez ce script après avoir installé Git

echo ========================================
echo   Publication sur GitHub
echo   Social Media Analytics Pro
echo ========================================
echo.

REM Vérifier si Git est installé
git --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Git n'est pas installe!
    echo.
    echo Veuillez installer Git depuis: https://git-scm.com/download/win
    echo Ou utilisez GitHub Desktop: https://desktop.github.com/
    pause
    exit /b 1
)

echo [OK] Git est installe
echo.

REM Demander le nom d'utilisateur Git (si pas déjà configuré)
echo Configuration Git (si pas deja faite):
set /p GIT_NAME="Entrez votre nom (pour Git): "
set /p GIT_EMAIL="Entrez votre email (pour Git): "

git config --global user.name "%GIT_NAME%"
git config --global user.email "%GIT_EMAIL%"

echo.
echo Configuration terminee!
echo.

REM Initialiser Git (si pas déjà fait)
if not exist ".git" (
    echo Initialisation du repository Git...
    git init
    echo [OK] Repository initialise
) else (
    echo [OK] Repository Git deja initialise
)

echo.
echo Preparation des fichiers...
git add .

echo.
set /p COMMIT_MSG="Message de commit (ou appuyez Entree pour 'Initial commit'): "
if "%COMMIT_MSG%"=="" set COMMIT_MSG=Initial commit - Social Media Analytics Pro

git commit -m "%COMMIT_MSG%"

echo.
echo ========================================
echo   Prochaine etape:
echo ========================================
echo.
echo 1. Creer un nouveau repository sur GitHub:
echo    https://github.com/new
echo.
echo 2. Ne cochez PAS "Initialize with README"
echo.
echo 3. Une fois cree, copiez l'URL du repository
echo    (exemple: https://github.com/VOTRE_USERNAME/REPO_NAME.git)
echo.
echo 4. Puis executez ces commandes dans PowerShell:
echo.
echo    git remote add origin https://github.com/VOTRE_USERNAME/REPO_NAME.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo OU utilisez GitHub Desktop (plus simple):
echo    https://desktop.github.com/
echo.
pause

