import pandas as pd
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from transform import clean_data, calculate_metricas, agregar_ventas

@pytest.fixture
def df_sucio():
    return pd.DataFrame({
        "id":              [1, 1, 2, 3],
        "fecha":           ["2025-01-10", "2025-01-10", "2025-02-15", "2025-03-20"],
        "producto":        ["Laptop", "Laptop", "Camiseta", "Casco"],
        "categoria":       ["Electronica", "Electronica", "Ropa", "Deportes"],
        "cantidad":        [2, 2, None, 5],
        "precio_unitario": [80000.0, 80000.0, 50000.0, None],
        "cliente_id":      [1, 1, 2, 3],
    })

def test_clean_elimina_duplicados(df_sucio):
    df = clean_data(df_sucio)
    assert len(df) == 3, "Debe eliminar 1 fila duplicada"

def test_clean_rellena_nulos_cantidad(df_sucio):
    df = clean_data(df_sucio)
    assert df["cantidad"].isnull().sum() == 0

def test_clean_rellena_nulos_precio(df_sucio):
    df = clean_data(df_sucio)
    assert df["precio_unitario"].isnull().sum() == 0

def test_clean_convierte_fecha(df_sucio):
    df = clean_data(df_sucio)
    assert pd.api.types.is_datetime64_any_dtype(df["fecha"])

def test_calculate_metrics_venta_total(df_sucio):
    df = clean_data(df_sucio)
    df = calculate_metricas(df)
    assert "venta_total" in df.columns

def test_calculate_metrics_mes(df_sucio):
    df = clean_data(df_sucio)
    df = calculate_metricas(df)
    assert "mes" in df.columns
    assert df["mes"].iloc[0] == 1

def test_aggregate_sales_columnas(df_sucio):
    df = clean_data(df_sucio)
    df = calculate_metricas(df)
    agg = agregar_ventas(df)
    assert "categoria" in agg.columns
    assert "mes" in agg.columns
    assert "venta_total_sum" in agg.columns

def test_aggregate_sales_agrupa_correctamente(df_sucio):
    df = clean_data(df_sucio)
    df = calculate_metricas(df)
    agg = agregar_ventas(df)
    assert len(agg) == 3