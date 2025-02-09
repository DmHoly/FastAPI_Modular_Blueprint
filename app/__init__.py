"""
📌 __init__.py - Permet d'importer `APIClient` directement
"""
# ✅ Rend  accessible depuis `app/
# sous la forme from app import APIClient
# sinon faut faire from app.api import APIClient
#

from .api import APIClient
from .backend import get_all_users, get_user_by_id

__all__ = ["APIClient", "get_all_users", "get_user_by_id"]  # ✅ Liste des éléments accessibles

