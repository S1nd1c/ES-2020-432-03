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

    def test_preuViatge_passtgers(self):
        viaje1 = Viaje(usr, 2)
        viaje2 = Viaje(usr, 4)
        viajes = [viaje1, viaje2]
        precios = [0,400,0,800]
        aux = []
        for i in range(len(viajes)):
            aux.append(viajes[i].sumaPrecios())
            viajes[i].addDestino(Flights(44343, "Mostoles", 200))
            aux.append(viajes[i].sumaPrecios())
        self.assertEqual(precios, aux)

    def test_precioVuelos0(self):
        viaje1 = Viaje(usr, 2)
        viaje2 = Viaje(usr, 4) 
        viajes = [viaje1, viaje2]

        for viaje in viajes:
            self.assertEqual(viaje.calculaPrecioVuelos(), 0)
        
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
    
    def destinos_ok(self):
        viaje1 = Viaje(usr, 2)
        dest1 = Flights(1234,"Sant Esteve de les Roures",100)
        dest2 = Flights(4737,"Talavera de la Reina",50)
        dests = [dest1,dest2]
        ok = ["Sant Esteve de les Roures","Talavera de la Reina"]
        for i in range(len(dest)):
            self.assertEqual(len(viaje1.lista_destinos),0)
            viaje1.addDestino(dests[i])
            for k,j in enumerate(viaje1.lista_destinos):
                self.assertEqual(j,ok[k])

    def test_preuViatge2(self):
        viaje1 = Viaje(usr, 2)
        viaje2 = Viaje(usr, 4)
        viajes = [viaje1, viaje2]
        precios = [400, 800]
        aux = []
        for i in range(len(viajes)):
            viajes[i].addDestino(
                Flights(44343, "Mostoles", 200))
            aux.append(viajes[i].calculaPrecioVuelos())
        self.assertEqual(precios, aux)

    def test_preuViatge(self):
        viaje1 = Viaje(usr, 1)
        viaje2 = Viaje(usr, 5)
        viajes = [viaje1, viaje2]
        precios = [400, 800]
        aux = []
        for i in range(len(viajes)):
            viajes[i].addDestino(
                Flights(44343, "Mostoles", 200))
            aux.append(viajes[i].calculaPrecioVuelos())
        self.assertEqual(precios, aux)

