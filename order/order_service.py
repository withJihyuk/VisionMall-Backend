from prisma.enums import OrderStatus
from starlette.responses import JSONResponse
from common.db import db
from order.order_dto import CreateOrderReqeustDto

def get_order_list(user_id: int):
    return db.orders.find_many(
        where={
            'userId': user_id
        }
    )

def create_order(request: CreateOrderReqeustDto, user_id: int):
    db.orders.create(
        data={
            'count': request.count,
            'status': request.status,
            'userId': user_id,
            'productId': request.productId,
            'zipCode': request.zipCode,
            'address': request.address,
        }
    )
    return JSONResponse(status_code=200, content={"status": "ok"})


def cancel_order(order_id: int, user_id: int):
    order = db.orders.find_first(
        where={
            "id": order_id,
            "userId": user_id
        }
    )
    if order.status == (OrderStatus.CONFIRMED or OrderStatus.PROCESSING):
        db.orders.update(
            where={
                "id": order_id,
            },
            data={
              "status": OrderStatus.CANCELED,
            }
        )
        return JSONResponse(status_code=200, content={"status": "ok"})
    else:
        return JSONResponse(status_code=400, content={"status": "취소가 불가능합니다."})


# def return_order(order_id: int):
#     order = db.orders.find_first(
#         where={
#             'orderId': order_id,
#         }
#     )
#     if order.status == OrderStatus.DELIVERED:
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
# def refund_order(order_id: int):
#     order = db.orders.find_first(
#         where={
#             'orderId': order_id,
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