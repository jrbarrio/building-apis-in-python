# Import the base class from pydantic
from pydantic import BaseModel

class CoffeeQualityInput(BaseModel):
    # Use apt data type for each attribute of coffee quality
    aroma: float  
    flavor: float  
    altitude: int  