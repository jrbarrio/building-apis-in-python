# Import class for plain text response
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Create global exception handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    # Return plain text response
    return PlainTextResponse(str(exc), status_code=400)