

if __name__ == "__main__":

    from app.backend import get_all_users, get_user_by_id

    # 🔹 Récupérer tous les utilisateurs
    users = get_all_users()
    print("📜 Liste des utilisateurs :", users)

    # 🔹 Récupérer un utilisateur spécifique
    user = get_user_by_id(2)
    print("🔍 Utilisateur ID=2 :", user)

    # 🔹 Tester un utilisateur inexistant
    unknown_user = get_user_by_id(99)
    print("⚠️ Utilisateur inconnu :", unknown_user)

