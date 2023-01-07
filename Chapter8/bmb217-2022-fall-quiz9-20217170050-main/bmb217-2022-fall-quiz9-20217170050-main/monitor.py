from hardware import Hardware

class Monitor(Hardware):
    """Monitor class inherited from hardware

    has constructor 
    """
    def __init__(self, brand, price, monitor_size, monitor_type) -> None:
        """Monitor constructor

        Args:
            brand (str): brand of Monitor
            price (int): price of Monitor
            monitor_size (str): size of Monitor 
            monitor_type (str): type of Monitor 
        """ 
        Hardware.__init__(self, brand, price)
        self.monitor_size = monitor_size
        self.monitor_type = monitor_type


