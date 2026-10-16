# Dicionário de Dados do Sistema

**Projeto Aplicado I — Grupo 25 — Empresa parceira: Schulz S.A.**

Os campos foram mapeados a partir do levantamento da AV1 (Dispositivo de controle,
Registro MMC e Planilha MMC). Tipos usados: **Texto**, **Real** e **Inteiro**.

Conforme a AV1, identificadores (matrícula, códigos de equipamento, número de série)
são tratados como **Texto**, para preservar a representação original (zeros à esquerda, letras).

## Tabela `tecnico`

| Campo | Tipo | Chave | Obrigatório | Descrição |
|---|---|---|---|---|
| matricula | Texto | PK | Sim | Matrícula do técnico/solicitante |
| nome | Texto | | Sim | Nome completo |
| setor | Texto | | Não | Setor do técnico ou solicitante |

## Tabela `equipamento`

| Campo | Tipo | Chave | Obrigatório | Descrição |
|---|---|---|---|---|
| codigo | Texto | PK | Sim | Código/TAG do instrumento |
| fabricante | Texto | | Não | Fabricante do instrumento |
| modelo | Texto | | Não | Modelo do instrumento |
| numero_serie | Texto | | Não | Número de série |
| unidade | Texto | | Não | Unidade de medida (ex.: mm) |
| data_calibracao | Texto | | Não | Data da calibração (AAAA-MM-DD) |
| proxima_calibracao | Texto | | Não | Data da próxima calibração (AAAA-MM-DD) |

## Tabela `medicao`

| Campo | Tipo | Chave | Obrigatório | Descrição |
|---|---|---|---|---|
| id | Inteiro | PK | Sim | Identificador da medição (automático) |
| codigo_equipamento | Texto | FK → equipamento.codigo | Sim | Equipamento medido |
| matricula_tecnico | Texto | FK → tecnico.matricula | Sim | Técnico que executou |
| parametro | Texto | | Sim | Característica medida |
| valor_nominal | Real | | Sim | Valor de referência |
| tolerancia_sup | Real | | Sim | Limite superior de tolerância |
| tolerancia_inf | Real | | Sim | Limite inferior de tolerância |
| medida_1 | Real | | Não | Primeira medição |
| medida_2 | Real | | Não | Segunda medição |
| valor_obtido | Real | | Não | Valor obtido (média das medições) |
| status | Texto | | Não | APROVADO ou REPROVADO |

## Resumo

- **Total de campos mapeados:** 21 (mínimo exigido: 12).
- **Tabelas:** 3.
- **Datas:** o SQLite não possui tipo de data próprio, então são guardadas como texto
  no formato AAAA-MM-DD.
- **Valores ausentes:** conforme o plano ETL da AV1, células vazias ou marcadores
  (`---`, `?`) são convertidos para `NULL`, nunca para zero.
