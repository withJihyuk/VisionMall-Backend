from starlette.responses import JSONResponse
from common.db import db
from order.order_dto import CreateOrderReqeustDto


async def create_order(request: CreateOrderReqeustDto):
    await db.orders.create(
        data={
            'count': request.count,
            'status': request.status,
            'userId': request.userId,
            'productId': request.productId,
            'zipCode': request.zipCode,
            'address': request.address,
        }
    )
    return JSONResponse(status_code=200, content={"status": "ok"})


# async def update_order():
#     await db.orders.update(
#         where={
#         }
#     )