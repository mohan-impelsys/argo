from django.test import SimpleTestCase


class SanityTests(SimpleTestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)
