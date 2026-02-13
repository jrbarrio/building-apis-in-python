# Import annotation for custom validation
from pydantic import BaseModel, model_validator

class InventoryRecord(BaseModel):
    name: str
    quantity: int

    # Create custom validator that runs after default validation
    @model_validator(mode="after")
    def validate_after(self):
        if len(self.quantity) < 0:
            # Raise request validation error
            raise RequestValidationError(
                "Negative quantity is not allowed!"
            )
        return self