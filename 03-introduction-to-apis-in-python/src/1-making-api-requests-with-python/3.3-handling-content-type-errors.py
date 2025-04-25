import requests

# Add a header to use in the request
headers = {'accept': "application/xml"}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Check if the server did not accept the request
if (response.status_code == requests.codes.not_acceptable):
  print('The server can not respond in XML')
  
  # Print the accepted content types
  print('These are the content types the server accepts: ' + response.headers["accept"])
else:
  print(response.text)