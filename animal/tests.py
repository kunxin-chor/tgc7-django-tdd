from django.test import TestCase
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

