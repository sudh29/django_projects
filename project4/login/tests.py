from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from login.models import UserProfileInfo


class LoginAuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="TestPassword123!",
        )
        self.profile = UserProfileInfo.objects.create(
            user=self.user,
            portfolio_site="https://portfolio.test",
        )

    def test_user_profile_creation(self):
        self.assertEqual(str(self.profile), "testuser")
        self.assertEqual(self.profile.portfolio_site, "https://portfolio.test")

    def test_special_requires_login(self):
        response = self.client.get(reverse("special"))
        # Unauthenticated users should be redirected to login
        self.assertEqual(response.status_code, 302)

    def test_special_authenticated_access(self):
        self.client.login(username="testuser", password="TestPassword123!")
        response = self.client.get(reverse("special"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You are logged in")
