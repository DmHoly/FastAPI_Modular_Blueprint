"""
📌 Dummy Service
----------------
Ce fichier simule un service backend en utilisant une base de données fictive.
"""

from typing import List, Dict

# Base de données bidon (simulation)
DUMMY_DB = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 35},
]

def get_all_users() -> List[Dict]:
    """Récupère tous les utilisateurs."""
    return DUMMY_DB

def get_user_by_id(user_id: int) -> Dict:
    """Récupère un utilisateur par son ID."""
    user = next((u for u in DUMMY_DB if u["id"] == user_id), None)
    return user if user else {"error": "Utilisateur non trouvé"}
