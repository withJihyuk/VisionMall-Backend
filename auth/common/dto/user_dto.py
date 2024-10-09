from pydantic import BaseModel


class UserDto(BaseModel):
    sub: str
    email: str
    name: str
    picture: str


def create_oauth_dto(data: dict) -> UserDto:
    return UserDto(
        sub=data["sub"],
        email=data["email"],
        name=data["given_name"],
        picture=data["picture"],
    )
