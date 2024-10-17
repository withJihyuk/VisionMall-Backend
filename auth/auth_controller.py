from fastapi import APIRouter
import auth.auth_service as auth
from auth.common.dto.refresh_token_dto import RefreshTokenDto

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

# TODO - 유저 정보 엔드포인트 제작하기