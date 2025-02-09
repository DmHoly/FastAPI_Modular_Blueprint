@echo off
title FastAPI Modular Blueprint - Launch Script
echo ===========================================
echo 🚀 Lancement de l'application...
echo ===========================================

:: Définition des variables d'environnement (si nécessaire)
set PYTHON_ENV=venv
set APP_PATH=%cd%\app

:: Activation de l'environnement virtuel (si utilisé)
if exist %PYTHON_ENV%\Scripts\activate.bat (
    echo 🔹 Activation de l'environnement virtuel...
    call %PYTHON_ENV%\Scripts\activate
)

:: Démarrer Nginx
echo 🔹 Démarrage de Nginx...
cd C:\nginx
start nginx

:: Démarrer le backend FastAPI
echo 🔹 Lancement du backend FastAPI...
cd %APP_PATH%
start cmd /k "uvicorn main:app --host 127.0.0.1 --port 8000 --reload"

:: Démarrer le frontend (Dash ou Streamlit)
echo 🔹 Lancement du frontend...
cd %APP_PATH%\frontend
start cmd /k "python main.py"

:: Fin du script
echo ===========================================
echo ✅ Tous les services ont été démarrés !
echo ===========================================
exit
