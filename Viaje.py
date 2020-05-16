from User import User
from Hotels import Hotels
from Flights import Flights
from Cars import Cars

class Viaje:

    def __init__(self, user:User):
        self.user = user

    def sumaPrecios(self, precio_hoteles, precio_coches, precio_vuelos):
        self.precioTotal =  precio_coches + precio_hoteles + precio_vuelos

    def  s