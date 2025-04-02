class Loja:
    def __init__(self, produto, carrinho):
        self.produto = produto
        self.carrinho = carrinho

    def pagamento(self, metodo_pagamento, total):   
        print("Pagamento efetuado com sucesso!")

    def pagamento_no_dinheiro(self, total, dinheiro):
        if(dinheiro < total):
            print("Dinheiro insuficiente!")
            return
        
        print("Pagamento efetuado com sucesso!")