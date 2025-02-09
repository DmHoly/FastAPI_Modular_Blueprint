"""
📌 Endpoint API - Dummy Users
-----------------------------
Expose un service factice qui retourne des utilisateurs fictifs.
"""

from fastapi import APIRouter
from app.backend.services import get_all_users, get_user_by_id  # Import simplifié


router = APIRouter()

@router.get("/users", tags=["Dummy Users"])
async def read_users():
    """Retourne la liste des utilisateurs fictifs."""
    return {"users": get_all_users()}

@router.get("/users/{user_id}", tags=["Dummy Users"])
async def read_user(user_id: int):
    """Retourne un utilisateur spécifique par ID."""
    return get_user_by_id(user_id)
