from passlib.context import CryptContext
from .user import User
from .database import Database
from typing import Optional

class UserService:
    """
    Service for user registration and authentication.
    """
    def __init__(self, db: Database):
        """
        Initialize with a Database instance.
        """
        self.user_model = User(db)
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def register(self, username: str, password: str) -> bool:
        """
        Register a new user with a hashed password.
        Returns True if successful, False otherwise.
        """
        hashed = self.pwd_context.hash(password)
        return self.user_model.create(username, hashed)

    def authenticate(self, username: str, password: str) -> Optional[int]:
        """
        Authenticate a user by username and password.
        Returns the user ID if successful, None otherwise.
        """
        user = self.user_model.get(username)
        if not user:
            return None
        if not self.pwd_context.verify(password, user[2]):
            return None
        return user[0]  # user_id 