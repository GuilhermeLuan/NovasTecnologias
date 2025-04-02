from entities.produto import Produto
from entities.carrinho import Carrinho

carrinho = Carrinho()


produto1 = Produto('Monitor', 50, 5)
produto2 = Produto('Teclado Gamer', 50, 5)


carrinho.adicionar_produtos(produto1, 2)
carrinho.adicionar_produtos(produto2, 2)

print(carrinho)

print(produto1.quantidade_estoque)
print(produto2.quantidade_estoque)