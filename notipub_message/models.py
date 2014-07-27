from django.db import models
from datetime import datetime, timedelta

from dowant.lib.logs import logs as logging
logger = logging.get_logger(__name__)

class DeviceToken(models.Model):
    token = models.TextField(null=False, default='')
    uuid = models.TextField(null=True, default='')
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['-created_at']

    def __unicode__(self):
        return self.uuid

