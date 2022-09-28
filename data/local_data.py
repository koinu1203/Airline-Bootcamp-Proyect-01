

from typing import Dict


AIRLINE_ROUTES: Dict[str,str]={
    "LIM - AYA" : 'Lima - Ayacucho',
    "LIM - CUS" : 'Lima - Cusco',
    "LIM - ARE" : 'Lima - Arequipa',
    "LIM - TAR" : 'Lima - Tarapoto',
    "AYA - LIM" : 'Ayacucho - Lima',
    "CUS - LIM" : 'Cusco - Lima',
    "ARE - LIM" : 'Arequipa - Lima',
    "TAR - LIM" : 'Tarapoto - Lima',
}

AIRLINE_PRICES: Dict[str,Dict[str,str]]={
    "LIM - AYA" : {'base_price': 55.19, 'economic_seat': 8.00, 'premium_seat':16.00},
    "LIM - CUS" : {'base_price': 136.51, 'economic_seat': 8.00, 'premium_seat':16.00},
    "LIM - ARE" : {'base_price': 90.59, 'economic_seat': 8.00, 'premium_seat':16.00},
    "LIM - TAR" : {'base_price': 71.89, 'economic_seat': 8.00, 'premium_seat':16.00},
    "AYA - LIM" : {'base_price': 40.42, 'economic_seat': 7.00, 'premium_seat':16.00},
    "CUS - LIM" : {'base_price': 124.32, 'economic_seat': 7.00, 'premium_seat':16.00},
    "ARE - LIM" : {'base_price': 86.59, 'economic_seat': 7.00, 'premium_seat':16.00},
    "TAR - LIM" : {'base_price': 68.42, 'economic_seat': 7.00, 'premium_seat':16.00},
}

AIRLINE_SCHEDULED_FLIGHTS: Dict[str,Dict[str,str]]={
    "LIM - AYA" : {'airplane':'A001', 'departure_hour': '06:30 AM'},
    "LIM - CUS" : {'airplane':'A002', 'departure_hour': '07:25 AM'},
    "LIM - ARE" : {'airplane':'A003', 'departure_hour': '08:10 AM'},
    "LIM - TAR" : {'airplane':'A004', 'departure_hour': '08:50 AM'},
    "AYA - LIM" : {'airplane':'A001', 'departure_hour': '15:45 AM'},
    "CUS - LIM" : {'airplane':'A002', 'departure_hour': '16:25 AM'},
    "ARE - LIM" : {'airplane':'A003', 'departure_hour': '17:15 AM'},
    "TAR - LIM" : {'airplane':'A004', 'departure_hour': '17:50 AM'},
}

AIRLINE_ESTIMATE_RANGE_PASSAGES: Dict[str,Dict[str,Dict[str,str]]]={
    "LIM - AYA" : {'economic': {'MIN': 120, 'MAX':130}, 'premium':{'MIN': 10, 'MAX':20}},
    "LIM - CUS" : {'economic': {'MIN': 130, 'MAX':144}, 'premium':{'MIN': 15, 'MAX':24}},
    "LIM - ARE" : {'economic': {'MIN': 115, 'MAX':138}, 'premium':{'MIN': 16, 'MAX':22}},
    "LIM - TAR" : {'economic': {'MIN': 100, 'MAX':120}, 'premium':{'MIN': 12, 'MAX':18}},
    "AYA - LIM" : {'economic': {'MIN': 100, 'MAX':115}, 'premium':{'MIN': 10, 'MAX':15}},
    "CUS - LIM" : {'economic': {'MIN': 105, 'MAX':120}, 'premium':{'MIN': 14, 'MAX':20}},
    "ARE - LIM" : {'economic': {'MIN': 100, 'MAX':110}, 'premium':{'MIN': 13, 'MAX':18}},
    "TAR - LIM" : {'economic': {'MIN': 90, 'MAX':105}, 'premium':{'MIN': 10, 'MAX':15}},
}