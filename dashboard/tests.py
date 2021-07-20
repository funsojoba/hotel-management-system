from django.test import TestCase

# Create your tests here.


class TestTesting(TestCase):
    
    def test_addition(self):
        self.assertEqual((2 + 2), 4)