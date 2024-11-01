from fastapi import APIRouter, Depends
import auth.auth_service as auth
from auth.common.dto.refresh_token_dto import RefreshTokenDto
from utils.token_handler import check_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/verify")
async def verify_id_token(code: str):
    value = await auth.verify_id_token(code)
    return value


@router.get("/login")
async def get_login_link():
    return auth.get_login_url()


@router.post("/refresh")
async def get_refresh_token(request: RefreshTokenDto):
    return await auth.get_refreshed_token(request.refresh_token)


@router.get("/info")
async def get_user_info(user_id: str = Depends(check_user)):
    return await auth.get_current_user(user_id)
