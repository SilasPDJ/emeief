from openpyxl import Workbook
import openpyxl
import os


PATH = r"C:\Users\sbferreira\OneDrive\BKP SECRETARIA\MATRICULA LISTA DE ALUNOS\2022"
morning, afternoon = "PERÍODO DA MANHÃ", "PERÍODO DA TARDE"
MORNING, AFTERNOON = os.path.join(PATH, morning), os.path.join(PATH, afternoon)

wb = Workbook()
wb.remove(wb.active)
[wb.create_sheet(sheet)
 for sheet in os.listdir(AFTERNOON) + os.listdir(MORNING) if not sheet.startswith("~")]


wb.save(f"{PATH}/nova_forma.xlsx")
wb.close()
