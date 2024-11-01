from common.db import db


async def get_product(products_id: int):
    return await db.products.find_unique(
        where={"id": products_id}, include={"option": True}
    )


async def get_all_product():
    return await db.products.find_many()
