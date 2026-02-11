# Import the background task class
from fastapi import BackgroundTasks
# Create a background task dependency
@app.post("/analyze_batch")
async def analyze_batch(
    reviews: Reviews,
    background_tasks: BackgroundTasks
):
    async def process_reviews(texts: List[str]):
        for text in texts:
            result = await asyncio.to_thread(sentiment_model, text)
            print(f"Processed: {result[0]['label']}")
    # Add the task of analysing reviews' texts to the background
    background_tasks.add_task(process_reviews, reviews.texts)
    return {"message": "Processing started"}