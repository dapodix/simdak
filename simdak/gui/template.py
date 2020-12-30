import os
import shutil
from tkinter.messagebox import askquestion, showwarning
from tkinter.filedialog import asksaveasfilename
from simdak.template import TEMPLATE_FILE


def template() -> None:
    filepath = asksaveasfilename(
        initialdir="/",
        title="Simpan file",
        filetypes=(("Excel file", "*.xlsx"), ("semua file", "*.*")),
    )
    try:
        shutil.copy(TEMPLATE_FILE, filepath)
        res = askquestion("Sukses", "Berhasil membuat template, buka file?")
        if res == "yes":
            os.startfile(filepath)
    except:
        showwarning("Gagal", "Gagal membuat template")
