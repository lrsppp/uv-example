from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from pathlib import Path


# sqlite db for testing
db_file_path = Path(__file__).resolve().parent.parent.parent / "data.db"
DATABASE_URL = f"sqlite:///{db_file_path}"

Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


def init_db():
    Base.metadata.create_all(bind=engine)
