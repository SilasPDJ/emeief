import os
import sys
from time import sleep
import pyautogui as pygui
import subprocess
import pandas as pd
from clipboard import copy, paste
# import pandas as pd


def ____get_word_num_pages(doc_path: str, visible=False) -> int:
    from win32com.client import Dispatch
    # open Word
    word = Dispatch('Word.Application')
    word.Visible = visible
    word = word.Documents.Open(doc_path)
    word.Mail
    # get number of sheets
    word.Repaginate()
    num_of_sheets = word.ComputeStatistics(2)
    word.Close(False)
    return num_of_sheets


def pandas_read(excel_file_path: str) -> list:
    # retorna lista de alunos vinda da planilha excel
    def get_campos(campo): return df[campo].to_list()
    with open(excel_file_path, "rb") as f:
        df = pd.read_excel(f)
    return get_campos("NOME")


PATH = r"C:\Users\sbferreira\OneDrive\BKP SECRETARIA\HISTÓRICO ESCOLAR\\2022"
file_word = os.path.join(PATH, "MODELO HISTÓRICO ESCOLAR 2021 - MAIO.docx")
file_excl = os.path.join(PATH, "mala-direta-lista-atual-teste.xlsx")

list_of_students = pandas_read(file_excl)

num_pages = len(list_of_students)
os.startfile(file_word)

# accept mala direta
while True:
    try:
        pygui.getWindowsWithTitle("Microsoft Word")[0].activate()
        break
    except Exception as e:
        print("not found ")
        pass

sleep(3)
pygui.hotkey("left", "enter", interval=.5)
# accept mala direta
print(num_pages)

for c in range(1, num_pages+1):
    sleep(5)
    # gerou
    pygui.getWindowsWithTitle("MODELO HISTÓRICO ESCOLAR")[0].activate()
    pygui.hotkey("alt")
    sleep(1)
    pygui.write("ofe")
    sleep(1)
    pygui.hotkey('tab')
    pygui.write(str(c))

    pygui.hotkey('tab')
    pygui.write(str(c))
    pygui.hotkey("enter")

    # salvou
    sleep(3.5)
    pygui.hotkey("alt")
    pygui.write("AM")
    sleep(2)
    pygui.write(list_of_students[c-1])
    pygui.hotkey('f4')
    sleep(.5)
    pygui.hotkey("right")
    sleep(.5)
    copy(PATH.replace("\\\\", '\\'))
    pygui.hotkey("ctrl", 'a')
    pygui.hotkey("del")
    sleep(.5)
    pygui.hotkey("ctrl", 'v')
    # pygui.write(PATH)  # write path in clipboard
    pygui.hotkey("enter", "enter", "enter", "enter", "enter", interval=.25)
    sleep(5)
