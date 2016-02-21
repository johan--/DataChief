import urllib2
import json
import time
from models import Location, Weather


class WeatherManager:
    def __init__(self):
        pass

    @staticmethod
    def weather_run():
        for location in Location.objects.all():
            weather_base = 'http://api.wunderground.com/api/e1fde55153190b2a/geolookup/conditions/q/'
            url = weather_base + urllib2.quote(location.city_name) + '/' + urllib2.quote(location.state_name) + '.json'
            print url
            f = urllib2.urlopen(url)
            json_string = f.read()
            parsed_json = json.loads(json_string)
            wind = parsed_json['current_observation']['precip_today_in']
            feels_like = parsed_json['current_observation']['feelslike_f']
            weather = parsed_json['current_observation']['weather']
            precipitation = float(parsed_json['current_observation']['precip_today_in'])
            temperature = parsed_json['current_observation']['temp_f']
            datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(int(parsed_json['current_observation']['observation_epoch'])/1000))
            print wind, precipitation, temperature, weather
            weather = Weather(wind=wind, precipitation=precipitation, temperature=temperature, weather=weather,
                        feels_like=feels_like, datetime=datetime)
            weather.location_id = location.id
            weather.save()