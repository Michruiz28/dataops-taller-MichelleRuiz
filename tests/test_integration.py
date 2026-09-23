import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from extract import extract_data
from transform import clean_data, calculate_metricas, agregar_ventas

DB_PATH = "data/ventas.db"

def test_pipeline_completo():
    # Extraer
    df = extract_data(DB_PATH)
    assert not df.empty, "El DataFrame extraido no debe estar vacio"

    # Transformar
    df = clean_data(df)
    df = calculate_metricas(df)

    # Agregar
    agg = agregar_ventas(df)

    # Validaciones finales
    assert not agg.empty, "El resultado agregado no debe estar vacio"
    assert "categoria" in agg.columns
    assert "mes" in agg.columns
    assert "venta_total_sum" in agg.columns
    assert (agg["venta_total_sum"] >= 0).all()