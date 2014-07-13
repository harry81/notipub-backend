from django.conf.urls import *

urlpatterns = patterns('notipub_message.views',
    url(r'^notipub$', 'home', name='home'),
    url(r'^notipub/register_token$', 'register_token', name='register_token'),
    url(r'^notipub/get_current_weather$', 'get_current_weather', name='get_current_weather'),
)
