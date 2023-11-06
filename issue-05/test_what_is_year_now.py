import unittest
from unittest.mock import patch
from what_is_year_now import what_is_year_now


class TestYear(unittest.TestCase):
    """
    Test class for what_is_year_now function.
    """

    def test_2012(self):
        """
        Test with first format of date.
        """
        with patch('what_is_year_now.json') as mocked:
            mocked.load.return_value = {'currentDateTime': '2012-12-21'}
            assert what_is_year_now() == 2012
            mocked.load.assert_called_once()

    def test_1999(self):
        """
        Test with second format of date.
        """
        with patch('what_is_year_now.json') as mocked:
            mocked.load.return_value = {'currentDateTime': '29.08.1999'}
            assert what_is_year_now() == 1999
            mocked.load.assert_called_once()

    def test_1984(self):
        """
        Test with invalid format of date.
        """
        with patch('what_is_year_now.json') as mocked:
            mocked.load.return_value = {'currentDateTime': '1984_1_1'}
            with self.assertRaises(ValueError):
                what_is_year_now()
            mocked.load.assert_called_once()
