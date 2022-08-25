from traceback import print_tb
import pandas as pd
import os


path = r"C:\Users\sbferreira\Downloads"
file = os.path.join(path, "Matrícula - Relação de Alunos por Classe.csv")
file = r"C:\Users\sbferreira\Desktop\pdj\desistoo.xlsx"
# df = pd.read_csv(file)
df = pd.read_excel(file)
def get_campos(campo): return df[campo].to_list()


p = get_campos("RA")
print(p)
