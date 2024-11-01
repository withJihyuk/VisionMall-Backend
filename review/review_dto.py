from pydantic import BaseModel, Field


class CreateReviewReqeustDto(BaseModel):
    rating: int = Field(..., gt=1, le=5)
    content: str
    orderId: int
    productId: int
