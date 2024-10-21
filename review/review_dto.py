from pydantic import BaseModel


class CreateReviewReqeustDto(BaseModel):
    rating: int
    content: str
    productId: int