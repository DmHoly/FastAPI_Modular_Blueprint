from fastapi import APIRouter
from app.api.endpoints import dummy_router  # Import simplifié grâce à __init__.py

router = APIRouter()

# Ajout des routes
router.include_router(dummy_router, prefix="/api", tags=["Dummy Users"])
