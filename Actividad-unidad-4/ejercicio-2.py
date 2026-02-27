# Datos de ejemplo

data = [7, 10, 8, 12, 15]

 
#Calcular mediana

#primero ordenar el conjunto de menos a mayor
data.sort()  
#7,8,10,12,15
n = len(data)

#para dectectar que si es impar o par
if n % 2 != 0:
    mediana = data[n//2]
else:
    mediana = (data[n//2 - 1] + data[n//2]) / 2

print(mediana)