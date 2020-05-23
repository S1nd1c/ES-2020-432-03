import unittest
from src.Viaje import Viaje
from src.Cars import Cars
from src.User import User

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
