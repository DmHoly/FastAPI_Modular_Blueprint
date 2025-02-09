from app.api import APIClient

if __name__ == "__main__":
    client = APIClient()
    users = client.get_users()
    print(users)
    user = client.get_user_by_id(1)
    print(user)