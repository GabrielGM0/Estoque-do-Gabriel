from cadastro_de_produtos import estoque
def registrar_saida(produto_id, quantidade):

    if produto_id in estoque:

        if estoque[produto_id]["quantidade"] >= quantidade:
            estoque[produto_id]["quantidade"] -= quantidade
            print(f"Saida registrada. Nova quantidade no estoque: {estoque[produto_id]['quantidade']}")
        else:
            print("Estoque insuficiente")

    else:
        print("Produto não encontrado")
