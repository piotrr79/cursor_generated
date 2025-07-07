# dummy_microservices_v2

## Overview

`dummy_microservices_v2` is a modular microservices application for displaying the current position of the International Space Station (ISS). The system is built with OOP and SOLID principles, and features:

- **Frontend:** React (TypeScript)
- **Backend:** FastAPI (Python)
- **Authentication:** Django (Python, JWT)
- **Database:** SQLite (for auth)
- **API Integration:** ISS position and geolocation via public APIs
- **Deployment:** Docker, Nginx, unit tests, and CI/CD ready

## Service Documentation

- [Frontend README](frontend/README.md)
- [Backend README](backend/README.md)
- [Auth README](auth/README.md)

## Architecture

```mermaid
graph TD
A[Frontend]--> B[Backend]
B[Backend] --> C[Authentication]
C[Authentication] --> B[Backend]
B[Backend] --> A[Frontend]
C --> E[(User DB)]

style A fill:#f9f,stroke:#333,stroke-width:4px
style B fill:#bbf,stroke:#333,stroke-width:2px
style C fill:#bbf,stroke:#333,stroke-width:2px
```

- **Frontend**: Handles user registration, login, and displays ISS position (protected route).
- **Backend**: Provides `/iss` endpoint, validates JWT via Auth service, fetches ISS position and geolocation.
- **Auth**: Django service for registration, login, and JWT issuance/validation.
- **All services**: Communicate via REST APIs and are containerized with Docker and Nginx.

## Services

### 1. Frontend (`frontend/`)
- React app (TypeScript)
- OOP/SOLID service classes for API and auth
- Registration, login, and ISS position display
- Unit tests (Jest, React Testing Library)
- Dockerfile and Nginx config for production

### 2. Backend (`backend/`)
- FastAPI app (Python)
- `/iss` endpoint (JWT-protected)
- OOP/SOLID service classes for ISS and Auth logic
- Unit tests (pytest, unittest.mock)
- Dockerfile and Nginx config for production

### 3. Auth (`auth/`)
- Django app (Python)
- Custom user model (email as username)
- Registration, login, JWT issuance/validation
- SQLite database
- Unit tests
- Dockerfile and Nginx config for production

## Running the Application

### Prerequisites
- Docker and Docker Compose installed

### Quick Start

1. **Clone the repository**
2. **Build and run all services** (example with Docker Compose):
   ```bash
   docker-compose up --build
   ```
3. **Access the app**
   - Frontend: [http://localhost](http://localhost)
   - Backend API: [http://localhost/api/backend/iss](http://localhost/api/backend/iss)
   - Auth API: [http://localhost/api/auth/]

### Service Endpoints

- **Frontend**: `/` (React app)
- **Backend**: `/api/backend/iss` (GET, JWT required)
- **Auth**: `/api/auth/register/`, `/api/auth/login/`, `/api/auth/token/verify/`

## Development

- Each service has its own README with detailed setup, testing, and usage instructions.
- All business logic is in service classes; controllers are flat.
- All classes and functions are documented and covered by unit tests.
- Prompts and responses are logged in `docs/prompts` for traceability.

## Technical Details

- See `docs/technical.md` for business logic, technology stack, and future considerations.
- See `docs/architecture.mermaid` for a visual architecture diagram.

## License

MIT (or specify your license) 