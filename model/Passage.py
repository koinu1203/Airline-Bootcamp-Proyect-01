from model.Route import Route


class Passage(object):
    def __init__(self, passage_id: int, passenger_name: str, tax: float, gross_price: float, isPremium: bool):

        self.passage_id: int = passage_id
        self.passenger_name: str = passenger_name
        self.tax: float = tax
        self.gross_price: float = gross_price
        self.isPremium: bool = isPremium
        self.checkClass()

    def __repr__(self) -> str:
        """
                Special method to represent the object of a class as a string
                """

        return str(self.passage_id)

    def checkClass(self):
        """
        check and raise exceptions in the current class 
        """

        if (self.tax < 0):
            raise Exception(
                f"The tax cannot be negative, id: {self.passage_id} - tax: {self.tax}")
        if (self.gross_price < 0):
            raise Exception(
                f"The gross_price cannot be negative, id: {self.passage_id} - gross_price: {self.gross_price}")
        pass

    def get_net_price(self) -> float:
        """
        return the net price of the passage 
        """

        return self.gross_price + self.tax
