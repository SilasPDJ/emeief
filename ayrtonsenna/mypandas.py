import pandas as pd
df = pd.read_excel("data_files/ramais.xlsm", "EMEIEF'S")
headers = df.iloc[3]
df.drop(df.index[3], inplace=True)
df.drop(df.index[0], inplace=True)
df.drop(df.index[1], inplace=True)
df = pd.DataFrame(df.values[:], columns=headers)

a = df.iloc[:12]
print(a)
