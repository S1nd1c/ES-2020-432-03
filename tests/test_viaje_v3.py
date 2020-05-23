import unittest
import pytest
from src.Viaje import Viaje
from src.Cars import Cars
from src.User import User
from src.Flights import Flights
from src.Hotels import Hotels

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


class test_viatje_v3(unittest.TestCase):

    def test_sumaPrecioAñadirCoche(self):
        viaje = Viaje(usr, 3)
        viaje.añadirCoche(car_1)
        viaje.añadirCoche(car_2)
        viaje.añadirCoche(car_3)
        self.assertEqual(viaje.calculaPrecioCoche(), 1380)
        viaje.num_viajeros = 6
        self.assertEqual(viaje.calculaPrecioCoche(), 2760)

    def test_sumaPrecioQuitarCoche(self):
        num_passatgers = 3

        viaje = Viaje(usr, num_passatgers)

        viaje.añadirCoche(car_1)
        viaje.añadirCoche(car_2)
        viaje.añadirCoche(car_3)
        viaje.quitarCoche(car_3)
        self.assertEqual(viaje.calculaPrecioCoche(), 1330)

    def test_sumaPrecioAñadirAlojamiento(self):
        num_passatgers = 3
        viaje = Viaje(usr, num_passatgers)

        viaje.añadirHotel(hotel_1)
        viaje.añadirHotel(hotel_2)

        self.assertEqual(viaje.calculaPrecioHoteles(), 1848)

    def test_sumaPrecioQuitarAlojamiento(self):
        num_passatgers = 3
        viaje = Viaje(usr, num_passatgers)

        viaje.añadirHotel(hotel_1)
        viaje.añadirHotel(hotel_2)
        viaje.quitarHotel(hotel_2)

        self.assertEqual(viaje.calculaPrecioHoteles(), 546)

    def test_confirmacionReservaVehiculos(self):

        num_passatgers = 3

        viaje = Viaje(usr, num_passatgers)

        viaje.addDestino(vuelo_1)
        viaje.addDestino(vuelo_2)
        viaje.addDestino(vuelo_3)

        self.assertEqual(viaje.reservarYpagar(), True)

    def test_ErrorReservaVehiculos(self):
        viaje1 = Viaje(usr, 3)
        viaje1.addDestino(vuelo_2)
        viaje1.addDestino(vuelo_1)
        viaje1.añadirCoche(car_1)
        viaje1.añadirCoche(car_2)
        self.assertEqual(viaje1.confirmaReserva_vehicle(), False)

    def test_confirmaReservaHotelsOk(self):
        viaje1 = Viaje(usr, 2)
        viaje1.addDestino(vuelo_2)
        viaje1.addDestino(vuelo_1)
        viaje1.añadirHotel(hotel_2)
        self.assertEqual(viaje1.confirmaReserva_hotel(), True)

    def test_confirmaReservaHotelsError(self):
        with pytest.raises(ValueError):
            viaje1 = Viaje(usr, 2)
            viaje1.addDestino(vuelo_2)
            viaje1.addDestino(vuelo_1)
            viaje1.añadirHotel(hotel_2)
            viaje1.añadirHotel(
                Hotels("2", "Talavera de la Reina", "C/ Lope de Vega 27", 60, 1, 1))
            viaje1.confirmaReserva_hotel()
