import . from Skyscanner
import . from User

class Flights:

    def __init__(self, codi_vol, destinacio, num_passatgers, preu):
        self.codi_vol = codi_vol
        self.destinacio = destinacio
        self.num_passatgers = num_passatgers
        self.preu = preu

    def reserva_vol(self, user:User):
        skyscanner = Skyscanner.Skyscanner()
        
        if skyscanner.confirm_reserve(user, self):
            return True
        else:
            return False
