-- V002: Indice en fecha para acelerar consultas por rango de tiempo
CREATE INDEX IF NOT EXISTS idx_ventas_fecha ON ventas(fecha);
