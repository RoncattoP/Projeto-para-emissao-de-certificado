# 02_dicionario.md — Dicionário de Dados do Sistema

**Unidade Curricular:** Projeto Aplicado I
**Empresa Parceira:** Schulz S.A.
**Tema 02:** Modelagem e Implementação de Banco de Dados (SQLite)
**Grupo 25:** Cristiane Nicolei | Matheus Martins | Priscilla Roncatto

---

## 1. Mapeamento das Tabelas e Campos

Tipos de dados: **Texto** (TEXT), **Real** (REAL), **Inteiro** (INTEGER) e **Data/Hora** (DATETIME).

### 1.1. Tabela: `tecnico` (Técnicos / Solicitantes)
| Nome do Campo | Tipo (SQLite) | Restrições / Chaves | Descrição / Regra de Negócio |
| :--- | :--- | :--- | :--- |
| `id_tecnico` | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador único do técnico. |
| `nome_tecnico` | TEXT | NOT NULL | Nome completo do profissional. |
| `matricula` | TEXT | NOT NULL, UNIQUE | Matrícula do colaborador. Texto, para preservar zeros à esquerda. |
| `email` | TEXT | NOT NULL | E-mail corporativo do colaborador. |
| `setor` | TEXT | NOT NULL | Departamento de atuação (Ex: Metrologia). |

### 1.2. Tabela: `equipamento` (Instrumentos e Máquinas)
| Nome do Campo | Tipo (SQLite) | Restrições / Chaves | Descrição / Regra de Negócio |
| :--- | :--- | :--- | :--- |
| `id_equipamento` | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador único do equipamento. |
| `codigo_tag` | TEXT | NOT NULL, UNIQUE | Código/TAG gravado no instrumento. Texto, para preservar o formato original. |
| `nome_equipamento` | TEXT | NOT NULL | Descrição do equipamento (Ex: Paquímetro). |
| `fabricante` | TEXT | NOT NULL | Fabricante do instrumento. |
| `modelo` | TEXT | NOT NULL | Modelo do instrumento. |

### 1.3. Tabela: `medicao` (Registro das Calibrações / Ensaios)
| Nome do Campo | Tipo (SQLite) | Restrições / Chaves | Descrição / Regra de Negócio |
| :--- | :--- | :--- | :--- |
| `id_medicao` | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador único do ensaio. |
| `id_equipamento` | INTEGER | NOT NULL, FOREIGN KEY (equipamento) | Vínculo com o equipamento avaliado. |
| `id_tecnico` | INTEGER | NOT NULL, FOREIGN KEY (tecnico) | Vínculo com o técnico responsável. |
| `parametro_medido` | TEXT | NOT NULL | Característica aferida (Ex: Comprimento, Pressão). |
| `valor_nominal` | REAL | NOT NULL | Valor de referência esperado. |
| `tolerancia_min` | REAL | NOT NULL | Limite inferior aceitável. |
| `tolerancia_max` | REAL | NOT NULL | Limite superior aceitável. |
| `valor_obtido` | REAL | NOT NULL | Leitura real coletada no ensaio. |
| `status_resultado` | TEXT | NOT NULL, CHECK ('APROVADO', 'REPROVADO') | Parecer: aprovado se o valor obtido estiver entre as tolerâncias. |
| `data_medicao` | DATETIME | DEFAULT CURRENT_TIMESTAMP | Data e hora automática do registro da medição. |

---

## 2. Relacionamentos

- `medicao.id_equipamento` referencia `equipamento.id_equipamento` (um equipamento tem várias medições).
- `medicao.id_tecnico` referencia `tecnico.id_tecnico` (um técnico realiza várias medições).
- `ON DELETE RESTRICT`: impede apagar um técnico ou equipamento que já tenha medições registradas, preservando o histórico dos certificados.

## 3. Observações

- O SQLite não possui tipo de data próprio. O campo `data_medicao` é guardado como texto no formato `AAAA-MM-DD HH:MM:SS`.
- Valores ausentes nas planilhas de origem (células vazias, `---`, `?`) são tratados como `NULL`
  na etapa de ETL descrita na AV1, e nunca convertidos para zero.
