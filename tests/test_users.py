from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import Session

from db.base import Base
from db.session import get_session
from main import app
from models.user import (  # noqa ... is this necessary to add 'User' table to 'Base'?
    User,
)

client = TestClient(app)


def test_register_user():
    # https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/#testing-database
    # testing with in-memotry test database
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    with Session(engine) as session:

        def get_session_override():
            return session

        app.dependency_overrides[get_session] = get_session_override

        user_data = {
            "email": "testuser@example.com",
            "password": "testpassword",  # pragma: allowlist secret
        }
        response = client.post("/users/register_user", json=user_data)
        app.dependency_overrides.clear()

        assert response.status_code == 200
        user = response.json()
        assert "id" in user
        assert user["email"] == user_data["email"]

        assert "hashed_password" not in user
