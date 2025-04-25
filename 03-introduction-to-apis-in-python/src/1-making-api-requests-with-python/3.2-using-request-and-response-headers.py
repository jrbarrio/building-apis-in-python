response = requests.get('http://localhost:3000/lyrics')

# Print the response content-type header
print(response.headers['content-type'])

#######################################################

response = requests.get('http://localhost:3000/lyrics')

# Print the response accept header
print(response.headers['accept'])

#######################################################

# Set the content type to application/json
headers = {"accept": 'application/json'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Print the response's text
print(response.text)