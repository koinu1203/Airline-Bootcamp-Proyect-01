from datetime import datetime
from model.Flight import Flight

from typing import List

class Timeline :
    
    def __init__(self, flights:List(Flight), timeline_day:datetime):
        
        self.flights:List(Flight) = flights
        self.timeline_day:datetime = timeline_day

    def current_date_format(date) -> str:
        """
        returns the current formatted date
        """
        months:tuple(str) = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        day:int = date.day
        month:str = months[date.month - 1]
        year:int = date.year
        messsage:str = "{} de {} del {}".format(day, month, year)

        return messsage