import pandas as pd

data={
     'Color de Ojos': ['Azul', 'Verde', 'Marrón', 'Azul', 'Marrón'],
     'Satisfacción':['Alta','Baja','Media','Alta','Baja'],
     'Edad':[25,34,42,28,37],
     'Numero de Hijos':[2,1,3,0,4],
     'Altura(cm)':[170,165,180,160,175]                
}
#Crear un dataframe
df = pd.DataFrame(data,columns=data)

#Realizar la codificación One-Hot
df_encoded= pd.get_dummies(df,columns=['Color de Ojos'])
print(df_encoded)