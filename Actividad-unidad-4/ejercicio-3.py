# Datos de ejemplo

data = [5, 7, 5, 10, 5]

 

#Calcular la moda
frecuencias = {}

for num in data:
    if num in frecuencias:
        frecuencias[num] += 1
    else:
        frecuencias[num] = 1

moda = max(frecuencias, key=frecuencias.get)
print(moda)