from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Review(BaseModel):
    text: str

# Create async endpoint at /analyze route
@app.post("/analyze")
# Write an asynchronous function to process review's text
async def analyze_review(review: Review):
    # Run the model in a separate thread to avoid any event loop blockage
    result = await asyncio.to_thread(sentiment_model, review)
    return {"sentiment": result[0]["label"]}