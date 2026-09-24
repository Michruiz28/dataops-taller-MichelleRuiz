-- V001: Creacion de la tabla ventas
CREATE TABLE IF NOT EXISTS ventas (
    id              INTEGER PRIMARY KEY,
    fecha           TEXT    NOT NULL,
    producto        TEXT    NOT NULL,
    categoria       TEXT    NOT NULL,
    cantidad        INTEGER DEFAULT 0,
    precio_unitario REAL,
    cliente_id      INTEGER
);

