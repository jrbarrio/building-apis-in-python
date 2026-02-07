from fastapi import FastAPI
from pydantic import BaseModel, Field, validator

app = FastAPI()

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str
    age: int
    
    @validator('email')
    def email_must_be_example_domain(cls, user_email):
        if not user_email.endswith("@mode360.com"):
            raise ValueError('Email must be from the mode360.com domain')
        return user_email

# Create a post request endpoint
@app.post("/register")
# Validate incoming user data with a pydantic model
def register_user(user: User):
    return {"status": "success", "user": user.dict()}
  
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)