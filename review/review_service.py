from starlette.responses import JSONResponse
from common.db import db
from review.ReviewDto import CreateReviewReqeustDto


async def create_review(request: CreateReviewReqeustDto, user_id: int):
    check_user_bought = db.orders.find_many(
        where={'OR': [
            {"userId": user_id},
            {"productId": request.product_id}
        ]}
    )
    if not check_user_bought:
        return JSONResponse(status_code=400, content="구매한 상품에만 리뷰를 작성 할 수 있어요.")
    await db.products.create(data={
        "rating": request.rating,
        "content": request.content,
        "userId": user_id,
        "productId": request.productId
    })
    return JSONResponse(status_code=200, content={"status": "ok"})


async def get_review(product_id: int):
    result = await db.products.find_many(where = {'OR': [{"id": product_id}]})
    return result


async def delete_review(review_id: int, user_id: int):
    await db.products.delete(
        data={
            "id": review_id,
            "userId": user_id
        }
    )
    return JSONResponse(status_code=200, content={"status": "ok"})