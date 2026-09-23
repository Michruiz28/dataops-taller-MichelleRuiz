import os
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def train_model(df, model_path="models/model.pkl"):
    # Definimos la variable independiente (mes) y dependiente (venta_total)
    X = df[["mes"]].values
    y = df["venta_total"].values

    # Dividimos los datos en entrenamiento y prueba para reproducibilidad
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Usamos una regresion lineal y la entrenamos
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    # Calculamos el r cuadrado para medir que tan bien predice el modelo
    y_pred = modelo.predict(X_test)
    r2 = r2_score(y_test, y_pred)

    # Guardamos el modelo entrenado en un archivo
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(modelo, model_path)
    print(f"Modelo guardado en '{model_path}' | R²: {r2:.4f}")

    return modelo, r2

if __name__ == "__main__":
    from extract import extract_data
    from transform import clean_data, calculate_metricas
    df = extract_data()
    df = clean_data(df)
    df = calculate_metricas(df)
    train_model(df)