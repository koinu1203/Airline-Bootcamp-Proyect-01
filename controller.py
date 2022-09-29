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
