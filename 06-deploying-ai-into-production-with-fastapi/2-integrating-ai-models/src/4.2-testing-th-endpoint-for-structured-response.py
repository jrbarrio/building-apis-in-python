import requests

url = "http://localhost:8080/analyze"
data = {"text": "This is great, I can totally relate."}

# Send post request and pass the sample request data
response = requests.post(url, json=data)

# Print prediction response
print(response.json())