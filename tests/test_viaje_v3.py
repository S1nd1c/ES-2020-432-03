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
        car_4 = Cars("6545JRY", "4x4", "Jeep", "Calle Aragón, 12", "Aeropuerto", 14, 350)
        car_5 = Cars("1561GHR", "Deportivo", "Peugeot", "Plaza Catalunya", "Aeropuerto", 7, 120)
        cars = [car_1, car_2, car_3]
        viaje = Viaje(usr, 3)
        viaje.añadirCoches(cars)
        self.assertEqual(viaje.calculaPrecioCoche(), 1050)
        viaje.num_viajeros = 6
        self.assertEqual(viaje.calculaPrecioCoche(), 2100)




