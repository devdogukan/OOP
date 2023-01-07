from hardware import Hardware

class Camera(Hardware):
    """Camera class inherited from hardware

    has constructor 
    """

    def __init__(self, brand, price, resolution) -> None:
        """camera constructor

        Args:
            brand (str): brand of camera
            price (int): price of camera
            resolution (str): resolution of camera
        """
        Hardware.__init__(self, brand, price)
        self.resolution = resolution
 
