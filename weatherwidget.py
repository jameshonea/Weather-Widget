import requests
import json
import time


loop = True
while loop == True:
    response = requests.get("https://api.darksky.net/forecast/8c4e31711730f9577556ad3878ae1fd0/39.855955, -86.338426")
    status_code = response.status_code

    json_data = response.json()
    print(json_data)

    print(json_data['currently'])

    print(" ")

    print(json_data['daily']['summary'])

    time.sleep(300)
