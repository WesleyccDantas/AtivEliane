class Cliente:
    def __init__(self, telefone, nome, endereco=None, cpf=None):
        self.telefone = telefone
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.senha = random.randint(1000, 9999)