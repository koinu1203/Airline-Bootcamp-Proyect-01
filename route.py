
CITY_CODE = {
    "Lima": "LIM",
    "Ayacucho": "AYA",
    "Cusco": "CUS",
    "Arequipa": "ARE",
    "Tarapoto": "TAR",
}


class Route:
    def __init__(self,_from:str,_to:str,base_price:float,economy_class:float,premiun_class:float):
        self.code = CITY_CODE[_from]+" - "+CITY_CODE[_to]
        self.name = _from+" - "+_to
        self.base_price = base_price
        self.economy_class = economy_class
        self.premiun_class = premiun_class
    