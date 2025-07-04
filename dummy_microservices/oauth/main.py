from fastapi import FastAPI, HTTPException, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from .models import Database
from .services import UserService, TokenService

app = FastAPI()
db = Database()
user_service = UserService(db)
token_service = TokenService(db)

class UserCreate(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(user: UserCreate):
    if user_service.register(user.username, user.password):
        return {"msg": "User registered"}
    raise HTTPException(status_code=400, detail="Username already registered")

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_id = user_service.authenticate(form_data.username, form_data.password)
    if not user_id:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = token_service.create_token(user_id)
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/verify")
def verify(token: str = Form(...)):
    user_id = token_service.verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"user_id": user_id} 