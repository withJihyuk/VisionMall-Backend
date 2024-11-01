from starlette.responses import JSONResponse
from common.db import db
from review.review_dto import CreateReviewReqeustDto


async def create_review(request: CreateReviewReqeustDto, user_id: int):
    try:
        await db.reviews.create(
            data={
                "rating": request.rating,
                "content": request.content,
                "optionId": request.optionId,
                "productId": request.productId,
                "userId": user_id,
            }
        )
        return JSONResponse(status_code=200, content={"status": "ok"})
    except Exception as e:
        print(e)
        return JSONResponse(status_code=400, content={"message": "잘못된 요청입니다."})


async def get_review(product_id: int):
    result = await db.reviews.find_many(where={"OR": [{"productId": product_id}]})
    return result


async def delete_review(review_id: int, user_id: int):
    try:
        await db.reviews.delete(where={"id": review_id, "userId": user_id})
    except Exception:
        return JSONResponse(status_code=400, content={"message": "잘못된 요청입니다."})
    return JSONResponse(status_code=200, content={"status": "ok"})
