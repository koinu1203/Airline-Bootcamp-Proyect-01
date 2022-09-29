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

    # This method print the flight with greatest number passengers
    def get_greatest_numbers_passengers(self) -> str:
        # Airplane code with greatest number passengers
        airplane_code: str = ''
        # Greatest numbers of passengers among the flights
        greater_number_passengers: int = 0

        # Iterate all the flights of the day
        for i in self.flights:
            # print(len(i.passages))
            # Compare and get greatest number passengers
            if (greater_number_passengers < len(i.passages)):
                airplane_code = i.airplane.code
                greater_number_passengers = len(i.passages)

        print(
            f"El avión con más pasajeros es: {airplane_code}. Con un total de {greater_number_passengers}.")