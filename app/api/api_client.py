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

    def generate_full_report(self, user_id):
        return requests.get(f"{self.base_url}/users/{user_id}/full_report").json()

    def generate_comparative_report(self, user_ids):
        return requests.get(f"{self.base_url}/comparative_report/{user_ids}").json()

    #@router.get("/graph/{user_id}/{data_type}")
    def generate_graph(self, user_id, data_type):
        return requests.get(f"{self.base_url}/graph/{user_id}/{data_type}").json()