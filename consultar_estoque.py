from cadastro_de_produtos import estoque

def consultar_estoque(produto_id):

    for produto in estoque:
        
        if produto.lower() == produto_id.lower():
            print(f"Produto: {produto}")
            print(f"Quantidade em estoque: {estoque[produto]['quantidade']}")
            return estoque[produto]['quantidade']
            
    print(f"Produto '{produto_id}' não encontrado.")
    return None
