from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from auth import auth_controller as auth
from product import product_controller as board
from review import review_controller as review
from analyze import analyze_controller as analyze
from order import order_controller as order
from common.db import connect_db, disconnect_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    print("DB 연결 성공")

    yield
    await disconnect_db()
    print("DB 연결 종료 성공")


app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
app.include_router(review.router)
app.include_router(board.router)
app.include_router(analyze.router)
app.include_router(order.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
