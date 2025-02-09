"""
📌 __init__.py - Centralisation des services backend
---------------------------------------------------
Ce fichier permet d'importer les services plus facilement.

--> from app.backend.services import get_all_users

"""

from .dummy_service import get_all_users, get_user_by_id

__all__ = ["get_all_users", "get_user_by_id"]
