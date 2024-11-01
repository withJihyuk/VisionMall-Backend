from pydantic import BaseModel, Field


class CreateReviewReqeustDto(BaseModel):
    rating:  int = Field(..., gt=0, le=6)
    content: str
    productId: int
    optionId:int