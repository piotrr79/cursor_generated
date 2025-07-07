# Auth Service (Django)

## Overview

This service provides authentication and authorization for the ISS microservices application. It is built with Django and Django REST Framework, using a custom user model (email as username) and JWT authentication (SimpleJWT). The service supports user registration, login, and token verification, and is designed with OOP and SOLID principles.

## Features

- **User Registration** (`/api/register/`)
- **User Login** (`/api/login/`)
- **JWT Issuance & Verification**
- **Custom User Model** (email as username)
- **SQLite Database**
- **Unit Tests for Registration and Login**
- **Dockerfile & Nginx config for production deployment**

## Architecture

- Django project: `auth_service`
- App: `users`
- Custom user model in `users/models.py`
- API endpoints in `users/views.py` and `users/urls.py`
- JWT authentication via `rest_framework_simplejwt`
- Static/media served via Nginx

## Endpoints

| Method | Endpoint           | Description         |
|--------|--------------------|--------------------|
| POST   | `/api/register/`   | Register a new user (email, password) |
| POST   | `/api/login/`      | Login and receive JWT tokens          |

- All endpoints return both `access` and `refresh` JWT tokens on success.

## Example Request/Response

**Register**
```http
POST /api/register/
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```
**Response**
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

**Login**
```http
POST /api/login/
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```
**Response**
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

## Database

- Uses SQLite by default (`db.sqlite3`)
- Custom user model (`users.User`) with email as the unique identifier

## Running the Service

### Prerequisites

- Python 3.11+
- pip

### Local Development

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8002
```

### Docker

Build and run with Docker:
```bash
docker build -t auth-service .
docker run -p 8002:8002 -p 80:80 auth-service
```

- Nginx serves static files and proxies API requests to Django (see `nginx.conf`).

## Configuration

- Main settings in `auth_service/settings.py`
- JWT settings via `rest_framework_simplejwt`
- Custom user model: `AUTH_USER_MODEL = 'users.User'`

## Testing

Run unit tests:
```bash
python manage.py test users
```
- Tests cover registration, login, and invalid login scenarios.

## OOP & SOLID Principles

- Business logic is encapsulated in serializers and model managers.
- Views are flat and only handle routing and response formatting.
- All classes and functions are documented and covered by unit tests.

## Deployment

- Use the provided `Dockerfile` and `nginx.conf` for production deployment.
- Exposes ports 8002 (Django) and 80 (Nginx).

## License

MIT (or specify your license) 