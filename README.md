\# DataOps Taller — Pipeline de Datos para Tienda en Línea

\*\*Autora:\*\* Michelle Dayana Ruiz Carranza  

\---



\## Descripción

Pipeline de datos completo que implementa principios de DataOps para una tienda 

en línea colombiana simulada (similar a tienda Éxito virtual). El sistema extrae datos de ventas desde una base de 

datos SQLite, los limpia y transforma, entrena un modelo simple de machine learning 

y automatiza todo el proceso con CI/CD mediante GitHub Actions.

\---



\## Diagrama de flujo del pipeline

\[Base de datos SQLite]

↓

extract.py ← Extrae los datos de ventas

↓

transform.py ← Limpia duplicados, nulos y calcula métricas

↓

train.py ← Entrena regresión lineal y guarda el modelo

↓

utils.py ← Exporta resultados a CSV

↓

\[aggregated\_sales.csv + modelo]



Automatizado con GitHub Actions en cada push 



\---



\## Estructura del repositorio

dataops-taller-MichelleRuiz/

├── .github/workflows/ci.yml # Pipeline CI/CD automatizado

├── data/

│ ├── ventas.db.dvc # Puntero DVC a la base de datos

│ └── snapshots/ # Copias semanales de la BD

├── migrations/

│ ├── V001\_create\_ventas\_table.sql

│ ├── V002\_add\_index\_on\_fecha.sql

│ └── V003\_add\_column\_descuento.sql

├── models/model.pkl # Modelo entrenado

├── notebooks/exploracion.ipynb # Analisis exploratorio

├── scripts/

│ ├── create\_db.py # Crea la base de datos simulada

│ ├── create\_snapshot.py # Genera snapshots semanales

│ └── apply\_migrations.py # Aplica migraciones SQL

├── src/

│ ├── extract.py # Extracción de datos

│ ├── transform.py # Limpieza y transformación

│ ├── train.py # Entrenamiento del modelo

│ └── utils.py # Exportar CSV

├── tests/

│ ├── test\_transform.py # Pruebas unitarias

│ ├── test\_data\_quality.py # Pruebas de calidad de datos

│ └── test\_integration.py # Prueba de integración completa

├── .gitignore

├── pytest.ini

├── requirements.txt

└── README.md





\---



\## Instrucciones para ejecutar localmente



\### 1. Clonar el repositorio desde la terminal de la maquina o desde bash

git clone https://github.com/Michruiz28/dataops-taller-MichelleRuiz.git

cd dataops-taller-MichelleRuiz



\### 2. Crear y activar entorno virtual

python -m venv venv

venv\\Scripts\\activate





\### 3. Instalar dependencias

pip install -r requirements.txt



\### 4. Crear la base de datos

python scripts/create\_db.py



\### 5. Ejecutar el pipeline completo

python src/extract.py

python src/transform.py

python src/train.py

python src/utils.py



\### 6. Ejecutar las pruebas

pytest -v



\### 7. Aplicar migraciones

python scripts/apply\_migrations.py



\### 8. Crear snapshot de datos

python scripts/create\_snapshot.py

\---



\## Decisiones de diseño



\- \*\*SQLite\*\* sobre PostgreSQL: ya que no requiere instalar un servidor externo y es cómodo para un entorno simulado y de desarrollo local como nuestro primer acercamiento.

\- \*\*Regresión lineal simple\*\*: el objetivo del taller es demostrar el flujo 

&#x20; DataOps completo, no la complejidad del modelo o la calidad de los resultados.

\- \*\*DVC\*\* para versionar datos: Git no fue diseñado para archivos binarios grandes por lo que DVC guarda solo un puntero en Git y el archivo real en un remoto separado.

\- \*\*GitHub Actions\*\* para CI/CD: herramienta gratuita integrada con GitHub que 

&#x20; no requiere infraestructura adicional.

\- \*\*Migraciones SQL numeradas\*\*: garantizan que cualquier entorno pueda reproducir la misma estructura de BD en el mismo orden.

\---



\## Resultados de las pruebas



Se ejecutaron 15 pruebas en total:

Donde hubo: 8 Unitarias

&#x09;    6 de calidad de datos

&#x09;    1 de integración

Y todas pasaron

\---



\## Informe



\### Introducción — Objetivos del taller



El objetivo principal de este taller es aplicar los principios de DataOps en un proyecto de datos real, implementando las prácticas vistas en clase como control de versiones, pruebas automatizadas, CI/CD y versionamiento holístico. Esto con el objetivo de comprender que DataOps no es solo teoría sino un conjunto de prácticas concretas que mejoran la calidad, reproducibilidad y velocidad de entrega en proyectos de datos.

\---



\### Desarrollo — Paso a paso



Tarea 1 — Configuración del repositorio: 

Se creó el repositorio en GitHub con la estructura de carpetas recomendada, 

se configuró el `.gitignore` para excluir entornos virtuales, datos y archivos 

sensibles, y se estableció la rama `feature/pipeline-inicial` para trabajar 

siguiendo buenas prácticas de Git.



Tarea 2 — Pipeline de datos: 

Se implementaron los 5 módulos del pipeline en Python: `create\_db.py` que genera 120 registros simulados con nulos y duplicados, `extract.py` los lee desde SQLite, `transform.py` los limpia y calcula métricas, `train.py` entrena una regresión lineal y `utils.py` exporta los resultados a CSV.



Tarea 3 — Pruebas automatizadas: 

Se implementaron 15 pruebas con pytest distribuidas en pruebas unitarias, 

de calidad de datos y de integración. Todas pasaron correctamente.



Tarea 4 — CI/CD:

Se configuró GitHub Actions para ejecutar automáticamente las pruebas, 

el análisis estático y el entrenamiento del modelo en cada push.



Tarea 5 — Versionamiento:

Se implementó DVC para versionar los datos, se crearon 3 migraciones SQL 

para versionar el esquema de la BD y se creó un script de snapshots semanales.



\---



\### Análisis



\*\*¿Qué diferencias encontré entre CI/CD tradicional y CI/CD para datos?\*\*  

En CI/CD tradicional el pipeline solo compila y prueba código. En datos, el 

pipeline también debe crear la base de datos, verificar la calidad de los datos de entrada y validar que el modelo entrenado supere métricas mínimas. Ademas, los datos son una dependencia externa que puede cambiar sin aviso, lo que hace que el pipeline sea mas complejo y menos predecible que uno de software convencional.



\*\*¿Qué desafíos específicos enfrenté al versionar datos?\*\*  

El principal desafío fue la incompatibilidad entre DVC y la configuración del 

`.gitignore`. Git ignoraba toda la carpeta `data/` como una unidad, lo que 

impedía que DVC guardara el archivo `.dvc` dentro de ella. La solución fue 

cambiar el `.gitignore` para ignorar solo los tipos de archivo específicos 

(`\*.db`, `\*.csv`) en lugar de ignorar la carpeta completa. Ademas 

la librería `pathspec 1.1.1` no era compatible con Python 3.13, lo que requirió instalar una versión específica (`0.12.1`).



\*\*¿Cómo aseguré la reproducibilidad del experimento?\*\*  

A través de cuatro mecanismos: `requirements.txt` con versiones fijas de todas 

las librerías, `random\_state=42` en el modelo para que la división de datos sea siempre igual, DVC para que los datos de entrenamiento sean siempre los mismos y migraciones SQL numeradas para reproducir la estructura de la BD en cualquier entorno.



\---



\### Conclusiones



\- DataOps no es solo teoría de buenas practicas, con este taller donde implementamos Git, pruebas automáticas y CI/CD  vimos que genera valor real desde el primer sprint al detectar errores antes de que lleguen a producción.

\- El mayor desafío no fue técnico sino de configuración: compatibilidades entre versiones de librerías y reglas del `.gitignore` con DVC tomaron más tiempo ya que no sabia que hacer por falta de practica anteriormente.

\- Limitación del enfoque: SQLite y un remoto local de DVC son soluciones 

&#x20; válidas para desarrollo pero no escalan a producción con grandes volúmenes de datos.

\- Recomendación para un equipo real: implementar DataOps de forma gradual, 

&#x20; empezando por Git y pruebas básicas antes de introducir orquestación y 

&#x20; versionamiento de datos, además de investigación exhaustiva para verificar compatibilidad de versiones de librerías y herramientas con nuestra maquina.



\---



\### Reflexión final



\*\*¿Qué haría diferente con 10 TB de datos y 20 científicos de datos?\*\*  

Con ese volumen y equipo, los cambios principales serían:

\- Reemplazar SQLite por PostgreSQL o Snowflake para manejar el volumen.

\- Reemplazar DVC local por DVC con S3 o Google Cloud Storage para almacenamiento distribuido.

\- Implementar Apache Iceberg o Delta Lake para versionamiento de datos con soporte ACID.

\- Usar Apache Airflow para orquestar los pipelines en lugar de ejecutarlos manualmente.

\- Implementar un catálogo de datos para que los 20 científicos puedan descubrir y entender los datasets disponibles sin depender de documentación manual.

\- Separar los entornos de desarrollo, staging y producción con infraestructura  entendible



¿Qué herramientas comerciales facilitarían el proceso?

Databricks: Integra almacenamiento, transformación, entrenamiento de modelos y CI/CD en una sola plataforma con soporte nativo para Delta Lake.

AWS SageMaker: Ofrece pipelines de ML completamente gestionados con versionamiento de modelos, monitoreo y despliegue automatizado.

Dataiku: Plataforma visual que permite a perfiles no técnicos participar en el pipeline de datos sin escribir código, ideal para equipos mixtos.



\---



\## Comandos básicos de Git utilizados



`git clone url`- Clona el repositorio 

&#x20;`git checkout -b feature/nombre` - Crea y cambia a una rama nueva 

&#x20;`git add .`- Agrega cambios al staging area 

&#x20;`git commit -m "mensaje"`- Guarda los cambios con mensaje

&#x20;`git push origin rama` - Sube los cambios a GitHub

&#x20;`git fetch origin` - Descarga cambios remotos

&#x20;`git merge origin/main` - Fusiona main en la rama actual

&#x20;`git log --oneline`- Historial de commits resumido



\---



\## Referencias



DataKitchen. (2017). \*The DataOps Manifesto\*. https://dataopsmanifesto.org  

Apache Software Foundation. (2024). \*Apache Airflow documentation\*. https://airflow.apache.org/docs/  

Iterative AI. (2024). \*DVC documentation\*. https://dvc.org/doc  

GitHub. (2024). \*GitHub Actions documentation\*. https://docs.github.com/en/actions  

Fowler, M. (2006). \*Continuous integration\*. https://martinfowler.com/articles/continuousIntegration.html  

The Linux Foundation. (2024). \*Delta Lake documentation\*. https://delta.io/



\## Herramientas IA usadas

Claude para investigación de errores, comandos, código y corrección de sintaxis del mismo. 



