from google.oauth2 import id_token
from google.auth.transport import requests
from starlette.responses import JSONResponse
from fastapi.security import HTTPBearer
from common.exception import unauthorized
from common.db import db
from utils.token_handler import TokenHandler
from auth.common.dto.user_dto import UserDto, create_oauth_dto
from auth.common.config import client_id

security = HTTPBearer()

def verify_by_token(token: str):
    try:
        token_val = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            client_id,
            clock_skew_in_seconds=0,
        )
        return register_or_login(create_oauth_dto(token_val))
    except Exception:
        raise unauthorized


async def register_or_login(user_dto: UserDto):
    token_handler = TokenHandler()
    result = await db.users.upsert(
        where={
            "email": user_dto.email,
        },
        data={"create": dict(user_dto), "update": dict(user_dto)},
    )
    access_token = token_handler.create_access_token(str(result.id))
    refresh_token = token_handler.create_refresh_token(str(result.id))
    await db.refreshtokens.upsert(
        where={"id": f"{result.id}.refresh"},
        data={
            "create": {"id": f"{result.id}.refresh", "token": refresh_token},
            "update": {"token": refresh_token},
        },
    )
    return JSONResponse(
        status_code=200,
        content={"access_token": access_token, "refresh_token": refresh_token},
    )


async def get_refreshed_token(refresh_token: str):
    tokenHandler = TokenHandler()
    sub = tokenHandler.decode_token(refresh_token)
    result = await db.refreshtokens.find_first(
        where={
            "token": refresh_token,
            "id": sub,
        }
    )
    access_token = tokenHandler.create_access_token((result.id.replace(".refresh", "")))
    return JSONResponse(
        status_code=200,
        content={"access_token": access_token, "refresh_token": refresh_token},
    )


async def get_current_user(user_id: str):
    result = await db.users.find_unique(where={"id": int(user_id)})
    return result
