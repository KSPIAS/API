from django.db import models
# from django.utils import timezone

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
    city = models.CharField(max_length=100 ,primary_key=True)
    type = models.CharField(max_length=100)
    language = models.CharField(max_length=20)
    unit = models.CharField(max_length=10)
    # data_date = models.DateTimeField(auto_now_add=True)
    data_date = models.DateTimeField(auto_now_add=False)
    
    class Meta:
        db_table = 'api_request'
        managed = False
    
    def __str__(self):
        return self.city