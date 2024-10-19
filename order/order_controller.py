from typing import List
from fastapi import APIRouter, Depends, HTTPException
import review.review_service as review
from order.order_dto import CreateOrderReqeustDto
from review.review_dto import CreateReviewReqeustDto
from utils.token_handler import check_user

router = APIRouter(prefix="/order", tags=["order"])


# @router.get("/order/{order_id}", response_model=List[CreateOrderReqeustDto])
# async def get_order_info_by_order_id(order_id: int):
#     result = await review.get_review(order_id)
#     if not result:
#         raise HTTPException(status_code=404, detail="상품을 찾을 수 없거나 리뷰가 아직 없어요.")
#     return result
#
# @router.post("/reviews/{product_id}")
# async def post_reviews_by_product_id(request:CreateReviewReqeustDto, user_id: int = Depends(check_user)):
#     return await review.create_review(request, user_id)
#
# @router.delete("/reviews/{review_id}")
# async def delete_reviews_by_id(review_id: int, user_id: int = Depends(check_user)):
#     return await review.delete_review(review_id, user_id)