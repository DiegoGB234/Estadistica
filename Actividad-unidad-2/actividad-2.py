import pandas as pd

# Dataset completo con las 14 combinaciones del Weather Dataset
weather_data = {
    'outlook':     ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast', 
                    'sunny', 'sunny', 'rainy', 'sunny', 'overcast', 'overcast', 'rainy'],
    'temperature': ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 
                    'mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild'],
    'humidity':    ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal', 
                    'high', 'normal', 'normal', 'normal', 'high', 'normal', 'high'],
    'windy':       [False, True, False, False, False, True, True, 
                    False, False, False, True, True, False, True],
    'play':        ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 
                    'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
}

df_weather = pd.DataFrame(weather_data)


 
#funcion Contar combinaciones por condición climática
def contar_combinaciones_por_condicion_climatica(df):
    return df['outlook'].value_counts()

#funcion de calcular la probabilidad mediante la frecuencia
def probabilidad_de_juego_por_categoria(df):
   for category in df.columns:
       print(f"\n  probabilidad de '${category}' ")
       for play in ['yes', 'no']:
           #filtrar por play
           sub_set=df[df['play']== play]
           #total del grupo
           n = len(sub_set)
           frecuencias = sub_set[category].value_counts()
           print(f"\n play={play},{n} casos ")
           for valor, frecuencia in frecuencias.items():
                #frecuencia y total
                prob = frecuencia / n            
                print(f"    {valor}: {frecuencia}/{n} = {prob:.4f}")
                print("\n----------------------------------------")

#funcion para filtraods por condiciones espcidicas
def filtrado_por_condiciones_especificas(outlook,temperature,humidity,windy,play,df):
    sub_set = df[
        (df['outlook'] == outlook) &
        (df['temperature'] == temperature) &
        (df['humidity'] == humidity) &
        (df['windy'] == windy) &
        (df['play'] == play)
    ]
    return sub_set


# Mostrar el dataset completo
print("\nWeather Dataset Completo:")
print(df_weather.to_string(index=True))
print(f"\nTotal de registros: {len(df_weather)}")
print("\n----------------------------------------")
#mostrando las combinaciones por condicion climatico
print(" \n combinaciones por condicion climatico")
print(contar_combinaciones_por_condicion_climatica(df_weather))
print("\n----------------------------------------")
#Calculando las  probabilidades de juego por categoría
print(probabilidad_de_juego_por_categoria(df_weather))
print("\n----------------------------------------")
# Filtrar datos por condiciones específicas
print(filtrado_por_condiciones_especificas('sunny', 'hot', 'high', False, 'no',df_weather))