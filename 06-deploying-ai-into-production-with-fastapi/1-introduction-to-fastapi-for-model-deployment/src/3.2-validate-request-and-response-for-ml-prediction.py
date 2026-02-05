class CoffeeQualityInput(BaseModel):
    aroma: float
    flavor: float
    altitude: int
    
class QualityPrediction(BaseModel):
    quality_score: float 
    confidence: float

# Specify the data model to validate response
@app.post("/predict", response_model=QualityPrediction) 
# Specify the data model to validate input request
def predict(coffee_data: CoffeeQualityInput):
    prediction = predict_quality(coffee_data)
    return prediction 