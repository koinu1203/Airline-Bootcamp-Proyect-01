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
