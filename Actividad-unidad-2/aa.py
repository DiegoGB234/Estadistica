import pandas as pd

 

#Crear un dataframe con una columna categórica

df = pd.DataFrame({'Color': ['Rojo', 'Azul', 'Verde', 'Rojo']})

 

#Codificar la variable categórica usando One-Hot Encoding

df_encoded = pd.get_dummies(df, columns=['Color'])

print(df_encoded)