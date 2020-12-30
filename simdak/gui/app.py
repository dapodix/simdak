import tkinter as tk
from . import MainMenu


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(MainApp, self).__init__(*args, **kwargs)
        self.title("Simdak")
        menu = MainMenu(self)
        self.config(menu=menu)
        self.menu = menu
