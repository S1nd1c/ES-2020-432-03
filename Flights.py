from Skyscanner import Skyscanner


class Flights:

    def __init__(self, codi_vol, destinacio, preu):
        self.codi_vol = codi_vol
        self.destinacio = destinacio
        self.preu = preu

    def reserva_vol(self, user:User):
        skyscanner = Skyscanner()
        
        if skyscanner.confirm_reserve(user, self):
            return True
        else:
            return False
