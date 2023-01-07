from vehicle import Vehicle

class Air(Vehicle):

    def __init__(self, price,wingspan,weight,passenger_count,max_altitude) -> None:
        super().__init__(price)
        self.wingspan = wingspan
        self.weight= weight
        self.passenger_count = passenger_count
        self.max_altitude = max_altitude
        print("air constructor run")

    def move(self):
        print("fly")