import os
import pandas as pd
PATH = r"C:\Users\sbferreira\Desktop\H\data_files"

arqs_csv = []
for arq in os.listdir(PATH):
    arq_path = os.path.join(PATH, arq)
    print(arq_path)
    if arq_path.endswith("csv"):
        arqs_csv.append(arq_path)

appended_data = []
for arq in arqs_csv:
    df = pd.read_csv(arq)
    appended_data.append(df)

pd.concat(appended_data).to_csv(
    os.path.join(PATH, "SALAS_GERAL_1junho2022-v2.csv"),  
    header=False, encoding='utf-8-sig')
