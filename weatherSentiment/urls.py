from django.conf.urls import url
from django.conf.urls import patterns
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [

    url(r'^data/$', views.get_data, name='get_data'),
    url(r'^demo/$', views.index, name='demo'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),

]
