from Route import Route

class Passage(object):
	def __init__(self, passage_id:int, passenger_name:str, tax:float, gross_price:float):
		
		self.passage_id: int = passage_id
		self.passenger_name: str = passenger_name
		self.tax: float = tax 
		self.gross_price: float = gross_price

	def __repr__(self) -> str:
		"""
    	Special method to represent the object of a class as a string
    	"""
		
		return self.passage_id
	
	def get_net_price(self) -> float:
		"""
		return the net price of the passage 
		"""

		return self.gross_price + self.tax;
	
