import numpy as np
# Datos de ejemplo

data = [5, 7, 9, 6, 10]

 

# Calcular la varianza
#sacando la media
media= sum(data) / len(data)
print(media)
#restamos la media con todlos loes elementos y aplicamos ² 
resul=[]
for res in data:
    resul.append({
      "valor":res,
      "resultado": (res - media)**2 
    })

# ahora  sumamos todos los valores y lo dividimos por la cantidad de elementos usando la varianza poblacional
total=0
for var in resul:
    total += float(var['resultado'])
    
varianza= total / len(data)

#mostrando resultado
print(f"La varianza es de :{varianza}")

