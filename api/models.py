from django.db import models

# Create your models here.

class Admission(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True) 
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    amount = models.IntegerField(max_length=10, blank=True)
     

