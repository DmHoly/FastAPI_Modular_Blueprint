from fastapi import APIRouter
from typing import List

from app.backend.services.graph_services import generate_graph

router = APIRouter()

@router.get("/graph/{user_id}/{data_type}")
def graph(user_id: int, data_type: str):
    """�? Génère un graphique pour un utilisateur."""
    return generate_graph(user_id, data_type)

