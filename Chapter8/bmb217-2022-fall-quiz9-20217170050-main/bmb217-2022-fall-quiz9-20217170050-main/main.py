from notebook import Notebook
from desktop import Desktop
from workstation import Workstation
from computer import Computer


notebook1 = Notebook("HP",25000,"I7",16,512,"RTX3060",15.6)
desktop1 = Desktop("Lenovo",8000,"I3",8,256,"Onboard",150,"Turkish","Yes",17,3000)
workstation1 = Workstation("Dell",60000,"Xeon",64,2048,"Quadro6000",500,"English","Ambient",500,"24mpx",200,"cordless",21,5000)
computer1 = Computer("Casper",5000,"AMD",4,128,"Onboard")

for hardware in [notebook1,desktop1,workstation1,computer1]:
    print(hardware.price, hardware.brand)

"""Example output
25000 HP
11150 Lenovo
66200 Dell
5000 Casper
"""
