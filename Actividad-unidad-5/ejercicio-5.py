import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)

horas_matutino = np.random.normal(8, 2, 25)
calif_matutino = horas_matutino * 6 + np.random.normal(40, 5, 25)
horas_vespertino = np.random.normal(6, 2, 25)
calif_vespertino = horas_vespertino * 7 + np.random.normal(38, 7, 25)
plt.scatter(horas_matutino, calif_matutino, color='blue',
label='Matutino', alpha=0.7)
plt.scatter(horas_vespertino, calif_vespertino, color='green',
label='Vespertino', alpha=0.7)
plt.title('Horas de estudio vs. calificación por turno escolar')
plt.xlabel('Horas de estudio semanales')
plt.ylabel('Calificación final')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()