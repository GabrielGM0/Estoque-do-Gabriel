estoque = {}

def cadastrar_produto(item, categoria, quantidade, preco):

    estoque[item] = {
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco
    }

    print(f"Produto {item} cadastrado com sucesso!")
