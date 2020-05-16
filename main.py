from Viaje import Viaje
from User import User
from Flights import Flights
from Hotels import Hotels
from Cars import Cars
import Bank

# Definicion de todos los vuelos, hoteles y coches
vuelo1 = Flights('15612F', 'MADRID', num_passatgers, 55)
vuelo2 = Flights('68745A', 'ESTAMBUL', num_passatgers, 90)
vuelo3 = Flights('86452T', 'LONDRES', num_passatgers, 85)
vuelo4 = Flights('32892P', 'AMSTERDAM', num_passatgers, 30)
vuelo5 = Flights('98748L', 'BUDAPEST', num_passatgers, 65)

#Listas con vuelos, hoteles y coches

flight_list = [vuelo1, vuelo2, vuelo3, vuelo4, vuelo5]
hotel_list = []
car_list = []


# Aqui va el flujo principal más los subflujos
def flux():

    user = User('Jesus Gil y Gil', '75245896W', '654879524', 'Calle Alamo 23, Marbella', 'jgil@gmail.com')

    