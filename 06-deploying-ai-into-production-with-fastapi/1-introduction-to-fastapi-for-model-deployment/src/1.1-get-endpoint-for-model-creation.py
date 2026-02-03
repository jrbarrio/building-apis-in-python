from fastapi import FastAPI, HTTPException

app = FastAPI()

# Add model_id as a path parameter in the route
@app.get("/model-info/{model_id}")
# Pass on the model id as an argument
async def get_model_info(model_id: int):
    if model_id == 0:
      	# Raise the right status code for not found
        raise HTTPException(status_code=404, detail="Model not found")
    model_info = get_model_details(id)  

    return {"model_id": model_id, "model_name": model_info}