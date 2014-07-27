# encoding: utf-8
import urllib, urllib2
import json
from django.conf import settings

def get_district(lat, lng):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    values = {'latlng' : '%s,%s' % (lat, lng),
              'language' : 'ko'
              }

    data = urllib.urlencode(values)
    req = urllib2.Request(url + data)
    
    _response = urllib2.urlopen(req)
    response = json.loads(_response.read())
    if response['status'] == u'OK':
        ret = "%s %s" % (response['results'][1]['address_components'][0]['short_name'], response['results'][0]['address_components'][0]['short_name']
    )
    else:
        ret = "None"

    return ret


def get_weathersummary(lat, lng):
    url = "https://api.forecast.io/forecast/%s/%s,%s" % (settings.FORECAST_IO_KEY, lat, lng)

    req = urllib2.Request(url)
    
    _response = urllib2.urlopen(req)
    response = json.loads(_response.read())

    return response.has_key('currently'), response['currently']['summary']
