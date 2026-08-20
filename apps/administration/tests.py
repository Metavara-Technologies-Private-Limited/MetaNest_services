from django.test import TestCase


class AdministrationSmokeTest(TestCase):
    def test_administration_loaded(self):
        """Smoke test to verify test runner configuration."""
        self.assertEqual(1 + 1, 2)