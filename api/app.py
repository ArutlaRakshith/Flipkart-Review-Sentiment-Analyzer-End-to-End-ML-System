from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
MODEL_PATH = os.path.join("model", "sentiment_model.joblib")

app = FastAPI(title="Flipkart Products Sentiment Predictor API")

class ReviewRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    sentiment: str
    confidence: float

@app.on_event("startup")
def load_model():
    global model
    model = joblib.load(MODEL_PATH)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Sentiment PredictorAPI is running"}

@app.post("/predict", response_model=PredictionResponse)
def predict_sentiment(request: ReviewRequest):
    text = request.text
    proba = model.predict_proba([text])[0]
    pred = model.predict([text])[0]

    sentiment = "positive" if pred == 1 else "negative"
    confidence = float(max(proba))

    return {
        "sentiment": sentiment,
        "confidence": round(confidence, 4)
    }
