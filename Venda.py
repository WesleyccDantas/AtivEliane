class Venda:
    def __init__(self, cliente, produtos, forma_pagamento, parcelas):
        self.cliente = cliente
        self.produtos = produtos
        self.forma_pagamento = forma_pagamento
        self.parcelas = parcelas
        self.valor_total = sum(produto.preco for produto in produtos)