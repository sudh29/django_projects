from django.test import TestCase, Client
from django.urls import reverse
from home.models import Contact


class HomeAppTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contact_model(self):
        contact = Contact.objects.create(
            name="John Doe",
            email="john@example.com",
            phone="9876543210",
            desc="Project inquiry",
        )
        self.assertEqual(str(contact), "John Doe")

    def test_pages_status_code(self):
        for route in ["home", "about", "projects", "contact"]:
            response = self.client.get(reverse(route))
            self.assertEqual(response.status_code, 200)

    def test_contact_submission(self):
        payload = {
            "name": "Jane Doe",
            "email": "jane@example.com",
            "phone": "9998887776",
            "desc": "Testing contact submission",
        }
        response = self.client.post(reverse("contact"), data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Contact.objects.filter(email="jane@example.com").exists())
