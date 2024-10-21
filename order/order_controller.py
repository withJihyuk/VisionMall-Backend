from typing import List
from fastapi import APIRouter, Depends
import order.order_service as order
from order.order_dto import CreateOrderReqeustDto
from utils.token_handler import check_user

router = APIRouter(prefix="/order", tags=["order"])


@router.get("/order", response_model=List[CreateOrderReqeustDto])
def get_orders(user_id: int = Depends(check_user)):
    return order.get_order_list(user_id)

@router.post("/order")
def create_order(request:CreateOrderReqeustDto, user_id: int = Depends(check_user)):
    return order.create_order(request, user_id)

@router.post("/order/{order_id}")
def cancel_order(order_id: int, user_id: int = Depends(check_user)):
    return order.cancel_order(order_id, user_id)

# 환불, 교환 제작 필요 -> user_id 받기