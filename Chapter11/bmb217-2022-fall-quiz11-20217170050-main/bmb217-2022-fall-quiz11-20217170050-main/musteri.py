from adres import Adres
from yemek import Yemek
from typing import List

class Musteri:

    def __init__(self, name, surname, balance, city, town) -> None:
        self.name:str          = name
        self.surname:str       = surname
        self.balance:str       = balance
        self.adres:Adres       = Adres(city, town)
        self.foods:List[Yemek] = []
        
    def siparis_ekle(self, food:Yemek):
        if self.balance >= food.price:
            self.foods.append(food)
            self.balance -= food.price
        
    def __str__(self) -> str:
        new_str = f'ad:{self.name},soyad:{self.surname},bakiye{self.balance}\n'
        new_str += str(self.adres) + '\n'
        
        for food in self.foods:
            new_str += str(food) + '\n'
            
        return new_str



        
