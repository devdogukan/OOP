class Adres:

    def __init__(self, city, town) -> None:
        self.city = city
        self.town = town
        
    def __str__(self) -> str:
        return f'adres:{self.city}-{self.town}'

