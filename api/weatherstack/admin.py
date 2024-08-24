from django.contrib import admin
from weatherstack.models import apilogin ,apilogins ,api_request

# Register your models here.
admin.site.register(apilogin)
admin.site.register(apilogins)
admin.site.register(api_request)