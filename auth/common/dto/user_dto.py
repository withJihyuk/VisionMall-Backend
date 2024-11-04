from typing import Optional

from pydantic import BaseModel

from order.order_dto import CreateOrderReqeustDto
from review.review_dto import CreateReviewReqeustDto


class UserDto(BaseModel):
    sub: str
    email: str
    name: str
    picture: str


def create_oauth_dto(data: dict) -> UserDto:
    return UserDto(
        sub=data["sub"],
        email=data["email"],
        name=data["given_name"],
        picture=data["picture"],
    )

class UserResponseDto(BaseModel):
    email: str
    name: str
    picture: str
    address: Optional[str] = "등록되지 않았습니다."
    reviews: list[CreateReviewReqeustDto] = []
    order: list[CreateOrderReqeustDto] = []