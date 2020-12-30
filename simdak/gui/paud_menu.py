import tkinter as tk
from .template import template as buat_template


class PaudMenu(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        super(PaudMenu, self).__init__(parent, *args, **kwargs)
        self.add_command(label="Buat Template", command=buat_template)
