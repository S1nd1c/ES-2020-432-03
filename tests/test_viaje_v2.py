import unittest
from Viaje import *
from User import User
from Flights import Flights
from PaymentData import PaymentData

usr = User("Jesus Gil y Gil", "75245896W", "654879524",
           "Calle Alamo 23, Marbella", "jgil@gmail.com")


class test_viaje_v2(unittest.TestCase):
    
    def test_confirmaPagamentDestinacio(self):
        viaje1 = Viaje(usr, 1)
        viaje2 = Viaje(usr, 5)
        viajes = [viaje1, viaje2]
        test_res = [True, True]
        payData = PaymentData('VISA', 'Jesus Gil y Gil', '9999999999999999', '433')
        for viaje in viajes:
            viaje.addDestino(Flights(87465, "Martorell", 200))
            viaje.user.seleccioMetodePagament(payData)
        for i, viaje in enumerate(viajes):
            self.assertEqual(viaje.reservarYpagar(), test_res[i])

            