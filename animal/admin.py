from django.contrib import admin

# Register your models here.
from .models import Animal, Vet

admin.site.register(Animal)
admin.site.register(Vet)
