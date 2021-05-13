import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%matplotlib inline

"""
notas =pd.Series([2, 7, 5, 10, 6])
notas

print(notas)


#===================================
#notas.values
#array([2, 7, 5, 10, 6])
#notas.index

#RangeIndex(start=0, step =1)

#===========================

notas = pd.Series([2, 7, 5, 10, 6], index=['Wilfred', 'Abbie', 'Harry', 'Julia', 'Carrie' ])
print(notas)
#================
#print( notas,'Julia')
#=================
print('Média:', notas.mean())
print('Desvio padrão:', notas.std())
#==============================
notas.describe()

#=================================
df = pd.DataFrame({'Aluno': ["Wilfred", "Abbie","harry", "Julia","Carrie"],
                   'Faltas': [3,4,2,1,4],
                   'Prova': [2,7,5,10,6],
                   'Seminário': [8.5,7.5,9.0,7.50,8.0]})
print(df)

print(df.dtypes)

df.columns
Index(['Aluno', 'Faltas', 'Prova', 'Seminario'], dtype='object')

df['Seminário']

df.describe()
#=========================
df.sort_values(by="Seminário")

print(df)

df.loc[3]
"""
df = pd.read_csv('dados.csv')
#print(df)

df.head()
print(df.head)
df.head(n=10)

