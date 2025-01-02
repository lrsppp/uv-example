from fastapi import FastAPI
from api.routes import router
from db.base import init_db
from contextlib import asynccontextmanager
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
