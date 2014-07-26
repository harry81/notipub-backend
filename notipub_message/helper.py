# encoding: utf-8
import urllib, urllib2
import json

def get_district(lat, lng):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {'latlng' : '%s,%s' % (lat, lng)}
    headers = { 'User-Agent' : user_agent }

    data = urllib.urlencode(values)
    req = urllib2.Request(url + data, None, headers)
    
    response = urllib2.urlopen(req)
    the_page = response.read()

    return u"서울"

def get_weathersummary(lat, lng):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {'latlng' : '%s,%s' % (lat, lng)}
    headers = { 'User-Agent' : user_agent }

    data = urllib.urlencode(values)
    req = urllib2.Request(url + data, None, headers)
    
    response = urllib2.urlopen(req)
    the_page = response.read()

    return 'hot'
