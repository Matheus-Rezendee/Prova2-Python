def criar_produto(nome, codigo, preco, estoque):
    return (nome, codigo, preco, estoque)

def atualizar_estoque(produto, quantidade):
    nome, codigo, preco, estoque = produto
    novo_estoque = estoque + quantidade
    return (nome, codigo, preco, novo_estoque)

def listar_produtos(produtos):
    for produto in produtos:
        nome, codigo, preco, estoque = produto
        print(f"Nome: {nome}, Código: {codigo}, Preço: R${preco:.2f}, Estoque: {estoque} unidades")

produto1 = criar_produto("Produto A", 101, 29.99, 50)
produto2 = criar_produto("Produto B", 102, 45.50, 30)
produto3 = criar_produto("Produto C", 103, 15.75, 20)

produto1 = atualizar_estoque(produto1, 10)
produto2 = atualizar_estoque(produto2, -5)
produto3 = atualizar_estoque(produto3, 15)

produtos = [produto1, produto2, produto3]
listar_produtos(produtos)

