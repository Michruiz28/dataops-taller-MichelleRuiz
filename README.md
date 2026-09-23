# Dataops-taller-MichelleRuiz
## Descripción
Pipeline de datos completo que implementa principios de DataOps para una 
tienda en línea simulada. El sistema extrae datos de ventas desde una base 
de datos SQLite, los limpia y transforma y entrena un modelo simple de 
machine learning.

## Instrucciones de instalación desde mi maquina

### 1. Clonar el repositorio
git clone https://github.com/Michruiz28/dataops-taller-MichelleRuiz.git
cd dataops-taller-MichelleRuiz

### 2. Crear y activar entorno virtual
python -m venv venv

# Windows
venv\Scripts\activate

### 3. Instalar dependencias
pip install -r requirements.txt

### 4. Crear la base de datos
python scripts/create_db.py

### 5. Ejecutar las pruebas
pytest -v
