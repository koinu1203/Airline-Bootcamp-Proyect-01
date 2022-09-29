from datetime import datetime
from model.Flight import Flight

from config.config import CURRENT_DATE_FORMAT
from typing import List


class Timeline(object):

    def __init__(self, flights: List[Flight], timeline_day: datetime):

        self.flights: List[Flight] = flights
        self.timeline_day: datetime = timeline_day

    def __repr__(self) -> str:
        """
        Special method to represent the object of a class as a string
        """

        return str(self.timeline_day)

    def current_date_format(self) -> str:
        """
        returns the current formatted date
        """

        day: int = self.timeline_day.day
        month: str = CURRENT_DATE_FORMAT[self.timeline_day.month - 1]
        year: int = self.timeline_day.year
        messsage: str = "{} de {} del {}".format(day, month, year)

        return messsage

    def get_number_of_passages_sale(self)->int:
        """
        returns the total of passages sold in all the flights in the day
        """

        total_passages = sum(v.get_number_passages() for v in self.flights)

        return total_passages
    
    def get_total_income_economic_passages(self)->float:
        """
        retunrs the total income from economic passages sales 
        """

        total_income:float = sum(v.get_total_income_by_economic_passages() for v in  self.flights)

        return total_income
    
    def get_total_income_premium_passages(self)->float:
        """
        retunrs the total income from premium passages sales 
        """
        
        total_income:float = sum(v.get_total_income_by_premium_passages() for v in  self.flights)

        return total_income
    

