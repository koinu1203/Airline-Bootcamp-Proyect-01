from inspect import _void
from data.parse_data import LOCAL_DATA
from model.Flight import Flight

local = LOCAL_DATA

# This method print the flight with greatest number passengers
def question10() -> str:

    # Airplane code with greatest number passengers
    airplane_code: str = ''
    # Greatest numbers of passengers among the flights
    greater_number_passengers: int = 0

    # Iterate all the flights of the day
    for i in local.flights:
        # print(len(i.passages))
        # Compare and get greatest number passengers
        if (greater_number_passengers < len(i.passages)):
            airplane_code = i.airplane.code
            greater_number_passengers = len(i.passages)

    print(
        f"El avión con más pasajeros es: {airplane_code}. Con un total de {greater_number_passengers}.")

def question_one()-> int:
    # What is the total number of passages sold among all the flights?
    total_passages_sale = local.get_number_of_passages_sale()
    
    return total_passages_sale

def question_two()->float:
    # What is the total income from the sale of economic passages?
    total_income_economic_passages = sum(v.get_total_income_by_economic_passages() for v in local.flights)

    return total_income_economic_passages

def question_three()->float:
    # What is the total income from the sale of premium passages?
    total_income_premium_passages = sum(v.get_total_income_by_premium_passages() for v in local.flights)

    return total_income_premium_passages
