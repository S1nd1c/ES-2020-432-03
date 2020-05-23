import unittest
import pytest
from src.Viaje import *
from src.User import User
from src.Flights import Flights
from src.PaymentData import PaymentData

usr = User("Jesus Gil y Gil", "75245896W", "654879524",
           "Calle Alamo 23, Marbella", "jgil@gmail.com")
metode_pagament = PaymentData("Mastercard","Jesus Gil Padre","123456","4242")

class test_viaje_v2(unittest.TestCase):
    
    def test_pagoEsperado(self):
        viaje1 = Viaje(usr, 2)
        viaje1.addDestino(Flights("1234","Sant Esteve de les Roures",100))
        viaje1.addDestino(Flights("4737","Talavera de la Reina",50))
        viaje1.user.seleccioMetodePagament(metode_pagament)
        self.assertEqual(metode_pagament,viaje1.user.dades_pagament)
    
    def test_errorPago(self):
        with pytest.raises(ValueError):
            viaje1 = Viaje(usr, 2)
            viaje1.addDestino(Flights("1234","Sant Esteve de les Roures",100))
            viaje1.addDestino(Flights(4737,"Talavera de la Reina",50))
            viaje1.user.seleccioMetodePagament(metode_pagament)
            viaje1.reservarYpagar()
    
    def test_errorReservaVols(self):
        with pytest.raises(ValueError):
            viaje1 = Viaje(usr, 2)
            metode_pagament = PaymentData("Mastercard","Jesus Gil Padre","123456","4242")
            viaje1.addDestino(Flights("1234","Sant Esteve de les Roures",100))
            viaje1.addDestino(Flights(4737,"Talavera de la Reina",50))
            viaje1.user.seleccioMetodePagament(metode_pagament)
            viaje1.reservarYpagar()

                
