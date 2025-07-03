# Dummy PHP ISS API (PHP + Nginx)

This project is a PHP application that exposes a simple API:
- `/` endpoint: returns "Hello World"
- `/iss` endpoint: returns the current ISS position and the country over which it is located (using external APIs)

---

## Requirements
- Docker (recommended) or PHP 8.2+, Composer

## Build and Run with Docker
```bash
cd dummy_php
# Build the Docker image
docker build -t dummy-php-nginx .
# Run the container (exposes app at http://localhost:8080/)
docker run -p 8080:80 dummy-php-nginx
```

## Manual Run (without Docker)
```bash
cd dummy_php
composer install
php -S localhost:8080
# App will be available at http://localhost:8080/
```

## Run Tests
```bash
cd dummy_php
./vendor/bin/phpunit tests
```

## Endpoints
- `GET /` — returns `Hello World`
- `GET /iss` — returns ISS position and country (JSON)

## Notes
- The Docker image uses Nginx as a reverse proxy.
- The `/iss` endpoint depends on external APIs and may be rate-limited. 