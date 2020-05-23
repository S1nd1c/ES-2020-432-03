from src.Rentalcars import Rentalcars
from src.User import User

class Cars:

    def __init__(self, id_cotxe, tipus, marca, ubi_recollida, ubi_devolucio, dias_estancia, preu):
        self.id_cotxe = id_cotxe
        self.tipus = tipus
        self.marca = marca
        self.ubi_recollida = ubi_recollida
        self.ubi_devolucio = ubi_devolucio
        self.dias_estancia = dias_estancia
        self.preu = preu

    def validateDataCar(self):
        return type(self.id_cotxe) == str and type(self.tipus) == str and type(self.marca) == str type(self.ubi_recollida) == str and type(self.ubi_devolucio) == str and type(self.dias_estancia) == int and type(self.preu) == int
    
    def reserva_coche(self, user:User):
        rentalcar = Rentalcars()        
        if rentalcar.confirm_reserve(user, self):
            return True
        else:
            return False