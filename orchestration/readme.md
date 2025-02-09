# 📌 Documentation - Orchestration avec Dagster

## 🎯 Objectif
Cette documentation explique comment orchestrer un appel automatique à l'API FastAPI en utilisant **Dagster**. L'objectif est d'automatiser les requêtes à l'API et de planifier leur exécution à intervalles réguliers.

---

## 🚀 Installation
Avant de commencer, installe les dépendances nécessaires :

```sh
pip install dagster dagster-webserver requests
```

---

## 📂 Structure du projet

```
/project
│── dagster_pipeline.py  # Script contenant l'orchestration Dagster
│── fastapi_app/          # Dossier contenant l'application FastAPI
│── README.md             # Documentation du projet
```

---

## 🔧 Configuration de Dagster

### 1️⃣ **Créer une opération (`@op`) qui appelle l’API**
Dans `dagster_pipeline.py`, ajoute le code suivant :

```python
import requests
from dagster import op, job

API_URL = "http://127.0.0.1:8000/"  # URL de l'API FastAPI

@op
def call_api():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Erreur API: {response.status_code}, {response.text}")

@job
def api_call_job():
    call_api()
```

### 2️⃣ **Exécuter le job manuellement**
Pour tester l'appel à l'API, exécute la commande suivante :

```sh
dagster job execute -m dagster_pipeline -j api_call_job
```

### 3️⃣ **Automatiser l’exécution avec un `schedule`**
Ajoute un `schedule` pour exécuter le job toutes les 5 minutes :

```python
from dagster import schedule

@schedule(cron_schedule="*/5 * * * *", job=api_call_job, execution_timezone="UTC")
def api_call_schedule():
    return {}
```

### 4️⃣ **Lancer Dagster et activer le `schedule`**
Démarre Dagster avec la commande suivante :

```sh
dagster dev
```

Ensuite, ouvre **l’interface Dagster** à l'adresse [http://127.0.0.1:3000](http://127.0.0.1:3000) et active le **schedule** pour exécuter l’appel API automatiquement.

---

## ✅ Résumé
- **Dagster op** → Appelle l’API.
- **Dagster job** → Orchestration de l’opération.
- **Dagster schedule** → Exécution automatique toutes les 5 minutes.

Avec cette configuration, ton API FastAPI est automatiquement interrogée selon l'intervalle défini 🚀🔥 !

