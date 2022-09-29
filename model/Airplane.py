class Airplane(object):

    def __init__(self, code: str, economy_seats: int, premiun_seats: int):
        self.code = code
        self.capacity: int = economy_seats + premiun_seats
        self.economy_seats: int = economy_seats
        self.premiun_seats: int = premiun_seats
        self.checkClass()

    def __repr__(self) -> str:
        """
        Special method to represent the object of a class as a string
        """

        return self.code

    def checkClass(self):
        """
        check and raise exceptions in the current class 
        """
        if self.capacity < 0:
            raise Exception(f"The airplane capacity cannot be negative")
        if self.economy_seats < 0:
            raise Exception(f"The airplane economy seats cannot be negative")
        if self.premiun_seats < 0:
            raise Exception(f"The airplane premiun seats cannot be negative")
        pass
