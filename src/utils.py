import os
import pandas as pd

def save_to_csv(df, path="data/agregar_ventas.csv"):
    # Creamos la carpeta si no existe
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    # Guardamos el DataFrame como archivo CSV
    df.to_csv(path, index=False)
    print(f"Archivo guardado en '{path}'")

if __name__ == "__main__":
    from extract import extract_data
    from transform import clean_data, calculate_metricas, agregar_ventas
    
    df = extract_data()
    df = clean_data(df)
    df = calculate_metricas(df)
    agg = agregar_ventas(df)
    save_to_csv(agg)