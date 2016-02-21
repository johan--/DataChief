import urllib2
import json
import time
from models import Location, Weather


class WeatherManager:
    def __init__(self):
        pass

    @staticmethod
    def weather_run():
        count=0
        for location in Location.objects.all():
            weather_base = 'http://api.wunderground.com/api/e1fde55153190b2a/geolookup/conditions/q/'
            url = weather_base + urllib2.quote(location.state_name) + '/' + urllib2.quote(location.city_name) + '.json'
            count += 1
            print count
            f = urllib2.urlopen(url)
            json_string = f.read()
            parsed_json = json.loads(json_string)
            if 'current_observation' in parsed_json:
                wind = parsed_json['current_observation']['precip_today_in']
                feels_like = parsed_json['current_observation']['feelslike_f']
                weather = parsed_json['current_observation']['weather']
                try:
                    float(parsed_json['current_observation']['precip_today_in'])
                    precipitation = float(parsed_json['current_observation']['precip_today_in'])
                except ValueError:
                    print 'Not string value'
                temperature = parsed_json['current_observation']['temp_f']
                try:
                    int(parsed_json['current_observation']['observation_epoch'])
                    datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(int(parsed_json['current_observation']['observation_epoch'])/1000))
                except ValueError:
                    print 'Not Integer value'
                print wind, precipitation, temperature, weather, datetime
                weather = Weather(wind=wind, precipitation=precipitation, temperature=temperature, weather=weather,
                            feels_like=feels_like, datetime=datetime)
                weather.location_id = location.id
                weather.save()