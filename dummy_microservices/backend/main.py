from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
import requests
import os

app = FastAPI()

OAUTH_URL = os.getenv("OAUTH_URL", "http://localhost:8001")
ISS_API_URL = "http://api.open-notify.org/iss-now.json"
NOMINATIM_URL = "https://nominatim.openstreetmap.org/reverse"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{OAUTH_URL}/token")

# Auth check with OAuth microservice
async def verify_token(token: str = Depends(oauth2_scheme)):
    resp = requests.post(f"{OAUTH_URL}/verify", json={"token": token})
    if resp.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid token")
    return resp.json()

@app.get("/iss")
async def get_iss_position(user=Depends(verify_token)):
    iss_resp = requests.get(ISS_API_URL)
    iss_resp.raise_for_status()
    iss_data = iss_resp.json()
    lat = iss_data["iss_position"]["latitude"]
    lon = iss_data["iss_position"]["longitude"]
    params = {
        "format": "json",
        "lat": lat,
        "lon": lon,
        "zoom": 10,
        "addressdetails": 1
    }
    nom_resp = requests.get(NOMINATIM_URL, params=params, headers={"User-Agent": "iss-microservice"})
    nom_resp.raise_for_status()
    address = nom_resp.json().get("address", {})
    if "country" in address:
        location = {"type": "country", "name": address["country"]}
    else:
        for key in ["sea", "ocean", "water", "river", "lake"]:
            if key in address:
                location = {"type": "sea", "name": address[key]}
                break
        else:
            location = {"type": "unknown", "name": "Unknown"}
    return {"latitude": lat, "longitude": lon, "location_type": location["type"], "location_name": location["name"]} 