import json

import requests

from settings import config

def get_msk_forecast():
    payload = {
        'lat' : '55.75396',
        'lon': '37.620393'
    }
    weather_key = {'X-Yandex-API-Key': config.YANDEX_API_TOKEN}
    r = requests.get('https://api.weather.yandex.ru/v2/forecast', params=payload, headers=weather_key)
    weather_data = json.loads(r.text)
    return weather_data['fact']

print(get_msk_forecast())