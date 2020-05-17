import Booking

class Hotels:

    def __init__(self, id_hotel, ciutat, direccio, preu, dies_estada, num_habs):
        self.id_hotel = id_hotel
        self.ciutat = ciutat
        self.direccio = direccio
        self.preu = preu
        self.dies_estada = dies_estada
        self.num_habs = num_habs


    def reserva_hotel(self, user:User):
        booking = Booking.Booking()
        
        if booking.confirm_reserve(user, self):
            return True
        else:
            return False    