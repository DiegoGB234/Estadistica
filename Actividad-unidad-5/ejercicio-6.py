import matplotlib.pyplot as plt
import numpy as np
np.random.seed(321)
edad_bajo = np.random.randint(30, 60, 20)
colesterol_bajo = np.random.normal(220, 20, 20)
edad_alto = np.random.randint(30, 60, 20)
colesterol_alto = np.random.normal(190, 15, 20)
plt.scatter(edad_bajo, colesterol_bajo, color='red', label='Actividadfísica baja', alpha=0.7)
plt.scatter(edad_alto, colesterol_alto, color='purple',
label='Actividad física alta', alpha=0.7)
plt.title('Edad vs. nivel de colesterol por grupo de actividad física')
plt.xlabel('Edad (años)')
plt.ylabel('Colesterol (mg/dL)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()