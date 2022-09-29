
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
