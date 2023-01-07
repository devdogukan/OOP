from computer import Computer
from keyboard import Keyboard
from monitor import Monitor

class Desktop(Computer, Keyboard, Monitor):
    """Desktop class inherited from Computer, Keyboard, Monitor

    
    has constructor 
    "Lenovo",8000,"I3",8,256,"Onboard",150,"Turkish","Yes",17,3000

    """
    def __init__(self, brand, price, cpu, ram, disk, gpu, keyboard_price, alphabet, backlight, monitor_size, monitor_price, monitor_type = "") -> None:
        """constructor of Desktop 


        calls computer, keyborad and monitor init methods with self

        sets the price of Desktop with sum of separate parts 
        
        """
        Computer.__init__(self, brand, price, cpu, ram, disk, gpu)
        Keyboard.__init__(self, brand, keyboard_price, alphabet, backlight)
        Monitor.__init__(self, brand, monitor_price, monitor_size, monitor_type)
        self.price = price + keyboard_price + monitor_price
