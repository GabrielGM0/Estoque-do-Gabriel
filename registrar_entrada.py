from cadastro_de_produtos import estoque
def registrar_entrada(produto_id, quantidade):

    if produto_id in estoque:
        estoque[produto_id]["quantidade"] += quantidade
        print(f"Entrada registrada. Nova quantidade no estoque: {estoque[produto_id]['quantidade']}")
    else:
        print("Produto não encontrado")
