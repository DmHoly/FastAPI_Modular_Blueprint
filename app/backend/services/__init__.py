"""
📌 __init__.py - Centralisation des services backend
---------------------------------------------------
Ce fichier permet d'importer les services plus facilement.

--> from app.backend.services import get_all_users

"""

from .dummy_service import get_all_users, get_user_by_id
from .graph_services import generate_graph
from .report_services import generate_full_report, generate_comparative_report

__all__ = ["get_all_users", "get_user_by_id", "generate_full_report", "generate_comparative_report", "generate_graph"]

