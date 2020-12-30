import tkinter as tk
from .template import template as buat_template


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(MainApp, self).__init__(*args, **kwargs)
        self.title("Simdak")
