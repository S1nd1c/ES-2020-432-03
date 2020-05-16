from Viaje import Viaje
from User import User
from Flights import Flights
from Hotels import Hotels
from Cars import Cars
import Bank

# Definicion de todos los vuelos, hoteles y coches
(self, id_cotxe, tipus, marca, ubi_recollida, ubi_devolucio,)
car_1 = Cars('1234ABC', 'Suv', 'BMW', 'Calle Falsa 123', 'Aeropuerto', 7)
car_2 = Cars('5089PFE', 'Deportivo', 'Audi', 'Plaza del Pueblo', 'Aeropuerto', 4)
car_3 = Cars('6205MOA', 'Familiar', 'Renault', 'Calle Karl Marx', 'Aeropuerto', 2)
car_4 = Cars('0427LTA', )
car_5 = Cars('9562MBC', 'prueba' )

vuelo1 = Flights('15612F', 'MADRID', num_passatgers, 55)
vuelo2 = Flights('68745A', 'ESTAMBUL', num_passatgers, 90)
vuelo3 = Flights('86452T', 'LONDRES', num_passatgers, 85)
vuelo4 = Flights('32892P', 'AMSTERDAM', num_passatgers, 30)
vuelo5 = Flights('98748L', 'BUDAPEST', num_passatgers, 65)

#Listas con vuelos, hoteles y coches

flight_list = [vuelo1, vuelo2, vuelo3, vuelo4, vuelo5]
hotel_list = []
car_list = [car_1,car_2,car_3,car_4,car_5]


# Aqui va el flujo principal más los subflujos
def flux():

    user = User('Jesus Gil y Gil', '75245896W', '654879524', 'Calle Alamo 23, Marbella', 'jgil@gmail.com')

    