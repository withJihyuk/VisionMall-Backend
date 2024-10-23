from typing import List
from fastapi import APIRouter, Depends, HTTPException
import review.review_service as review
from review.review_dto import CreateReviewReqeustDto
from utils.token_handler import check_user

router = APIRouter(prefix="/review", tags=["review"])


@router.get("/reviews/{product_id}", response_model=List[CreateReviewReqeustDto])
async def get_reviews_by_product_id(product_id: int):
    result = await review.get_review(product_id)
    if not result:
        raise HTTPException(
            status_code=404, detail="상품을 찾을 수 없거나 리뷰가 아직 없어요."
        )
    return result


@router.post("/reviews/{product_id}")
async def post_reviews_by_product_id(
    request: CreateReviewReqeustDto, user_id: str = Depends(check_user)
):
    return await review.create_review(request, int(user_id))


@router.delete("/reviews/{review_id}")
async def delete_reviews_by_id(review_id: int, user_id: str = Depends(check_user)):
    return await review.delete_review(review_id, int(user_id))
