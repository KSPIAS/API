from django.db import models

# Create your models here.
class apilogin(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class apilogins(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class api_request(models.Model):
    type = models.CharField(max_length=100)
    query = models.CharField(max_length=100)
    language = models.CharField(max_length=20)
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.query