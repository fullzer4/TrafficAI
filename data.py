import pandas as pd

df = pd.read_csv("./CO2EmissionFiles/data.csv")

#df = df.sample(frac=0.30) #fracao dos dados
#df = df.drop(columns=[]) # remover colunas
#df = df.dropna() # limpa linhas vazias
print(df.keys()) 


# df.to_csv("data6.csv", index=False) # salvar