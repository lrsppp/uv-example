# NOTE: mv to routes/users.py
from fastapi import APIRouter, Depends
from schemas.user import UserCreate, UserResponse
from services.user_service import create_user
from db.session import get_session
from sqlalchemy.orm import Session

user_router = APIRouter(prefix="/users")


@user_router.post("/register_user", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_session)):
    return create_user(user, db)
