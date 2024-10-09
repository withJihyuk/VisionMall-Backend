from fastapi import APIRouter, Depends
import auth.auth_service as auth
from auth.auth_service import get_current_user
from auth.common.dto.refresh_token_dto import RefreshTokenDto
from auth.common.dto.user_dto import UserDto

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


@router.get("/user")
async def user_info(user: UserDto = Depends(get_current_user)):
    return user
