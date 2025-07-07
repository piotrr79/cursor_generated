from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth import AuthService
from app.iss_service import ISSService
from typing import Any
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s"
)

class BackendApp:
    """
    Main FastAPI backend app for ISS position API with JWT authentication.
    Sets up global logging configuration.
    """
    def __init__(self) -> None:
        self.app: FastAPI = FastAPI()
        self.auth_service: AuthService = AuthService()
        self.iss_service: ISSService = ISSService()
        self.security = HTTPBearer()
        self._add_routes()

    def _add_routes(self) -> None:
        @self.app.get("/iss")
        def get_iss_position(credentials: HTTPAuthorizationCredentials = Depends(self.security)) -> Any:
            """
            Get the current ISS position and location (country/sea/ocean).
            Requires a valid JWT token.
            Logs incoming requests and errors.
            """
            logging.info("Received request for /iss endpoint")
            token = credentials.credentials
            user = self.auth_service.verify_token(token)
            if not user:
                logging.warning("Unauthorized access attempt to /iss endpoint")
                raise HTTPException(status_code=401, detail="Invalid or expired token")
            try:
                result = self.iss_service.get_iss_position_with_location()
                logging.info("/iss endpoint response: %s", result)
                return result
            except Exception as e:
                logging.error("Internal server error at /iss endpoint: %s", e)
                raise HTTPException(status_code=500, detail="Internal server error")

backend_app = BackendApp()
app = backend_app.app 