import requests
import json
import time
import winsound
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
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

class MainView(GridLayout):
    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)

        self.cols = 1

        self.t = GridLayout()
        self.t.cols = 4

        self.l = GridLayout()
        self.l.cols = 1

        self.currenttemp = Label(text='test', font_size='40sp')
        self.l.add_widget(self.currenttemp)

        self.lbot = GridLayout()
        self.lbot.cols = 1
        
        self.currenthilo = Label(text='test')
        self.lbot.add_widget(self.currenthilo)
        self.feelslike = Label(text='test /n test')
        self.lbot.add_widget(self.feelslike)
        self.windspeed = Label(text='test')
        self.lbot.add_widget(self.windspeed)

        self.l.add_widget(self.lbot)

        self.t.add_widget(self.l)

        self.lmid = Label(text='')
        self.t.add_widget(self.lmid)

        self.rmid = Label(text='')
        self.t.add_widget(self.rmid)

        self.r = GridLayout()
        self.r.cols = 1

        self.weathericon = Image(source='image/sunny.png')
        self.r.add_widget(self.weathericon)

        self.rbot = GridLayout()
        self.rbot.cols = 1

        self.humidity = Label(text='test')
        self.rbot.add_widget(self.humidity)
        self.pressure = Label(text='test /n test')
        self.rbot.add_widget(self.pressure)
        self.placehold = Label(text='')
        self.rbot.add_widget(self.placehold)

        self.r.add_widget(self.rbot)

        self.t.add_widget(self.r)

        self.add_widget(self.t)

        self.update(1)
        Clock.schedule_interval(self.update, 300)

        '''
        self.cols = 2
        self.topleft = GridLayout()
        self.topleft.cols = 1
        self.currenthilo = Label(text='test')
        self.topleft.add_widget(self.currenthilo)
        self.currenttemp = Label(text="test", font_size='40sp')
        self.topleft.add_widget(self.currenttemp)

        self.feelslike = Label(text='test /n test')
        self.topleft.add_widget(self.feelslike)

        self.add_widget(self.topleft)

        self.weathericon = Image(source='image/sunny.png', size=(50,150))
        self.add_widget(self.weathericon)

        #self.add_widget(Label(text="  "))
        #self.add_widget(Label(text="  "))

        self.left = GridLayout()
        self.left.cols = 2

        #self.left.add_widget(Label(text="Feels Like: "))
        #self.feelslike = Label(text="test")
        #self.left.add_widget(self.feelslike)

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
        self.d1mid = Image(source='image/sunny.png', size=(25,25))
        self.r.add_widget(self.d1mid)

        self.d1right = GridLayout()
        self.d1right.cols = 1
        self.d1rt = Label(text='test')
        self.d1rb = Label(text='test')
        self.d1right.add_widget(self.d1rt)
        self.d1right.add_widget(self.d1rb)
        self.r.add_widget(self.d1right)
        

        self.d2left = Label(text='test')
        self.r.add_widget(self.d2left)
        self.d2mid = Image(source='image/sunny.png', size=(25,25))
        self.r.add_widget(self.d2mid)

        self.d2right = GridLayout()
        self.d2right.cols = 1
        self.d2rt = Label(text='test')
        self.d2rb = Label(text='test')
        self.d2right.add_widget(self.d2rt)
        self.d2right.add_widget(self.d2rb)
        self.r.add_widget(self.d2right)

        self.d3left = Label(text='test')
        self.r.add_widget(self.d3left)
        self.d3mid = Image(source='image/sunny.png', size=(25,25))
        self.r.add_widget(self.d3mid)

        self.d3right = GridLayout()
        self.d3right.cols = 1
        self.d3rt = Label(text='test')
        self.d3rb = Label(text='test')
        self.d3right.add_widget(self.d3rt)
        self.d3right.add_widget(self.d3rb)
        self.r.add_widget(self.d3right)

        self.d4left = Label(text='test')
        self.r.add_widget(self.d4left)
        self.d4mid = Image(source='image/sunny.png', size=(25,25))
        self.r.add_widget(self.d4mid)
        
        self.d4right = GridLayout()
        self.d4right.cols = 1
        self.d4rt = Label(text='test')
        self.d4rb = Label(text='test')
        self.d4right.add_widget(self.d4rt)
        self.d4right.add_widget(self.d4rb)
        self.r.add_widget(self.d4right)

        self.d5left = Label(text='test')
        self.r.add_widget(self.d5left)
        self.d5mid = Image(source='image/sunny.png', size=(25,25))
        self.r.add_widget(self.d5mid)

        self.d5right = GridLayout()
        self.d5right.cols = 1
        self.d5rt = Label(text='test')
        self.d5rb = Label(text='test')
        self.d5right.add_widget(self.d5rt)
        self.d5right.add_widget(self.d5rb)
        self.r.add_widget(self.d5right)
        

        self.add_widget(self.r)
        '''


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
        

        self.currenthilo.text = str(json_data['daily']['data'][0]['temperatureHigh']) + ' | ' + str(json_data['daily']['data'][0]['temperatureLow'])
        self.currenttemp.text = str(json_data['currently']['temperature']) + ' F'
        self.feelslike.text = 'Feels Like ' + str(json_data['currently']['apparentTemperature']) + ' F'
        self.windspeed.text = str(json_data['currently']['windSpeed']) + ' mph'
        #self.windgust.text = str(json_data['currently']['windGust']) + ' mph'
        self.humidity.text = str(round(json_data['currently']['humidity']* 100)) + '%'
        self.pressure.text = str(json_data['currently']['pressure']) + ' mb'
        #self.precipprob.text = str(json_data['currently']['precipProbability'])+ '%'


        # this determines the weather icon to be used.
        if json_data['currently']['icon'] == 'clear-day':
            self.weathericon.source = 'image/sunny.png'
        elif json_data['currently']['icon'] == 'cloudy':
            self.weathericon.source = 'image/cloudy.png'
        elif json_data['currently']['icon'] == 'rain':
            self.weathericon.source = 'image/rainy.png'
        elif json_data['currently']['icon'] == 'partly-cloudy-day':
            self.weathericon.source = 'image/partlycloudy.png'
        elif json_data['currently']['icon'] == 'clear-night':
            self.weathericon.source = 'image/nightclear.png'
        elif json_data['currently']['icon'] == 'partly-cloudy-night':
            self.weathericon.source = 'image/nightpartlycloudy.png'

        '''

        below are dictionaries containing values for each day. the needed values
        from each are time, summary, icon, precipProbability, temperatureHigh, temperatureLow,
        apparentTemperatureHigh, apparentTemperatureLow, dewPoint, humidity, pressure, windSpeed,
        windGust, windBearing.

        '''
    
        d1 = json_data['daily']['data'][1]
        print(json_data['daily']['data'])
        d2 = json_data['daily']['data'][2]
        d3 = json_data['daily']['data'][3]
        d4 = json_data['daily']['data'][4]
        d5 = json_data['daily']['data'][5]
        '''

        self.d1left.text = str(datetime.utcfromtimestamp(int(d1['time'])).strftime('%A'))
        #self.d1mid.text = " "
        self.d1rt.text = 'High    ' + str(d1['temperatureHigh'])
        self.d1rb.text = 'Low    ' + str(d1['temperatureLow'])

        self.d2left.text = str(datetime.utcfromtimestamp(int(d2['time'])).strftime('%A'))
        #self.d2mid.text = " "
        self.d2rt.text = 'High    ' + str(d2['temperatureHigh'])
        self.d2rb.text = 'Low    ' + str(d2['temperatureLow'])

        self.d3left.text = str(datetime.utcfromtimestamp(int(d3['time'])).strftime('%A'))
        #self.d3mid.text = " "
        self.d3rt.text = 'High    ' + str(d3['temperatureHigh'])
        self.d3rb.text = 'Low    ' + str(d3['temperatureLow'])

        self.d4left.text = str(datetime.utcfromtimestamp(int(d4['time'])).strftime('%A'))
        #self.d4mid.text = " "
        self.d4rt.text = 'High    ' + str(d4['temperatureHigh'])
        self.d4rb.text = 'Low    ' + str(d4['temperatureLow'])

        self.d5left.text = str(datetime.utcfromtimestamp(int(d5['time'])).strftime('%A'))
        #self.d5mid.text = " "
        self.d5rt.text = 'High    ' + str(d5['temperatureHigh'])
        self.d5rb.text = 'Low    ' + str(d5['temperatureLow'])
        '''

        


class hello(App):
    def build(self):
        return MainView()

hello().run()
