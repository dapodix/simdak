from __future__ import annotations
import os
from openpyxl import Workbook, load_workbook
from openpyxl.worksheet.worksheet import Worksheet
from typing import Union
from . import RkasData, SimdakPaud

CWD = os.getcwd()


def exports(email: str, password: str, filepath: str = "", sheet: str = "Sheet1"):
    print("Export")
    simdak = SimdakPaud(email, password)
    rkas = simdak.rkas()[0]
    rkas_datas = rkas.get(save_as=RkasData)
    filepath = filepath or os.path.join(CWD, f"{rkas.npsn}.xlsx")
    ws: Worksheet = None
    if os.path.isfile(filepath):
        wb = load_workbook(filepath)
        ws = wb.get_sheet_by_name(sheet)
    else:
        wb = Workbook()
        ws = wb.active
        ws.title = sheet
    ws["A1"] = "No"
    for k, v in RkasData.MAPPING.items():
        ws[f"{v}1"] = k.replace("_", " ").title()
    for i, rkas_data in enumerate(rkas_datas):
        rkas_data.to_row(ws, i + 2)
        ws[f"A{i+2}"] = i + 1
    wb.save(filepath)


def imports(email: str, password: str, filepath: str = "", sheet: str = "Sheet1"):
    print("Import")
    simdak = SimdakPaud(email, password)
    rkas = simdak.rkas()[0]
    filepath = filepath or os.path.join(CWD, f"{rkas.npsn}.xlsx")
