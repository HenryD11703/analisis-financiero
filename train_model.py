import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib # Librería para guardar y cargar modelos

print("Iniciando el entrenamiento del modelo...")

# 1. Cargar y preparar los datos
df = pd.read_csv('data/AAPL_limpio.csv', index_col='Date', parse_dates=True)
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['SMA_200'] = df['Close'].rolling(window=200).mean()
df.dropna(inplace=True)

# 2. Definir características (X) y objetivo (y)
features = ['Open', 'High', 'Low', 'Volume', 'SMA_50', 'SMA_200']
X = df[features]
y = df['Close']

# 3. Crear y entrenar el modelo (usando TODOS los datos)
# Como este es nuestro modelo final para producción, lo entrenamos con todos los datos disponibles.
model = LinearRegression()
model.fit(X, y)

# 4. Guardar el modelo en un archivo
joblib.dump(model, 'modelo_regresion.joblib')

print("Modelo entrenado y guardado exitosamente como 'modelo_regresion.joblib'")