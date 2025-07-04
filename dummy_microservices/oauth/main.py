from fastapi import FastAPI, HTTPException, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from .database import Database
from .user_service import UserService
from .token_service import TokenService

class OAuthApp:
    def __init__(self):
        self.app = FastAPI()
        self.db = Database()
        self.user_service = UserService(self.db)
        self.token_service = TokenService(self.db)
        self._add_routes()

    def _add_routes(self):
        @self.app.post("/register")
        def register(user: UserCreate):
            if self.user_service.register(user.username, user.password):
                return {"msg": "User registered"}
            raise HTTPException(status_code=400, detail="Username already registered")

        @self.app.post("/token")
        def login(form_data: OAuth2PasswordRequestForm = Depends()):
            user_id = self.user_service.authenticate(form_data.username, form_data.password)
            if not user_id:
                raise HTTPException(status_code=401, detail="Incorrect username or password")
            access_token = self.token_service.create_token(user_id)
            return {"access_token": access_token, "token_type": "bearer"}

        @self.app.post("/verify")
        def verify(token: str = Form(...)):
            user_id = self.token_service.verify_token(token)
            if not user_id:
                raise HTTPException(status_code=401, detail="Invalid token")
            return {"user_id": user_id}

class UserCreate(BaseModel):
    username: str
    password: str

oauth_app = OAuthApp()
app = oauth_app.app 