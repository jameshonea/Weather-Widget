import requests

response = requests.get("https://api.darksky.net/forecast/8c4e31711730f9577556ad3878ae1fd0/39.855955, -86.338426")
status_code = response.status_code

print(status_code)
