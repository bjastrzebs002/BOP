import unittest
from Bop import Bop


class TestBop(unittest.TestCase):
    base_mock, symbol_mock = "USD", "EUR"
    bop = Bop(base_mock, symbol_mock)

    def test_tomorrow_prediction(self):
        # given
        prediction = self.bop.predict_tomorrow_option()

        # then
        self.assertTrue(1 >= prediction >= -1, "Prediction should be a value between <-1, 1>")


