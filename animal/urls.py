from django.urls import path
import animal.views


urlpatterns = [
    path('create/', animal.views.create_animal)
]
