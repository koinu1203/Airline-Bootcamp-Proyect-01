#from model.Route import Route
class Passage(object):
	def __init__(self, passage_id:int, passenger_name:str, route:Route, price:float):
		
		self.passage_id: int = passage_id
		self.passenger_name: str = passenger_name
		self.route: Route = route 
		self.price: float = price

		pass