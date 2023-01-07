from mother import Mother
from father import Father

class Child(Father,Mother):

    def __init__(self) -> None:
        super().__init__()
        print("child constructor run")

    def hair_color(self):
        Mother.hair_color(self)
    
    def music_talent(self):
        print("has no talent")