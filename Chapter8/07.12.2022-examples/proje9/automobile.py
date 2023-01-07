from land import Land
from motor import Motor

class Automobile(Land, Motor):

    def __init__(self, price, vehicle_type, wheel_count, seat_count,motor_volume,fuel,power) -> None:
        super().__init__(price, vehicle_type, wheel_count, seat_count)
        Motor.__init__(self,motor_volume,fuel,power)
        print("Automobile constructor run")

