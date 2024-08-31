from django.db import models
from django.utils import timezone

# Create your models here.
# class apilogin(models.Model):
#     content = models.TextField()


class apilogin(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)

    class Meta:
        db_table = 'apilogin'
        managed = False

    def __str__(self):
        return self.name

class api_request(models.Model):
    request_id = models.CharField(max_length=100, primary_key=True)
    city = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    language = models.CharField(max_length=20)
    unit = models.CharField(max_length=10)
    # data_date = models.DateTimeField(auto_now_add=True)
    data_date = models.DateTimeField(auto_now_add=False)
    
    class Meta:
        db_table = 'api_request'
        managed = False

    def __str__(self):
        return self.request_id
    
class api_location(models.Model):
    location_id = models.CharField(max_length=100, primary_key=True)
    request_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    timezone_id = models.CharField(max_length=50)
    local_time = models.DateTimeField()
    localtime_epoch = models.CharField(max_length=50)
    utc_offset = models.CharField(max_length=10)
    data_date = models.DateTimeField()

    class Meta:
        db_table = 'api_location'
        managed = False

    def __str__(self):
        return self.location_id
 
class api_current(models.Model):
    current_id = models.CharField(max_length=100, primary_key=True)
    request_id = models.CharField(max_length=100)
    observation_time = models.CharField(max_length=20)
    temperature = models.IntegerField()
    weather_code = models.IntegerField()
    weather_icons = models.CharField(max_length=255)
    weather_descriptions = models.CharField(max_length=100)
    wind_speed = models.IntegerField()
    wind_degree = models.IntegerField()
    wind_dir = models.CharField(max_length=50)
    pressure = models.IntegerField()
    precip = models.IntegerField()
    humidity = models.IntegerField()
    cloudcover = models.IntegerField()
    feelslike = models.IntegerField()
    uv_index = models.IntegerField()
    visibility = models.IntegerField()
    is_day = models.CharField(max_length=10)
    data_date = models.DateTimeField()

    class Meta:
        db_table = 'api_current'
        managed = False

    def __str__(self):
        return self.current_id