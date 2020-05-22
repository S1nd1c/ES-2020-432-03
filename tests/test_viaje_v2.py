import unittest
from Viaje import *
from User import User
from Flights import Flights
from PaymentData import PaymentData

usr = User("Jesus Gil y Gil", "75245896W", "654879524",
           "Calle Alamo 23, Marbella", "jgil@gmail.com")


class test_viaje_v2(unittest.TestCase):
    
    def test_pagoEsperado(self):
        viaje1 = Viaje(usr, 2)
        metode_pagament = PaymentData("Mastercard","Jesus Gil Padre",123456,4242)
        viaje1.addDestino(Flights(1234,"Sant Esteve de les Roures",100))
        viaje1.addDestino(Flights(4737,"Talavera de la Reina",50))
        viaje1.user.seleccioMetodePagament(metode_pagament)
        self.assertEqual(metode_pagament,viaje1.user.dades_pagament)

            
