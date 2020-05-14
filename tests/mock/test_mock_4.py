import unittest
from src.Hotels import Hotels
from requests.exceptions import Timeout
from unittest import mock

class TestMock3(unittest.TestCase):
    
    @mock.patch('src.Hotels')
    def test_get_always_true(self, mock_hotels):
        # set up the mock
        self.assertTrue(mock_hotels.get_always_true())
        mock_hotels.get_always_true.return_value = False
        self.assertFalse(mock_hotels.get_always_true())
        

if __name__ == '__main__':
    unittest.main()