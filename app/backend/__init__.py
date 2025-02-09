"""
📌 __init__.py - Rendre `/app/backend/` un package Python
"""
# 🔹 Import des services
from .services import get_all_users, get_user_by_id, generate_full_report, generate_comparative_report, generate_graph

# ✅ Liste des éléments accessibles
__all__ = ["get_all_users", "get_user_by_id", "generate_full_report", "generate_comparative_report", "generate_graph"]
