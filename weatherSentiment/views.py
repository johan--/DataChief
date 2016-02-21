from django.http import HttpResponse
from django.template import loader
from weatherManager import WeatherManager
from twitterManager import TwitterManager
from weatherSentiment.models import Weather, Location

def index(request):
    TwitterManager.start_stream([])
    WeatherManager.weather_run()
    context = {}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def get_data(request):
    context = {}
    weather_data = Weather.objects.all()
    print weather_data
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))