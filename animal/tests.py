from django.test import TestCase
from django.shortcuts import get_object_or_404

from .models import Animal


# Create your tests here.
class AnimalModelTestCase(TestCase):

    def test_create_animal_model(self):
        a = Animal()
        a.name = "Fluffy"
        a.breed = "Golden Retriever"
        a.is_sterlized = False
        a.age = 8
        a.gender = "M"

        a.save()

        self.assertTrue(a.id > 0)
        saved_animal = get_object_or_404(Animal, pk=a.id)
        self.assertTrue(saved_animal is not None)

        self.assertEqual(saved_animal.name, "Fluffy")
        self.assertEqual(saved_animal.breed, "Golden Retriever")
        self.assertEqual(saved_animal.is_sterlized, False)
        self.assertEqual(saved_animal.age, 8)
        self.assertEqual(saved_animal.gender, "M")


