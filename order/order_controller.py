from typing import List
from fastapi import APIRouter, Depends
import order.order_service as order
from order.order_dto import CreateOrderReqeustDto
from utils.token_handler import check_user

router = APIRouter(prefix="/order", tags=["order"])


@router.get("/order")
async def get_orders(user_id: str = Depends(check_user)):
    return await order.get_order_list(int(user_id))


@router.post("/order")
async def create_order(request: CreateOrderReqeustDto, user_id: str = Depends(check_user)):
    return await order.create_order(request, int(user_id))


# @router.post("/order/{order_id}")
# async def cancel_order(order_id: int, user_id: str = Depends(check_user)):
#     return await order.cancel_order(order_id, int(user_id))


# 환불, 교환 제작 필요 -> user_id 받기
