from fastapi import APIRouter, Depends
import auth.auth_service as auth
from auth.common.dto.id_token_dto import IdTokenDto
from auth.common.dto.refresh_token_dto import RefreshTokenDto
from utils.token_handler import check_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token")
async def verify_by_token(id_token: IdTokenDto):
    return await auth.verify_by_token(id_token.token)


@router.post("/refresh")
async def get_refresh_token(request: RefreshTokenDto):
    return await auth.get_refreshed_token(request.refresh_token)


@router.get("/info")
async def get_user_info(user_id: str = Depends(check_user)):
    return await auth.get_current_user(user_id)
