from pydantic import BaseModel


class IdTokenDto(BaseModel):
    token: str