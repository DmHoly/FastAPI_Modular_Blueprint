"""
📌 Backend - Génération de Rapports pour les Utilisateurs
"""

from app.backend.services.dummy_service import get_user_by_id
from typing import List, Dict

def generate_full_report(user_id: int) -> Dict:
    """📊 Génère un rapport détaillé pour un utilisateur."""
    user = get_user_by_id(user_id)
    if "error" in user:
        return user

    report = {
        "user": user["name"],
        "age": user["age"],
        "type1_data": user.get("type1_data", "Non disponible"),
        "type1_kpi": user.get("type1_kpi", "Non disponible"),
        "summary": f"📌 Rapport généré pour {user['name']}"
    }
    return report


def generate_comparative_report(user_ids: List[int]) -> Dict:
    """📊 Génère un rapport comparatif pour plusieurs utilisateurs."""
    report = {"comparative_report": []}

    for user_id in user_ids:
        user = get_user_by_id(user_id)
        if "error" in user:
            continue

        report["comparative_report"].append({
            "user": user["name"],
            "type1_data": user.get("type1_data", "Non disponible"),
            "type1_kpi": user.get("type1_kpi", "Non disponible"),
        })

    report["summary"] = f"📌 Rapport comparatif pour {len(report['comparative_report'])} utilisateurs"
    return report
