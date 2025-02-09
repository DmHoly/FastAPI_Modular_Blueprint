"""
📌 Main.py - Point d'entrée de l'application FastAPI
---------------------------------------------------
Ce fichier démarre l'API FastAPI et inclut toutes les routes définies.
"""

from fastapi import FastAPI
from app.api.routes import router  # 🔹 Import des routes API

# Initialisation de l'application FastAPI
app = FastAPI(title="FastAPI Modular Blueprint")

# Inclure les routes API
app.include_router(router)

# Endpoint de test
@app.get("/")
async def root():
    routes = {route.path: route.name for route in app.routes}
    return {
        "message": "🚀 FastAPI est en ligne !",
        ""
        ""
        ""
        "routes_disponibles": routes
    }

# Lancer avec uvicorn si ce fichier est exécuté directement
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
