import unittest
from src.Viaje import Viaje
from src.Cars import Cars
from src.User import User
from src.Flights import Flights
from src.Hotels import Hotels

usr = User("Jesus Gil y Gil", "75245896W", "654879524",
           "Calle Alamo 23, Marbella", "jgil@gmail.com")


class test_viatje_v3(unittest.TestCase):

    def test_sumaPrecioAñadirCoche(self):
        car_1 = Cars("1234ABC", "Suv", "BMW",
                     "Calle Falsa 123", "Aeropuerto", 7, 150)
        car_2 = Cars("5089PFE", "Deportivo", "Audi",
                     "Plaza del Pueblo", "Aeropuerto", 4, 70)
        car_3 = Cars("6205MOA", "Familiar", "Renault",
                     "Calle Karl Marx", "Aeropuerto", 2, 25)
        viaje = Viaje(usr, 3)
        viaje.añadirCoche(car_1)
        viaje.añadirCoche(car_2)
        viaje.añadirCoche(car_3)
        self.assertEqual(viaje.calculaPrecioCoche(), 1380)
        viaje.num_viajeros = 6
        self.assertEqual(viaje.calculaPrecioCoche(), 2760)

    def test_sumaPrecioQuitarCoche(self):
        car_1 = Cars("1234ABC", "Suv", "BMW",
                     "Calle Falsa 123", "Aeropuerto", 7, 150)
        car_2 = Cars("5089PFE", "Deportivo", "Audi",
                     "Plaza del Pueblo", "Aeropuerto", 4, 70)
        car_3 = Cars("6205MOA", "Familiar", "Renault",
                     "Calle Karl Marx", "Aeropuerto", 2, 25)
        viaje = Viaje(usr, 3)
        viaje.añadirCoche(car_1)
        viaje.añadirCoche(car_2)
        viaje.añadirCoche(car_3)
        viaje.quitarCoche(car_3)
        self.assertEqual(viaje.calculaPrecioCoche(), 1330)

    def test_sumaPrecioAñadirAlojamiento(self):
        hotel_1 = Hotels(1, "Jerez de la Frontera",
                         "Morenos, 10, 11402 Jerez de la Frontera, España", 26, 7, 1)
        hotel_2 = Hotels(2, "Talavera de la Reina",
                         "Roma, 1, 45600 Talavera de la Reina, España", 62, 7, 1)

        viaje = Viaje(usr, 3)

        viaje.añadirHotel(hotel_1)
        viaje.añadirHotel(hotel_2)

        self.assertEqual(viaje.calculaPrecioHoteles(), 1302)

    def test_sumaPrecioQuitarAlojamiento(self):
        hotel_1 = Hotels(1, "Jerez de la Frontera",
                         "Morenos, 10, 11402 Jerez de la Frontera, España", 26, 7, 1)
        hotel_2 = Hotels(2, "Talavera de la Reina",
                         "Roma, 1, 45600 Talavera de la Reina, España", 62, 7, 1)

        viaje = Viaje(usr, 3)

        viaje.añadirHotel(hotel_1)
        viaje.añadirHotel(hotel_2)
        viaje.quitarHotel(hotel_2)

        self.assertEqual(viaje.calculaPrecioHoteles(), 546)

    def test_confirmacionReservaVehiculos(self):

        num_passatgers = 3

        vuelo_1 = Flights("15612F", "MADRID", 55)
        vuelo_2 = Flights("68745A", "ESTAMBUL", 90)
        vuelo_3 = Flights("86452T", "LONDRES", 85)
        viaje = Viaje(usr, num_passatgers)   

        viaje.addDestino(vuelo_1)
        viaje.addDestino(vuelo_2)
        viaje.addDestino(vuelo_3)

        self.assertEqual(viaje.reservarYpagar(), True)