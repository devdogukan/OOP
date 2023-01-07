from land import Land

class Bike(Land):

    def __init__(self, price, vehicle_type, wheel_count, seat_count) -> None:
        super().__init__(price, vehicle_type, wheel_count, seat_count)
        print("bike constructor run")