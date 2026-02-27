import numpy as np
# Datos de ejemplo

data = [8, 14, 10, 12, 18]

 

# Calcular percentiles
percentiles = np.percentile(data, [25, 50, 75])
print("Percentiles 25, 50, 75:", percentiles)