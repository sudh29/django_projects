from django.test import TestCase, Client
from django.urls import reverse
from basicapp.forms import FormName


class BasicAppFormTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_form_validation_valid(self):
        data = {
            "name": "Alice Smith",
            "email": "alice@example.com",
            "verify_email": "alice@example.com",
            "text": "This is a valid inquiry.",
        }
        form = FormName(data=data)
        self.assertTrue(form.is_valid())

    def test_form_validation_email_mismatch(self):
        data = {
            "name": "Bob Jones",
            "email": "bob@example.com",
            "verify_email": "different@example.com",
            "text": "Hello world",
        }
        form = FormName(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("__all__", form.errors)

    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_form_view_post_success(self):
        response = self.client.post(
            reverse("formpage"),
            {
                "name": "Charlie",
                "email": "charlie@test.com",
                "verify_email": "charlie@test.com",
                "text": "Testing form post",
            },
        )
        self.assertEqual(response.status_code, 200)
