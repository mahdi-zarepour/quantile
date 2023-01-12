import unittest

from quantile.percentile import Percentile 


class TestPecsentile(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.p = 15
        self.p15 = Percentile(data=self.data, p=15)

    def test_p_checker(self):
        self.assertTrue(self.p15.p_checker(self.p))

    def test_recognize_data_index(self):
        self.assertEqual(self.p15.recognize_data_index(), (1, 0.6499999999999999))

    def test_percentile_calculator(self):
        self.assertEqual(self.p15.percentile_calculator(), 1.65)
