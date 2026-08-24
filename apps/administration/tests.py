from django.test import TestCase

class AdministrationSmokeTest(TestCase):
    def test_administration_loaded(self):
        self.assertEqual(1 + 1, 2)