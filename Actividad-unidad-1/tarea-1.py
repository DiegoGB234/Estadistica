import pandas as pd
from sklearn.datasets import load_iris

# Cargando datos iris
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['species'] = pd.Categorical.from_codes(data.target, data.target_names)

# primeras 10 filas la funicoon funciona para obtener los primeras filas del datasets 
print("Las primeras 10 filas:")
print(df.head(10))

# ultimas 8 filas usando tail
print("\nLas últimas 8 filas:")
print(df.tail(8))

# información general del dataset
print("\nInformación general del dataset:")
df.info()

# estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())