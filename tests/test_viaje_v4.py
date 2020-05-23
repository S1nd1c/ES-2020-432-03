import unittest
import pytest
from src.Viaje import *
from src.User import User
from src.Flights import Flights
from src.PaymentData import PaymentData

usr = User("Jesus Gil y Gil", "75245896W", "654879524",
           "Calle Alamo 23, Marbella", "jgil@gmail.com")


class test_viaje_v4(unittest.TestCase):

    def test_volverRealizarPago(self):
        