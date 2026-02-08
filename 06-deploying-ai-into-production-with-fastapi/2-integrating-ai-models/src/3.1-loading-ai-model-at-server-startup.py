# Import the context manager decorator from contextlib module
from contextlib import asynccontextmanager

sentiment_model = None

def load_model():
    global sentiment_model
    sentiment_model = SentmentAnalyzer("sentiment_model.joblib")

# Use FastAPI's context manager to define lifespan event
@asynccontextmanager
def lifespan(app: FastAPI):
    # Call the function to load the model
    load_model()
    yield