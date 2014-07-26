# encoding: utf-8
from django.test import TestCase
from .helper import get_district, get_weathersummary

# Create your tests here.
class NotipubTests(TestCase):
    def test_get_district(self):
        lat = 37.4978062
        lng = 127.0026627
        
        self.assertEqual(get_district(lat, lng), u"서울")

    def test_get_weathersummary(self):
        lat = 37.4978062
        lng = 127.0026627
        
        self.assertEqual(get_weathersummary(lat, lng), "warm")
