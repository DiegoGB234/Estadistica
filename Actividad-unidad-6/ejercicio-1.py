import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


np.random.seed(10)


alturas = np.random.normal(loc=165, scale=10, size=200)


media = np.mean(alturas)
desv = np.std(alturas)
print(f"Media: {media:.2f} cm")
print(f"Desviación estándar: {desv:.2f} cm")


plt.hist(alturas, bins=15, density=True, alpha=0.6, color='skyblue', edgecolor='black')


x = np.linspace(min(alturas), max(alturas), 100)
plt.plot(x, norm.pdf(x, media, desv), 'r--', linewidth=2, label='Distribución normal teórica')

plt.title('Histograma de alturas de 200 estudiantes')
plt.xlabel('Altura (cm)')
plt.ylabel('Densidad')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.show()