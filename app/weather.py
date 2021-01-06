"""Weather data parser."""
import logging
import sys
import time
from datetime import datetime, timedelta
from itertools import groupby

import requests

API_KEY = '<your api key>'

PLACE = '<your city>'
UNITS = 'metric'

API_URL = f'http://api.openweathermap.org/data/2.5/forecast?q={PLACE}&appid={API_KEY}&units={UNITS}'
IMG_URL = 'http://openweathermap.org/img/wn/{}@2x.png'

IDS = ['date', 'day', 'maxtemp', 'mintemp', 'morning', 'afternoon', 'evening', 'rain']
PRE = ['', '', 'max ', 'min ', '', '', '', 'static/img/umbrella.png']
POST = ['', '', u'\u00B0', u'\u00B0', 'Morning', 'Afternoon', 'Evening/Night', ' %']

NEXT_DAY_HOUR = 18

CURRENT = None
LAST_UPDATED = 0


def get_ids():
    return cw.IDS if 'custom_weather' in sys.modules else IDS

def get_pre():
    return cw.PRE if 'custom_weather' in sys.modules else PRE

def get_post():
    return cw.POST if 'custom_weather' in sys.modules else POST


def get_icon_links(weather_data, start_time=0):
    """Returns links for weather icons."""
    icons = [min(day, key=lambda x: (x['datetime'].hour - start_time) % 24)['weather'][0]['icon']
             for day in weather_data]
    return [IMG_URL.format(icon) for icon in icons]


def get_openweather_data():
    """Gathers weather data and returns the required list."""
    response = requests.get(API_URL).json()
    weather_data = response['list']

    # Add date info
    for entry in weather_data:
        entry['date'] = datetime.fromtimestamp(entry['dt']).date()
        entry['datetime'] = datetime.fromtimestamp(entry['dt'])

    # Determine first and last day
    dt_now = datetime.now()
    first_day = dt_now + timedelta(1) if dt_now.hour >= NEXT_DAY_HOUR else dt_now
    last_day = first_day + timedelta(4)

    weather_data = [e for e in weather_data if e['date'] >= first_day.date()]
    weather_data = [e for e in weather_data if e['date'] < last_day.date()]

    # Group by day
    weather_data = [list(g[1]) for g in groupby(weather_data, lambda e: e['date'])]

    # Gather data
    dates = [day[0]['date'].strftime('%d.%m.') for day in weather_data]
    weekdays = [day[0]['date'].strftime('%A') for day in weather_data]

    max_temps = [round(max(day, key=lambda x: x['main']['temp_max'])['main']['temp_max'])
                 for day in weather_data]
    min_temps = [round(min(day, key=lambda x: x['main']['temp_min'])['main']['temp_min'])
                 for day in weather_data]

    mornings = get_icon_links(weather_data, start_time=9)
    afternoons = get_icon_links(weather_data, start_time=14)
    evenings = get_icon_links(weather_data, start_time=18)

    precipitations = [round(max(day, key=lambda x: x['pop'])['pop'] * 100)
                      for day in weather_data]

    return [dates, weekdays, max_temps, min_temps, mornings, afternoons, evenings, precipitations]


def get_data():
    """Updates and returns weather data."""
    global CURRENT
    global LAST_UPDATED

    if time.time() - LAST_UPDATED < 300:
        return CURRENT

    get_weather_data = cw.get_data if 'custom_weather' in sys.modules else get_openweather_data

    try:
        CURRENT = get_weather_data()
    except Exception as exc:
        logging.error('Failed to retrieve weather data: %s', exc)
        return []

    LAST_UPDATED = time.time()

    return CURRENT

try:
    import custom_weather as cw
except ModuleNotFoundError:
    logging.info('Using default weather module.')
