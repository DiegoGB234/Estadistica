import matplotlib.pyplot as plt
import numpy as np
np.random.seed(200)
calificaciones = np.concatenate([
np.random.normal(75, 8, 110), # mayoría de los estudiantes
np.random.uniform(30, 59, 5), # calificaciones bajas
np.random.uniform(91, 100, 5) # calificaciones altas
])
calificaciones = np.clip(calificaciones, 0, 100)
plt.figure(figsize=(8, 5))
plt.hist(calificaciones, bins=10, color='orange', edgecolor='black')
plt.title('Distribución de calificaciones en el examen final')
plt.xlabel('Calificación')
plt.ylabel('Número de estudiantes')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()