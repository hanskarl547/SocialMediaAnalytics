@echo off
echo 🚀 Installation de Social Media Analytics Pro...

:: Vérifier que Python est installé
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python n'est pas installé. Veuillez l'installer depuis https://www.python.org/downloads/
    pause
    exit /b
)

:: Mettre à jour pip
echo 🔄 Mise à jour de pip...
python -m pip install --upgrade pip

:: Installer les dépendances
echo 📦 Installation des dépendances...
pip install -r requirements.txt

:: Créer le fichier .env si absent
IF NOT EXIST ".env" (
    echo 🔧 Création du fichier .env...
    copy .env.example .env
)

echo ✅ Installation terminée !
pause
