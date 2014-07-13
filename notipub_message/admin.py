from django.contrib import admin
from notipub_message.models import DeviceToken

class DeviceTokenAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'token', 'created_at', 'lat', 'lng')
    ordering = ['-created_at']

admin.site.register(DeviceToken ,DeviceTokenAdmin)
