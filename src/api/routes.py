# TODO: maybe mv to routes/users.py
from fastapi import APIRouter, Depends
from schemas.user import UserCreate, UserResponse
from services.user_service import create_user
from db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/users/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)
