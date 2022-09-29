from config.config import IGV_PERCENT, CITY_TO_CODE


class Route(object):
    def __init__(
        self,
        _from: str,
        _to: str,
        base_price: float,
        economy_class: float,
        premiun_class: float
    ):
        self.code: str = CITY_TO_CODE[_from]+" - "+CITY_TO_CODE[_to]
        self.name: str = _from+" - "+_to
        self._from: str = _from
        self._to: str = _to
        self.base_price: float = base_price
        self.economy_class: float = economy_class
        self.premiun_class: float = premiun_class
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

        if self.base_price < 0:
            raise Exception(f"The base price of the route cannot be negative")
        if self.economy_class < 0:
            raise Exception(
                f"The price of the economy class cannot be negative")
        if self.premiun_class < 0:
            raise Exception(
                f"The price of the premiun class cannot be negative")
        if self._from == self._to:
            raise Exception(
                f"Flights cannot have the same departure and destination")
        pass

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

    def get_code_from(self) -> str:
        """
        get city code from route _from
        """

        return CITY_TO_CODE[self._from]

    def get_code_to(self) -> str:
        """
        get city code from route _to
        """

        return CITY_TO_CODE[self._to]
