from fastapi import FastAPI

app = FastAPI()

# Create health check endpoint
@app.get("/health")
async def get_health():
    # Return status OK
    return {"status": "OK"}