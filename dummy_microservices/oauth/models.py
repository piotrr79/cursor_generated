import sqlite3
from datetime import datetime
from typing import Optional

DB_PATH = "users.db"

class Database:
    def __init__(self, db_path=DB_PATH):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        c = self.conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """)
        c.execute("""
        CREATE TABLE IF NOT EXISTS tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            access_token TEXT NOT NULL,
            expires_at TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """)
        self.conn.commit()

    def get_cursor(self):
        return self.conn.cursor()

class User:
    def __init__(self, db: Database):
        self.db = db

    def create(self, username: str, password: str) -> bool:
        c = self.db.get_cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.db.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get(self, username: str) -> Optional[sqlite3.Row]:
        c = self.db.get_cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        return c.fetchone()

    def get_by_id(self, user_id: int) -> Optional[sqlite3.Row]:
        c = self.db.get_cursor()
        c.execute("SELECT * FROM users WHERE id=?", (user_id,))
        return c.fetchone()

class Token:
    def __init__(self, db: Database):
        self.db = db

    def create(self, user_id: int, access_token: str, expires_at: datetime):
        c = self.db.get_cursor()
        c.execute(
            "INSERT INTO tokens (user_id, access_token, expires_at) VALUES (?, ?, ?)",
            (user_id, access_token, expires_at.isoformat())
        )
        self.db.conn.commit()

    def get(self, access_token: str) -> Optional[sqlite3.Row]:
        c = self.db.get_cursor()
        c.execute("SELECT * FROM tokens WHERE access_token=?", (access_token,))
        return c.fetchone()

    def is_valid(self, access_token: str) -> bool:
        token = self.get(access_token)
        if not token:
            return False
        expires_at = datetime.fromisoformat(token[3])
        return datetime.utcnow() < expires_at 