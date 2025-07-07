import requests
import logging
from typing import Optional

logger = logging.getLogger("auth_service")

class AuthService:
    """
    Service for validating JWT tokens with the Django auth microservice.
    """
    def __init__(self, auth_url: str = "http://localhost:8001/api/") -> None:
        self.auth_url = auth_url

    def verify_token(self, token: str) -> Optional[dict]:
        """
        Verify a JWT token with the Django auth service.
        Returns user info if valid, None otherwise.
        Logs validation attempts, results, and errors.
        """
        try:
            logger.info("Verifying JWT token with auth service at %s", self.auth_url)
            resp = requests.post(f"{self.auth_url}token/verify/", data={"token": token})
            if resp.status_code == 200:
                logger.info("Token valid. User info: %s", resp.json())
                return resp.json()
            logger.warning("Token invalid or expired. Status code: %s", resp.status_code)
            return None
        except Exception as e:
            logger.error("Error verifying token: %s", e)
            return None 