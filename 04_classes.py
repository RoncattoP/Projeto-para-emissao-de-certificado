class Tecnico : 
    def __init__(self, ID, email, nome, setor, matricula):
        self.ID = ID
        self.email = email
        self.nome = nome
        self.setor = setor
        self.matricula = matricula


class Equipamento :
    def __init__(self,Id_equipamento, codigo_tag, nome_equipamento, fabricante, modelo):
        self.Id_equipamento = Id_equipamento
        self.codigo_tag = codigo_tag
        self.nome = nome_equipamento
        self.fabricante = fabricante
        self.modelo = modelo

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