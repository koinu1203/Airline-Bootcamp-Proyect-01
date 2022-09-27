from random import randint

Airplane_Code = [
    {
   "code":"A001",
   "economy_seats":randint(120,130),
   "premiun_seats":randint(10,20),
    },
    {
   "code":"A002",
   "economy_seats":randint(130,144),
   "premiun_seats":randint(15,24),
    },
      {
   "code":"A003",
   "economy_seats":randint(115,138),
   "premiun_seats":randint(16,22),
    },
       {
   "code":"A004",
   "economy_seats":randint(100,150),
   "premiun_seats":randint(16,22),
    },
           {
   "code":"A001",
   "economy_seats":randint(100,115),
   "premiun_seats":randint(10,15),
    },
    {
   "code":"A002",
   "economy_seats":randint(105,120),
   "premiun_seats":randint(14,20),
    },
      {
   "code":"A003",
   "economy_seats":randint(100,110),
   "premiun_seats":randint(13,18),
    },
       {
   "code":"A004",
   "economy_seats":randint(90,105),
   "premiun_seats":randint(10,15),
    }
]

class Airplane:
    def __init__(self,code:str,economy_seats:int,premiun_seats:int):
        self.code = code
        self.capacity : int = economy_seats + premiun_seats 
        self.economy_seats = economy_seats 
        self.premiun_seats = premiun_seats
   
    