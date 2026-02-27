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

# Mostrar el dataset completo
print("\nWeather Dataset Completo:")
print(df_weather.to_string(index=True))
print(f"\nTotal de registros: {len(df_weather)}")

