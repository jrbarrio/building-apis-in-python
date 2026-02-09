# Import the function that handles dependencies
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader

# Create the API key instance
api_key_header = APIKeyHeader(name="X-API-Key")
API_KEY = "your_secret_key"

# Pass the APIKeyHeader instance and verify against input api_key
def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:  
      	# Raise the HTTP exception here
        raise HTTPException(status_code=403, detail="Invalid API Key")  
    return api_key