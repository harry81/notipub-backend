from django.contrib import admin
from notipub_message.models import DeviceToken

class DeviceTokenAdmin(admin.ModelAdmin):
    ordering = ['-created_at']

admin.site.register(DeviceToken ,DeviceTokenAdmin)
