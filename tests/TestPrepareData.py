import unittest
from PrepareData import PrepareData
from RequestHandler import RequestHandler


class TestPrepareData(unittest.TestCase):
    base_mock, symbol_mock = "USD", "EUR"
    pd = PrepareData(symbol_mock)
    rh = RequestHandler(base_mock, symbol_mock)
    rh_data = rh.get_data()
    rh_data_single = rh.get_100daysback_data()

    def test_prepared_data_input(self):
        # given
        prepared_data = self.pd.prepare(self.rh_data)

        # then
        self.assertTrue(len(prepared_data[0]) != 0, "List of rates should not be empty")
        any(self.assertEqual(len(p), 100, "List of rates should not be empty") for p in prepared_data[0])

    def test_prepared_data_results(self):
        # given
        prepared_data = self.pd.prepare(self.rh_data)

        # then
        self.assertTrue(len(prepared_data[1]) != 0, "List of results should not be empty")

    def test_prepared_data_equal_amount(self):
        # given
        prepared_data = self.pd.prepare(self.rh_data)

        # then
        self.assertEqual(len(prepared_data[0]), len(prepared_data[1]), "List of input data and list results should has"
                                                                       "the same length")

    def test_signle_prepare_data_input(self):
        # given
        prepared_data = self.pd.single_dict_prepare(self.rh_data_single)

        # then
        self.assertTrue(len(prepared_data) != 0, "List of rates should not be empty")
        self.assertEqual(len(prepared_data), 100, "Length of list of rates should be equals 100")



