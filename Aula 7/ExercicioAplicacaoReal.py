import pandas as pd

igm_df = pd.read_csv("Aula 7/igm_modificado.csv")

# print(igm_df.info())

ind_des = igm_df['indice_governanca']
ind_des_notnull = ind_des.dropna(inplace=True)
print(ind_des_notnull.count())  