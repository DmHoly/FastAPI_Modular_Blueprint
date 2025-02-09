from fastapi import APIRouter
from app.api.endpoints import dummy_router  # Import simplifié grâce à __init__.py
from app.api.endpoints import reports_router  # Import simplifié grâce à __init__.py
from app.api.endpoints import graph_router  # Import simplifié grâce à __init__.py
router = APIRouter()

# Ajout des routes
router.include_router(dummy_router, prefix="/api", tags=["Dummy Users"])
router.include_router(reports_router, prefix="/api", tags=["Reports"])
router.include_router(graph_router, prefix="/api", tags=["Graph"])