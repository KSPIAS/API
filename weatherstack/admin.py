from django.contrib import admin
from weatherstack.models import apilogin ,api_request

# Register your models here.
admin.site.register(apilogin)
admin.site.register(api_request)