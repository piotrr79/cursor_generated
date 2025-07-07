# Backend Service (FastAPI)

## Overview
This backend service provides the ISS (International Space Station) position and geolocation information via a REST API. It is designed with OOP and SOLID principles, and integrates with the Auth microservice for JWT authentication.

## Architecture
- **Framework:** FastAPI (Python)
- **Structure:**
  - `main.py`: FastAPI app, controller, and dependency injection
  - `iss_service.py`: OOP service for ISS position and geolocation logic
  - `auth.py`: OOP service for JWT validation via Django Auth microservice
- **Testing:** pytest, unittest.mock

## Endpoints
### `GET /iss`
- **Description:** Returns the current ISS position and its geolocated country or sea/ocean.
- **Authentication:** Requires JWT Bearer token (validated via Auth microservice)
- **Response Example:**
  ```json
  {
    "latitude": "10.0",
    "longitude": "20.0",
    "location_type": "country",
    "location_name": "Testland"
  }
  ```
- **Errors:**
  - `401 Unauthorized`: Invalid or missing token
  - `500 Internal Server Error`: Upstream or internal error

## Authentication
- Uses JWT tokens issued by the Auth (Django) microservice
- Token is validated by calling the Auth service `/auth/jwt/verify/`

## Running the Service
1. **Install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Start the server:**
   ```bash
   uvicorn app.main:app --reload
   ```
3. **Docker:**
   See the provided Dockerfile and Nginx config for containerized deployment.

## Testing
- Run all unit tests:
  ```bash
  PYTHONPATH=. pytest tests/
  ```
- Tests cover controller, ISSService, and error handling (with mocks for external APIs).

## OOP & SOLID Principles
- All business logic is encapsulated in service classes (`ISSService`, `AuthService`)
- Controllers are flat and only handle routing and dependency injection
- Type hints and docstrings are provided throughout
- Exception handling and logging are implemented for robustness

## Contact
For questions or contributions, see the main project repository. 