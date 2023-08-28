"""
Sample tests

"""

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 12)