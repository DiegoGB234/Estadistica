import pandas as pd
from sklearn.datasets import load_iris


# Cargando datos iris
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['species'] = pd.Categorical.from_codes(data.target, data.target_names)

#mostrando la cantidad de muestras que se encuentro  en la columna species
# usando value_counts() por que  cuenta cuántas veces se repite cada valor único
print("\n mostrando la  cantidan de muestas que se encientran  en la columna species:")
print(df['species'].value_counts())
print("\n------------------------------")
#calculando el promedio, para calcular el promedio usamos groupby para agrupar las filas  comparten el mismo valor en este caso species
#la funcion mean es una forma de sacar el promedio o media usando grouby para agrupar y luego aplicamos y nos da el resultado
print("\nPromedio de cada característica por especie:")
print(df.groupby('species').mean())
print("\n------------------------------")
#resument estadistico 
#describe da un resumen estadistico que retorna  media desviacion estandar entre otros 
print("\nResumen estadístico agrupado por especie:")
print(df.groupby('species').describe())
print("\n------------------------------")