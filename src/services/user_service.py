from models.user import User
from schemas.user import UserCreate
from sqlalchemy.orm import Session
from core.security import get_password_hash


def create_user(user: UserCreate, db: Session):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise ValueError("User with this email already exists")

    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
