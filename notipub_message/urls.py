from django.conf.urls import *

urlpatterns = patterns('notipub_message.views',
    url(r'^notipub$', 'home', name='home'),
    url(r'^register_token$', 'register_token', name='register_token'),
)
