from db.base import init_db
from models.user import User  # noqa

import shutil

if __name__ == "__main__":
    init_db()
    shutil.move("data.db", "../../data.db")
