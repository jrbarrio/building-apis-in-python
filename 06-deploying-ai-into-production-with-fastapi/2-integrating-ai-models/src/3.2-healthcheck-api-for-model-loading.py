from model import SentimentAnalyzer
from fastapi import FastAPI
from contextlib import asynccontextmanager

def load_model():
    global sentiment_model
    sentiment_model = SentimentAnalyzer("sentiment_model.joblib")

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_model()
    yield

app = FastAPI(title="Sentiment Analysis API", lifespan=lifespan)

# Define a GET endpoint at route "/health"
@app.get("/health")
def health_check():
  	# Check whether sentiment_model is loaded or not.
    if sentiment_model is not None:
        return {
          	# Mark status as healthy and loaded boolean to True
            "status": "healthy",
            "model_loaded": True
        }
    # Mark status as unhealthy and loaded boolean to False
    return {
        "status": "unhealthy",
        "model_loaded": False
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)