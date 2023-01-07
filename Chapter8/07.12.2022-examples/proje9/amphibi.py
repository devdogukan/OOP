from land import Land
from water import Water
from motor import Motor

class Amphibi(Land,Water,Motor):

    def __init__(self, price, vehicle_type, wheel_count, seat_count,length,ship_type,motor_volume,fuel,power) -> None:
        Land.__init__(self,price, vehicle_type, wheel_count, seat_count)
        Water.__init__(self,price,length,ship_type)
        Motor.__init__(self,motor_volume,fuel,power)
        print("Amphibi constructor run")

    def move(self):
        Land.move(self)
        Water.move(self)