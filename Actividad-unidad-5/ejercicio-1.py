import matplotlib.pyplot as plt
import numpy as np
#definienddo la combinacion
np.random.seed(10)
calificaciones_grupo_A = np.random.randint(1, 100, 30)
calificaciones_grupo_B = np.random.randint(50, 95, 30)
print("A",calificaciones_grupo_A)
print("-------------------------")
print("B",calificaciones_grupo_B)
plt.boxplot([calificaciones_grupo_A, calificaciones_grupo_B],
labels=['Grupo A', 'Grupo B'],
patch_artist=True)
plt.title('Comparación de calificaciones finales entre dos grupos')
plt.ylabel('Calificación')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()