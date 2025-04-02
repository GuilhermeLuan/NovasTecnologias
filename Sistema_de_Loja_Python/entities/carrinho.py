class Carrinho:
    def __init__(self):
        self.produtos_no_carrinho = []
        self.total = 0

    def adicionar_produto(self, produto, quantidade):
        if(quantidade > produto.quantidade_estoque or quantidade < 0):
            print("Quantidade indisponível")
            return
        produto.diminuir_estoque(quantidade)
        self.produtos_no_carrinho.append(produto)
        self.calcular_total()
    
    def remover_produto(self, produto):
        if(produto not in self.produtos_no_carrinho):
            print("Produto não está no carrinho")
            return
        produto.aumentar_estoque(1)
        self.produtos_no_carrinho.remove(produto)              

    
    def calcular_total(self):
        for produto in self.produtos_no_carrinho:
            self.total += produto.preco

    def esvasiar_carrinho(self):
        self.produtos_no_carrinho = []
        self.total = 0
    
    def __str__(self):
        produtos = ', '.join([produto.nome for produto in self.produtos_no_carrinho])
        return f"Produtos no carrinho: {produtos}, Total: {self.total}"

        