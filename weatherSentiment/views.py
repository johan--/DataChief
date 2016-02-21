from django.http import HttpResponse
from django.template import loader
from weatherManager import WeatherManager
from twitterManager import TwitterManager

def index(request):
    # TwitterManager.start_stream([])
    # WeatherManager.weather_run()
    context = {}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))