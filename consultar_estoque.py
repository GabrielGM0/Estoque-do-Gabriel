from cadastro_de_produtos import estoque

def consultar_estoque(produto_id):

    for produto in estoque:
        if produto['item'].lower() == produto_id.lower():
            print(f"Produto: {produto['item']}")
            print(f"Quantidade em estoque: {produto['quantidade']}")
            return produto['quantidade']
    print(f"Produto '{produto_id}' não encontrado.")
    return None