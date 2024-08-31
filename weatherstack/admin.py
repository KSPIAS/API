from django.contrib import admin
from weatherstack.models import apilogin ,api_request ,api_location ,api_current

# Register your models here.
admin.site.register(apilogin)
admin.site.register(api_request)
admin.site.register(api_location)
admin.site.register(api_current)