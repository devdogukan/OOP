from hardware import Hardware

class Keyboard(Hardware):
    """Keyboard class inherited from hardware

    has constructor 
    """
    def __init__(self, brand, price, alphabet, backlight) -> None:
        """Keyboard constructor

        Args:
            brand (str): brand of Keyboard
            price (int): price of Keyboard
            alphabet (str): resolution of Keyboard
            backlight (str): backlight of Keyboard
        """ 
        Hardware.__init__(self, brand, price)
        self.alphabet = alphabet
        self.backlight = backlight

