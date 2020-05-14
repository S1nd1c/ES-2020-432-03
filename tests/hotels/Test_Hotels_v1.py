import os
import sys
import tempfile
import unittest

# TO BE ABLE TO DEBUG THE TESTS 2-ways:
# 1: Configure PYTHONPATH
# 2: Add path to src folder manually (copy at the header of each test)
    #TEST_DIR = os.path.dirname(os.path.abspath(__file__))
    #PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
    #PROJECT_DIR = os.path.join(PROJECT_DIR, '..', 'src')
    # if not PROJECT_DIR is sys.path:
    #   sys.path.insert(0, PROJECT_DIR)

from src.Hotels import Hotels

class TestHotels(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    @classmethod
    def setUpClass(cls):
        cls.Hotels = Hotels()

        with open(cls.tmpfilepath, "w") as f:
            f.write('Hola!')

    def test_rm(self):
        # remove file
        self.Hotels.rm(self.tmpfilepath)
        # test that it was actually removed
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Error. Not possible to remove file.")

if __name__ == '__main__':
    unittest.main(exit=False)