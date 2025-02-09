"""
📌 __init__.py - Rendre `/app/backend/` un package Python
"""

from .services import get_all_users, get_user_by_id  # 🔹 Import des services

__all__ = ["get_all_users", "get_user_by_id"]
