from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data={
     'Color de Ojos': ['Azul', 'Verde', 'Marrón', 'Azul', 'Marrón'],
     'Satisfacción':['Alta','Baja','Media','Alta','Baja'],
     'Edad':[25,34,42,28,37],
     'Numero de Hijos':[2,1,3,0,4],
     'Altura(cm)':[170,165,180,160,175]                
}
#Crear el objeto scaler
df = pd.DataFrame(data['Altura(cm)'])

 

#Normalizar los datos
scaler=MinMaxScaler()
df_normalized=scaler.fit_transform(df)
print(df_normalized)