from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Optional
from .models import Database, User, Token
import os

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

class UserService:
    def __init__(self, db: Database):
        self.user_model = User(db)
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def register(self, username: str, password: str) -> bool:
        hashed = self.pwd_context.hash(password)
        return self.user_model.create(username, hashed)

    def authenticate(self, username: str, password: str) -> Optional[int]:
        user = self.user_model.get(username)
        if not user:
            return None
        if not self.pwd_context.verify(password, user[2]):
            return None
        return user[0]  # user_id

class TokenService:
    def __init__(self, db: Database):
        self.token_model = Token(db)

    def create_token(self, user_id: int) -> str:
        expires_at = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = {"sub": str(user_id), "exp": expires_at}
        access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        self.token_model.create(user_id, access_token, expires_at)
        return access_token

    def verify_token(self, access_token: str) -> Optional[int]:
        try:
            payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = int(payload.get("sub"))
            if not self.token_model.is_valid(access_token):
                return None
            return user_id
        except JWTError:
            return None 