import requests

# Import the correct exception class
from requests.exceptions import ConnectionError

url ="http://wronghost:3000/albums"

try: 
    r = requests.get(url) 
    print(r.status_code)
# Use the imported class to intercept the connection error
except ConnectionError as conn_err: 
    print(f'Connection Error! {conn_err}.')

try: 
    r = requests.get(url) 
	# Enable raising errors for all error status_codes
    r.raise_for_status()
    print(r.status_code)
# Intercept the error 
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')

