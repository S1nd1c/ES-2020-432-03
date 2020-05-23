from src.PaymentData import PaymentData
from src.Bank import Bank 

class User:

    def __init__(self, nom, dni, telefon, direccio, email):
        self.nom = nom
        self.dni = dni
        self.telefon = telefon
        self.direccio = direccio
        self.email = email


    def validateInput(self):
        return type(self.nom) == str and type(self.dni) == str and type(self.telefon) == str and type(self.direccio) == str and type(self.email) == str

    def seleccioMetodePagament(self,payment_data:PaymentData):
        self.dades_pagament=payment_data
    
    def pagament(self, precio):
        self.dades_pagament.añadirImporte(precio)
        banco = Bank()
        if self.validateInput() and self.dades_pagament.validateData():
            return banco.do_payment(self,self.dades_pagament)
        else:
            raise ValueError('Error en procesar el pagament')
        

        
        

