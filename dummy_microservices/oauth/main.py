from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt, JWTError
import sqlite3
import os
from datetime import datetime, timedelta

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
DB_PATH = "users.db"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()

# DB setup
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")
conn.commit()

class UserCreate(BaseModel):
    username: str
    password: str

def get_user(username: str):
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    return c.fetchone()

def create_user(username: str, password: str):
    hashed = pwd_context.hash(password)
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/register")
def register(user: UserCreate):
    if get_user(user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    if create_user(user.username, user.password):
        return {"msg": "User registered"}
    raise HTTPException(status_code=500, detail="Registration failed")

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if not user or not verify_password(form_data.password, user[2]):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token({"sub": user[1]})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/verify")
def verify(token: str = Depends(lambda: None)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username or not get_user(username):
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"username": username}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token") 