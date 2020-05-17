import unittest
from Viaje import *
from User import User
from Flights import Flights
from PaymentData import PaymentData

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
    
    def test_destinos_ok(self):
        viaje1 = Viaje(usr, 2)
        dest1 = Flights(1234,"Sant Esteve de les Roures",100)
        dest2 = Flights(4737,"Talavera de la Reina",50)
        dests = [dest1,dest2]
        ok = ["Sant Esteve de les Roures","Talavera de la Reina"]
        self.assertEqual(len(viaje1.lista_destinos),0)
        for i in range(len(dests)):
            viaje1.addDestino(dests[i])
            for k,j in enumerate(viaje1.lista_destinos):
                self.assertEqual(j,ok[k])

    def test_vuelos_ok(self):
        viaje1 = Viaje(usr, 2)
        dest1 = Flights(8452,"Villa Puri",100)
        dest2 = Flights(5745,"Guarroman",50)
        dests = [dest1,dest2]
        ok = [dest1, dest2]
        self.assertEqual(len(viaje1.lista_vuelos),0)
        for i in range(len(dests)):
            viaje1.addDestino(dests[i])
            for k,j in enumerate(viaje1.lista_vuelos):
                self.assertEqual(j,ok[k])

    def test_preuViatge(self):
        viaje1 = Viaje(usr, 1)
        viaje2 = Viaje(usr, 5)
        viajes = [viaje1, viaje2]
        precios = [0,200,0,1000]
        aux = []
        for i in range(len(viajes)):
            aux.append(viajes[i].sumaPrecios())
            viajes[i].addDestino(Flights(87465, "Martorell", 200))
            aux.append(viajes[i].sumaPrecios())
        self.assertEqual(precios, aux)

    def test_rmDestino(self):
        viaje1 = Viaje(usr, 2)
        viaje2 = Viaje(usr, 4)
        viajes = [viaje1,viaje2]
        destinos = ["España","Italia"]

        for destino in range(len(viajes)):
            destinos.append(viajes[i].lista_destinos)
            viajes[i].rmDestino(Flights(58555,"España",75))
        self.assertEqual(viajes,destinos)

    def test_confirmaPagamentDestinacio(self):
        viaje1 = Viaje(usr, 1)
        viaje2 = Viaje(usr, 5)
        viajes = [viaje1, viaje2]
        test_res = [True, True]
        for viaje in viajes:
            viaje.addDestino(Flights(87465, "Martorell", 200))
        payData = PaymentData('VISA', 'Jesus Gil y Gil', '9999999999999999', '433')
        for i, viaje in enumerate(viajes):
            self.assertEqual(viaje.reservarYpagar(payData), test_res[i])
