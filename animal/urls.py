from django.urls import path
import animal.views


urlpatterns = [
    path('create/', animal.views.create_animal),
    path('update/<animal_id>/', animal.views.update_animal)
]
