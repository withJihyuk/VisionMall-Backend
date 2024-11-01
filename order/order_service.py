from starlette.responses import JSONResponse
from common.db import db
from order.order_dto import CreateOrderReqeustDto


async def get_order_list(user_id: str):
    return await db.orders.find_many(where={"userId": int(user_id)})


async def create_order(request: CreateOrderReqeustDto, user_id: str):
    try:
        await db.orders.create(
            data={
                "count": request.count,
                "status": request.status,
                "userId": int(user_id),
                "optionId": request.optionId,
                "productId": request.productId,
                "zipCode": request.zipCode,
                "address": request.address,
            }
        )
    except Exception:
        return JSONResponse(
            status_code=400,
            content={"message": "요청에 실패했습니다. 요청이 올바른지 확인 해주세요."},
        )
    return JSONResponse(status_code=200, content={"status": "ok"})


# async def cancel_order(order_id: int, user_id: int):
#     order = await db.orders.find_first(where={"id": order_id, "userId": user_id})
#     print(order.status)
#     if order.status == (OrderStatus.CONFIRMED or OrderStatus.PROCESSING or OrderStatus.PENDING):
#         db.orders.update(
#             where={
#                 "id": order_id,
#                 "userId": user_id,
#             },
#             data={
#                 "status": OrderStatus.CANCELED,
#             },
#         )
#         return JSONResponse(status_code=200, content={"status": "ok"})
#     else:
#         return JSONResponse(status_code=400, content={"status": "취소가 불가능합니다."})
#
#
# def return_order(order_id: int, user_id: int):
#     order = db.orders.find_first(
#         where={
#             'orderId': order_id,
#             'userId' :user_id
#         }
#     )
#     if order["status"] == OrderStatus.DELIVERED:
#         db.orders.update(
#             where={
#                 'orderId': order_id,
#             },
#             data={
#                 "status": OrderStatus.RETURNED,
#             }
#         )
#         return JSONResponse(status_code=200, content={"status": "ok"})
#     else:
#         return JSONResponse(status_code=400, content={"status": "반품이 불가능합니다."})
#
#
# def refund_order(order_id: int, user_id: int):
#     order = db.orders.find_first(
#         where={
#             'orderId': order_id,
#             'userId':  user_id
#         }
#     )
#     if order.status == OrderStatus.DELIVERED:
#         db.orders.update(
#             where={
#                 'orderId': order_id,
#             },
#             data={
#                 "status": OrderStatus.REFUNDED,
#             }
#         )
#         return JSONResponse(status_code=200, content={"status": "ok"})
#     else:
#         return JSONResponse(status_code=400, content={"status": "반품이 불가능합니다."})
#
