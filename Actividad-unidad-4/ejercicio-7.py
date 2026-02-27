import matplotlib.pyplot as plt

import seaborn as sns

from sklearn. datasets import load_iris

import pandas as pd

 

# Cargar el conjunto de datos Iris

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

 

# Crear histograma para la longitud del sépalo

plt.hist(df['sepal length (cm)'], bins=10, alpha=0.5, color='blue')

plt.title("Histograma de Longitud de Sépalo")

plt.xlabel("Longitud de Sépalo (cm)")

plt.ylabel("Frecuencia")


plt.show()