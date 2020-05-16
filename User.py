from . import PaymentData
from . import Bank 
from . import Viaje

class User:

    def __init__(self, nom, dni, telefon, direccio, email):
        self.nom = nom
        self.dni = dni
        self.telefon = telefon
        self.direccio = direccio
        self.email = email

    def pagament(self, viaje:Viaje):
        

