import tkinter as tk

from . import PaudMenu


class FileMenu(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        super(FileMenu, self).__init__(parent, *args, **kwargs)
        self.add_command(label="Keluar", command=self.quit)


class MainMenu(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        super(MainMenu, self).__init__(parent, *args, **kwargs)
        self.file_menu = FileMenu(self)
        self.paud_menu = PaudMenu(self)

        self.add_cascade(label="File", menu=self.file_menu)
        self.add_cascade(label="Simdak Paud", menu=self.paud_menu)
