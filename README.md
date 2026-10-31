# MVP de Calibração (Parte 1): Projeto Aplicado I, Schulz S.A.

Sistema em Python, com banco de dados SQLite, que substitui o controle manual de calibrações em planilhas do setor de Metrologia.

**Grupo 25:** Cristiane Nicolei | Matheus Martins | Priscilla Roncatto

## Arquivos

| Arquivo | Função |
|---|---|
| `01_estrutura.md` | Organização dos dados em três entidades (Técnico, Equipamento e Medição) |
| `02_dicionario.md` | Dicionário de dados, gerado por `gerar_dicionario_md.py` |
| `03_banco.sql` | Script DDL: cria as tabelas `tecnico`, `equipamento` e `medicao` |
| `04_classes.py` | Classes `Banco`, `Tecnico`, `Equipamento` e `Medicao`, com validação de tolerância e acesso ao banco |
| `05_main.py` | Demonstração: INSERT, SELECT, UPDATE, JOIN e tratamento de erro |
| `06_mvp_parte1.md` | Documentação técnica do MVP (Parte 1) |
| `executar_banco.py` | Cria o banco `schulz_calibracao.db` a partir do `03_banco.sql` |
| `gerar_dicionario_md.py` | Gera o `02_dicionario.md` |

## Requisitos

- Python 3 (testado com a versão 3.15).
- Nenhuma biblioteca externa: o módulo `sqlite3` já vem com o Python.

## Como executar

A demonstração completa roda com um único comando, de qualquer pasta:

```bash
python 05_main.py
```

Cada execução recria o banco `demo_calibracao.db` do zero, então o resultado é sempre o mesmo. O terminal mostra o cadastro de técnicos, equipamento e medições, a leitura e a atualização dos registros, o relatório de calibração (JOIN entre as três tabelas) e um teste de erro SQL com matrícula repetida.

Para criar apenas o banco vazio, com as três tabelas:

```bash
python executar_banco.py
```

## Regra de calibração

Uma medição é **APROVADO** quando `tolerancia_min <= valor_obtido <= tolerancia_max`, e **REPROVADO** caso contrário. O cálculo está no método `validar_calibracao()` da classe `Medicao`.

## Observações

- O arquivo se chama `04_classes.py` e, por começar com número, o `05_main.py` o importa com `importlib`.
- Os arquivos `.db` gerados nas execuções não são enviados ao repositório (estão no `.gitignore`).
- O DELETE não foi implementado de forma intencional: o banco usa `ON DELETE RESTRICT` para preservar o histórico das calibrações.
