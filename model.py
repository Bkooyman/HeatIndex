
import requests
from heatindex import *

class WeatherClient(object):
    def __init__(self):
        # hard-coded College Park, MD lat/long https://api.weather.gov/points/38.9967,-76.9275
        # could make this dynamic to any location, but proj det. only UMDCP
        self.sess = requests.Session()
        self.base_url = 'https://api.weather.gov/gridpoints/LWX/100,76/forecast'

    def get_current_temperature(self):
        """
        returns the current temperature in F
        """
        resp = self.sess.get(self.base_url)
        return resp.json()['properties']['periods'][0]['temperature']
    
    def get_current_humidity(self):
        """
        returns the current humidity in "wmoUnit:percent"
        e.g. "64"
        """
        resp = self.sess.get(self.base_url)
        return resp.json()['properties']['periods'][0]['relativeHumidity']['value']
        
    def get_HI_forecast(self):
        """
        returns the week forecast for temp and humidity
        """
        # creates a list of dictionaries (maps)
        forecast = []
        resp = self.sess.get(self.base_url)
        for period in resp.json()['properties']['periods']:
            name = period['name']
            temperature = period['temperature']
            humidity = period['relativeHumidity']['value']
            heatIndex = calculate_HI(temperature, humidity)
            riskLevel = get_risk_level(heatIndex)
            icon = period['icon']
            shortForecast = period['shortForecast']
            detailedForecast = period['detailedForecast']
            forecast.append({'name': name,
                              'temperature': temperature, 
                              'humidity': humidity, 
                              'heatIndex': heatIndex, 
                              'riskLevel': riskLevel, 
                              'icon': icon, 
                              'shortForecast': shortForecast,  
                              'detailedForecast': detailedForecast})
        return forecast


