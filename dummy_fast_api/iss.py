from fastapi import APIRouter, HTTPException
from iss_logic import ISSService

class ISSRouter:
    def __init__(self):
        self.iss_service = ISSService()
        self.router = APIRouter()
        self.router.add_api_route("/iss", self.get_iss_position, methods=["GET"])

    def get_iss_position(self):
        """
        Fetch the current ISS position and return latitude, longitude, and country.
        """
        try:
            return self.iss_service.get_iss_position_with_country()
        except Exception:
            raise HTTPException(status_code=502, detail="Failed to fetch ISS position")

def get_router():
    return ISSRouter().router 