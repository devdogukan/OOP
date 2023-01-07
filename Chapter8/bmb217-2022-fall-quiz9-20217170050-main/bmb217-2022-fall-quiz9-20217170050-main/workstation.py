from desktop import Desktop
from camera import Camera
from microphone import Microphone

class Workstation(Desktop, Camera, Microphone):
    """Workstation class inherited from Desktop, Camera, Microphone

    """
    #                  "Dell",60000,"Xeon",64,2048,"Quadro6000",500,"English","Ambient",        500,           "24mpx",       200,       "cordless",21,5000
    def __init__(self, brand, price, cpu, ram, disk, gpu,microphone_price, alphabet, backlight, keyboard_price, resolution, camera_price, microphone_brand, monitor_size, monitor_price,microphone_type="", monitor_type="") -> None:
        """constructor of Workstation 


        calls Desktop, Camera and Microphone init methods with self

        sets the price of Workstation with sum of separate parts 
        
        """
        Camera.__init__(self, brand, camera_price, resolution)
        Microphone.__init__(self, microphone_brand, microphone_price, microphone_type)
        Desktop.__init__(self, brand, price, cpu, ram, disk, gpu,keyboard_price, alphabet, backlight, monitor_size, monitor_price, monitor_type)
        self.price = price + keyboard_price + camera_price + microphone_price + monitor_price