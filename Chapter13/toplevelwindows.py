from settings import Settings
from settingsWindow import SettingsWindow
from tkinter import *

class Window:
    def __init__(self, master) -> None:
        self.frame = Frame(master)
        
        button = Button(self.frame, text="Open Settings", command=self.open)
        button.pack(padx=50, pady=50)
        
        self.label = Label(self.frame, text="")
        self.label.pack(pady=10)
        
        self.frame.pack(padx=10, pady=10)
        
    def open(self):
        SettingsWindow(self.update)
        
    def update(self, settings:Settings):
        self.label.config(text = settings)
        
root = Tk()
window = Window(root)
root.mainloop()