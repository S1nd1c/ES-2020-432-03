import unittest
from unittest import mock
import pytest
from src.Viaje import *
from src.User import User
from src.Flights import Flights
from src.PaymentData import PaymentData

usr = User("Jesus Gil y Gil", "75245896W", "654879524",
           "Calle Alamo 23, Marbella", "jgil@gmail.com")
car_1 = Cars("1234ABC", "Suv", "BMW", "Calle Falsa 123", "Aeropuerto", 7, 150)
car_2 = Cars("5089PFE", "Deportivo", "Audi",
             "Plaza del Pueblo", "Aeropuerto", 4, 70)
car_3 = Cars("6205MOA", "Familiar", "Renault",
             "Calle Karl Marx", "Aeropuerto", 2, 25)

hotel_1 = Hotels(1, "Jerez de la Frontera",
                 "Morenos, 10, 11402 Jerez de la Frontera, España", 26, 7, 1)
hotel_2 = Hotels(2, "Talavera de la Reina",
                 "Roma, 1, 45600 Talavera de la Reina, España", 62, 7, 1)

vuelo_1 = Flights("15612F", "MADRID", 55)
vuelo_2 = Flights("68745A", "ESTAMBUL", 90)
vuelo_3 = Flights("86452T", "LONDRES", 85)

metode_pagament = PaymentData("Mastercard","Jesus Gil Padre",123456,4242)



class test_viaje_v4(unittest.TestCase):

    @mock.patch('src.Bank')
    def test_volverRealizarPago(self, mock_bank):
        num_passatgers = 3

        viaje = Viaje(usr, num_passatgers)

        viaje.addDestino(vuelo_1)
        viaje.addDestino(vuelo_2)
        viaje.user.seleccioMetodePagament(metode_pagament)

        mock_bank.do_payment.return_value = False
        self.assertTrue(viaje.reservarYpagar())

        #viaje.reservarYpagar().return_value = False


    