class PaymentData:

    def __init__(self, tipus_targeta, nom, numero, codi):
        self.tipus_targeta = tipus_targeta
        self.nom = nom
        self.numero = numero
        self.codi = codi

    def solicita_dades_pagament(nom,preu):
        tipus_targeta = input('Introdueix el tipus de pagament: ')
        numero = input('Introdueix el numero de la targeta: ')
        codi = input('Introdueix el codi de la targeta: ')
        PaymentData(tipus_targeta,nom,numero,codi,preu)