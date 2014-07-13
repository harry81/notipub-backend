# encoding: utf-8

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from gcm import GCM, GCMNotRegisteredException

from notipub_message.models import DeviceToken


class Command(BaseCommand):
    def handle(self, *args, **options):
        gcm = GCM(settings.GOOGLE_API_KEY)

        for reg_id in set(DeviceToken.objects.all().values_list('token', flat=True)):
            payload = {}
            payload['message']=u"서울은 맑음"
            payload['msgcnt']="3"
            payload['timeStamp']="2014 07 03 20 20 00."
            try:
                canonical_id = gcm.plaintext_request(registration_id=reg_id, data=payload)
                token = DeviceToken.objects.filter(registration_id=reg_id)
                token.registration_id = canonical_id
                token.save()
                self.stdout.write('Sent to [%s].' % reg_id, ending='')
            except GCMNotRegisteredException:
                token = DeviceToken.objects.filter(registration_id=reg_id)
                token.delete()
                self.stdout.write('Deleted  [%s].' % reg_id, ending='')

    

