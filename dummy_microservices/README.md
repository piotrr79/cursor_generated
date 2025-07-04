**Note:** This codebase was generated with [Cursor](https://www.cursor.so/).

# Code generation with Curson failed. Despite instructions in /docs folder and defined rules following thigs failed:
- **OOP / SOLID** - Cursor ignored guaidance and generated flat code, not encapsulated in classes. Wen asked for refactoring created nested classes in one file and ignored some other files from refactoring. When asked for splitting files did not executed prompt correctly (while several request was merged into one prompt).
- **Type hints** - Missing type hints in Python code, even thus it was defined as requirement in /docs
- **Ignored files** - For fronted attached template file was ingored, React app was created without css styles and core html. Attached template was considered as final React template (not example) and was not attached to fronted app. Public folder is missing.

## Conclusion: while it works well with simpler pices of code (like the one in /dummy_fast_api) too complex and too extended prompts might be to complicated to handle correctly and without human participation. 

## Prompts must be simpler, the best referrign to smaller parts of code and also run by qualified developer.


# Dummy Microservices ISS Application

This project demonstrates a microservices architecture for displaying the current position of the International Space Station (ISS). It includes:

- **Backend API** (FastAPI, Python)
- **Frontend UI** (React, TypeScript)
- **Custom OAuth Authorization Provider** (FastAPI, Python)

All services communicate via REST APIs. The system requires user registration and login to access ISS position data.

## Architecture

```
Frontend (React) <-> Backend (FastAPI) <-> OAuth (FastAPI)
```
- The frontend interacts with the backend for ISS data and authentication.
- The backend verifies tokens and fetches ISS/country/sea info.
- The backend delegates authentication to the OAuth service.

## Microservices

### 1. Backend (`backend/`)
- FastAPI app exposing `/iss` endpoint (protected, requires JWT).
- Forwards authentication to the OAuth service.
- Fetches ISS position and country/sea/ocean info.
- See `backend/requirements.txt` for dependencies.

### 2. OAuth (`oauth/`)
- FastAPI app for user registration, login, and JWT issuing.
- Stores users and tokens in SQLite.
- OOP/SOLID structure: `database.py`, `user.py`, `token.py`, `user_service.py`, `token_service.py`.
- Unit tests in `test_services.py`.
- Dockerfile and Nginx config for containerized deployment.
- See `oauth/README.md` for more details.

### 3. Frontend (`frontend/`)
- React + TypeScript app for user registration, login, and ISS position display.
- Uses UI template from `docs/template`.
- Communicates with backend and OAuth via REST API.
- See `frontend/README.md` for setup and usage.

## Setup & Run

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### OAuth
```bash
cd oauth
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```
Or use Docker (see `oauth/README.md`).

### Frontend
```bash
cd frontend
npm install
npm start
```

## Documentation & History
- See `docs/prompts` for a full history of prompts and responses during development.
- See `docs/technical.md` and `docs/architecture.mermaid` for technical and architectural details.

---

This project is for demonstration and educational purposes. Contributions and improvements are welcome! 