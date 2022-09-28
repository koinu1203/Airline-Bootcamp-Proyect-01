from ..config import DEPARTURE_HOUR
from model.Route import Route
from model.Passage import Passage
from model.Airplane import Airplane

from typing import List


class Flight(object):

    def __init__(self, route: Route, passages: List(Passage), airplane: Airplane, departure_hour: str):
        self.route: route = route
        self.passages: List(Passage) = passages
        self.airplane: Airplane = airplane
        self.departure_hour: str = departure_hour
