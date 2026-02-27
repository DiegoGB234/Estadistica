import numpy as np
import math
# Datos de ejemplo

data = [15, 17, 19, 13, 20]

 

# Calcular la desviación estándar
# sacando la media
media = sum(data) / len(data)

#sacando la varianza muestral de poblacional
varianza= sum(((x - media) ** 2 for x in data)) / (len(data))
print(varianza)

#sacando la desviacion estandar
desviacion_estandar= math.sqrt(varianza)
print(f"\n la  desviacion estandar es : {desviacion_estandar}")

#usando la libreria nupy
desviacion_estandar= np.std(data)
print(f"\n la  desviacion estandar es : {desviacion_estandar}")