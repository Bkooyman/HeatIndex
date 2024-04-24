from flask import Flask
from flask import render_template
from datetime import datetime
from flask import g
from model import WeatherClient
from heatindex import *
app = Flask(__name__)

weather_client = WeatherClient()

@app.route('/')
def home():
    g.riskLevelsDict = {
    "No Risk": "noRisk-color",
    "Minor": "minor-color",
    "Moderate": "moderate-color",
    "Major": "major-color",
    "Extreme": "extreme-color",
    }
    humidity = weather_client.get_current_humidity()
    temperature = weather_client.get_current_temperature()
    hi = calculate_HI(temperature, humidity)
    risk_level = get_risk_level(hi)
    return render_template('home.html', humidity=humidity, temperature=temperature, hi=hi, risk_level=risk_level)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/norisk')
def norisk():
    return render_template('noRisk.html')

@app.route('/minor')
def minor():
    return render_template('minor.html')

@app.route('/moderate')
def moderate():
    return render_template('moderate.html')

@app.route('/major')
def major():
    return render_template('major.html')

@app.route('/extreme')
def extreme():
    return render_template('extreme.html')

@app.route('/forecast')
def forecast():
    forecast = weather_client.get_HI_forecast()
    return render_template('forecast.html', forecast= forecast)
