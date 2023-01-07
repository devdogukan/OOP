from grandpa import Grandpa

class Father(Grandpa):

    def __init__(self) -> None:
        super().__init__()
        print("father constructor run")

    def hair_color(self):
        print("hair color : yellow")

    def music_talent(self):
        print("has music talent")