# from .data import router as data_router
# from .user import router as user_router  # 📌 Ajout du nouvel endpoint
#
# __all__ = ["data_router", "user_router"]

"""
📌 __init__.py - Centralisation des endpoints API
-------------------------------------------------
Ce fichier permet d'importer les endpoints plus facilement.
"""

from .dummy import router as dummy_router

__all__ = ["dummy_router"]
