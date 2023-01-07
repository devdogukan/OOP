from vehicle import Vehicle

class Land(Vehicle):

    def __init__(self,price,vehicle_type,wheel_count,seat_count) -> None:
        Vehicle.__init__(self,price)
        self.vehicle_type = vehicle_type
        self.wheel_count = wheel_count
        self.seat_count = seat_count
        print("land constructor run")

    def move(self):
        print("move by wheel")