from django.http import HttpResponse
import TwitterParse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")