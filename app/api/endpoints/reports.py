"""
📌 API - Génération de Rapports
-------------------------------
- `/api/users/{user_id}/full_report` : Génère un rapport détaillé.
- `/api/comparative_report?users=1,2,3` : Compare plusieurs utilisateurs.
"""

from fastapi import APIRouter, Query
from typing import List
from app.backend.services.report_services import (
    generate_full_report,
    generate_comparative_report
)

router = APIRouter()

@router.get("/users/{user_id}/full_report")
async def full_report(user_id: int):
    """📄 Génère un rapport complet pour un utilisateur."""
    return generate_full_report(user_id)

@router.get("/comparative_report")
async def comparative_report(users: str = Query(..., description="Liste d'IDs utilisateurs séparés par des virgules")):
    """📊 Génère un rapport comparatif pour plusieurs utilisateurs."""
    user_id_list = [int(uid) for uid in users.split(",")]
    return generate_comparative_report(user_id_list)
