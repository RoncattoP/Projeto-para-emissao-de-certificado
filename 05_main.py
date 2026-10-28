# ==============================================================================
# UNIDADE CURRICULAR: PROJETO APLICADO I - SCHULZ S.A.
# ITEM 05: SCRIPT PRINCIPAL DE DEMONSTRAÇÃO DO MVP (PARTE 1)
# GRUPO 25: Cristiane Nicolei | Matheus Martins | Priscilla Roncatto
# ==============================================================================
import importlib
import os
import sqlite3

# O módulo começa com número (04_classes), então usamos importlib.
classes = importlib.import_module("04_classes")
Banco = classes.Banco
Tecnico = classes.Tecnico
Equipamento = classes.Equipamento
Medicao = classes.Medicao

NOME_BANCO = "demo_calibracao.db"

# ------------------------------------------------------------------------------
# 1. PREPARAÇÃO: recria o banco do zero a cada execução (demonstração repetível)
# ------------------------------------------------------------------------------
if os.path.exists(NOME_BANCO):
    os.remove(NOME_BANCO)

conexao = sqlite3.connect(NOME_BANCO)
with open("03_banco.sql", "r", encoding="utf-8") as arquivo:
    conexao.executescript(arquivo.read())
conexao.close()

banco = Banco(NOME_BANCO)

print("=" * 70)
print(" MVP PARTE 1 - SISTEMA DE CALIBRAÇÃO | SCHULZ S.A.")
print("=" * 70)

# ------------------------------------------------------------------------------
# 2. INSERT: instancia os objetos e grava no SQLite
# ------------------------------------------------------------------------------
print("\n[1] Cadastrando técnicos e equipamento...")

t1 = Tecnico(None, "ava@schulz.com", "Ava", "Metrologia", "001")
t1.salvar(banco)
print(f"    Técnico gravado: {t1.nome} (ID {t1.ID})")

t2 = Tecnico(None, "jan@schulz.com", "Jan", "Metrologia", "002")
t2.salvar(banco)
print(f"    Técnico gravado: {t2.nome} (ID {t2.ID})")

e1 = Equipamento(None, "PAQ-001", "Paquímetro", "Mitutoyo", "500-196")
e1.salvar(banco)
print(f"    Equipamento gravado: {e1.codigo_tag} - {e1.nome} (ID {e1.Id_equipamento})")

print("\n[2] Registrando medições (o status é calculado pela tolerância)...")

# Valor dentro dos limites (9.9 a 10.1) -> APROVADO
m1 = Medicao(None, e1.Id_equipamento, t1.ID, "Comprimento", 10, 9.9, 10.1, 10.02, None, None)
m1.salvar(banco)
print(f"    Medição {m1.Id_medicao}: valor 10.02 -> {m1.status_resultado}")

# Valor fora dos limites -> REPROVADO
m2 = Medicao(None, e1.Id_equipamento, t2.ID, "Comprimento", 10, 9.9, 10.1, 10.5, None, None)
m2.salvar(banco)
print(f"    Medição {m2.Id_medicao}: valor 10.5  -> {m2.status_resultado}")

# ------------------------------------------------------------------------------
# 3. SELECT: lista os técnicos cadastrados
# ------------------------------------------------------------------------------
print("\n[3] Técnicos cadastrados (SELECT):")
for tec in Tecnico.listar(banco):
    print(f"    ID {tec.ID} | {tec.nome} | matrícula {tec.matricula} | {tec.setor}")

# ------------------------------------------------------------------------------
# 4. UPDATE: altera o setor de um técnico e lê de novo para confirmar
# ------------------------------------------------------------------------------
print("\n[4] Atualizando o setor do técnico Jan (UPDATE):")
t2.setor = "Qualidade"
t2.atualizar(banco)
for tec in Tecnico.listar(banco):
    if tec.ID == t2.ID:
        print(f"    {tec.nome} agora está no setor: {tec.setor}")

# ------------------------------------------------------------------------------
# 5. JOIN: relatório de calibração
# ------------------------------------------------------------------------------
print("\n[5] RELATÓRIO DE CALIBRAÇÃO (JOIN entre medicao, equipamento e tecnico)")
print("=" * 70)
for linha in Medicao.relatorio(banco):
    (id_medicao, codigo_tag, nome_equipamento, nome_tecnico, parametro,
     nominal, tol_min, tol_max, obtido, status, data) = linha
    print(f" Medição nº {id_medicao}  |  {data}")
    print(f" Equipamento : {codigo_tag} - {nome_equipamento}")
    print(f" Técnico     : {nome_tecnico}")
    print(f" Parâmetro   : {parametro}  (nominal {nominal})")
    print(f" Limites     : {tol_min} a {tol_max}")
    print(f" Obtido      : {obtido}")
    print(f" RESULTADO   : {status}")
    print("-" * 70)

# ------------------------------------------------------------------------------
# 6. TRATAMENTO DE ERROS SQL: tenta gravar uma matrícula repetida
# ------------------------------------------------------------------------------
print("\n[6] Teste de erro SQL (matrícula repetida):")
duplicado = Tecnico(None, "outro@schulz.com", "Outro", "Metrologia", "001")
duplicado.salvar(banco)
print(f"    ID gerado: {duplicado.ID}  (None = o banco recusou o registro)")

print("\nDemonstração concluída.")
