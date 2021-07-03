from django.db import models

# Create your models here.

class Cafe(models.Model):
    name = models.CharField(max_length=15)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    