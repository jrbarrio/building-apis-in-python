import requests

# Create the authentication tuple with the correct values for basic authentication
authentication = ('john@doe.com', 'Warp_ExtrapolationsForfeited2')

# Use the correct function argument to pass the authentication tuple to the API
response = requests.get('http://localhost:3000/albums', auth=authentication)

# Check if the status code on the response object matches a successful response
if(response.status_code == requests.codes.ok):
    print("Success!")
# Check if the status code indicates a failed authentication attempt
elif(response.status_code == requests.codes.unauthorized):    print('Authentication failed')
else:
    print('Another error occurred')