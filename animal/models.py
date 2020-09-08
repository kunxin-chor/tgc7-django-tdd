from django.db import models

# Create your models here.


class Animal(models.Model):
    name = models.CharField(blank=False, max_length=255)
    breed = models.CharField(blank=False, max_length=255)
    is_sterlized = models.BooleanField(blank=False, default=False)
    age = models.IntegerField(blank=True, default=1)
    gender = models.CharField(blank=False, max_length=1)
    vet = models.ForeignKey("Vet", on_delete=models.RESTRICT)
    microchip = models.CharField(blank=False, max_length=26)


class Vet(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    address = models.CharField(blank=False, max_length=255)
    years = models.IntegerField(blank=False, default=1)
    license = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Specie(models.Model):
    name = models.CharField(blank=False, max_length=100)
