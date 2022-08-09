import pandas as pd
import os
PATH = r"C:\Users\sbferreira\Desktop\H\data_files"
arq = os.path.join(PATH, "SALAS_GERAL_1junho2022.xlsx")


def get_campos(campo): return df[campo].to_list()


df = pd.read_excel(arq)
# print(df)


newdf = pd.DataFrame({"nome": [], "ra": []})

nm = get_campos("nomes")

for v in nm:
    try:
        nome, ra = v.split("\t")
        print(ra)
    except:
        print(v[0])
