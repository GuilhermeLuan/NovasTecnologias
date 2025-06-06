# Sistema de Loja com POO

Projeto em Python que simula o controle de uma loja virtual utilizando os princípios da Programação Orientada a Objetos (POO).

## Descrição

Este sistema permite que o usuário:
- **Visualize** os produtos disponíveis na loja (nome, preço e estoque).
- **Adicione** produtos ao carrinho de compras com verificação de estoque.
- **Aplique** descontos (em percentual) em produtos específicos.
- **Visualize** os itens adicionados ao carrinho.
- **Finalize** a compra por meio de um pagamento simulado, com cálculo de troco.
- **Controle** o estoque dos produtos.
- **Navegue** por um menu interativo no terminal.

O projeto é organizado em múltiplas classes, cada uma com responsabilidades específicas:

- **Produto:** Representa um item da loja com atributos como nome, preço e quantidade em estoque.
- **Carrinho:** Responsável por armazenar os produtos selecionados pelo usuário, calcular o total da compra e esvaziar o carrinho após o pagamento.
- **Loja:** Gerencia os produtos, a exibição das informações e o processo de pagamento.

## Como Executar

1. **Pré-requisitos:**  
   - Certifique-se de ter o [Python 3.x](https://www.python.org/downloads/) instalado.

2. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
    ```
2. **Executar o projeto:**
   ```bash
   python main.py
    ```