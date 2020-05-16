class Hotels:

    def __init__(self, id_hotel, ciutat, direccio, preu, data_entrada, data_sortida, num_habs):
        self.id_hotel = id_hotel
        self.ciutat = ciutat
        self.direccio = direccio
        self.preu = preu
        self.data_entrada = data_entrada
        self.data_sortida = data_sortida
        self.num_habs = num_habs


    def reserva_hotel(self, user:User):
        booking = Booking.Booking()
        
        if booking.confirm_reserve(user, self):
            return True
        else:
            return False    