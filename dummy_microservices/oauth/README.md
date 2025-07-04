# OAuth Microservice (OOP/SOLID)

This is a FastAPI-based OAuth microservice for user registration, authentication, and JWT issuing, refactored to use OOP and SOLID principles.

## Features
- User registration and authentication
- JWT access token issuing and verification
- SQLite database for users and tokens
- OOP and SOLID design (UserService, TokenService, Database, User, Token)
- Unit tests for core logic
- Dockerized with Nginx as a reverse proxy

## Database Schema
- `users`: id, username, password
- `tokens`: id, user_id, access_token, expires_at

## Project Structure
- `models.py`: Database, User, Token classes
- `services.py`: UserService, TokenService (business logic)
- `main.py`: FastAPI app and endpoints
- `test_services.py`: Unit tests
- `Dockerfile`, `nginx.conf`: Containerization and proxy config

## Setup & Run

### Local
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   uvicorn main:app --reload --port 8001
   ```
3. The API is available at http://localhost:8001

### Docker
1. Build the image:
   ```bash
   docker build -t oauth-app .
   ```
2. Run the container:
   ```bash
   docker run -p 8001:8001 -p 80:80 oauth-app
   ```
3. The API is available at http://localhost:80

## Endpoints
- `POST /register` — Register a new user
- `POST /token` — Obtain JWT token
- `POST /verify` — Verify JWT token

## Testing
Run unit tests with:
```bash
pytest test_services.py
``` 