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

        self.currenttemp = Label(text='test', font_size='50sp')
        self.l.add_widget(self.currenttemp)

        self.lbot = GridLayout()
        self.lbot.cols = 1
        
        self.currenthilo = Label(text='test')
        self.lbot.add_widget(self.currenthilo)
        self.feelslike = Label(text='test /n test')
        self.lbot.add_widget(self.feelslike)
        self.pl = Label(text='')
        self.lbot.add_widget(self.pl)

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
        self.windspeed = Label(text='')
        self.rbot.add_widget(self.windspeed)

        self.r.add_widget(self.rbot)

        self.t.add_widget(self.r)

        self.add_widget(self.t)

        self.b = GridLayout()
        self.b.cols = 6

        self.d1 = GridLayout()
        self.d1.cols = 1

        self.d1sp3 = Label(text='')
        self.d1.add_widget(self.d1sp3)

        self.d1day = Label(text='test', bold=True, font_size='20sp')
        self.d1.add_widget(self.d1day)

        self.d1icon = Image(source='image/sunny.png')
        self.d1.add_widget(self.d1icon)

        self.d1sp1 = Label(text='')
        self.d1.add_widget(self.d1sp1)

        self.d1hi = Label(text='tet')
        self.d1.add_widget(self.d1hi)

        self.d1sp2 = Label(text='')
        self.d1.add_widget(self.d1sp2)

        self.d1lo = Label(text='tet')
        self.d1.add_widget(self.d1lo)

        self.b.add_widget(self.d1)


        self.d2 = GridLayout()
        self.d2.cols = 1

        self.d2sp3 = Label(text='')
        self.d2.add_widget(self.d2sp3)

        self.d2day = Label(text='test', bold=True, font_size='20sp')
        self.d2.add_widget(self.d2day)

        self.d2icon = Image(source='image/sunny.png')
        self.d2.add_widget(self.d2icon)

        self.d2sp1 = Label(text='')
        self.d2.add_widget(self.d2sp1)

        self.d2hi = Label(text='tet')
        self.d2.add_widget(self.d2hi)

        self.d2sp2 = Label(text='')
        self.d2.add_widget(self.d2sp2)

        self.d2lo = Label(text='tet')
        self.d2.add_widget(self.d2lo)

        self.b.add_widget(self.d2)


        self.d3 = GridLayout()
        self.d3.cols = 1

        self.d3sp3 = Label(text='')
        self.d3.add_widget(self.d3sp3)

        self.d3day = Label(text='test', bold=True, font_size='20sp')
        self.d3.add_widget(self.d3day)

        self.d3icon = Image(source='image/sunny.png')
        self.d3.add_widget(self.d3icon)

        self.d3sp1 = Label(text='')
        self.d3.add_widget(self.d3sp1)

        self.d3hi = Label(text='tet')
        self.d3.add_widget(self.d3hi)

        self.d3sp2 = Label(text='')
        self.d3.add_widget(self.d3sp2)

        self.d3lo = Label(text='tet')
        self.d3.add_widget(self.d3lo)

        self.b.add_widget(self.d3)


        self.d4 = GridLayout()
        self.d4.cols = 1

        self.d4sp3 = Label(text='')
        self.d4.add_widget(self.d4sp3)

        self.d4day = Label(text='test', bold=True, font_size='20sp')
        self.d4.add_widget(self.d4day)

        self.d4icon = Image(source='image/sunny.png')
        self.d4.add_widget(self.d4icon)

        self.d4sp1 = Label(text='')
        self.d4.add_widget(self.d4sp1)

        self.d4hi = Label(text='tet')
        self.d4.add_widget(self.d4hi)

        self.d4sp2 = Label(text='')
        self.d4.add_widget(self.d4sp2)

        self.d4lo = Label(text='tet')
        self.d4.add_widget(self.d4lo)

        self.b.add_widget(self.d4)


        self.d5 = GridLayout()
        self.d5.cols = 1

        self.d5sp3 = Label(text='')
        self.d5.add_widget(self.d5sp3)

        self.d5day = Label(text='test', bold=True, font_size='20sp')
        self.d5.add_widget(self.d5day)

        self.d5icon = Image(source='image/sunny.png')
        self.d5.add_widget(self.d5icon)

        self.d5sp1 = Label(text='')
        self.d5.add_widget(self.d5sp1)

        self.d5hi = Label(text='tet')
        self.d5.add_widget(self.d5hi)

        self.d5sp2 = Label(text='')
        self.d5.add_widget(self.d5sp2)

        self.d5lo = Label(text='tet')
        self.d5.add_widget(self.d5lo)

        self.b.add_widget(self.d5)


        self.d6 = GridLayout()
        self.d6.cols = 1

        self.d6sp3 = Label(text='')
        self.d6.add_widget(self.d6sp3)

        self.d6day = Label(text='test', bold=True, font_size='20sp')
        self.d6.add_widget(self.d6day)

        self.d6icon = Image(source='image/sunny.png')
        self.d6.add_widget(self.d6icon)

        self.d6sp1 = Label(text='')
        self.d6.add_widget(self.d6sp1)

        self.d6hi = Label(text='tet')
        self.d6.add_widget(self.d6hi)

        self.d6sp2 = Label(text='')
        self.d6.add_widget(self.d6sp2)

        self.d6lo = Label(text='tet')
        self.d6.add_widget(self.d6lo)

        self.b.add_widget(self.d6)

        
        self.add_widget(self.b)

        self.update(1)
        Clock.schedule_interval(self.update, 300)


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
        self.feelslike.text = 'Feels Like: ' + str(json_data['currently']['apparentTemperature']) + ' F'
        self.windspeed.text = 'Wind speed: ' + str(json_data['currently']['windSpeed']) + ' mph'
        #self.windgust.text = str(json_data['currently']['windGust']) + ' mph'
        self.humidity.text = 'Humidity: ' + str(round(json_data['currently']['humidity']* 100)) + '%'
        self.pressure.text = 'Pressure: ' + str(json_data['currently']['pressure']) + ' mb'
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
        d2 = json_data['daily']['data'][2]
        d3 = json_data['daily']['data'][3]
        d4 = json_data['daily']['data'][4]
        d5 = json_data['daily']['data'][5]
        d6 = json_data['daily']['data'][6]



        self.d1day.text = str(datetime.utcfromtimestamp(int(d1['time'])).strftime('%A'))[:3]
        #self.d1icon.source =
        self.d1hi.text = str(d1['temperatureHigh'])
        self.d1lo.text = str(d1['temperatureLow'])

        self.d2day.text = str(datetime.utcfromtimestamp(int(d2['time'])).strftime('%A'))[:3]
        #self.d2icon.source =
        self.d2hi.text = str(d2['temperatureHigh'])
        self.d2lo.text = str(d2['temperatureLow'])

        self.d3day.text = str(datetime.utcfromtimestamp(int(d3['time'])).strftime('%A'))[:3]
        #self.d3icon.source =
        self.d3hi.text = str(d3['temperatureHigh'])
        self.d3lo.text = str(d3['temperatureLow'])

        self.d4day.text = str(datetime.utcfromtimestamp(int(d4['time'])).strftime('%A'))[:3]
        #self.d4icon.source =
        self.d4hi.text = str(d4['temperatureHigh'])
        self.d4lo.text = str(d4['temperatureLow'])

        self.d5day.text = str(datetime.utcfromtimestamp(int(d5['time'])).strftime('%A'))[:3]
        #self.d5icon.source =
        self.d5hi.text = str(d5['temperatureHigh'])
        self.d5lo.text = str(d5['temperatureLow'])

        self.d6day.text = str(datetime.utcfromtimestamp(int(d6['time'])).strftime('%A'))[:3]
        #self.d6icon.source =
        self.d6hi.text = str(d6['temperatureHigh'])
        self.d6lo.text = str(d6['temperatureLow'])
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
