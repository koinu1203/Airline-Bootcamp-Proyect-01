from typing import List
from model.Route import Route
from model.Airplane import Airplane
from model.Flight import Flight
from model.Passage import Passage
from model.Timeline import Timeline
from datetime import date
from local_data import *
from config.config import *

def generate_passage(route:Route,airplane:Airplane) -> list[Passage]:
    pass

def generate_routes()-> list[Route]:
    pass

def generate_airplanes() -> list[Airplane]:
    for key in AIRLINE_SCHEDULED_FLIGHTS:
        print(key)
    pass

def generate_flights() -> list[Flight]:
    airplanes = generate_airplanes()

    flights: list[Flight] = []
    for i in range(6):
        pass
    return flights

def generate_local_data() -> Timeline:
    flights = generate_flights()
    current_day = date.today()
    timeline = Timeline(flights,current_day)
    return timeline


LOCAL_DATA:Timeline = generate_local_data()