from fastapi import APIRouter
import auth.auth_service as auth

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/verify")
async def verify_id_token(code: str):
    value = await auth.verify_id_token(code)
    return value


@router.get("/login")
async def get_login_link():
    return auth.get_login_url()


@router.put("/refresh")
async def get_refresh_token(refresh_token: str):
    return await auth.get_refreshed_token(refresh_token)
