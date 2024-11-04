from typing import List
from fastapi import APIRouter, Depends
import order.order_service as order
from order.order_dto import CreateOrderReqeustDto, GetOrderResponseDto
from utils.token_handler import check_user

router = APIRouter(prefix="/order", tags=["order"])


@router.get("/order", response_model=List[GetOrderResponseDto])
async def get_orders(user_id: str = Depends(check_user)):
    return await order.get_order_list(user_id)


@router.post("/order")
async def create_order(
    request: CreateOrderReqeustDto, user_id: str = Depends(check_user)
):
    return await order.create_order(request, user_id)


# @router.post("/order/{order_id}")
# async def cancel_order(order_id: int, user_id: str = Depends(check_user)):
#     return await order.cancel_order(order_id, int(user_id))