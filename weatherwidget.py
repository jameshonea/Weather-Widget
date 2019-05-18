import requests
import json
import time
import winsound

def update_list(li, val):
    # updates list of values used to generate a graph (for example, past 24-hour temperature).
    # if the list is longer than 24 hours worth of data, it deletes the first value as the
    # latest value is appended.

    li.append(val)

    num_datapoints = round(86400/300) # calculate the num of datapoints based on interval between API endpoint access.

    if len(li) > num_datapoints:
        del li[0]

    return li




temp_list = []
humid_list = []
press_list = []
alerts_check = {} # this will be used to check for new alerts each iteration

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

    '''

    below are dictionaries containing values for each day. the needed values
    from each are time, summary, icon, precipProbability, temperatureHigh, temperatureLow,
    apparentTemperatureHigh, apparentTemperatureLow, dewPoint, humidity, pressure, windSpeed,
    windGust, windBearing.

    '''
    
    d1 = json_data['daily']['data'][1]
    d2 = json_data['daily']['data'][2]
    d3 = json_data['daily']['data'][3]
    d4 = json_data['daily']['data'][4]
    d5 = json_data['daily']['data'][5]


    try:
        alerts = json_data['alerts']

        # check for new alerts

        if len(alerts) > len(alerts_check):

            # need to add unique sounding for tornado and severe warnings
            # if neither of those then else clause playing lesser sound
            
            winsound.PlaySound("severealert.wav", winsound.SND_ASYNC)

            # after playing sound, update alerts_check for next iteration

            alerts_check = alerts
    except Exception:
        pass



    temp_list = update_list(temp_list, current_temp)
    humid_list = update_list(humid_list, humidity)
    press_list = update_list(press_list, pressure)

    #j = json_data['daily']['data'][2]
    #print(j['temperatureHigh'])


    print(" ")
    print(json_data['currently'])
 
    print(json_data['daily']['summary'])

    print(temp_list)
    print(humid_list)
    print(press_list)

    

    
    time.sleep(60)
