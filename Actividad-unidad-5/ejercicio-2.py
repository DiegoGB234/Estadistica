import matplotlib.pyplot as plt
import numpy as np
#“Una empresa de servicios está interesada en comparar la variabilidad de los tiempos de espera de sus clientes en tres sucursales diferentes: Sucursal 1, #Sucursal 2 y Sucursal 3. Para ello, se han recolectado datos de los tiempos de espera (en minutos) de 40 clientes en cada sucursal. Elabore un diagrama de caja #(boxplot) que permita comparar la dispersión, la mediana y la presencia de valores atípicos en los tiempos de espera de cada sucursal.”
 
np.random.seed(20)
tiempos_sucursal_1 = np.random.normal(15, 3, 40)
tiempos_sucursal_2 = np.random.normal(20, 5, 40)
tiempos_sucursal_3 = np.random.normal(10, 2, 40)
plt.boxplot([tiempos_sucursal_1, tiempos_sucursal_2,
tiempos_sucursal_3],
labels=['Sucursal 1', 'Sucursal 2', 'Sucursal 3'],
patch_artist=True)
plt.title('Comparación de tiempos de espera en tres sucursales')
plt.ylabel('Tiempo de espera (minutos)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()