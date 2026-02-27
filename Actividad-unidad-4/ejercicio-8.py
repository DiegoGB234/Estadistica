import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.datasets import load_iris

import pandas as pd

 

# Cargar el conjunto de datos Iris

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

 

#Crear gráfico de cajas

sns.boxplot(x=iris.target_names[iris.target], y=df['sepal length (cm)'])

plt.title("Gráfico de Cajas - Longitud del Sépalo")

plt.show()