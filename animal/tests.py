from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


from .models import Animal, Vet, Specie
from .forms import AnimalForm
import django.db.utils


# Create your tests here.
class AnimalModelTestCase(TestCase):

    def test_create_animal_model(self):

        user = User(username="test_user")
        user.save()

        v = Vet(first_name="Tan", last_name="Ah Kow",
                address="Yishun Ring Road", years=1,
                license="ABX12324")
        v.save()

        a = Animal()
        a.owner = user
        a.name = "Fluffy"
        a.breed = "Golden Retriever"
        a.is_sterlized = False
        a.age = 8
        a.gender = "M"
        a.vet = v

        a.save()

        self.assertTrue(a.id > 0)
        saved_animal = get_object_or_404(Animal, pk=a.id)
        self.assertTrue(saved_animal is not None)

        self.assertEqual(saved_animal.name, "Fluffy")
        self.assertEqual(saved_animal.breed, "Golden Retriever")
        self.assertEqual(saved_animal.is_sterlized, False)
        self.assertEqual(saved_animal.age, 8)
        self.assertEqual(saved_animal.gender, "M")
        self.assertEqual(saved_animal.vet, v)
        self.assertEqual(saved_animal.owner, user)

    def test_default_age_is_1(self):
        v = Vet(first_name="Tan", last_name="Ah Kow",
                address="Yishun Ring Road", years=1,
                license="ABX12324")
        v.save()

        user = User(username="test_user")
        user.save()

        a = Animal()
        a.name = "Fluffy"
        a.breed = "Golden Retriever"
        a.is_sterlized = False
        a.gender = "M"
        a.vet = v
        a.owner = user

        a.save()
        saved_animal = get_object_or_404(Animal, pk=a.id)
        self.assertEqual(saved_animal.age, 1)


class VetModelTestCase(TestCase):

    def test_years_in_practise_should_default_to_one(self):
        v = Vet()
        v.first_name = "Tan"
        v.last_name = "Ah Kow"
        v.address = "Yishun Ring Road"
        v.license = "ABC1234X"
        v.save()

        saved_vet = get_object_or_404(Vet, pk=v.id)
        self.assertEqual(saved_vet.years, 1)

    def test_it_should_have_first_name(self):
        v = Vet()
        v.last_name = "Ah Kow"
        v.first_name = None
        v.address = "Yishun Ring Road"
        v.license = "ABC1234X"

        with self.assertRaises(django.db.utils.IntegrityError):
            v.save()

    def test_it_should_have_last_name(self):
        v = Vet()
        v.last_name = None
        v.first_name = "Tan"
        v.address = "Yishun Ring Road"
        v.license = "ABC1234X"

        with self.assertRaises(django.db.utils.IntegrityError):
            v.save()

    def test_it_should_have_address(self):
        v = Vet()
        v.last_name = "Ah Kow"
        v.first_name = "Tan"
        v.address = None
        v.license = "ABC1234X"

        with self.assertRaises(django.db.utils.IntegrityError):
            v.save()

    def test_it_should_have_license_number(self):
        v = Vet()
        v.last_name = "Ah Kow"
        v.first_name = "Tan"
        v.address = "Yishun Ring Road"
        v.license = None

        with self.assertRaises(django.db.utils.IntegrityError):
            v.save()


class AnimalFormTestCase(TestCase):

    def setUp(self):
        self.vet = Vet(first_name="Tan", last_name="Ah Kow",
                       address="Yishun Ring Road", years=1,
                       license="ABX12324")
        self.vet.save()

    def test_if_name_is_complusory(self):
        form = AnimalForm({
            "breed": "Golden Retriever",
            "is_sterlized": "False",
            "age": 20,
            "gender": "M",
            "vet": self.vet
        })

        self.assertFalse(form.is_valid())

    def test_if_breed_is_complusory(self):

        form = AnimalForm({
            "name": "Fluffy",
            "is_sterlized": "False",
            "age": 20,
            "gender": "M",
            "vet": self.vet
        })

        self.assertFalse(form.is_valid())

    def test_if_age_is_optional(self):
        form = AnimalForm({
            "name": "Fluffy",
            "is_sterlized": "False",
            "gender": "M",
            "vet": self.vet
        })

        self.assertFalse(form.is_valid())


class AnimalViewTestCase(TestCase):

    def setUp(self):
        self.vet = Vet(first_name="Tan", last_name="Ah Kow",
                       address="Yishun Ring Road", years=1,
                       license="ABX12324")
        self.vet.save()

        self.vet2 = Vet(first_name="Tan", last_name="Ah Kow",
                        address="Yishun Ring Road", years=1,
                        license="ABX12324")
        self.vet2.save()

        self.specie = Specie(name="Dog")
        self.specie.save()

        self.user = User(username="test_user")
        self.user.save()

    def test_can_get_animal_form(self):
        response = self.client.get('/animals/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'animal/create_animal.template.html')

    def test_can_create_animal(self):

        response = self.client.post('/animals/create/', {
            "name": "Cookie",
            "breed": "Lab",
            "is_sterlized": True,
            "age": 5,
            "gender": "F",
            "vet": str(self.vet.id),
            "microchip": "TEST121212",
            "owner": str(self.user.id)
        })
        self.assertEqual(response.status_code, 200)
        dog = Animal.objects.filter(name="Cookie")
        self.assertEqual(dog.count(), 1)

        the_dog = Animal.objects.get(name="Cookie")
        self.assertEqual(the_dog.vet, self.vet)

    def test_can_get_edit_animal_form(self):
        animal = Animal(name="Cookie", breed="Cat", is_sterlized=True, age=3,
                        gender="M", vet=self.vet, owner=self.user)
        animal.save()

        response = self.client.get(f'/animals/update/{animal.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'animal/update_animal.template.html')

    def test_can_edit_animal(self):
        animal = Animal(name="Cookie", breed="Cat", is_sterlized=True, age=3,
                        gender="M", vet=self.vet, microchip="ABX12313123", owner=self.user)
        animal.save()

        response = self.client.post(f'/animals/update/{animal.id}/', {
            'name': 'Cookie2',
            'breed': 'Cat2',
            'is_sterlized': False,
            'age': 32,
            'gender': "F",
            'vet': str(self.vet2.id),
            'microchip': "ABX14151",
            'owner': str(self.user.id)
        })

        self.assertEqual(response.status_code, 200)
        print(response.content)
        dog = get_object_or_404(Animal, pk=animal.id)

        self.assertEquals(dog.name, "Cookie2")
        self.assertEquals(dog.breed, "Cat2")
        self.assertEquals(dog.is_sterlized, False)
        self.assertEquals(dog.age, 32)
        self.assertEquals(dog.gender, 'F')
        self.assertEquals(dog.vet, self.vet2)
