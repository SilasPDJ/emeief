import pandas as pd
df = pd.read_excel("C:\\Users\\icodansiguer\\Desktop\\Silas\\__TURMAS.xlsx")
# print(df[0])
print(df)
turmas = df["Turmas"].to_list()
codigos = df["Códigos"].to_list()
# campos = df[campo].to_list()
# pra virar metodo get_df(campo)
# return campos
for codigo in codigos:
    print(codigo)


