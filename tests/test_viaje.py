import unittest
from Viaje import *
from User import User
from Flights import Flights

usr = User("Jesus Gil y Gil", "75245896W", "654879524",
           "Calle Alamo 23, Marbella", "jgil@gmail.com")


class test_viaje(unittest.TestCase):

    def test_numViatjers(self):
        viaje1 = Viaje(usr, 2)
        viaje2 = Viaje(usr, 4)
        viaje3 = Viaje(usr, 10)
        viaje4 = Viaje(usr, 1)

        viajes = [viaje1, viaje2, viaje3, viaje4]
        test_res = [2, 4, 10, 1]

        for i, viaje in enumerate(viajes):
            self.assertEqual(viaje.num_viajeros, test_res[i])

    def test_noDestino(self):
        viaje1 = Viaje(usr, 2)
        viaje2 = Viaje(usr, 4)
        viajes = [viaje1, viaje2]

        for viaje in viajes:
            self.assertTrue(not viaje.lista_destinos)

    def test_noVuelo(self):
        viaje1 = Viaje(usr, 2)
        viaje2 = Viaje(usr, 4)
        viajes = [viaje1, viaje2]

        for viaje in viajes:
            self.assertTrue(not viaje.lista_vuelos)

    def test_preuViatge(self):
        viaje1 = Viaje(usr, 2)
        viaje2 = Viaje(usr, 4)
        viajes = [viaje1, viaje2]
        precios = [400, 800]
        aux = []
        for i in len(viajes):
            viajes[i].addDestino(
                Flights(44343, "Mostoles", viajes[i].num_passatgers, 200))
            aux.append(viajes[i].calculaPrecioVuelos())
        self.assertEqual(precios, aux)

     def test_precioVuelos0(self):
        viaje1 = Viaje(usr, 2)
        viaje2 = Viaje(usr, 4) 
        viajes = [viaje1, viaje2]

        for viaje in viajes:
            self.assertEqual(viaje.calculaPrecioVuelo(), 0)
        
     def test_precioHoteles0(self):
        viaje1 = Viaje(usr, 2)
        viaje2 = Viaje(usr, 4) 
        viajes = [viaje1, viaje2]

        for viaje in viajes:
            self.assertEqual(viaje.calculaPrecioHoteles(), 0)
    
     def test_precioCoches0(self):
        viaje1 = Viaje(usr, 2)
        viaje2 = Viaje(usr, 4) 
        viajes = [viaje1, viaje2]

        for viaje in viajes:
            self.assertEqual(viaje.calculaPrecioVuelos(), 0)

    def test_precioTotal0(self):
        viaje1 = Viaje(usr, 2)
        viaje2 = Viaje(usr, 4) 
        viajes = [viaje1, viaje2]

        for viaje in viajes:
            self.assertEqual(viaje.sumaPrecios(), 0)

