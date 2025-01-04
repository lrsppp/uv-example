from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from db.base import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
