import unittest
from Viaje import Viaje
from Cars import Cars
from User import User

usr = User("Jesus Gil y Gil", "75245896W", "654879524",
           "Calle Alamo 23, Marbella", "jgil@gmail.com")
class test_viatje_v3(unittest.TestCase):

    def test_sumaPrecioAñadirCoche(self):
        car_1 = Cars("1234ABC", "Suv", "BMW", "Calle Falsa 123", "Aeropuerto", 7, 150)
        car_2 = Cars("5089PFE", "Deportivo", "Audi", "Plaza del Pueblo", "Aeropuerto", 4, 70)
        car_3 = Cars("6205MOA", "Familiar", "Renault", "Calle Karl Marx", "Aeropuerto", 2, 25)
        viaje = Viaje(usr, 3)
        viaje.añadirCoche(car_1)
        viaje.añadirCoche(car_2)
        viaje.añadirCoche(car_3)
        self.assertEqual(viaje.calculaPrecioCoche(), 1380)
        viaje.num_viajeros = 6
        self.assertEqual(viaje.calculaPrecioCoche(), 2760)
    
    def test_sumaPrecioQuitarCoche(self):
        self.assertEqual(1,1)


    def test_ErrorReservaVehiculos:
        viaje1 = Viaje(usr, 3)
        viaje1.addDestino(vuelo_2)
        viaje1.addDestino(vuelo_1)
        viaje1.añadirCoche(car_1)
        viaje1.añadirCoche(Ca)
        self.assertEqual(viaje1.confirmaReserva_vehicle(),False)

    def test_confirmaReservaHotelsOk(self):
        viaje1 = Viaje(usr, 2)
        viaje1.addDestino(vuelo_2)
        viaje1.addDestino(vuelo_1)
        viaje1.añadirHotel(hotel_2)
        viaje1.añadirHotel(hotel_3)
        self.assertEqual(viaje1.confirmaReserva_hotel(),True)

    def test_confirmaReservaHotelsError(self):
        with pytest.raises(ValueError):
            viaje1 = Viaje(usr, 2)
            viaje1.addDestino(vuelo_2)
            viaje1.addDestino(vuelo_1)
            viaje1.añadirHotel(hotel_2)
            viaje1.añadirHotel(Hotels("2","Talavera de la Reina","C/ Lope de Vega 27",60,1,1))
            viaje1.confirmaReserva_hotel()