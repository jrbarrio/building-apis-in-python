from pydantic import BaseModel, field_validator, Field

class User(BaseModel):
    username: str = Field(..., min_length=5, max_length=20)  
    email: str
    age: int

    # Add the Pydantic decorator to validate
    @field_validator('email')  
    def email_must_be_example_domain(cls, user_email):
        # Use the endswith method to validate the email ends with @mode360.com
        if not user_email.endswith("@mode360.com"):
            raise ValueError('Email must be from the mode360.com domain')
        return user_email