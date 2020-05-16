from User import User
from Hotels import Hotels
from Flights import Flights
from Cars import Cars

class Viaje:


    def __init__(self, user:User, num_viajeros, lista_vuelos, lista_hoteles, lista_coches):
        self.user = user
        self.num_viajeros = num_viajeros
        self.lista_coches = lista_coches
        self.lista_vuelos = lista_vuelos
        self.lista_hoteles = lista_hoteles
        
    def sumaPrecios(self):
        self.precioTotal =  precio_coches + precio_hoteles + precio_vuelos

    def addDestino(self, vol:Flights):
        if vol not in llista_vols:
            self.llista_vols.append(vol)
