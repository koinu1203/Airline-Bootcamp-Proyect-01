
from model.Route import Route
from model.Passage import Passage
from model.Airplane import Airplane

from typing import List


class Flight(object):

    def __init__(self, route: Route, passages: List[Passage], airplane: Airplane, departure_hour: str):
        self.route: Route = route
        self.passages: List[Passage] = passages
        self.airplane: Airplane = airplane
        self.departure_hour: str = departure_hour

    def __repr__(self) -> str:
        """
        Special method to represent the object of a class as a string
        """

        return self.departure_hour

    def checkClass(self):
        """
        check and raise exceptions in the current class 
        """

        if (len(self.passages) > self.airplane.capacity):
            raise Exception(
                f"The airplane {self.airplane.code} only has the capacity to {self.airplane.capacity}. Ticket overbooking")
        if (len(self.get_economic_passages_list()) > self.airplane.economy_seats):
            raise Exception(
                f"The airplane {self.airplane.code} only has {self.airplane.economy_seats} economic seats. Ticket overbooking")
        if (len(self.get_premium_passages_list()) > self.airplane.premiun_seats):
            raise Exception(
                f"The airplane {self.airplane.code} only has {self.airplane.economy_seats} premium seats. Ticket overbooking")

    def get_number_passages(self) -> int:
        """
        get the total number of passage sold by this flight
        """

        return len(self.passages)

    def get_economic_passages_list(self) -> list[Passage]:
        """
        return a list with all the economic passages sale
        """

        economic_passages: list[Passage] = []
        for passage in self.passages:
            if not passage.isPremium:
                economic_passages.append(passage)

        return economic_passages

    def get_premium_passages_list(self) -> list[Passage]:
        """
        return a list with all the premium passages sale
        """

        premium_passages: list[Passage] = []
        for passage in self.passages:
            if passage.isPremium:
                premium_passages.append(passage)

        return premium_passages

    def get_total_income_by_all_passages(self) -> float:
        """
        returns the total income by all passages sales in the flight
        """
        total_income_all_passages: float = sum(
            p.gross_price for p in self.passages)

        return total_income_all_passages

    def get_total_income_by_economic_passages(self) -> float:
        """
        returns the total income by the economic passages sales in the flight
        """
        total_income_economic_passages: float = 0.0
        for passage in self.passages:
            if not passage.isPremium:
                total_income_economic_passages += passage.get_net_price()

        return total_income_economic_passages

    def get_total_income_by_premium_passages(self) -> float:
        """
        returns the total income by the premium passages sales in the flight
        """
        total_income_premium_passages: float = 0.0
        for passage in self.passages:
            if passage.isPremium:
                total_income_premium_passages += passage.get_net_price()

        return total_income_premium_passages

    def get_total_IGV_charge(self) -> float:
        """
        return the total of IGV charge 
        """

        total_IGV_Charge = sum(v.tax for v in self.passages)

        return total_IGV_Charge

    def get_route_code(self) -> str:
        """
        return the route code in flight
        """

        return self.route.code
