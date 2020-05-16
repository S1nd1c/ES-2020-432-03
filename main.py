from Viaje import Viaje
from User import User
from Flights import Flights
from Hotels import Hotels
from Cars import Cars
import Bank

# Definicion de todos los vuelos, hoteles y coches

car_1 = Cars("1234ABC", "Suv", "BMW", "Calle Falsa 123", "Aeropuerto", 7)
car_2 = Cars("5089PFE", "Deportivo", "Audi", "Plaza del Pueblo", "Aeropuerto", 4)
car_3 = Cars("6205MOA", "Familiar", "Renault", "Calle Karl Marx", "Aeropuerto", 2)
car_4 = Cars('6545JRY', '4x4', 'Jeep', 'Calle Aragón, 12', 'Aeropuerto', 14)
car_5 = Cars('1561GHR', 'Deportivo', 'Peugeot', 'Plaza Catalunya', 'Aeropuerto', 7)

vuelo_1 = Flights("15612F", "MADRID", num_passatgers, 55)
vuelo_2 = Flights("68745A", "ESTAMBUL", num_passatgers, 90)
vuelo_3 = Flights("86452T", "LONDRES", num_passatgers, 85)
vuelo_4 = Flights("32892P", "AMSTERDAM", num_passatgers, 30)
vuelo_5 = Flights("98748L", "BUDAPEST", num_passatgers, 65)

hotel_1 = Hotels(1, "Jerez de la Frontera", "Morenos, 10, 11402 Jerez de la Frontera, España", 26, 7, 1)
hotel_2 = Hotels(2, "Talavera de la Reina", "Roma, 1, 45600 Talavera de la Reina, España", 62, 7, 1)
hotel_3 = Hotels(3, "L'Hospitalet de Llobregat", "Plaza Europa, 45, 08908 L'Hospitalet de Llobregat, España", 124, 7, 1)
hotel_4 = Hotels(4, "Mérida", "Avenida Reina Sofia, 8, 06800 Mérida, España", 44, 7, 1)
hotel_5 = Hotels(5, "Teruel", "Ronda del Turia, 1, 44002 Teruel, España", 35, 7, 1)


#Listas con vuelos, hoteles y coches

flight_list = [vuelo_1, vuelo_2, vuelo_3, vuelo_4, vuelo_5]
hotel_list = [hotel_1, hotel_2,hotel_3, hotel_4,hotel_5]
car_list = [car_1,car_2,car_3,car_4,car_5]


# Aqui va el flujo principal más los subflujos
def flux():

    user = User("Jesus Gil y Gil", "75245896W", "654879524", "Calle Alamo 23, Marbella", "jgil@gmail.com")

    