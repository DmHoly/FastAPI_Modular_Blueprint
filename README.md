# 🚀 FastAPI Modular Blueprint

## 📋 Description  
Ce blueprint est une **architecture modulaire** pour construire des **applications FastAPI** avec une gestion propre du backend, de la base de données, et du frontend.  

Il est conçu pour être **dupliqué** et servir de base à n'importe quel projet nécessitant **FastAPI + SQLAlchemy + Dash/Streamlit + Jupyter Notebook**.

---

## 📂 **Structure du projet**
- **Backend (`/backend/`)** → Services et logique métier  
- **Base de données (`/database/`)** → Gestion avec SQLAlchemy  
- **Frontend (`/frontend/`)** → Interface utilisateur indépendante  
- **Notebooks (`/notebooks/`)** → Exemples interactifs pour tester le backend  

---

## 📂 **Arborescence du projet**

```plaintext
/FastAPI_Modular_Blueprint
│── /app
│   │── /api                 # 📡 Gestion des endpoints FastAPI
│   │   │── __init__.py      # 📌 Simplifie les imports des endpoints
│   │   │── routes.py        # 📌 Regroupe toutes les routes de l'API
│   │   │── endpoints        # 📌 Dossier contenant les différentes routes API
│   │   │   │── __init__.py  # 📌 Import centralisé des endpoints
│   │   │   │── data.py      # 📌 API pour récupérer les données et les graphiques
│
│   │── /backend             # 🧠 Gestion de la logique métier (services)
│   │   │── __init__.py      # 📌 Centralise tous les imports du backend
│   │   │── services         # 📌 Dossier contenant les services backend
│   │   │   │── __init__.py  # 📌 Simplifie l'import des services
│   │   │   │── data_service.py  # 📌 Gestion des données SampleData
│   │   │   │── graph_service.py  # 📌 Génération des graphiques avec matplotlib
│
│   │── /database            # 🗄️ Gestion de la base de données (SQLAlchemy)
│   │   │── __init__.py      # 📌 Import centralisé pour la base de données
│   │   │── database.py      # 📌 Connexion à la base SQLite (SQLAlchemy)
│   │   │── models.py        # 📌 Définition des tables avec SQLAlchemy
│   │   │── data_loader.py   # 📌 Script pour remplir la base avec des données
│
│   │── /frontend            # 🎨 Gestion de l'interface utilisateur
│   │   │── __init__.py      # 📌 Permet de gérer l'interface indépendamment
│   │   │── main.py          # 📌 Point d’entrée de l’interface (Dash, Streamlit, etc.)
│   │   │── components       # 📌 Composants réutilisables pour l'affichage
│   │   │   │── __init__.py  # 📌 Pour gérer les composants plus facilement
│   │   │   │── graph_component.py  # 📌 Composant pour afficher les graphiques
│   │   │   │── data_table.py  # 📌 Composant pour afficher les données
│   │   │── pages            # 📌 Pages de l'interface utilisateur
│   │   │   │── __init__.py  # 📌 Gestion centralisée des pages
│   │   │   │── home.py      # 📌 Page d'accueil
│   │   │   │── sample_view.py  # 📌 Page pour visualiser un Sample
│
│   │── main.py              # 🚀 Point d’entrée principal de l’application FastAPI
│
│── /notebooks               # 📊 Dossier contenant les exemples en Jupyter Notebook
│   │── 01_usage_backend.ipynb  # 📌 Exemple d'utilisation du backend
│   │── 02_visualisation_graphs.ipynb  # 📌 Exemple de génération de graph
│
│── /config                  # ⚙️ Configuration globale (Nginx, settings, etc.)
│   │── nginx.conf           # 📌 Reverse Proxy (Nginx)
│   │── settings.py          # 📌 Fichier de configuration globale
│
│── requirements.txt         # 📜 Liste des dépendances Python
│── README.md                # 📌 Documentation du blueprint
│── run.bat                  # 🏃 Script pour lancer le projet sous Windows

```
## 🚀 **Comment configurer les `__init__.py` ?**

Les fichiers `__init__.py` permettent de **simplifier les imports** et **d'améliorer la lisibilité** du projet.  
Grâce à eux, on évite d'avoir des **chemins d'import trop longs** et **répétitifs**.

---

## 📂 **Table des matières**
1. [Backend (`/app/backend/`)](#backend)
2. [Services (`/app/backend/services/`)](#services)
3. [Base de données (`/app/database/`)](#database)
4. [API (`/app/api/`)](#api)
5. [Frontend (`/app/frontend/`)](#frontend)

---

## 📌 <a name="backend"></a>**📂 Dans `/app/backend/`**
- 📌 **Objectif** : Permet d’accéder rapidement aux services du backend.
- 📌 **Fichier** : `/app/backend/__init__.py`

```python
from .services import get_sample_from_id, SampleData, Type1_data_graph_gen

__all__ = ["get_sample_from_id", "SampleData", "Type1_data_graph_gen"]
```
✅ Import rapide dans tout le projet :
```python
from app.backend import get_sample_from_id, SampleData
```
🔴 Au lieu de devoir écrire :
```python
from app.backend.services.data_service import get_sample_from_id
from app.backend.services.data_service import SampleData
```
---

## 🚀 **Comment utiliser ce blueprint ?**
### 1️⃣ **Dupliquer le projet**
```sh
git clone https://github.com/mon-projet.git Mon_Nouveau_Projet
cd Mon_Nouveau_Projet
```

## 🎯 Pourquoi ces dépendances ?

| 📦 **Librairie**  | 📋 **Utilisation** |
|------------------|------------------|
| `fastapi` | 📡 Framework backend ultra-rapide |
| `uvicorn` | 🚀 Serveur ASGI pour exécuter FastAPI |
| `sqlalchemy` | 🗄️ ORM pour gérer la base de données |
| `sqlite` | 🗃️ Base de données légère et portable |
| `pandas` | 📊 Manipulation et analyse de données |
| `matplotlib` | 📈 Génération de graphiques |
| `dash` | 🎨 Framework web pour créer des interfaces |
| `streamlit` | 📺 Alternative à Dash pour un frontend simplifié |
| `jupyter` | 📜 Exécuter et tester le backend dans des notebooks |
| `pydantic` | 🛡️ Validation des données dans FastAPI |
| `python-dotenv` | 🔑 Chargement des variables d’environnement |
| `requests` | 🌐 Appeler des API externes depuis le backend |
