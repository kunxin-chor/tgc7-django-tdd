from django.db import models

# Create your models here.


class Animal(models.Model):
    name = models.CharField(blank=False, max_length=255)
    breed = models.CharField(blank=False, max_length=255)
