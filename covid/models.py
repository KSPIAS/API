from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.name
    
# class apilogin(models.Model):
#     name = models.CharField(max_length=100)
#     pwd = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name