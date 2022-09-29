from data.parse_data import LOCAL_DATA
from model.Flight import Flight
from model.Timeline import Timeline

local = LOCAL_DATA

def question10() -> str:
    local.get_greatest_numbers_passengers()
