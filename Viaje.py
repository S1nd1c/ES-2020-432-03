from User import User
from Hotels import Hotels
from Flights import Flights
from Cars import Cars

class Viaje:


    def __init__(self, user:User, num_viajeros):
        self.user = user
        self.num_viajeros = num_viajeros
        
    def sumaPrecios(self, precio_hoteles, precio_coches, precio_vuelos):
        self.precioTotal =  precio_coches + precio_hoteles + precio_vuelos

    def addDestino(self, vol:Flights):
        if vol not in llista_vols:
            self.llista_vols.append(vol)
    
    def rmDestino(self, vol:Flights):
        if vol not in llista_vols:
            self.llista_vols.remove(vol)