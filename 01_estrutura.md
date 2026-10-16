# Organização dos Dados (Modelo Conceitual Simplificado)

**Projeto Aplicado I — Grupo 25 — Empresa parceira: Schulz S.A.**
**Integrantes:** Cristiane Nicolei, Matheus Martins, Priscilla Roncatto

## 1. Visão geral

Na Entrega 1, o grupo mapeou o processo de calibração do setor de Metrologia da Schulz S.A.
Hoje ele depende de planilhas Excel preenchidas manualmente (Dispositivo de controle,
Registro MMC e Planilha MMC). Esse processo gera retrabalho, erros de digitação e dados
repetidos em várias abas.

Para substituir as planilhas, o banco de dados relacional (SQLite) foi dividido em
**3 entidades principais**: Técnico/Solicitante, Equipamento e Medição.

## 2. Entidade 1: Técnico/Solicitante (`tecnico`)

Armazena as pessoas envolvidas no processo: o metrologista que executa a calibração e o
solicitante do setor.

- Identificador interno (`id_tecnico`), nome, matrícula, e-mail e setor.
- A matrícula é única (`UNIQUE`), então não existem dois cadastros da mesma pessoa.
- Cada pessoa é cadastrada **uma única vez**.
- Um técnico pode realizar várias medições ao longo do tempo.

## 3. Entidade 2: Equipamento (`equipamento`)

Armazena o instrumento que é calibrado.

- Identificador interno (`id_equipamento`), código/TAG, nome, fabricante e modelo.
- O código/TAG é único (`UNIQUE`), pois identifica o instrumento fisicamente.
- Um equipamento pode ter várias medições, uma para cada parâmetro e cada calibração.

## 4. Entidade 3: Medição (`medicao`)

Armazena cada parâmetro medido durante a calibração de um equipamento.

- Parâmetro medido, valor nominal, tolerâncias mínima e máxima e valor obtido.
- Status do resultado (APROVADO ou REPROVADO) e data/hora do registro.
- Liga-se ao **equipamento** e ao **técnico** por chaves estrangeiras.

## 5. Relacionamentos

| Relação | Cardinalidade | Significado |
|---|---|---|
| Equipamento → Medição | 1 para N | Um equipamento possui várias medições |
| Técnico → Medição | 1 para N | Um técnico realiza várias medições |

Esquema simplificado:

```
TECNICO (1) ----< MEDICAO >---- (1) EQUIPAMENTO
```

## 6. Por que evitar dados duplicados?

Na AV1, o diagnóstico encontrou 50 anomalias nas planilhas. Várias delas vêm de informações
repetidas em mais de um lugar. Separar os dados em 3 entidades resolve isso por estes motivos:

1. **Consistência:** o dado do técnico ou do equipamento existe em um só lugar. Ao corrigi-lo,
   todas as medições passam a refletir a correção.
2. **Menos erros de digitação:** a medição guarda apenas a chave (`id_tecnico`, `id_equipamento`),
   e não o texto repetido. Isso evita nomes escritos de formas diferentes.
3. **Rastreabilidade metrológica:** cada resultado aponta para o equipamento e o técnico
   corretos, requisito das normas do setor para o certificado de calibração.
4. **Integridade:** as chaves estrangeiras impedem registrar uma medição de um equipamento
   ou de um técnico que não existe. O `ON DELETE RESTRICT` impede apagar quem já tem medições.
5. **Histórico:** o mesmo equipamento acumula várias calibrações sem copiar seus dados.
6. **Menos retrabalho e menos espaço:** o cadastro é feito uma única vez e reaproveitado.

## 7. Arquivos da entrega

| Arquivo | Função |
|---|---|
| `01_estrutura.md` | Este documento (modelo conceitual) |
| `02_dicionario.md` | Dicionário de dados, gerado por `gerar_dicionario_md.py` |
| `03_banco.sql` | Script DDL com as 3 tabelas, PK e FK |
| `executar_banco.py` | Executa o `.sql` e cria o banco `schulz_calibracao.db` |

## 8. Conclusão

A divisão em Técnico/Solicitante, Equipamento e Medição organiza os dados hoje espalhados
nas planilhas. O banco garante histórico, integridade e segurança para os certificados de
calibração da Schulz S.A.
