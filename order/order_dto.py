from prisma.enums import OrderStatus
from pydantic import BaseModel

class CreateOrderReqeustDto(BaseModel):
    productId: int
    count: int
    status: OrderStatus = OrderStatus.PENDING
    userId: int
    zipCode: str
    address: str

def create_order_dto(data: dict) -> CreateOrderReqeustDto:
    return CreateOrderReqeustDto(
        productId=data['productId'],
        count=data['count'],
        status=data['status'],
        userId=data['userId'],
        zipCode=data['zipCode'],
        address=data['address'],
    )

def get_order_dto(data: dict) -> CreateOrderReqeustDto:
    return CreateOrderReqeustDto(
        productId=data['productId'],
        count=data['count'],
        status=data['status'],
    )