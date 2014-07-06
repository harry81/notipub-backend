from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from gcm import GCM



reg_id="APA91bGm4KBvvDdecHnp1vzLdFA3xxW8am1WZTxX0-Qwf6vUqpvhMS0pMCqX0TSJuocmaDPT7kQKTh2VU0eR0o9B0ZxECCHkpFoz97KD6K-vxxLBgQN4vROZL2QUG32qsf06XnM-3j36p3ZiX4GT7sri5qJu-fjfrw"

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("hello", ending='')
        gcm = GCM(settings.GOOGLE_API_KEY)
        payload = {}
        payload['message']="this is a message."
        payload['msgcnt']="4"
        payload['timeStamp']="2014 07 03 20 20 00."
        gcm.plaintext_request(registration_id=reg_id, data=payload)

    

