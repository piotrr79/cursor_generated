# Dummy FastAPI App

This is a simple FastAPI app with a Hello World endpoint.

## Setting up a Python virtual environment

1. Create a virtual environment (recommended):
   ```bash
   python3 -m venv env
   ```
2. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
   - On Windows:
     ```cmd
     .\env\Scripts\activate
     ```

Then proceed with the steps below to install dependencies and run the app.

## How to run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   uvicorn main:app --reload
   ```
3. Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the Hello World response. 