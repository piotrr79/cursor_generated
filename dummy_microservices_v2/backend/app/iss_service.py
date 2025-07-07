import requests
import logging
from typing import Dict

logger = logging.getLogger("iss_service")

class ISSService:
    """
    Service for fetching ISS position and resolving country or sea/ocean.
    """
    ISS_API_URL = "http://api.open-notify.org/iss-now.json"
    NOMINATIM_URL = "https://nominatim.openstreetmap.org/reverse"
    USER_AGENT = {"User-Agent": "iss-fastapi-app"}

    def get_iss_position(self) -> Dict[str, str]:
        """
        Fetch the current ISS position (latitude, longitude).
        Logs the API call and result.
        """
        logger.info("Fetching ISS position from %s", self.ISS_API_URL)
        response = requests.get(self.ISS_API_URL, timeout=5)
        response.raise_for_status()
        iss_data = response.json()
        lat = iss_data["iss_position"]["latitude"]
        lon = iss_data["iss_position"]["longitude"]
        logger.info("ISS position: latitude=%s, longitude=%s", lat, lon)
        return {"latitude": lat, "longitude": lon}

    def get_location_info(self, lat: str, lon: str) -> Dict[str, str]:
        """
        Given latitude and longitude, return the country or sea/ocean name.
        Logs the API call, result, and errors.
        """
        params = {
            "format": "json",
            "lat": lat,
            "lon": lon,
            "zoom": 10,
            "addressdetails": 1
        }
        try:
            logger.info("Resolving location for lat=%s, lon=%s", lat, lon)
            response = requests.get(self.NOMINATIM_URL, headers=self.USER_AGENT, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            address = data.get("address", {})
            if "country" in address:
                logger.info("Location resolved: country=%s", address["country"])
                return {"type": "country", "name": address["country"]}
            for key in ["sea", "ocean", "water", "river", "lake"]:
                if key in address:
                    logger.info("Location resolved: sea=%s", address[key])
                    return {"type": "sea", "name": address[key]}
            logger.warning("Location unknown for lat=%s, lon=%s", lat, lon)
            return {"type": "unknown", "name": "Unknown"}
        except Exception as e:
            logger.error("Error resolving location for lat=%s, lon=%s: %s", lat, lon, e)
            return {"type": "unknown", "name": "Unknown"}

    def get_iss_position_with_location(self) -> Dict[str, str]:
        """
        Fetch the ISS position and resolve the country or sea/ocean.
        Logs the combined result.
        """
        pos = self.get_iss_position()
        location = self.get_location_info(pos["latitude"], pos["longitude"])
        result = {**pos, "location_type": location["type"], "location_name": location["name"]}
        logger.info("ISS position with location: %s", result)
        return result 