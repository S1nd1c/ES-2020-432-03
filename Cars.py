from Rentalcars import Rentalcars
import User

class Cars:

    def __init__(self, id_cotxe, tipus, marca, model, ubi_recollida, ubi_devolucio, data_recollida, data_devolucio):
        self.id_cotxe = id_cotxe
        self.tipus = tipus
        self.marca = marca
        self.model = model
        self.ubi_recollida = ubi_recollida
        self.ubi_devolucio = ubi_devolucio
        self.data_recollida = data_recollida
        self.data_devolucio = data_devolucio

    def reserva_coche(self, user:User):
        rentalcar = Rentalcars.Rentalcars()
        
        if rentalcar.confirm_reserve(user, self):
            return True
        else:
            return False