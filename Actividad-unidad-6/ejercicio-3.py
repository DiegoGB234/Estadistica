import numpy as np

# Ingresos de 85 personas (85% del total) entre 10,000 y 25,000
ingresos_validos = np.random.randint(10000, 25001, size=85)

# 15 valores faltantes representados como 0
ingresos_faltantes = np.zeros(15)

# Unir todos los ingresos
ingresos = np.concatenate((ingresos_validos, ingresos_faltantes))

# Media considerando los ceros
media_con_ceros = np.mean(ingresos)

# Media solo con valores válidos (sin ceros)
media_sin_ceros = np.mean(ingresos[ingresos != 0])

print(f"Media con ceros: ${media_con_ceros:,.2f}")
print(f"Media sin ceros: ${media_sin_ceros:,.2f}")