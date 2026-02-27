import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Cargar el dataset Titanic
df = sns.load_dataset("titanic")

# ===============================
# MEDIDAS DE TENDENCIA CENTRAL Y DISPERSIÓN
# ===============================

columnas = ['age', 'fare', 'sibsp']

for col in columnas:
    datos = df[col].dropna()
    
    print(f"\n----- Análisis de {col} -----")
    
    # Media
    media = np.mean(datos)
    print(f"Media: {media}")
    
    # Mediana
    mediana = np.median(datos)
    print(f"Mediana: {mediana}")
    
    # Moda
    moda = df[col].mode()[0]
    print(f"Moda: {moda}")
    
    # Varianza
    varianza = np.var(datos)
    print(f"Varianza: {varianza}")
    
    # Desviación estándar
    desviacion = np.std(datos)
    print(f"Desviación estándar: {desviacion}")

# ===============================
# HISTOGRAMA (Edad)
# ===============================

plt.hist(df['age'].dropna(), bins=10)
plt.title("Histograma de la Edad - Titanic")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()

# ===============================
# BOXPLOT (Edad por supervivencia)
# ===============================

sns.boxplot(x='survived', y='age', data=df)
plt.title("Edad por Supervivencia")
plt.show()

# ===============================
# DIAGRAMA DE DISPERSIÓN (Edad vs Tarifa)
# ===============================

sns.scatterplot(x='age', y='fare', data=df)
plt.title("Edad vs Tarifa")
plt.show()

# ===============================
# MATRIZ DE CORRELACIÓN
# ===============================

correlacion = df[['age','fare','sibsp','parch']].corr()

sns.heatmap(correlacion, annot=True)
plt.title("Matriz de Correlación")
plt.show()