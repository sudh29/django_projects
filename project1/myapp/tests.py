from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import home


class MyAppTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve("/")
        self.assertEqual(view.func, home)

    def test_home_page_template(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "myapp/home.html")
