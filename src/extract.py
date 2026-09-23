import os
import sqlite3
import pandas as pd

def extract_data(db_path="data/ventas.db"):
    # Verificamos que la base de datos exista antes de conectarnos para leerla
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"No se encontro la base de datos en: {db_path}")

    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM ventas", conn)
    conn.close()

    print(f"Extraccion exitosa: {len(df)} registros cargados desde '{db_path}'")
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())