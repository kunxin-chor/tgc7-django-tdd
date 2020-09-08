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


class VetModelTestCase(TestCase):

    def test_years_in_practise_should_default_to_one(self):
        v = Vet()
        v.first_name = "Tan"
        v.last_name = "Ah Kow"
        v.address = "Yishun Ring Road"
        v.license = "ABC1234X"
        v.save()

        saved_vet = get_object_or_404(Vet, pk=id)
        self.assertEqual(saved_vet.years, 1)

    def test_it_should_have_first_name(self):
        v = Vet()
        v.last_name = "Ah Kow"
        v.address = "Yishun Ring Road"
        v.license = "ABC1234X"
        v.first_name = "Tan"

        with self.assertRaises():
            v.save()

    def test_it_should_have_last_name(self):
        pass

    def test_it_should_have_address(self):
        pass

    def test_it_should_have_license_number(self):
        pass
