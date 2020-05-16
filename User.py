from PaymentData import PaymentData
from Bank import Bank 
from Viaje import Viaje

class User:

    def __init__(self, nom, dni, telefon, direccio, email, pagament:PaymentData):
        self.nom = nom
        self.dni = dni
        self.telefon = telefon
        self.direccio = direccio
        self.email = email
        self.pagament = pagament

    def validateInput():
        return type(self.nom) == str and type(self.dni) == str and type(self.telefon) == str and type(self.direccio) == str and tpye(self.email) == str

    def pagament(self, viaje:Viaje):
        viaje.sumaPrecios()
        preu = viaje.precioTotal
        if (Bank.do_payment(self,self.pagament)):
            return True
        else:
            print("Error: Pagament no realitzat correctament")
            return False

        
        

