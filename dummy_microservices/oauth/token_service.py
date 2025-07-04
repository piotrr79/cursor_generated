from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Optional
from .token import Token
from .database import Database
import os

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

class TokenService:
    """
    Service for creating and verifying JWT access tokens.
    """
    def __init__(self, db: Database):
        """
        Initialize with a Database instance.
        """
        self.token_model = Token(db)

    def create_token(self, user_id: int) -> str:
        """
        Create a new JWT access token for a user and store it in the database.
        Returns the access token string.
        """
        expires_at = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = {"sub": str(user_id), "exp": expires_at}
        access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        self.token_model.create(user_id, access_token, expires_at)
        return access_token

    def verify_token(self, access_token: str) -> Optional[int]:
        """
        Verify a JWT access token and check its validity in the database.
        Returns the user ID if valid, None otherwise.
        """
        try:
            payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = int(payload.get("sub"))
            if not self.token_model.is_valid(access_token):
                return None
            return user_id
        except JWTError:
            return None 