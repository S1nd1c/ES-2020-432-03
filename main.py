from Viaje import Viaje
from User import User
from Cars import Cars
import Bank

# Definicion de todos los vuelos, hoteles y coches

car_1 = 'BMW'
car_2 = 'Audi'
car_3 = 'Seat'
car_4 = 'Renault'
car_5 = 'Peugeot'

#Listas con vuelos, hoteles y coches

flight_list = []
hotel_list = []
car_list = [car_1,car_2,car_3,car_4,car_5]


# Aqui va el flujo principal más los subflujos
def flux():

    user = User('Jesus Gil y Gil', '75245896W', '654879524', 'Calle Alamo 23, Marbella', 'jgil@gmail.com')

    