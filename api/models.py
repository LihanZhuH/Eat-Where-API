from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    rating = models.IntegerField(default=3)
