-- Projeto Aplicado I - Grupo 25 - Schulz S.A.
-- Entrega 02: Script DDL (SQLite)

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS tecnico (
    matricula TEXT PRIMARY KEY,
    nome      TEXT NOT NULL,
    setor     TEXT
);

CREATE TABLE IF NOT EXISTS equipamento (
    codigo             TEXT PRIMARY KEY,
    fabricante         TEXT,
    modelo             TEXT,
    numero_serie       TEXT,
    unidade            TEXT,
    data_calibracao    TEXT,
    proxima_calibracao TEXT
);

CREATE TABLE IF NOT EXISTS medicao (
    id                 INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_equipamento TEXT NOT NULL,
    matricula_tecnico  TEXT NOT NULL,
    parametro          TEXT NOT NULL,
    valor_nominal      REAL NOT NULL,
    tolerancia_sup     REAL NOT NULL,
    tolerancia_inf     REAL NOT NULL,
    medida_1           REAL,
    medida_2           REAL,
    valor_obtido       REAL,
    status             TEXT CHECK (status IN ('APROVADO', 'REPROVADO')),
    FOREIGN KEY (codigo_equipamento) REFERENCES equipamento (codigo),
    FOREIGN KEY (matricula_tecnico)  REFERENCES tecnico (matricula)
);
