import matplotlib.pyplot as plt
import numpy as np

np.random.seed(100)
tiempos_entrega = np.concatenate([
np.random.normal(4, 1, 180), # mayoría de los pedidos
np.random.uniform(8, 15, 20) # algunos retrasados
])
tiempos_entrega = np.clip(tiempos_entrega, 1, 15) # limitar entre 1 y 15 días
plt.figure(figsize=(8, 5))
plt.hist(tiempos_entrega, bins=14, color='skyblue', edgecolor='black')
plt.title('Distribución de tiempos de entrega de pedidos')
plt.xlabel('Tiempo de entrega (días)')
plt.ylabel('Número de pedidos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()