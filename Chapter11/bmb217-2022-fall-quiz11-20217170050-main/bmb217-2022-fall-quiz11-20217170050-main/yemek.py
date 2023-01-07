class Yemek:

    def __init__(self, food_name, price) -> None:
        self.food_name = food_name
        self.price = price
        
    def __str__(self) -> str:
        return f'*yemek:{self.food_name},{self.price}tl'