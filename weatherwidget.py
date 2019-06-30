import requests
import json
import time
import winsound
from kivy.config import Config
Config.set('graphics', 'width',  650)
Config.set('graphics', 'height', 400)
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
import random
from datetime import datetime
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

def update_list(li, val):
    # updates list of values used to generate a graph (for example, past 24-hour temperature).
    # if the list is longer than 24 hours worth of data, it deletes the first value as the
    # latest value is appended.

    li.append(val)

    num_datapoints = round(86400/300) # calculate the num of datapoints based on interval between API endpoint access.

    if len(li) > num_datapoints:
        del li[0]

    return li





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


    '''

class MainView(Widget):

    currenttemp = ObjectProperty(None)
    currenthilo = ObjectProperty(None)
    feelslike = ObjectProperty(None)
    weathericon = ObjectProperty(None)
    humidity = ObjectProperty(None)
    pressure = ObjectProperty(None)
    windspeed  = ObjectProperty(None)
    precipprob = ObjectProperty(None)
    d1day = ObjectProperty(None)
    d1icon = ObjectProperty(None)
    d1hi = ObjectProperty(None)
    d1lo = ObjectProperty(None)
    d2day = ObjectProperty(None)
    d2icon = ObjectProperty(None)
    d2hi = ObjectProperty(None)
    d2lo = ObjectProperty(None)
    d3day = ObjectProperty(None)
    d3icon = ObjectProperty(None)
    d3hi = ObjectProperty(None)
    d3lo = ObjectProperty(None)
    d4day = ObjectProperty(None)
    d4icon = ObjectProperty(None)
    d4hi = ObjectProperty(None)
    d4lo = ObjectProperty(None)
    d5day = ObjectProperty(None)
    d5icon = ObjectProperty(None)
    d5hi = ObjectProperty(None)
    d5lo = ObjectProperty(None)
    d6day = ObjectProperty(None)
    d6icon = ObjectProperty(None)
    d6hi = ObjectProperty(None)
    d6lo = ObjectProperty(None)
    forecast = ObjectProperty(None)
    riseset = ObjectProperty(None)

    def determine_icon(self, string):

        # this is used to determine the icon for each day (including current conditions).
        if string == 'clear-day':
            bell = 'image/sunny.png'
        elif string == 'cloudy':
            bell = 'image/cloudy.png'
        elif string == 'rain':
            bell = 'image/rainy.png'
        elif string == 'partly-cloudy-day':
            bell = 'image/partlycloudy.png'
        elif string == 'clear-night':
            bell = 'image/nightclear.png'
        elif string == 'partly-cloudy-night':
            bell = 'image/nightclear.png'
        elif string == 'sleet':
            bell = 'image/snow.png'
        elif string == 'snow':
            bell = 'image/snow.png'
        elif string == 'wind':
            bell = 'image/wind.png'
        elif string == 'fog':
            bell = 'image/cloudy.png'

        return bell

    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.update(0)
        Clock.schedule_interval(self.update, 300)

    def determine_icon(self, string):
        if string == 'clear-day':
            bell = 'image/sunny.png'
        elif string == 'cloudy':
            bell = 'image/cloudy.png'
        elif string == 'rain':
            bell = 'image/rainy.png'
        elif string == 'partly-cloudy-day':
            bell = 'image/partlycloudy.png'
        elif string == 'clear-night':
            bell = 'image/nightclear.png'
        elif string == 'partly-cloudy-night':
            bell = 'image/nightclear.png'
        elif string == 'sleet':
            bell = 'image/snow.png'
        elif string == 'snow':
            bell = 'image/snow.png'
        elif string == 'wind':
            bell = 'image/wind.png'
        elif string == 'fog':
            bell = 'image/cloudy.png'

        return bell

    
    
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
        

        self.currenthilo.text = ' ' + str(json_data['daily']['data'][0]['temperatureHigh']) + ' | ' + str(json_data['daily']['data'][0]['temperatureLow'])
        self.currenttemp.text = str(json_data['currently']['temperature']) + ' F'
        self.feelslike.text = ' ' + str(json_data['currently']['apparentTemperature']) + ' F'
        self.windspeed.text = str(json_data['currently']['windSpeed']) + ' mph '
        #self.windgust.text = str(json_data['currently']['windGust']) + ' mph'
        self.humidity.text = str(round(json_data['currently']['humidity']* 100)) + ' %  '
        self.pressure.text = str(json_data['currently']['pressure']) + ' hPa '
        self.precipprob.text = ' ' + str(json_data['currently']['precipProbability'])+ '%'
        #self.riseset.text = ' ' + str(datetime.utcfromtimestamp(int(json_data['daily']['data'][0]['sunsetTime'])).strftime('%H:%M'))
        self.forecast.text = str(json_data['daily']['data'][0]['summary'])

        self.weathericon.source = str(self.determine_icon(json_data['currently']['icon']))


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
        d6 = json_data['daily']['data'][6]


        self.d1day.text = str(datetime.utcfromtimestamp(int(d1['time'])).strftime('%A'))[:3]
        self.d1icon.source = str(self.determine_icon(d1['icon']))
        self.d1hi.text = str(d1['temperatureHigh'])
        self.d1lo.text = str(d1['temperatureLow'])

        self.d2day.text = str(datetime.utcfromtimestamp(int(d2['time'])).strftime('%A'))[:3]
        self.d2icon.source = str(self.determine_icon(d2['icon']))
        self.d2hi.text = str(d2['temperatureHigh'])
        self.d2lo.text = str(d2['temperatureLow'])

        self.d3day.text = str(datetime.utcfromtimestamp(int(d3['time'])).strftime('%A'))[:3]
        self.d3icon.source = str(self.determine_icon(d3['icon']))
        self.d3hi.text = str(d3['temperatureHigh'])
        self.d3lo.text = str(d3['temperatureLow'])

        self.d4day.text = str(datetime.utcfromtimestamp(int(d4['time'])).strftime('%A'))[:3]
        self.d4icon.source = str(self.determine_icon(d4['icon']))
        self.d4hi.text = str(d4['temperatureHigh'])
        self.d4lo.text = str(d4['temperatureLow'])

        self.d5day.text = str(datetime.utcfromtimestamp(int(d5['time'])).strftime('%A'))[:3]
        self.d5icon.source = str(self.determine_icon(d5['icon']))
        self.d5hi.text = str(d5['temperatureHigh'])
        self.d5lo.text = str(d5['temperatureLow'])

        self.d6day.text = str(datetime.utcfromtimestamp(int(d6['time'])).strftime('%A'))[:3]
        self.d6icon.source = str(self.determine_icon(d6['icon']))
        self.d6hi.text = str(d6['temperatureHigh'])
        self.d6lo.text = str(d6['temperatureLow'])

        

    


                                      
  


class hello(App):
    def build(self):
        return MainView()

hello().run()
