**Note:** This codebase was generated with [Cursor](https://www.cursor.so/).

# Project Overview

This repository contains several example applications and services in different languages and frameworks, each demonstrating ISS (International Space Station) position tracking or related logic.

## Contents

### dummy_fast_api
A Python FastAPI application that exposes an API to get the current position of the ISS, including the country or sea/ocean it is currently over. Includes:
- `main.py`: FastAPI app entry point
- `iss_logic.py`: Logic for fetching ISS position and reverse geocoding
- `iss.py`: API router for ISS endpoint
- `requirements.txt`: Python dependencies
- `Dockerfile`, `nginx.conf`, `start.sh`: Containerization and deployment
- `test_iss.py`, `test_main.py`: Unit tests
- `README.md`: Usage and setup instructions

### dummy_ml
A Python machine learning example with:
- `model.py`: Example ML model code
- `api.py`: API for model serving
- `test_model.py`: Tests for the model
- `requirements.txt`: Python dependencies
- `Readme.md`: Details and usage

### dummy_apex
A Salesforce Apex example with:
- `IssService.cls`, `IssApi.cls`, `HelloApi.cls`: Apex classes for ISS logic and APIs
- `IssServiceTest.cls`: Apex test class
- `Readme.md`: Details and usage

### dummy_php
A PHP application with:
- `index.php`: Main entry point
- `ISSService.php`: Service logic for ISS
- `tests/ISSServiceTest.php`: Unit tests
- `composer.json`: PHP dependencies
- `Dockerfile`, `nginx.conf`, `supervisord.conf`: Containerization and deployment
- `Readme.md`: Details and usage

### dummy_java
A Java Spring Boot application with:
- `src/main/java/com/example/iss/`: Main application code
  - `DummyJavaApplication.java`: Main class
  - `controller/IssController.java`: REST controller for ISS endpoint
  - `service/IssService.java`: Service logic for ISS
- `src/test/java/com/example/iss/`: Unit tests
  - `controller/IssControllerTest.java`: Controller tests
  - `service/IssServiceTest.java`: Service tests
- `pom.xml`: Maven build file
- `Dockerfile`, `nginx.conf`, `supervisord.conf`: Containerization and deployment
- `Readme.md`: Details and usage

---

Each subfolder contains its own README with more detailed setup and usage instructions specific to that implementation. 