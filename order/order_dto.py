from prisma.enums import OrderStatus
from pydantic import BaseModel


class CreateOrderReqeustDto(BaseModel):
    productId: int
    count: int
    optionId: int
    address: str


class GetOrderResponseDto(BaseModel):
    id: int
    productId: int
    count: int
    status: OrderStatus
    optionId: int
    address: str
