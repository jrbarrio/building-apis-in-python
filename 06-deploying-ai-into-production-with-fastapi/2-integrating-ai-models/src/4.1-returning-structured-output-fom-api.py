# Create a POST request endpoint
@app.post("/analyze")
# Capture the request text for validation as per CommentRequest model
def analyze_comment(request: CommentRequest):
    try:
        # Specify pass the request text to the model
        result = sentiment_model(request.text)
        # Specify the result attributes to complete the comment response
        return CommentResponse(text=request.text, 
                               sentiment=result[0]["label"], 
                               confidence=result[0]["score"])
    except Exception:
        raise HTTPException(status_code=500,
            detail="Prediction failed"
        )