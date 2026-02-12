# Add v2 model
class PenguinV2(BaseModel):
    data: str

@app.post("/v1/penguin_classifier")
def classify_penguin_v1(penguin: PenguinV1):
    values = list(penguin.model_dump().values())
    result = classifier.predict([values])[0]
    return result

# Add v2 endpoint
@app.post("/v2/penguin_classifier")
# Use v2 model
def classify_penguin_v2(penguin: PenguinV2):
    values = penguin.data.split()
    result = classifier.predict([values])[0]
    return result