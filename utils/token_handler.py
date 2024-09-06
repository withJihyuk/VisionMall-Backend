import os
from typing import Union
from datetime import datetime, timedelta
from jose import jwt
from common.exception import unauthorized


class TokenHandler:
    secret = os.environ.get("SECRET_KEY")
    algorithm = os.environ.get("ALGORITHM")
    access_expires = timedelta(hours=2)
    refresh_expires = timedelta(days=14)

    def encode_token(self, sub: Union[int, str], expires: timedelta):
        payload = {
            "exp": datetime.now() + expires,
            "iat": datetime.now(),
            "sub": sub,
        }
        return jwt.encode(payload, self.secret, self.algorithm)

    def decode_token(self, token: str):
        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            return payload["sub"]
        except Exception:
            raise unauthorized

    def create_access_token(self, user_id: str):
        sub = user_id
        return self.encode_token(sub, self.access_expires)

    def create_refresh_token(self, user_id: str):
        sub = f"{user_id}.refresh"
        return self.encode_token(sub, self.refresh_expires)
