import sqlite3
import random
from datetime import date, timedelta

# Categorias y productos de una tienda simulada
CATEGORIAS = ["Electronica", "Ropa", "Alimentos", "Hogar", "Deportes"]
PRODUCTOS = {
    "Electronica": ["Laptop", "Celular", "Tablet"],
    "Ropa":        ["Camiseta", "Pantalon", "Falda"],
    "Alimentos":   ["Cafe", "Chocolate", "Arroz"],
    "Hogar":       ["Ollas", "Vasos", "Utensilios"],
    "Deportes":    ["Casco", "Guantes", "Rodilleras"],
}

def generar_fecha():
    # Genera una fecha aleatoria dentro del año 2025
    inicio = date(2025, 1, 1)
    return str(inicio + timedelta(days=random.randint(0, 364)))

def crear_base_datos(db_path="data/ventas.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Si la tabla ya existe la eliminamos para empezar limpio
    cursor.execute("DROP TABLE IF EXISTS ventas")
    cursor.execute("""
        CREATE TABLE ventas (
            id              INTEGER PRIMARY KEY,
            fecha           TEXT,
            producto        TEXT,
            categoria       TEXT,
            cantidad        INTEGER,
            precio_unitario REAL,
            cliente_id      INTEGER
        )
    """)

    # Generamos 100 registros con algunos nulos para simular datos reales
    registros = []
    for i in range(1, 101):
        cat = random.choice(CATEGORIAS)
        prod = random.choice(PRODUCTOS[cat])
        cantidad = random.randint(1, 20) if random.random() > 0.03 else None
        precio = round(random.uniform(20000.0, 100000.0), 1) if random.random() > 0.03 else None
        registros.append((
            i,
            generar_fecha(),
            prod, cat,
            cantidad, precio,
            random.randint(1, 50)
        ))

    # Agregamos 20 duplicados para que las pruebas de calidad tengan sentido
    duplicados = random.sample(registros, 20)
    for d in duplicados:
        registros.append((None, d[1], d[2], d[3], d[4], d[5], d[6]))
    # Linea de codigo solicitada a claude para insertar los registros a la base
    cursor.executemany(
        "INSERT OR IGNORE INTO ventas VALUES (?,?,?,?,?,?,?)",
        [(r[0], r[1], r[2], r[3], r[4], r[5], r[6]) for r in registros]
    )
    conn.commit()
    conn.close()
    print(f"Base de datos creada en '{db_path}' con {len(registros)} registros en total.")

if __name__ == "__main__":
    crear_base_datos()