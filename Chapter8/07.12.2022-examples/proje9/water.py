from vehicle import Vehicle

class Water(Vehicle):

    def __init__(self, price, length, ship_type) -> None:
        super().__init__(price)
        self.length = length
        self.ship_type = ship_type
        print("water constructor run")

    def move(self):
        print("floating")