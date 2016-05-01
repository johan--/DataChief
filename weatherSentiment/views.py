from django.http import HttpResponse
from django.template import loader
from WeatherManager import WeatherManager
from TwitterManager import TwitterManager
from weatherSentiment.models import Weather, Location

def index(request):
    TwitterManager.start_stream([])
    WeatherManager.weather_run()
    context = {}
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render(context, request))

def get_data(request):
    context = {}
    weathers = Weather.objects.all()
    for weather in weathers:
        print weather.wind
        print weather.precipitation
        print weather.temperature
        print weather.weather
        print weather.location_id
        location = Location.objects.get(id=weather.location_id)
        print location.city_name
        print location.state_name
        print location.zip
        print location.lat
        print location.lng
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))