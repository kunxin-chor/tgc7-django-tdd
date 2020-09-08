from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):

    def test_get_home_page(self):
        # simulate the browser going to the / URL
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/welcome.template.html')
