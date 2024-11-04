from prisma.enums import OrderStatus
from pydantic import BaseModel


class CreateOrderReqeustDto(BaseModel):
    productId: int
    count: int
    status: OrderStatus = OrderStatus.PENDING
    optionId: int
    address: str


class GetOrderReqeustDto(BaseModel):
    productId: int
    count: int
    status: OrderStatus = OrderStatus.PENDING


def order_to_response_body(data: dict) -> GetOrderReqeustDto:
    return GetOrderReqeustDto(
        productId=data["productId"],
        count=data["count"],
        status=data["status"],
    )
