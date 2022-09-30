from datetime import date
from decimal import Rounded
from model.Flight import Flight

from config.config import CURRENT_DATE_FORMAT
from typing import Dict, List


class Timeline(object):

    def __init__(self, flights: List[Flight], timeline_day: date):

        self.flights: List[Flight] = flights
        self.timeline_day: date = timeline_day
        self.checkClass()

    def __repr__(self) -> str:
        """
        Special method to represent the object of a class as a string
        """

        return str(self.timeline_day)

    def checkClass(self):
        """
        check and raise exceptions in the current class 
        """
        flights_dict: Dict[str, Dict[str, str]] = {}
        flights_check: Dict[str, bool] = {}
        # Check that all planes are assigned two flights, one outbound and one back
        for flight in self.flights:
            airplane_code = flight.airplane.code
            route_from = flight.route._from
            route_to = flight.route._from
            if airplane_code not in flights_dict:
                if airplane_code not in flights_check:
                    flights_check[airplane_code] = False
                elif flights_check[airplane_code]:
                    raise Exception(
                        f"The airplane {airplane_code} already had a round trip today")
                else:
                    flights_dict[airplane_code] = {
                        '_from': route_from, '_to': route_to}
            else:
                if flights_dict[airplane_code]['_to'] != route_from or flights_dict[airplane_code]['_from'] != route_to:
                    raise Exception(
                        f"The airplane {airplane_code} expecte return from {flights_dict[airplane_code]['_to']} but the current route is {route_from} - {route_to}")
                else:
                    flights_check[airplane_code] = True
                    del flights_dict[airplane_code]
        pass

    def current_date_format(self) -> str:
        """
        returns the current formatted date
        """

        day: int = self.timeline_day.day
        month: str = CURRENT_DATE_FORMAT[self.timeline_day.month - 1]
        year: int = self.timeline_day.year
        messsage: str = "{} de {} del {}".format(day, month, year)

        return messsage

    def get_number_of_passages_sale(self) -> int:
        """
        returns the total number of passages sold in all the flights in the day
        """

        total_passages = sum(v.get_number_passages() for v in self.flights)

        return total_passages

    def get_number_of_economic_passages(self) -> int:
        """
        returns the total number of economic passages sold in all the flights in the day
        """

        total_economic_passages = sum(
            len(v.get_economic_passages_list()) for v in self.flights)

        return total_economic_passages

    def get_number_of_premium_passages(self) -> int:
        """
        returns the total number of premium passages sold in all the flights in the day
        """

        total_economic_passages = sum(
            len(v.get_premium_passages_list()) for v in self.flights)

        return total_economic_passages

    def get_total_income_economic_passages(self) -> float:
        """
        retunrs the total income from economic passages sales 
        """

        total_income: float = sum(
            v.get_total_income_by_economic_passages() for v in self.flights)

        return total_income

    def get_total_income_premium_passages(self) -> float:
        """
        retunrs the total income from premium passages sales 
        """

        total_income: float = sum(
            v.get_total_income_by_premium_passages() for v in self.flights)

        return total_income

    def get_flights_by_airplane_code(self,airplane_code:str)-> List[Flight]:
        """
        returns the flights on which the aircraft has been scheduled
        """

        flights_list = list[Flight]=[]
        for flight in self.flights:
            if flight.airplane.code.lower() == airplane_code.lower():
                flights_list.append(flight)
        return flights_list

    def get_list_of_airplanes_codes(self)->List[str]:
        """
        returns all the airplanes codes in flights
        """
        airplane_codes_list:List[str] = []
        for v in self.flights:
            if v.airplane.code not in airplane_codes_list:
                airplane_codes_list.append(v.airplane.code)
        
        return airplane_codes_list

    # This method print the flight with greatest number passengers

    def get_airplane_with_highest_numbers_passengers_on_all_flights(self) -> None:
        """
        returns the airplane with the highest number of passengers on all its flights
        """
        airplanes_codes = self.get_list_of_airplanes_codes()
        highest_num_passager = sum(v.get_number_passages() for v in self.get_flights_by_airplane_code(airplanes_codes[0]))
        airplane_selected = airplanes_codes[0]
        del airplanes_codes[0]
        for a in airplanes_codes:
            sum_num_passagers = sum(v.get_number_passages() for v in self.get_flights_by_airplane_code(a))
            if highest_num_passager> sum_num_passagers:
                highest_num_passager = sum_num_passagers
                airplane_selected = a
        
        print(
            f"The plane with the most passengers is: {airplane_selected} with {highest_num_passager} passengers carried.")

    def get_greatest_numbers_passengers(self) -> None:
        # Airplane code with greatest number passengers
        airplane_code: str = ''
        # Greatest numbers of passengers among the flights
        greater_number_passengers: int = 0

        # Iterate all the flights of the day
        for i in self.flights:
            # Compare and get greatest number passengers
            if (greater_number_passengers < len(i.passages)):
                airplane_code = i.airplane.code
                greater_number_passengers = len(i.passages)

        print(
            f"10.- The plane with the most passengers is: {airplane_code}. With a total of {greater_number_passengers} passagers.")

    def get_the_firsts_flights_with_the_highest_sales(self, num: int) -> str:

        flight_list: list[Dict[str:float]] = [{'route': f.get_route_code(), 'profits': round(
            f.get_total_income_by_all_passages(), 2)} for f in self.flights]
        
        firsts_flights_list: list[str] = []
        more_than = 0
        if len(flight_list) < num:
            raise Exception(f"The param num cannot be more than the scheduled flights. ")
        while len(firsts_flights_list) < num:
            index = 0 if flight_list[0]['profits'] > flight_list[1]['profits'] else 1
            more_than = flight_list[index]['profits']
            firsts_flights_list.append(
                flight_list[index])
            del flight_list[index]
            for item in flight_list:
                if len(firsts_flights_list) == num:
                    break
                elif item['profits'] > more_than:
                    firsts_flights_list.append(item)

        return firsts_flights_list
