import os
import sys
import unittest

from src.Cars import Cars

class TestCars(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Cars = Cars()

    def test_BankObject(self):

        assert(True)

if __name__ == '__main__':
    unittest.main(exit=False)