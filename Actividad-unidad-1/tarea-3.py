import pandas as pd
from sklearn.datasets import load_iris

# Cargar datos
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['species'] = pd.Categorical.from_codes(data.target, data.target_names)

# exportar DataFrame completo
df.to_csv("iris_completo.csv", index=False)

# guardar estadísticas en txt
with open("estadisticas_iris.txt", "w") as f:
    f.write("=== Estadísticas Generales ===\n\n")
    f.write(str(df.describe()))
    
    f.write("\n\n=== Estadísticas por Especie ===\n\n")
    f.write(str(df.groupby('species').describe()))

# crear reporte automático
with open("reporte_iris.txt", "w") as f:
    f.write("REPORTE AUTOMÁTICO DATASET IRIS\n")
    f.write("="*40 + "\n\n")
    
    conteo = df['species'].value_counts()
    f.write("Número de muestras por especie:\n")
    f.write(str(conteo))
    
    f.write("\n\nPromedios por especie:\n")
    f.write(str(df.groupby('species').mean()))
    
    f.write("\n\nConclusiones:\n")
    f.write("- El dataset contiene 3 especies diferentes.\n")
    f.write("- Cada especie tiene 50 muestras.\n")
    f.write("- Las especies presentan diferencias notables en el tamaño de los pétalos.\n")

print("Archivos exportados correctamente ")