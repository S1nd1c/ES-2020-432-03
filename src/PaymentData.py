class PaymentData:

    def __init__(self, tipus_targeta, nom, numero, codi):
        self.tipus_targeta = tipus_targeta
        self.nom = nom
        self.numero = numero
        self.codi = codi

    def validateData(self):
        return type(self.nom) == str and type(self.tipus_targeta) == str and type(self.numero) == str and type(self.codi) == str 