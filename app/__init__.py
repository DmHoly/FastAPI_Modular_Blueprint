"""
📌 __init__.py - Permet d'importer `APIClient` directement
"""

from .api import APIClient  # ✅ Rend `APIClient` accessible depuis `app/`

__all__ = ["APIClient"]

