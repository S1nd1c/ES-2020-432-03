from Hotels import Hotels
from Flights import Flights
from Cars import Cars
from Skyscanner import Skyscanner
from Booking import Booking
from Rentalcars import Rentalcars
from Bank import Bank
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
            return 0

        final_price = 0

        for vuelo in self.lista_vuelos:
            final_price += vuelo.preu * self.num_viajeros
        return final_price
        
    def calculaPrecioCoche(self):
        if not self.lista_coches:
            return 0
        
        final_price = 0

        for coche in self.lista_coches:
            final_price += (coche.preu * coche.dias_estancia)
        
        return final_price * ((self.num_viajeros // 4) + 1)

    def calculaPrecioHoteles(self):
        if not self.lista_hoteles:
            return 0

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
    
    def rmDestino(self, codi_vol, destinacio, preu):
        nuevos_destinos = []
        nuevos_vuelos = []
        for i, vuelo in enumerate(self.lista_vuelos):
            if vuelo.codi_vol != codi_vol and vuelo.destinacio != destinacio and vuelo.preu != preu:
                nuevos_vuelos.append(vuelo)
                nuevos_destinos.append(vuelo.destinacio)
        self.lista_destinos = nuevos_destinos
        self.lista_vuelos = nuevos_vuelos

    def añadirVuelos(self, lista_vuelos):
        self.lista_vuelos = lista_vuelos

    def añadirHoteles(self, lista_hoteles):
        self.lista_hoteles = lista_hoteles

    def añadirCoche(self, coche: Cars):
        if coche not in self.lista_coches:
            self.lista_coches.append(coche)

    def quitarCoche(self, del_coche: Cars):
    lista_coches = []
    for coche in self.lista_coches:
        if coche != del_coche
        lista_coches.append(coche)
    self.lista_coches = lista_coches

    def confirmaReserva_vehicle(self):
        if not self.lista_coches:
            return 0
        for coche in self.lista_coches:
            cars = Rentalcars()
            cars.confirm_reserve(self.user, coche)
        return True

    def cancelaReserva_vehicle(self): # OJO PIOJO A ESTA FUNCION
        for coche in self.lista_coches:
            cars = Cars()
            if cars.reserva_coche(self.user, coche) != True:
                return True
            else:
                return False

    def confirmaReserva_vol(self): 
        if not self.lista_vuelos:
            return 0
        for vuelo in self.lista_vuelos:
            sksc = Skyscanner()
            sksc.confirm_reserve(self.user, vuelo)
        return True

    def cancelaReserva_vol(self): # OJO PIOJO A ESTA FUNCION
        for vuelo in self.lista_vuelos:
            sksc = Flights()
            if sksc.reserva_vol(self.user, vuelo) != True:
                return True
            else:
                return False

    def confirmaReserva_hotel(self):
        if not self.lista_hoteles:
            return 0
        for hotel in self.lista_hoteles:
            hotels = Booking()
            hotels.confirm_reserve(self.user, hotel)
        return True
    
    def cancelaReserva_hotel(self): # OJO PIOJO A ESTA FUNCION
        for hotel in self.lista_hoteles:
            hotels = Booking()
            if hotels.reserva_hotel(self.user, hotel) != True:
                return True
            else:
                return False

    def reservarYpagar(self):
        self.confirmaReserva_hotel()
        self.confirmaReserva_vehicle()
        self.confirmaReserva_vol()
        self.precio = self.sumaPrecios()
        if self.user.pagament(self):
            return True
        else:
            raise ValueError("Error: Pagament no realitzat correctament")