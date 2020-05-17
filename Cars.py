from Rentalcars import Rentalcars
import User

class Cars:

    def __init__(self, id_cotxe, tipus, marca, ubi_recollida, ubi_devolucio, dias_estancia, preu):
        self.id_cotxe = id_cotxe
        self.tipus = tipus
        self.marca = marca
        self.model = model
        self.ubi_recollida = ubi_recollida
        self.ubi_devolucio = ubi_devolucio
        self.dias_estancia = dias_estancia
        self.preu = preu

    def reserva_coche(self, user:User):
        rentalcar = Rentalcars.Rentalcars()
        
        if rentalcar.confirm_reserve(user, self):
            return True
        else:
            return False