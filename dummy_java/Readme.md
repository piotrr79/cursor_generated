**Note:** This codebase was generated with [Cursor](https://www.cursor.so/).

# Dummy Java ISS API (Spring Boot + Nginx)

This project is a Java Spring Boot application that exposes a simple API:
- `/` endpoint: returns "Hello World"
- `/iss` endpoint: returns the current ISS position and the country over which it is located (using external APIs)

---

## Requirements
- Docker (recommended) or Java 21 and Maven

## Build and Run with Docker
```bash
cd dummy_java
# Build the Docker image
docker build -t dummy-java-nginx .
# Run the container (exposes app at http://localhost:8080/)
docker run -p 8080:80 dummy-java-nginx
```

## Manual Build and Run (without Docker)
```bash
cd dummy_java
mvn clean package
java -jar target/dummy-java-1.0-SNAPSHOT.jar
# App will be available at http://localhost:8080/
```

## Run Tests
```bash
cd dummy_java
mvn test
```

## Endpoints
- `GET /` — returns `Hello World`
- `GET /iss` — returns ISS position and country (JSON)

## Notes
- The Docker image uses Nginx as a reverse proxy.
- The `/iss` endpoint depends on external APIs and may be rate-limited. 