from model import SentimentAnalyzer, verify_api_key
from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

class SentimentRequest(BaseModel):
    text: str

@app.post("/predict")
def get_prediction(
    request: SentimentRequest,
    # Authenticate the incoming API key using verify_api_key function
    api_key: str = Depends(verify_api_key)
):
    sentiment_model = SentimentAnalyzer("sentiment_model.joblib")
    result = sentiment_model(request.text)
    return {
        "text": request.text,
        "sentiment": result,
        "status": "success"
    }
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)