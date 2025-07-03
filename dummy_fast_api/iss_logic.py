import requests

class ISSService:
    """
    Service class for fetching ISS position and country information.
    """
    ISS_API_URL = "http://api.open-notify.org/iss-now.json"
    NOMINATIM_URL = "https://nominatim.openstreetmap.org/reverse"
    USER_AGENT = {"User-Agent": "iss-fastapi-app"}

    def get_iss_position(self):
        """
        Fetch the current ISS position (latitude, longitude).
        Returns a tuple (lat, lon) as strings.
        Raises an exception if the API call fails.
        """
        response = requests.get(self.ISS_API_URL, timeout=5)
        response.raise_for_status()
        iss_data = response.json()
        lat = iss_data["iss_position"]["latitude"]
        lon = iss_data["iss_position"]["longitude"]
        return lat, lon

    def get_country_from_lat_lon(self, lat: str, lon: str) -> str:
        """
        Given latitude and longitude as strings, return the country name using OpenStreetMap's Nominatim API.
        Returns 'Unknown' if the country cannot be determined.
        """
        params = {
            "format": "json",
            "lat": lat,
            "lon": lon,
            "zoom": 5,
            "addressdetails": 1
        }
        try:
            response = requests.get(self.NOMINATIM_URL, headers=self.USER_AGENT, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            return data.get("address", {}).get("country", "Unknown")
        except Exception:
            return "Unknown"

    def get_iss_position_with_country(self):
        """
        Fetch the current ISS position and return latitude, longitude, and country.
        Returns a dict with keys: latitude, longitude, country.
        Raises an exception if the ISS API call fails.
        """
        lat, lon = self.get_iss_position()
        country = self.get_country_from_lat_lon(lat, lon)
        return {"latitude": lat, "longitude": lon, "country": country} 