from django.shortcuts import render, HttpResponse

from .forms import AnimalForm
# Create your views here.


def create_animal(self):
    form = AnimalForm()

    return render(self, 'animal/create_animal.template.html', {
        'form': form
    })
