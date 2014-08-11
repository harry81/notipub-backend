# encoding: utf-8

import time
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from gcm import GCM

from notipub_message.models import DeviceToken
from notipub_message.helper import get_district, get_weathersummary


class Command(BaseCommand):
    def handle(self, *args, **options):
        gcm = GCM(settings.GOOGLE_API_KEY)

        for uuid in set(DeviceToken.objects.all().values_list('uuid', flat=True)):
            tok = DeviceToken.objects.filter(uuid=uuid).order_by('created_at')[0]

            payload = {}
            payload['title']="%s" % (get_district(tok.lat, tok.lng))
            payload['message']= "%s " % (get_weathersummary(tok.lat, tok.lng)[1])
            payload['timeStamp']=str(time.time())
            payload['lat']=str(tok.lat)
            payload['lng']=str(tok.lng)
            payload['notId']="101"

            try:
                canonical_id = gcm.plaintext_request(registration_id=tok.token, data=payload)
                if canonical_id:
                    token = DeviceToken.objects.filter(token=tok.token)
                    token.token = canonical_id
                    token.save()
                    self.stdout.write('Sent to [%s].' % tok.token, ending='')
            except :

                token = DeviceToken.objects.filter(token=tok.token)
                token.delete()
                self.stdout.write('Deleted  [%s].' % tok.token, ending='')

    

