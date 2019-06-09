import requests
import json
import time
import winsound
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
import random
from datetime import datetime

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
    


    try:
        temp_list = update_list(temp_list, current_temp)
        humid_list = update_list(humid_list, humidity)
        press_list = update_list(press_list, pressure)
    except Exception:
        # first pass through throws an error cause temp_list doesnt exist yet. not sure how else to fix this yet.
        temp_list = []
        humid_list = []
        press_list = []

        # set below to zero now otherwise this will also throw an error
        prev_storm_distance = 0 
        prev_sound_played = False


    print(" ")
    print(json_data['currently'])
 
    print(json_data['daily']['summary'])


# below code doesn't work as intended because nearestStormDistance is not accurate (sure, blame the API...). Trying to find a different way to work this.
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








    
loop = True
while loop == True:

    main_loop()



    
    time.sleep(300)
    '''

class MainView(GridLayout):
    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)

        self.cols = 2
        self.currenttemp = Label(text="test")
        self.add_widget(self.currenttemp)

        self.weathericon = Label(text='icon')
        self.add_widget(self.weathericon)

        self.add_widget(Label(text="  "))
        self.add_widget(Label(text="  "))

        self.left = GridLayout()
        self.left.cols = 2

        self.left.add_widget(Label(text="Feels Like: "))
        self.feelslike = Label(text="test")
        self.left.add_widget(self.feelslike)

        self.left.add_widget(Label(text='Wind Speed: '))
        self.windspeed = Label(text='test')
        self.left.add_widget(self.windspeed)

        self.left.add_widget(Label(text='Wind Gust: '))
        self.windgust = Label(text='test')
        self.left.add_widget(self.windgust)

        self.left.add_widget(Label(text='Humidity: '))
        self.humidity = Label(text='test')
        self.left.add_widget(self.humidity)

        self.left.add_widget(Label(text='Pressure: '))
        self.pressure = Label(text='test')
        self.left.add_widget(self.pressure)

        self.left.add_widget(Label(text='Precipitation Probability: '))
        self.precipprob = Label(text='test')
        self.left.add_widget(self.precipprob)


        self.add_widget(self.left)

        


        self.r = GridLayout()
        self.r.cols = 3


        self.d1left = Label(text='test')
        self.r.add_widget(self.d1left)
        self.d1mid = Label(text='test')
        self.r.add_widget(self.d1mid)
        self.d1right = Label(text='test')
        self.r.add_widget(self.d1right)
        

        self.d2left = Label(text='test')
        self.r.add_widget(self.d2left)
        self.d2mid = Label(text='test')
        self.r.add_widget(self.d2mid)
        self.d2right = Label(text='test')
        self.r.add_widget(self.d2right)

        self.d3left = Label(text='test')
        self.r.add_widget(self.d3left)
        self.d3mid = Label(text='test')
        self.r.add_widget(self.d3mid)
        self.d3right = Label(text='test')
        self.r.add_widget(self.d3right)

        self.d4left = Label(text='test')
        self.r.add_widget(self.d4left)
        self.d4mid = Label(text='test')
        self.r.add_widget(self.d4mid)
        self.d4right = Label(text='test')
        self.r.add_widget(self.d4right)

        self.d5left = Label(text='test')
        self.r.add_widget(self.d5left)
        self.d5mid = Label(text='test')
        self.r.add_widget(self.d5mid)
        self.d5right = Label(text='test')
        self.r.add_widget(self.d5right)
        

        self.add_widget(self.r)

        self.update(1)
        Clock.schedule_interval(self.update, 5)

    def update(self, dt):
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

        self.currenttemp.text = str(json_data['currently']['temperature'])
        self.feelslike.text = str(json_data['currently']['apparentTemperature'])
        self.windspeed.text = str(json_data['currently']['windSpeed'])
        self.windgust.text = str(json_data['currently']['windGust'])
        self.humidity.text = str(json_data['currently']['humidity'])
        self.pressure.text = str(json_data['currently']['pressure'])
        self.precipprob.text = str(json_data['currently']['precipProbability'])

        
        '''

        below are dictionaries containing values for each day. the needed values
        from each are time, summary, icon, precipProbability, temperatureHigh, temperatureLow,
        apparentTemperatureHigh, apparentTemperatureLow, dewPoint, humidity, pressure, windSpeed,
        windGust, windBearing.

        '''
    
        d1 = json_data['daily']['data'][1]
        print(datetime.utcfromtimestamp(int(d1['time'])).strftime('%A'))
        d2 = json_data['daily']['data'][2]
        d3 = json_data['daily']['data'][3]
        d4 = json_data['daily']['data'][4]
        d5 = json_data['daily']['data'][5]

        self.d1left.text = str(datetime.utcfromtimestamp(int(d1['time'])).strftime('%A'))
        self.d1mid.text = " "
        self.d1right.text = str(d1['temperatureHigh'])

        self.d2left.text = str(datetime.utcfromtimestamp(int(d2['time'])).strftime('%A'))
        self.d2mid.text = " "
        self.d2right.text = str(d2['temperatureHigh'])

        self.d3left.text = str(datetime.utcfromtimestamp(int(d3['time'])).strftime('%A'))
        self.d3mid.text = " "
        self.d3right.text = str(d3['temperatureHigh'])

        self.d4left.text = str(datetime.utcfromtimestamp(int(d4['time'])).strftime('%A'))
        self.d4mid.text = " "
        self.d4right.text = str(d4['temperatureHigh'])

        self.d5left.text = str(datetime.utcfromtimestamp(int(d5['time'])).strftime('%A'))
        self.d5mid.text = " "
        self.d5right.text = str(d5['temperatureHigh'])

        


class hello(App):
    def build(self):
        return MainView()

hello().run()
