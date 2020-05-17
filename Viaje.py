from Hotels import Hotels
from Flights import Flights
from Cars import Cars
from Skyscanner import Skyscanner
from Booking import Booking
from Rentalcars import Rentalcars

class Viaje:


    def __init__(self, user, num_viajeros):
        self.user = user
        self.num_viajeros = num_viajeros
        self.lista_coches = []
        self.lista_vuelos = []
        self.lista_hoteles = []
        self.lista_destinos = []


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
            self.lista_destinos.append(vuelo.destinacio)
    
    def rmDestino(self, vuelo:Flights):
        if vuelo not in self.lista_vuelos:
            self.lista_vuelos.remove(vuelo)
            self.lista_destinos.remove(vuelo.destinacio)

    def añadirVuelos(self, lista_vuelos):
        self.lista_vuelos = lista_vuelos

    def añadirHoteles(self, lista_hoteles):
        self.lista_hoteles = lista_hoteles

    def añadirCoches(self, lista_coches):
        self.lista_coches = lista_coches

    def confirmaReserva_vehicle(self):
        if not self.lista_coches:
            raise ValueError("Añade coches a la clase para poder reservarlos")
        for coche in self.lista_coches:
            cars = Rentalcars()
            cars.confirm_reserve(self.user, coche)
        return True

    def cancelaReserva_vehicle(self):

        for coche in self.lista_coches:
            cars = Cars()
            if cars.reserva_coche(self.user, coche) != True:
                return True
            else:
                return False

    def confirmaReserva_vol(self):
        if not self.lista_vuelos:
            raise ValueError("Añade vuelos a la clase para poder reservarlos")
        for vuelo in self.lista_vuelos:
            sksc = Skyscanner()
            sksc.confirm_reserve(self.user, vuelo)
        return True

    def cancelaReserva_vol(self):

        for vuelo in self.lista_vuelos:
            sksc = Flights()
            if sksc.reserva_vol(self.user, vuelo) != True:
                return True
            else:
                return False

    def confirmaReserva_hotel(self):
        if not self.lista_hoteles:
            raise ValueError("Añade hoteles a la clase para poder reservarlos")
        for hotel in self.lista_hoteles:
            hotels = Booking()
            hotels.confirm_reserve(self.user, hotel)
        return True
    
    def cancelaReserva_hotel(self):

        for hotel in self.lista_hoteles:
            hotels = Booking()
            if hotels.reserva_hotel(self.user, hotel) != True:
                return True
            else:
                return False
