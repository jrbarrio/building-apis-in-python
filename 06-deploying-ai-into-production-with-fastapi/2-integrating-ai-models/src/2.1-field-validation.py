# Import the base model and field validator from Pydantic
from pydantic import BaseModel, Field

# Inherit Pydantic's base model
class User(BaseModel): 
    # Set minimum and maximum name length
    username: str = Field(..., min_length=5, max_length=20)
    email: str
    age: int

user = User(username="john_doe", email="john@mode360.com", age=25)
print(user)