from pydantic import BaseModel


class CreateReviewReqeustDto(BaseModel):
    rating: int
    content: str
    userId: int
    productId: int

def create_review_dto(data: dict) -> CreateReviewReqeustDto:
    return CreateReviewReqeustDto(
        rating=data['rating'],
        content=data['content'],
        userId=data['userId'],
        productId=data['productId']
    )

def get_review_dto(data: dict) -> CreateReviewReqeustDto:
    return CreateReviewReqeustDto(
        rating=data['rating'],
        content=data['content'],
        userId=data['userId']
    )