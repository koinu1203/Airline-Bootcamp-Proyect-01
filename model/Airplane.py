
class Airplane:
    def __init__(self,code:str,economy_seats:int,premiun_seats:int):
        self.code = code
        self.capacity : int = economy_seats + premiun_seats 
        self.economy_seats = economy_seats 
        self.premiun_seats = premiun_seats
        
    def __repr__(self) -> str:
        """
        Special method to represent the object of a class as a string
        """

        return self.code
    