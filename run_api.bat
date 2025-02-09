@echo off
title 🚀 Lancement de l'API FastAPI
echo ===========================================
echo 🔹 Démarrage de l'API FastAPI...
echo ===========================================

:: Définir le chemin Python pour éviter ModuleNotFoundError
set PYTHONPATH=%cd%

:: Démarrer FastAPI avec uvicorn
cd app
start cmd /k "uvicorn main:app --host 127.0.0.1 --port 8000 --reload"

:: Fin du script
echo ===========================================
echo ✅ API FastAPI est en cours d'exécution !
echo ===========================================
exit
