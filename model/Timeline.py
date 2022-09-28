from datetime import datetime
from model.Flight import Flight

from config.config import CURRENT_DATE_FORMAT
<<<<<<< HEAD


from typing import List

class Timeline :
    
    def __init__(self, flights:List[Flight], timeline_day:datetime):
        
        self.flights:list(Flight) = flights
        self.timeline_day:datetime = timeline_day
    
=======
from typing import List


class Timeline(object):

    def __init__(self, flights: List[Flight], timeline_day: datetime):

        self.flights: List[Flight] = flights
        self.timeline_day: datetime = timeline_day

>>>>>>> main
    def __repr__(self) -> str:
        """
        Special method to represent the object of a class as a string
        """

        return str(self.timeline_day)

    def current_date_format(date) -> str:
        """
        returns the current formatted date
        """

        day: int = date.day
        month: str = CURRENT_DATE_FORMAT[date.month - 1]
        year: int = date.year
        messsage: str = "{} de {} del {}".format(day, month, year)

        return messsage
