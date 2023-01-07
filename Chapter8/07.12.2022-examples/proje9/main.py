from bike import Bike
from automobile import Automobile
from amphibi import Amphibi

bike1 = Bike(2000,'Bisiklet',2,2)
bike1.move()

auto1 = Automobile(300000,'otomobil',4,5,1400,'benzin',110)
print(auto1.price,auto1.power,auto1.wheel_count)
auto1.move()

amphi1 = Amphibi(5000000,'Hertürlü',6,2,8,'askeri',5000,'Motorin',2000)
print(amphi1.price,amphi1.wheel_count,amphi1.length,amphi1.fuel)
amphi1.move()