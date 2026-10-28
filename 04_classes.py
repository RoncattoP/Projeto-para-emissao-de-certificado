import sqlite3


class Banco:
    def __init__(self, nome_banco="schulz_calibracao.db"):
        self.nome_banco = nome_banco

    def conectar(self):
        conexao = sqlite3.connect(self.nome_banco)
        conexao.execute("PRAGMA foreign_keys = ON")
        return conexao

class Tecnico : 
    def __init__(self, ID, email, nome, setor, matricula):
        self.ID = ID
        self.email = email
        self.nome = nome
        self.setor = setor
        self.matricula = matricula
    
    def salvar(self, banco):
        conexao = banco.conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO tecnico (nome_tecnico, matricula, email, setor) "
                "VALUES (?, ?, ?, ?)",
                (self.nome, self.matricula, self.email, self.setor),
            )
            conexao.commit()
            self.ID = cursor.lastrowid
        except sqlite3.Error as erro:
            print(f"Erro ao salvar técnico: {erro}")
        finally:
            conexao.close()

    @staticmethod
    def listar(banco):
        conexao = banco.conectar()
        tecnicos = []
        try:
            cursor = conexao.cursor()
            cursor.execute(
                "SELECT id_tecnico, nome_tecnico, matricula, email, setor "
                "FROM tecnico"
            )
            for linha in cursor.fetchall():
                tecnicos.append(Tecnico(linha[0], linha[3], linha[1], linha[4], linha[2]))   # <-- você preenche
        except sqlite3.Error as erro:
            print(f"Erro ao listar técnicos: {erro}")
        finally:
            conexao.close()
        return tecnicos

class Equipamento :
    def __init__(self,Id_equipamento, codigo_tag, nome_equipamento, fabricante, modelo):
        self.Id_equipamento = Id_equipamento
        self.codigo_tag = codigo_tag
        self.nome = nome_equipamento
        self.fabricante = fabricante
        self.modelo = modelo

    def salvar(self, banco):
        conexao = banco.conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO equipamento (codigo_tag, nome_equipamento, fabricante, modelo) "
                "VALUES (?, ?, ?, ?)",
                (self.codigo_tag, self.nome, self.fabricante, self.modelo),
            )
            conexao.commit()
            self.Id_equipamento = cursor.lastrowid
        except sqlite3.Error as erro:
            print(f"Erro ao salvar equipamento: {erro}")
        finally:
            conexao.close()

class Medicao :
    def __init__(self, Id_medicao, Id_equipamento, Id_tecnico, parametro_medido, valor_nominal, tolerancia_min, tolerancia_max, valor_obtido, status_resultado, data_medicao):
        self.Id_medicao = Id_medicao
        self.Id_equipamento = Id_equipamento
        self.Id_tecnico = Id_tecnico
        self.parametro_medido = parametro_medido
        self.valor_nominal = valor_nominal
        self.tolerancia_min = tolerancia_min
        self.tolerancia_max = tolerancia_max
        self.valor_obtido = valor_obtido
        self.status_resultado = status_resultado
        self.data_medicao = data_medicao

    def salvar(self, banco):
        self.validar_calibracao()
        conexao = banco.conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO medicao (id_equipamento, id_tecnico, parametro_medido, valor_nominal, tolerancia_min, tolerancia_max, valor_obtido, status_resultado) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (self.Id_equipamento, self.Id_tecnico, self.parametro_medido, self.valor_nominal, self.tolerancia_min, self.tolerancia_max, self.valor_obtido, self.status_resultado),
            )
            conexao.commit()
            self.Id_medicao = cursor.lastrowid
        except sqlite3.Error as erro:
            print(f"Erro ao salvar med: {erro}")
        finally:
            conexao.close()   

    def validar_calibracao(self):
        if self.tolerancia_min <= self.valor_obtido <= self.tolerancia_max:
            self.status_resultado = "APROVADO"
        else:
            self.status_resultado = "REPROVADO"
        return self.status_resultado

if __name__ == "__main__":
    for valor in (10.02, 10.5, 9.9, 9.5):
        m = Medicao(1, 1, 1, "Comprimento", 10, 9.9, 10.1, valor, None, None)
        print(valor, "->", m.validar_calibracao())

    banco = Banco()
    t = Tecnico(None, "ana@schulz.com", "Ana", "Metrologia", "001")
    t.salvar(banco)
    print("ID gerado:", t.ID)

    e = Equipamento(None, "PAQ-001", "Paquímetro", "Mitutoyo", "500-196")
    e.salvar(banco)
    print("ID equipamento:", e.Id_equipamento)

    m = Medicao(None, 1, 1, "Comprimento", 10, 9.9, 10.1, 10.02, None, None)
    m.salvar(banco)
    print("ID medição:", m.Id_medicao)

    for tec in Tecnico.listar(banco):
        print(tec.ID, tec.nome, tec.matricula)