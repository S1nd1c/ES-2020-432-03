from . import User
from . import Hotels


class Booking():

    def __init__(self):
        pass

    def confirm_reserve(self, user: User, hotels: Hotels) -> bool:
        return True