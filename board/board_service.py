from common.db import db

async def create_post(title: str, content: str):
    return await db.board.create(
        data={
            'title': title,
            'content': content,
        }
    )


async def get_post(post_id: int):
    return await db.board.find_unique(
        where={'id': post_id}
    )


async def get_all_posts():
    return await db.board.find_many()


async def update_post(post_id: int, title: str, content: str):
    return await db.board.update(
        where={'id': post_id},
        data={
            'title': title,
            'content': content,
        }
    )


async def delete_post(post_id: int):
    return await db.board.delete(
        where={'id': post_id}
    )