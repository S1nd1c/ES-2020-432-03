from User import User
from Hotels import Hotels
from Flights import Flights
from Cars import Cars
from Skyscanner import Skyscanner
from Booking import Booking
from Rentalcars import Rentalcars

class Viaje:


    def __init__(self, user:User, num_viajeros):
        self.user = user
        self.num_viajeros = num_viajeros
        
    def calculaPrecioVuelos(self):
        if not self.lista_vuelos:
            raise ValueError("Añade vuelos a la clase para poder calcular el precio")

        final_price = 0

        for vuelo in self.lista_vuelos:
            final_price += vuelo.preu * self.num_viajeros
        return final_price
        

    def calculaPrecioCoche(self):
        if not self.lista_coches:
            raise ValueError("Añade coches a la clase para poder calcular el precio")
        
        final_price = 0

        for coche in self.lista_coches:
            final_price += (coche.preu * (coche.preu % self.num_viajeros) * coche.dias_estancia)
        
        return final_price

    def calculaPrecioHoteles(self):
        if not self.lista_hoteles:
            raise ValueError("Añade hoteles a la clase para poder calcular el precio")

        final_price = 0

        for hotel in self.lista_hoteles:
            final_price += (hotel.preu * hotel.num_habs * hotel.dies_estada)

        return final_price

    def sumaPrecios(self):
        precio_hoteles = self.calculaPrecioHoteles()
        precio_coches = self.calculaPrecioCoche()
        precio_vuelos = self.calculaPrecioVuelos()

        return precio_coches + precio_hoteles + precio_vuelos

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

    def confirmaReserva(self):
        #Confirmacion de vuelos
        if not self.lista_vuelos:
            raise ValueError("Añade vuelos a la clase para poder reservarlos")
        for vuelo in self.lista_vuelos:
            sksc = Skyscanner()
            sksc.confirm_reserve(self.user, vuelo)
        #Confirmacion de hoteles
        if not self.lista_hoteles:
            raise ValueError("Añade hoteles a la clase para poder reservarlos")
        for hotel in self.lista_hoteles:
            hotels = Booking()
            hotels.confirm_reserve(self.user, hotel)
        #Confirmacion de coches
        if not self.lista_coches:
            raise ValueError("Añade coches a la clase para poder reservarlos")
        for coche in self.lista_coches:
            cars = Rentalcars()
            cars.confirm_reserve(self.user, coche)
        return True
