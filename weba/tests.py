import datetime
from django.test import TestCase


# Create your tests here.

class QuestionTestCase(TestCase):
    def test_was(self):
        # self.assertEqual(True, True)
        # self.assertIn(1, [1,2,3])
        self.assertIs("hoof", "hoof")