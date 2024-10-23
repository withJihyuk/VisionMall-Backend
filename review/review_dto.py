from pydantic import BaseModel


class CreateReviewReqeustDto(BaseModel):
    rating: int
    content: str
    orderId: int
    productId: int
