import unittest
from src.Hotels import Hotels
from requests.exceptions import Timeout
from unittest import mock

class TestMock3(unittest.TestCase):
    
    @mock.patch('src.Hotels.os.path')
    @mock.patch('src.Hotels.os')
    def test_rm(self, mock_os, mock_path):
        # create the Class
        objHotel = Hotels()
        # set up the mock
        mock_path.isfile.return_value = False
        objHotel.rm("dummy path")
        # test the remove call is NOT called.
        self.assertFalse(mock_os.remove.called, "Error removing the file if not present.")
        # make the file 'exist'
        mock_path.isfile.return_value = True
        objHotel.rm("dummy path")
        mock_os.remove.assert_called_with("dummy path")

    

if __name__ == '__main__':
    unittest.main()