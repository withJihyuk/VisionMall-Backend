import os
from typing import Union
from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt
from common.exception import unauthorized

security = HTTPBearer()


class TokenHandler:
    secret = os.environ.get("SECRET_KEY")
    algorithm = os.environ.get("ALGORITHM")
    access_expires = timedelta(days=5)
    refresh_expires = timedelta(days=14)

    def encode_token(self, sub: str, expires: timedelta):
        payload = {
            "exp": datetime.now() + expires,
            "iat": datetime.now(),
            "sub": sub,
        }
        return jwt.encode(payload, self.secret, self.algorithm)

    def decode_token(self, token: str):
        payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
        print(payload)
        return payload["sub"]

    def create_access_token(self, user_id: str):
        sub = user_id
        return self.encode_token(sub, self.access_expires)

    def create_refresh_token(self, user_id: str):
        sub = f"{user_id}.refresh"
        token = self.encode_token(sub, self.refresh_expires)
        return token


def check_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    access_token = credentials.credentials
    sub = TokenHandler().decode_token(access_token)
    return sub
