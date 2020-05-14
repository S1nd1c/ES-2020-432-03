import unittest
from src.Cars import Cars
from requests.exceptions import Timeout
from unittest.mock import patch

class TestMock2(unittest.TestCase):
    
    def test_get_seat_lean_specifications(self):
        with patch('src.Cars.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                Cars.download_seat_leon_specifications()
                # Assert that the mock was called exactly once
                mock_requests.get.assert_called_once()

if __name__ == '__main__':
    unittest.main()