# encoding: utf-8

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from gcm import GCM

from notipub_message.models import DeviceToken


class Command(BaseCommand):
    def handle(self, *args, **options):
        gcm = GCM(settings.GOOGLE_API_KEY)

        for token in set(DeviceToken.objects.all().values_list('token', flat=True)):
            payload = {}
            payload['message']=u"서울은 맑음"
            payload['msgcnt']="3"
            payload['timeStamp']="2014 07 03 20 20 00."
            print 'Sented to [%s].' % token
            gcm.plaintext_request(registration_id=reg_id, data=payload)
    

