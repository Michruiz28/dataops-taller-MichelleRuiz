import sqlite3
import os
import glob

def apply_migrations(db_path="data/ventas.db", migrations_dir="migrations/"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Obtenemos los scripts en orden alfabético (V001, V002, V003...)
    scripts = sorted(glob.glob(os.path.join(migrations_dir, "V*.sql")))

    for script in scripts:
        print(f"Aplicando: {script}")
        with open(script) as f:
            cursor.executescript(f.read())

    conn.commit()
    conn.close()
    print("migraciones aplicadas correctamente.")

if __name__ == "__main__":
    apply_migrations()