from datetime import date
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

    # This method print the flight with greatest number passengers

    def get_greatest_numbers_passengers(self) -> None:
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
    # This method print the flight with greatest number passengers

    def get_greatest_numbers_passengers(self) -> None:
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

    def get_the_first_three_flights_with_the_highest_sales(self) -> str:

        venta_por_vuelo = []

        for a in self.flights:
            ventas_por_pasaje = []
            suma_ventas_por_pasaje = 0
            for e in a.passages:
                ventas_por_pasaje.append(e.get_net_price())

            suma_ventas_por_pasaje = sum(ventas_por_pasaje)

            venta_por_vuelo.append(suma_ventas_por_pasaje)

        print(venta_por_vuelo, "\n")

        tres_primeros = []

        for i in venta_por_vuelo:
            if len(tres_primeros) == 3:
                break
            if len(tres_primeros) == 0:
                tres_primeros.append(venta_por_vuelo[0] if venta_por_vuelo[0] > venta_por_vuelo[1] else venta_por_vuelo[1])
            else:
                tres_primeros = sorted(tres_primeros, reverse=False)
                if i > tres_primeros[0]:
                    tres_primeros.append(i)
        print(tres_primeros)

