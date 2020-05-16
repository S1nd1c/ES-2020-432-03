from User import User
from Hotels import Hotels
from Flights import Flights
from Cars import Cars

class Viaje:


    def __init__(self, user:User, num_viajeros):
        self.user = user
        self.num_viajeros = num_viajeros
        
    #TODO borrar las listas incializadas arriba 

    def calculaPrecioCoche(self, lista_coches):
        final_price = 0

        for coche in lista_coches:
            final_price += (coche.preu * (coche.preu % self.num_viajeros))
        
        return final_price

    def calculaPrecioHoteles(self, lista_hoteles):
        final_price = 0

        for hotel in lista_hoteles:
            final_price += (hotel.preu * hotel.num_habs * hotel.dies_estada)

        return final_price

    def sumaPrecios(self):
        pass

    def addDestino(self, vuelo:Flights):
        if vuelo not in self.lista_vuelos:
            self.lista_vuelos.append(vuelo)
    
    def rmDestino(self, vuelo:Flights):
        if vuelo not in self.lista_vuelos:
            self.lista_vuelos.remove(vuelo)

    def añadirVuelos(self, lista_vuelos):
        self.lista_vuelos = lista_vuelos

    
    def añadirHoteles(self, lista_hoteles):
        self.lista_hoteles = lista_hoteles

    
    def añadirCoches(self, lista_coches):
        self.lista_coches = lista_coches