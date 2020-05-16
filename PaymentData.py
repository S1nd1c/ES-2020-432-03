class PaymentData:

    def __init__(self, tipus, nom, numero, codi, preu):
        self.tipus = tipus
        self.nom = nom
        self.numero = numero
        self.codi = codi
        self.preu = preu

    def solicita_dades_pagament(nom,preu):
        nb = input('Introdueix el tipus de pagament: ')
        nb = input('Introdueix el numero de la targeta: ')
        nb = input('Introdueix el codi de la targeta: ')
        PaymentData(tipus,nom,numero,codi,preu)