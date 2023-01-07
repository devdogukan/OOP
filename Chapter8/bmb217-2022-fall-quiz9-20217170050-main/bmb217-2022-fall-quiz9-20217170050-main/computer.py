from hardware import Hardware

class Computer(Hardware):
    """Computer class inherited from hardware

    has constructor
    """

    def __init__(self, brand, price, cpu, ram, disk, gpu) -> None: 
        """constructor of computer
        

        Args:
            brand (str): brand of computer
            price (int): price of computer
            cpu (_type_): cpu of computer
            ram (_type_): ram of computer
            disk (_type_): disk of computer
            gpu (_type_): gpu of computer
        """ 
        Hardware.__init__(self, brand, price)
        self.cpu = cpu
        self.ram = ram
        self.disk = disk
        self.gpu = gpu
