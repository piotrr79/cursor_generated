from datetime import datetime
from typing import Optional
from .database import Database

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

    def get(self, access_token: str) -> Optional[object]:
        c = self.db.get_cursor()
        c.execute("SELECT * FROM tokens WHERE access_token=?", (access_token,))
        return c.fetchone()

    def is_valid(self, access_token: str) -> bool:
        token = self.get(access_token)
        if not token:
            return False
        expires_at = datetime.fromisoformat(token[3])
        return datetime.utcnow() < expires_at 