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







def main_loop():

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
    '''

    sev_sound_played = False # flag to prevent two sounds from playing at same time

    try:
        alerts = json_data['alerts']

        # check for new alerts

        if len(alerts) > len(alerts_check):

            # need to add unique sounding for tornado and severe warnings
            # if neither of those then else clause playing lesser sound
            
            winsound.PlaySound("severealert.wav", winsound.SND_ASYNC)
            sev_sound_played = True

            # after playing sound, update alerts_check for next iteration

            alerts_check = alerts
    except Exception:
        pass



    if json_data['currently']['nearestStormDistance'] < 50:

        if prev_storm_distance - json_data['currently']['nearestStormDistance'] > 0:
            if prev_sound_played == False:
                if sev_sound_played == False:
                    winsound.PlaySound('stormalert.wav', winsound.SND_ASYNC)

                counter = 15 # counter to decrease to prevent playing sound for a bit
                prev_sound_played = True

        prev_storm_distance = json_data['currently']['nearestStormDistance'] # sets after loop to check against value on next pass-through

    if prev_sound_played == True:
        if counter > 0:
            counter = counter - 1
            print(counter)
        else:
            prev_sound_played = False
    

    


    



    temp_list = update_list(temp_list, current_temp)
    humid_list = update_list(humid_list, humidity)
    press_list = update_list(press_list, pressure)
    '''


    print(" ")
    print(json_data['currently'])
 
    print(json_data['daily']['summary'])

temp_list = []
humid_list = []
press_list = []
alerts_check = {} # this will be used to check for new alerts each iteration
prev_sound_played = False # used to check if a sound has played recently
prev_storm_distance = 0 # used to check if a storm has gotten closer since last iteration
                        # i do this to eliminate most false positives hopefully

    
loop = True
while loop == True:

    main_loop()



    
    time.sleep(300)
