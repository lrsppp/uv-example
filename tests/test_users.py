from fastapi.testclient import TestClient
from main import app
from db.base import SessionLocal
from models.user import User

client = TestClient(app)


def delete_user_by_email(email: str):
    session = SessionLocal()
    user = session.query(User).filter(User.email == email).first()
    if user:
        session.delete(user)
        session.commit()


def test_register_user():
    user_data = {"email": "testuser@example.com", "password": "testpassword"}
    response = client.post("/users/", json=user_data)

    assert response.status_code == 200
    user = response.json()
    assert "id" in user
    assert user["email"] == user_data["email"]

    assert "hashed_password" not in user
    delete_user_by_email(email="testuser@example.com")  # cleanup
