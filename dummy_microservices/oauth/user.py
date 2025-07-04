from typing import Optional
from .database import Database

class User:
    def __init__(self, db: Database):
        self.db = db

    def create(self, username: str, password: str) -> bool:
        c = self.db.get_cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.db.conn.commit()
            return True
        except Exception:
            return False

    def get(self, username: str) -> Optional[object]:
        c = self.db.get_cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        return c.fetchone()

    def get_by_id(self, user_id: int) -> Optional[object]:
        c = self.db.get_cursor()
        c.execute("SELECT * FROM users WHERE id=?", (user_id,))
        return c.fetchone() 