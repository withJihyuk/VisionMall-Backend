from pydantic import BaseModel


class RefreshTokenDto(BaseModel):
    refresh_token: str


def create_refresh_token_dto(data: dict) -> RefreshTokenDto:
    return RefreshTokenDto(refresh_token=data["refresh_token"])
