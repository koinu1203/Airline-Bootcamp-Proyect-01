from typing import Dict, Tuple


IGV_PERCENT: int = 18

CITY_TO_CODE : Dict[str,str] = {
    "Lima": "LIM",
    "Ayacucho": "AYA",
    "Cusco": "CUS",
    "Arequipa": "ARE",
    "Tarapoto": "TAR"
}

DEPARTURE_HOUR: Tuple[str] = (
    "06:30 AM",
    "07:25 AM",
    "08:10 AM",
    "15:45 PM",
    "16:25 PM",
    "17:15 PM",
    "17:50 PM"
)

CURRENT_DATE_FORMAT: Tuple[str] = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                                   "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

MAX_SEATS_CAPACITY = 168
PREMIUM_SEATS = 24

SCHEDULED_ROUTES: Tuple[str] = (
    "LIM - AYA",
    "LIM - CUS",
    "LIM - ARE",
    "LIM - TAR",
    "AYA - LIM",
    "CUS - LIM",
    "ARE - LIM",
    "TAR - LIM",
) 
