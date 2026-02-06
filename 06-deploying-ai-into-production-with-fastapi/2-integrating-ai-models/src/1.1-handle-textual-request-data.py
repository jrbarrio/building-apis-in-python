@app.post("/analyze_comment")
def analyze_comment(text: str):
    problem_keywords = ["spam", "hate", "offensive", "abuse"]
    
    # Convert the input text to lowercase
    text_lower = text.lower()
    # Extract matching flags using list comprehension
    found_issues = [keyword for keyword in problem_keywords if keyword in text_lower]
    # Return the dictionary with required keys
    return {
        "issues": found_issues,
        "issue_count": len(found_issues),
        "original_text": text
    }