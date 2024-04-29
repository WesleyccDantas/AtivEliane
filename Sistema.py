import Cliente 
import Produto
import Venda

class Sistema:
    def __init__(self):
        self.clientes = []
        self.produtos = []
        self.vendas = []

    def cadastrar_cliente(self, telefone, nome, endereco, cpf):
        cliente_existente = self.buscar_cliente(telefone)
        if cliente_existente:
            print("Cliente já cadastrado.")
        else:
            novo_cliente = Cliente(telefone, nome, endereco, cpf)
            self.clientes.append(novo_cliente)
            print(f"Cliente cadastrado com sucesso. Sua senha é: {novo_cliente.senha}")

    def buscar_cliente(self, telefone):
        for cliente in self.clientes:
            if cliente.telefone == telefone:
                return cliente
        return None

    def realizar_venda(self, telefone, senha, produtos, forma_pagamento, parcelas):
        cliente = self.buscar_cliente(telefone)
        if not cliente:
            print("Cliente não encontrado.")
            return
        if cliente.senha != senha:
            print("Senha inválida.")
            return
        venda = Venda(cliente, produtos, forma_pagamento, parcelas)
        self.atualizar_estoque(produtos)
        self.vendas.append(venda)
        print("Venda realizada com sucesso.")

    def atualizar_estoque(self, produtos_vendidos):
        for produto_vendido in produtos_vendidos:
            for produto_estoque in self.produtos:
                if produto_vendido.nome == produto_estoque.nome:
                    produto_estoque.quantidade -= produto_vendido.quantidade

# Exemplo de uso do sistema
sistema = Sistema()

# Cadastro de produtos
produto1 = Produto("Facas Ginsu", 10, 50.0)
produto2 = Produto("Meias Vivarina", 20, 10.0)
sistema.produtos.append(produto1)
sistema.produtos.append(produto2)

# Cadastro de clientes
sistema.cadastrar_cliente("123456789", "João", "Rua A, 123", "123.456.789-10")

# Realização de venda
produtos_vendidos = [Produto("Facas Ginsu", 2, 50.0)]
sistema.realizar_venda("123456789", 1234, produtos_vendidos, "Cartão de Crédito", 3)