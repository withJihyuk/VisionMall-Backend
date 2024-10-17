from typing import List
from fastapi import APIRouter, Depends

import review.review_service as review
from review.ReviewDto import CreateReviewReqeustDto
from utils.token_handler import check_user

router = APIRouter(prefix="/review", tags=["review"])


@router.get("/reviews/{product_id}", response_model=List[CreateReviewReqeustDto])
async def get_reviews_by_product_id(product_id: int):
    return await review.get_review(product_id)

@router.post("/reviews/{product_id}")
async def post_reviews_by_product_id(request:CreateReviewReqeustDto, user_id: int = Depends(check_user)):
    return await review.create_review(request, user_id)

@router.delete("/reviews/{review_id}")
async def delete_reviews_by_id(review_id: int, user_id: int = Depends(check_user)):
    return await review.delete_review(review_id, user_id)