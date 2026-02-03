from fastapi import FastAPI, HTTPException

app = FastAPI()

model_db = {}

class ModelInfo(BaseModel):
    model_id: int
    model_name: str
    description: str

# Create the POST request endpoint
@app.post("/register-model", status_code=201)
# Pass the model info from the request as function parameter 
def register_model(model_info: ModelInfo):
    # Add new model's information dictionary to the model database
    model_db[model_info.model_id] = model_info.model_dump()
    
    return {"message": "Model registered successfully", "model": model_info}, 201