from fastapi import FastAPI
from pydantic import BaseModel
from model import PiiDetector

app = FastAPI()
detector = PiiDetector()

class PredictRequest(BaseModel):
    text: str

@app.post("/predict")
def predict(request: PredictRequest):
    label = detector.predict(request.text)
    return {"label": label}

@app.get("/")
def root():
    return {"message": "PII Detection API. Use POST /predict with {'text': ...}"} 