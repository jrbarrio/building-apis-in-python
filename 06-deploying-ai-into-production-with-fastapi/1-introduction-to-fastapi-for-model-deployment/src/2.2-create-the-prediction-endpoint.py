from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Create a POST request endpoint at the route "/predict"
@app.post("/predict")
async def predict_progression(features: DiabetesFeatures):
    input_data = [[
        features.age,
        features.bmi,
        features.blood_pressure
    ]]
    
    # Use the predict method to make a prediction
    prediction = model.predict(input_data)
    return {"predicted_progression": float(prediction[0])}