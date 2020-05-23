from src.Skyscanner import Skyscanner


class Flights:

    def __init__(self, codi_vol, destinacio, preu):
        self.codi_vol = codi_vol
        self.destinacio = destinacio
        self.preu = preu

    def dataVolOK(self):
        return type(self.codi_vol) == str and type(self.destinacio) == str and type(self.preu) == int
    
    def reserva_vol(self, user):
        skyscanner = Skyscanner()
        
        if self.dataVolOK() and skyscanner.confirm_reserve(user, self):
            return True
        else:
            return False
