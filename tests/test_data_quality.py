import pandas as pd
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from extract import extract_data
from transform import clean_data

DB_PATH = "data/ventas.db"

@pytest.fixture(scope="module")
def df_limpio():
    df = extract_data(DB_PATH)
    return clean_data(df)

def test_columnas_esperadas(df_limpio):
    columnas = {"id","fecha","producto","categoria","cantidad","precio_unitario","cliente_id"}
    assert columnas.issubset(set(df_limpio.columns))

def test_cantidad_no_negativa(df_limpio):
    assert (df_limpio["cantidad"] >= 0).all()

def test_precio_positivo(df_limpio):
    assert (df_limpio["precio_unitario"] > 0).all()

def test_sin_fechas_futuras(df_limpio):
    hoy = pd.Timestamp.today()
    assert (df_limpio["fecha"] <= hoy).all()

def test_sin_nulos_despues_limpieza(df_limpio):
    assert df_limpio["cantidad"].isnull().sum() == 0
    assert df_limpio["precio_unitario"].isnull().sum() == 0

def test_categorias_validas(df_limpio):
    validas = {"Electronica","Ropa","Alimentos","Hogar","Deportes"}
    invalidas = set(df_limpio["categoria"].unique()) - validas
    assert len(invalidas) == 0