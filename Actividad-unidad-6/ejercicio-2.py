import numpy as np

# Sueldos de 98 empleados normales entre 15,000 y 30,000
sueldos_normales = np.random.randint(15000, 30001, size=98)

# Sueldos de 2 directivos (outliers)
sueldos_directivos = np.array([160000, 180000])

# Unir los sueldos en un solo array
sueldos = np.concatenate((sueldos_normales, sueldos_directivos))

# Calcular media y mediana
media = np.mean(sueldos)
mediana = np.median(sueldos)

print(f"Media: ${media:,.2f}")
print(f"Mediana: ${mediana:,.2f}")