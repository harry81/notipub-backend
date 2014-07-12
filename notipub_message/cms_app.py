from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class Notipub(CMSApp):
    name = _("Notipub")
    urls = ["notipub_message.urls"]

apphook_pool.register(Notipub)
