


if __name__ == "__main__":

    # 🌍 : Utilisation de l’API (via requests)
    import requests
    import json

    BASE_URL = "http://127.0.0.1:8000/api"
    # 🔹 Récupérer un utilisateur spécifique
    user_id = 2
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    print(f"🔍 Utilisateur ID={user_id} :", response.json())

    # 🔹 Tester un utilisateur inexistant
    unknown_user_id = 99
    response = requests.get(f"{BASE_URL}/users/{unknown_user_id}")
    print(f"⚠️ Utilisateur ID={unknown_user_id} :", response.json())

    