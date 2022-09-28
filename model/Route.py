
from config.config import IGV_PERCENT,CITY_TO_CODE

class Route(object):
    def __init__(
        self,
        _from:str,
        _to:str,
        base_price:float,
        economy_class:float,
        premiun_class:float
    ):
        self.code : str = CITY_TO_CODE[_from]+" - "+CITY_TO_CODE[_to]
        self.name : str = _from+" - "+_to
        self._from : str = _from
        self._to : str = _to
        self.base_price : float = base_price
        self.economy_class : float = economy_class
        self.premiun_class : float = premiun_class

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
    
    def get_code_from(self)->str:
        """
        get city code from route _from
        """

        return CITY_TO_CODE[self._from]

    def get_code_to(self)->str:
        """
        get city code from route _to
        """

        return CITY_TO_CODE[self._to]