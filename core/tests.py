from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def test_home_view_returns_welcome_message(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "¡Hola, Django!")
