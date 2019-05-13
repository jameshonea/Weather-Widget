import requests
import json
import time


loop = True
while loop == True:
    response = requests.get("https://api.darksky.net/forecast/8c4e31711730f9577556ad3878ae1fd0/39.855955, -86.338426")
    status_code = response.status_code

    json_data = response.json()

    current_temp = json_data['currently']['temperature']
    feels_like = json_data['currently']['apparentTemperature']
    summary = json_data['currently']['summary']
    wind_speed = json_data['currently']['windSpeed']
    wind_gust = json_data['currently']['windGust']
    wind_bearing = json_data['currently']['windBearing']
    humidity = json_data['currently']['humidity']
    pressure = json_data['currently']['pressure']
    precip_prob = json_data['currently']['precipProbability']

    minute_sum = json_data['minutely']['summary']

    ''' below are dictionaries containing values for each day. the needed values
    from each are time, summary, icon, precipProbability, temperatureHigh, temperatureLow,
    apparentTemperatureHigh, apparentTemperatureLow, dewPoint, humidity, pressure, windSpeed,
    windGust, windBearing.
    '''
    d1 = json_data['daily']['data'][1]
    

    '''

    still need to add alerts dict here


    '''

    j = json_data['daily']['data'][2]
    print(j['temperatureHigh'])


    print(" ")

    #print(json_data['daily']['summary'])

    time.sleep(300)
