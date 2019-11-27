import unittest
from src.bop import RequestHandler


class TestRequestHandler(unittest.TestCase):
    mock_base, mock_symbol = "USD", "EUR"
    rh = RequestHandler.RequestHandler(mock_base, mock_symbol)
    rh_data = rh.get_data()

    def test_load(self):
        self.assertTrue(self.rh_data, "Should be not empty")

    def test_type_list(self):
        self.assertIsInstance(self.rh_data, list, "Should be a list")

    def test_type_dict(self):
        self.assertIsInstance(self.rh_data[0], dict, "Should be a dictionary")


