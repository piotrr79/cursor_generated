**Note:** This codebase was generated with [Cursor](https://www.cursor.so/).

# Project Overview

This is a test of code generation with Cursor. This repository contains several example applications and services in different languages and frameworks, each demonstrating ISS (International Space Station) position tracking or related logic.

As a first `dummy_fast_api` was generated and improved with several extra prompts. When code quality was good enough to meet standards Cursor was asked to convert it to different languages, Salesforce Apex in `dummy_apex`, PHP in `dummy_php` and Java in `dummy_java`. Conversion was done each time from initial Python code.

Next for PHP Cursor was asked to generate the same code with Symfony framework, in `dummy_symfony`, also by converting initial Python code to PHP.

In another test Cursor was prompted to generate the same apllication from the beginning, but this time in microservices architecture, with system architecture, technologies to be used, UI templates and rules defined in project, in /docs folder. There supposed to be three microservices, forntend in React, backend in Python FastApi and Authorisation app in Python Django. Project folder is `dummy_microservices`.

# Conclusions:
- **While Cursor is very good in generating smaller chunks of code it not so efficient in complex apllication generation (like `dummy_microservices`). Quality of generated code does not meet standards.**
- **In case of smaller application (e.g. `dummy_fast_api`) it still requires several prompts to refactor code to meet OOP and SOLID, by default gerated code is procedural.**

# Complex code generation issues based on `dummy_microservices`:
- **OOP / SOLID** - Cursor ignored guaidance defined in rules and generated flat code, not encapsulated in classes. Wen asked for refactoring created nested classes in one file and ignored some other files from refactoring. When asked for splitting files did not executed prompt correctly, while several request was merged into one prompt. It looks that like in every AI prompts cannot be too general.
- **Type hints** - Missing type hints in Python code, even thus it was defined as requirement in /docs
- **Docs** - Missing Docs in Python code, even thus it was defined as requirement in /docs
- **Ignored files** - For fronted attached template file was ingored, React app was created without css styles and core html. Attached template was considered as final React template (not example) and was not attached to fronted app. Public folder is missing.
- **Effectiveness** - In case of microservices app it is better to genrate each app as a separate project, with microservices to be linked together at the end by developer.

## General remark: while it works well with simpler pices of code (like the one in /dummy_fast_api) too complex and too extended prompts might be to complicated to handle correctly and without programmer participation. 


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

### dummy_symfony
The `dummy_symfony` project is a refactored version of the PHP ISS logic, implemented using the Symfony framework. It demonstrates how to build a modern PHP web application with:

- **API Endpoint**: Exposes `/iss` to return the current ISS position, including the country or sea/ocean name.
- **Service Layer**: Encapsulates ISS logic and geolocation in a Symfony service class.
- **UI**: Includes a simple HTML/JS frontend (`public/ui.html`) to interact with the API.
- **OOP and Best Practices**: Follows Symfony conventions for controllers, services, and routing.
- **Docker & Nginx**: Includes Dockerfile and Nginx configuration for containerized deployment.

For setup, usage, and more details, see `dummy_symfony/README.md`.

### dummy_microservices
The `dummy_microservices` project demonstrates a modular microservices architecture for displaying the current position of the International Space Station (ISS). It consists of three main services:

- **Backend API** (FastAPI, Python): Exposes a protected `/iss` endpoint, fetches ISS position and country/sea/ocean info, and delegates authentication to the OAuth service.
- **Frontend UI** (React, TypeScript): Allows user registration, login, and displays the ISS position. Communicates with the backend and OAuth services via REST API.
- **OAuth Authorization Provider** (FastAPI, Python): Handles user registration, login, JWT issuing, and token verification. Uses SQLite for user and token storage. Follows OOP and SOLID principles.

All services communicate via REST APIs. The system requires user registration and login to access ISS position data. Each service is independently deployable and can be run locally or in Docker containers.

For detailed setup, architecture, and usage instructions, see `dummy_microservices/README.md`.



---

Each subfolder contains its own README with more detailed setup and usage instructions specific to that implementation. 