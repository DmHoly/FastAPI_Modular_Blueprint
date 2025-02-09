"""
📌 Dummy Service
----------------
Ce fichier simule un service backend en utilisant une base de données fictive.
"""

from typing import List, Dict

# Base de données bidon (simulation)
DUMMY_DB = [
    {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "type1_data": {"score": 85, "level": "high"},
        "type1_kpi": {"performance": 90, "efficiency": 80},
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 25,
        "type1_data": {"score": 70, "level": "medium"},
        "type1_kpi": {"performance": 75, "efficiency": 70},
    },

    {
        "id": 3,
        "name": "Charlie",
        "age": 35,
        "type1_data": {"score": 60, "level": "low"},
        "type1_kpi": {"performance": 65, "efficiency": 60},
        "type2_data": {"score": 75, "level": "medium"},
        "type2_kpi": {"performance": 80, "efficiency": 70},
    },
]

def get_all_users() -> List[Dict]:
    """Récupère tous les utilisateurs."""
    return DUMMY_DB

def get_user_by_id(user_id: int) -> Dict:
    """Récupère un utilisateur par son ID."""
    user = next((u for u in DUMMY_DB if u["id"] == user_id), None)
    return user if user else {"error": "Utilisateur non trouvé"}
