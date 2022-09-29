from typing import List
from model.Route import Route
from model.Airplane import Airplane
from model.Flight import Flight
from model.Passage import Passage
from model.Timeline import Timeline
from datetime import date
from local_data import *
from config.config import *
import random


def generate_passage(route_code:str,id_count:int) -> list[Passage]:
    """
    randomly generate tickets for the airline
    """
    # calculate random number for number of passages
    range_economic: Dict[str,float]= AIRLINE_ESTIMATE_RANGE_PASSAGES[route_code]['economic']
    range_premiun: Dict[str,float] = AIRLINE_ESTIMATE_RANGE_PASSAGES[route_code]['premium']
    economic_seats_occupied:int = random.randrange(range_economic['MIN'],range_economic['MAX'])
    premiun_seats_occupied:int = random.randrange(range_premiun['MIN'],range_premiun['MAX'])

    # calculate economic and premiun price
    prices = AIRLINE_PRICES[route_code]
    economic_seat_price:float = float(prices['base_price'] + prices['economic_seat'])
    premiun_seat_price:float = float(prices['base_price'] + prices['premium_seat'])

    # calculate IGV 
    economic_seat_tax:float = (float(IGV_PERCENT)/100.0)*economic_seat_price
    premiun_seat_tax:float = (float(IGV_PERCENT)/100.0)*premiun_seat_price
    
    # generate passage
    passages:list[Passage]=[]
    # generate economict seats 
    for i in range(economic_seats_occupied):
        # TODO: generar de manera ramdon los nombres de los pajeros
        passages.append(Passage(id_count,'LoreIpsum',economic_seat_tax,economic_seat_price))
        id_count +=1
    
    # generate premiun seats
    for i in range(premiun_seats_occupied):
        # TODO: generar de manera ramdon los nombres de los pajeros
        passages.append(Passage(id_count,'LoreIpsum',premiun_seat_tax,premiun_seat_price))
        id_count +=1

    return passages


def parse_routes()-> Dict[str,Route]:
    """
    
    """
    routes: Dict[str,Route]={}
    for k in AIRLINE_ROUTES:
        value = AIRLINE_ROUTES[k]
        value = value.split(' - ')
        routes[k] = Route( value[0], value[1],
            AIRLINE_PRICES[k]['base_price'],
            AIRLINE_PRICES[k]['economic_seat'],
            AIRLINE_PRICES[k]['premium_seat']
        )
    return routes


def generate_flights() -> list[Flight]:
    flights: list[Flight] = []
    airplanes: Dict[str,Airplane] = {}
    routes: Dict[str,Route] = parse_routes()
    id_count=0
    for key in AIRLINE_SCHEDULED_FLIGHTS:
        airplane_code:str = AIRLINE_SCHEDULED_FLIGHTS[key]['airplane']
        if key not in airplanes:
            airplanes[key] = Airplane(airplane_code,ECONOMIC_SEATS,PREMIUM_SEATS)
        passages = generate_passage(key,id_count)
        id_count += len(passages)
        departure_hour = AIRLINE_SCHEDULED_FLIGHTS[key]['departure_hour']
        flights.append(Flight(routes[key],passages,airplanes[key],departure_hour))

    return flights

def generate_local_data() -> Timeline:
    flights = generate_flights()
    current_day = date.today()
    timeline = Timeline(flights,current_day)
    return timeline


LOCAL_DATA:Timeline = generate_local_data()