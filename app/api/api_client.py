"""
📌 Client API - Simplifie l'utilisation de l'API en Python
"""
import requests

class APIClient:
    def __init__(self, base_url="http://127.0.0.1:8000/api"):
        self.base_url = base_url

    def get_users(self):
        return requests.get(f"{self.base_url}/users").json().get("users", [])

    def get_user_by_id(self, user_id):
        return requests.get(f"{self.base_url}/users/{user_id}").json()

