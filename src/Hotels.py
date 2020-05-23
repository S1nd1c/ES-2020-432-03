import src.Booking

class Hotels:

    def __init__(self, id_hotel, ciutat, direccio, preu, dies_estada, num_habs):
        self.id_hotel = id_hotel
        self.ciutat = ciutat
        self.direccio = direccio
        self.preu = preu
        self.dies_estada = dies_estada
        self.num_habs = num_habs

    def dataHotelOK(self):
        return type(self.id_hotel) == int and type(self.ciutat) == str and type(self.direccio) == str and type(self.preu) == int and type(self.dies_estada) == int and type(self.num_habs) == int

    def reserva_hotel(self, user):
        booking = Booking.Booking() 
        if booking.confirm_reserve(user, self):
            return True
        else:
            return False    