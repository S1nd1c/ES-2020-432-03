from Viaje import Viaje
from User import User
from Flights import Flights
from Hotels import Hotels
from Cars import Cars
import Bank

from Hotels import Hotels
from Cars import Cars
from Flights import Flights


# Definicion de todos los vuelos, hoteles y coches
car_1 = 'BMW'
car_2 = 'Audi'
car_3 = 'Seat'
car_4 = 'Renault'
car_5 = 'Peugeot'

vuelo1 = Flights('15612F', 'MADRID', num_passatgers, 55)
vuelo2 = Flights('68745A', 'ESTAMBUL', num_passatgers, 90)
vuelo3 = Flights('86452T', 'LONDRES', num_passatgers, 85)
vuelo4 = Flights('32892P', 'AMSTERDAM', num_passatgers, 30)
vuelo5 = Flights('98748L', 'BUDAPEST', num_passatgers, 65)

# Definicion de todos los vuelos, hoteles y coches
hotel_1 = Hotels(1, 'Jerez de la Frontera', 'Morenos, 10, 11402 Jerez de la Frontera, España', 26, 7)
hotel_1 = Hotels(2, 'Talavera de la Reina', 'Roma, 1, 45600 Talavera de la Reina, España', 62, 7)
hotel_1 = Hotels(3, "L'Hospitalet de llobregat", "Plaza Europa, 45, 08908 L'Hospitalet de Llobregat, España", 124, 7)
hotel_1 = Hotels(4, 'Mérida', 'Avenida Reina Sofia, 8, 06800 Mérida, España', 44, 7)
hotel_1 = Hotels(5, 'Teruel', 'Ronda del Turia, 1, 44002 Teruel, España', 35, 7)
#Listas con vuelos, hoteles y coches

flight_list = [vuelo1, vuelo2, vuelo3, vuelo4, vuelo5]
hotel_list = [hotel_1, hotel_2, hotel_3, hotel_4, hotel_5]
car_list = [car_1,car_2,car_3,car_4,car_5]


# Aqui va el flujo principal más los subflujos
def flux():

    user = User('Jesus Gil y Gil', '75245896W', '654879524', 'Calle Alamo 23, Marbella', 'jgil@gmail.com')

    