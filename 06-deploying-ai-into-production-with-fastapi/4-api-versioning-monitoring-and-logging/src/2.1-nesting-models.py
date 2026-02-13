from datetime import date
from pydantic import BaseModel
# Import class for nested lists
from typing import List

class ModelInput(BaseModel):
    latitude: float
    longitude: float
    date: date

# Create batch input model
class BatchInput(BaseModel):
    job_name: str
    # Inputs are list of model inputs
    inputs: List[ModelInput]