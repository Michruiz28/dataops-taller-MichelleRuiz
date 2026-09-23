import pandas as pd

def clean_data(df):
    # Eliminamos filas completamente duplicadas
    antes = len(df)
    df = df.drop_duplicates()
    print(f"Duplicados eliminados: {antes - len(df)}")

    # Rellenamos nulos: cantidad con 0, precio con el promedio
    df["cantidad"] = df["cantidad"].fillna(0).astype(int)
    df["precio_unitario"] = df["precio_unitario"].fillna(df["precio_unitario"].mean())

    # Convertimos la columna fecha a tipo datetime
    df["fecha"] = pd.to_datetime(df["fecha"])

    return df


def calculate_metricas(df):
    # Calculamos la venta total y extraemos el mes de la fecha
    df["venta_total"] = df["cantidad"] * df["precio_unitario"]
    df["mes"] = df["fecha"].dt.month
    return df


def agregar_ventas(df):
    # Agrupamos por categoria y mes sumando las ventas totales
    return (
        df.groupby(["categoria", "mes"])["venta_total"]
        .sum()
        .reset_index()
        .rename(columns={"venta_total": "venta_total_sum"})
    )

if __name__ == "__main__":
    from extract import extract_data
    df = extract_data()
    df = clean_data(df)
    df = calculate_metricas(df)
    print(agregar_ventas(df))