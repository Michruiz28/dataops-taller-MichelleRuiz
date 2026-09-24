-- V003: Nueva columna para descuentos (valor entre 0 y 1)
ALTER TABLE ventas ADD COLUMN descuento REAL DEFAULT 0.0;