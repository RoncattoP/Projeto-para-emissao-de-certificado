-- ==============================================================================
-- UNIDADE CURRICULAR: PROJETO APLICADO I
-- EMPRESA PARCEIRA: SCHULZ S.A.
-- ITEM 03: SCRIPT DDL DE CRIAÇÃO DO BANCO DE DADOS RELACIONAL (SQLite)
-- GRUPO 25: Cristiane Nicolei | Matheus Martins | Priscilla Roncatto
-- ==============================================================================

-- 1. Ativar obrigatoriedade de Chaves Estrangeiras no SQLite
PRAGMA foreign_keys = ON;

-- 2. TABELA 1: TECNICO (ou Solicitante)
CREATE TABLE IF NOT EXISTS tecnico (
    id_tecnico   INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_tecnico TEXT NOT NULL,
    matricula    TEXT NOT NULL UNIQUE,
    email        TEXT NOT NULL,
    setor        TEXT NOT NULL
);

-- 3. TABELA 2: EQUIPAMENTO
CREATE TABLE IF NOT EXISTS equipamento (
    id_equipamento   INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_tag       TEXT NOT NULL UNIQUE,
    nome_equipamento TEXT NOT NULL,
    fabricante       TEXT NOT NULL,
    modelo           TEXT NOT NULL
);

-- 4. TABELA 3: MEDICAO (Tabela Transacional com FKs)
CREATE TABLE IF NOT EXISTS medicao (
    id_medicao       INTEGER PRIMARY KEY AUTOINCREMENT,
    id_equipamento   INTEGER NOT NULL,
    id_tecnico       INTEGER NOT NULL,
    parametro_medido TEXT NOT NULL,
    valor_nominal    REAL NOT NULL,
    tolerancia_min   REAL NOT NULL,
    tolerancia_max   REAL NOT NULL,
    valor_obtido     REAL NOT NULL,
    status_resultado TEXT NOT NULL CHECK (status_resultado IN ('APROVADO', 'REPROVADO')),
    data_medicao     DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_equipamento) REFERENCES equipamento (id_equipamento)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (id_tecnico) REFERENCES tecnico (id_tecnico)
        ON DELETE RESTRICT ON UPDATE CASCADE
);
