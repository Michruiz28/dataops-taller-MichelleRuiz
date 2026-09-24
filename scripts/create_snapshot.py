import shutil
import os
from datetime import date

def create_snapshot(src="data/ventas.db", dest_dir="data/snapshots/"):
    # Creamos la carpeta de snapshots si no existe
    os.makedirs(dest_dir, exist_ok=True)

    # Generamos el nombre con la fecha de hoy
    fecha = date.today().strftime("%Y%m%d")
    dest = os.path.join(dest_dir, f"ventas_{fecha}.db")

    # Copiamos la BD con el nombre de fecha
    shutil.copy2(src, dest)
    print(f"Snapshot creado: {dest}")

if __name__ == "__main__":
    create_snapshot()