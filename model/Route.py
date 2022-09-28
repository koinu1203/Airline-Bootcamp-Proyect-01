from ..config import IGV_PERCENT,CITY_TO_CODE

class Route(object):
    def __init__(
        self,
        _from:str,
        _to:str,
        base_price:float,
        economy_class:float,
        premiun_class:float
    ):
        self.code = CITY_TO_CODE[_from]+" - "+CITY_TO_CODE[_to]
        self.name = _from+" - "+_to
        self.base_price = base_price
        self.economy_class = economy_class
        self.premiun_class = premiun_class

    def __repr__(self) -> str:
        """
        Special method to represent the object of a class as a string
        """
        return self.code
    
    def generate_price_economy_class(self) -> float:
        """
        generate economic price including IGV
        """
 
        return (self.base_price+self.economy_class)*(1.0+(float(IGV_PERCENT)/100.0))

    def generate_price_premiun_class(self) -> float:
        """
        generate economic price including IGV
        """
 
        return (self.base_price+self.premiun_class)*(1.0+(float(IGV_PERCENT)/100.0))