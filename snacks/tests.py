from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.


class SnacksTest(SimpleTestCase):

    def test_home_status(self):
        self.helper_tests('home', 'home.html')


    def test_about_status(self):
        self.helper_tests('about', 'about.html')
    

    def helper_tests(self, url_name, template_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)
