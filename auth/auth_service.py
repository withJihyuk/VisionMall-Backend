import os
from google.oauth2 import id_token
from google.auth.transport import requests
from google_auth_oauthlib.flow import InstalledAppFlow
from starlette.responses import JSONResponse

from common.exception import unauthorized
from common.db import db
from utils.token_handler import TokenHandler
from auth.dto.user_dto import UserDto, create_oauth_dto

client_config = {
    "installed": {
        "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
        "client_secret": os.environ.get("GOOGLE_CLIENT_SECRET"),
        "redirect_uri": "urn:ietf:wg:oauth:2.0:oob",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "grant_type": "authorization_code",
    }
}
SCOPES = [
    "openid",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]
flow = InstalledAppFlow.from_client_config(client_config, scopes=SCOPES)


def get_login_url():
    flow.redirect_uri = os.environ.get("GOOGLE_REDIRECT_URL")
    auth_url, _ = flow.authorization_url(prompt="consent")
    return auth_url


def verify_id_token(auth_code: str):
    try:
        flow.fetch_token(code=auth_code)
        credentials = flow.credentials
        token_val = id_token.verify_oauth2_token(
            credentials.id_token,
            requests.Request(),
            os.environ.get("GOOGLE_CLIENT_ID"),
            clock_skew_in_seconds=0,
        )
        return register_or_login(create_oauth_dto(token_val))
    except Exception:
        raise unauthorized


async def register_or_login(user_dto: UserDto):
    token_handler = TokenHandler()

    await db.user.upsert(
        where={
            "email": user_dto.email,
        },
        data={"create": dict(user_dto), "update": dict(user_dto)},
    )

    access_token = token_handler.create_access_token(user_dto.sub)
    refresh_token = token_handler.create_refresh_token(user_dto.sub)

    await db.refreshtoken.create(
        data={"id": f"{user_dto.sub}.refresh", "token": refresh_token}
    )

    return JSONResponse(
        status_code=200,
        content={"access_token": access_token, "refresh_token": refresh_token},
    )


async def get_refreshed_token(refresh_token: str):
    tokenHandler = TokenHandler()
    sub = tokenHandler.decode_token(refresh_token)

    result = await db.refreshtoken.find_first(
        where={
            "token": refresh_token,
            "id": sub,
        }
    )

    user_id = result.id.replace(".refresh", "")
    access_token = tokenHandler.create_access_token(user_id)

    return JSONResponse(
        status_code=200,
        content={"access_token": access_token, "refresh_token": refresh_token},
    )
