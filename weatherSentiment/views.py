from django.http import HttpResponse
from Weather import WeatherManager

def index(request):
    WeatherManager.weather_run()
    return HttpResponse("Hello, world. You're at the polls index.")