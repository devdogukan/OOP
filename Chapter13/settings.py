class Settings:
    def __init__(self, input, option) -> None:
        self.input = input
        self.option = option
        
    def __str__(self):
        return f'{self.input} - {self.option}'