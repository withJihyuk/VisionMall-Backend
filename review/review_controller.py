from typing import List
from fastapi import APIRouter
import review.review_service as review
from review.ReviewDto import CreateReviewReqeustDto

router = APIRouter(prefix="/review", tags=["review"])


@router.get("/reviews/{product_id}", response_model=List[CreateReviewReqeustDto])
async def get_reviews_by_product_id(product_id: int):
    return await review.get_review(product_id)

@router.post("/reviews/{product_id}")
async def post_reviews_by_product_id(request:CreateReviewReqeustDto):
    return await review.create_review(request)

@router.delete("/reviews/{review_id}")
async def delete_reviews_by_id(review_id: int):
    return await review.delete_review(review_id)