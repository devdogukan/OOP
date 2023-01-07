from hardware import Hardware

class Microphone(Hardware):
    """Microphone class inherited from hardware

    has constructor 
    """
    def __init__(self, brand, price, microphone_type) -> None:
        """Microphone constructor

        Args:
            brand (str): brand of Microphone
            price (int): price of Microphone
            microphone_type (str): type of Microphone 
        """ 
        Hardware.__init__(self, brand, price)
        self.microphone_type = microphone_type
