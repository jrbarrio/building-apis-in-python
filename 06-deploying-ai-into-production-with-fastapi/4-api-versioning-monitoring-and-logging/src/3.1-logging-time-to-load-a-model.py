from fastapi import FastAPI
import logging
import joblib 
import time

# Get the uvicorn error logger
logger = logging.getLogger('uvicorn.error')

start_time = time.perf_counter()
model = joblib.load('penguin_classifier.pkl')
process_time = time.perf_counter() - start_time
# Log the process time at the INFO level
logger.info(f"Process time was {process_time} seconds.")

app = FastAPI()