from fastapi import FastAPI
from auth import auth_controller as auth
from product import product_controller as board

from common.db import connect_db, disconnect_db
import uvicorn
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    print("DB 연결 성공")

    yield
    await disconnect_db()
    print("DB 연결 종료 성공")


app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
app.include_router(board.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
