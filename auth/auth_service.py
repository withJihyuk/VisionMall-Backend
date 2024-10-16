from google.oauth2 import id_token
from google.auth.transport import requests
from starlette.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends
from common.exception import unauthorized
from common.db import db
from utils.token_handler import TokenHandler
from auth.common.dto.user_dto import UserDto, create_oauth_dto
from auth.common.config import flow, client_id, redirect_url

security = HTTPBearer()


def get_login_url():
    flow.redirect_uri = redirect_url
    auth_url, _ = flow.authorization_url(prompt="consent")
    return auth_url


def verify_id_token(auth_code: str):
    try:
        flow.fetch_token(code=auth_code)
        credentials = flow.credentials
        token_val = id_token.verify_oauth2_token(
            credentials.id_token,
            requests.Request(),
            client_id,
            clock_skew_in_seconds=0,
        )
        return register_or_login(create_oauth_dto(token_val))
    except Exception:
        raise unauthorized


async def register_or_login(user_dto: UserDto):
    token_handler = TokenHandler()
    await db.users.upsert(
        where={
            "email": user_dto.email,
        },
        data={"create": dict(user_dto), "update": dict(user_dto)},
    )
    access_token = token_handler.create_access_token(user_dto.sub)
    refresh_token = token_handler.create_refresh_token(user_dto.sub)
    await db.refreshtokens.upsert(
        where={"id": f"{user_dto.sub}.refresh"},
        data={
            "create": {"id": f"{user_dto.sub}.refresh", "token": refresh_token},
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
    access_token = tokenHandler.create_access_token(result.id)
    return JSONResponse(
        status_code=200,
        content={"access_token": access_token, "refresh_token": refresh_token},
    )


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    access_token = credentials.credentials
    sub = TokenHandler().decode_token(access_token)
    result = await db.users.find_unique(where={"sub": sub})
    return result


async def check_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    access_token = credentials.credentials
    sub = TokenHandler().decode_token(access_token)
    return sub
