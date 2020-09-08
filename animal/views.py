from django.shortcuts import render, HttpResponse, get_object_or_404

from .forms import AnimalForm
from .models import Animal
# Create your views here.


def create_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Animal is added")
        else:
            return render(request, 'animal/create_animal.template.html', {
                'form': form
            })
    else:
        form = AnimalForm()

        return render(request, 'animal/create_animal.template.html', {
            'form': form
        })


def update_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    if request.method == "POST":
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return HttpResponse("Animal updated")
        else:
            return render(request, 'animal/update_animal.template.html', {
                'form': form
            })
    else:

        form = AnimalForm(instance=animal)
        return render(request, 'animal/update_animal.template.html', {
            'form': form
        })
