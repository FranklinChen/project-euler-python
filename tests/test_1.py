from unittest import TestCase

from .context import project_euler
from project_euler import problem_1

class Test1(TestCase):
    """
    Silly tests just to illustrate use of unittest.
    """

    def test_should_be_multiple(self):
        self.assertTrue(problem_1.multiple_3_or_5(30))

    def test_should_not_be_multiple(self):
        self.assertFalse(problem_1.multiple_3_or_5(4))

    def test_sum_should_work(self):
        self.assertEqual(problem_1.sum_multiple_3_or_5_below(10), 23)
