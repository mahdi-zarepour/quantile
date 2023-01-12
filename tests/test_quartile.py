import unittest

from statistics_quantile.quartile import Quartile 


class TestQuartile(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.q = 1
        self.q1 = Quartile(data=self.data, q=1)

    def test_q_checker(self):
        self.assertTrue(self.q1.q_checker(self.q))

    def test_recognize_data_index(self):
        self.assertEqual(self.q1.recognize_data_index(), (2, 0.75))

    def test_quartile_calculator(self):
        self.assertEqual(self.q1.quartile_calculator(), 2.75)
