from starlette.responses import JSONResponse
from common.db import db
from review.ReviewDto import CreateReviewReqeustDto


async def create_review(request: CreateReviewReqeustDto):
    await db.products.create(data={
        "rating": request.rating,
        "content": request.content,
        "userId": request.userId,
        "productId": request.productId
    })
    return JSONResponse(status_code=200, content={"status": "ok"})


async def get_review(product_id: int):
    return await db.products.find_many(
        {"productId": product_id}
    )


async def delete_review(review_id: int):
    await db.products.delete(
        data={
            "id": review_id,
        }
    )
    return JSONResponse(status_code=200, content={"status": "ok"})