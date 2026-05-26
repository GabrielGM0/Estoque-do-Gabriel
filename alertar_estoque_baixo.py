from cadastro_de_produtos import estoque
def alertar_estoque_baixo(limite):
    print("\n=== -Alerta Produto Com Estoque Baixo- ===")

    encontrou = False

    for produto, dados in estoque.items():

        if dados["quantidade"] <= limite:
            print(f"{produto} -> Quantidade: {dados['quantidade']}")
            encontrou = True

    if not encontrou:
        print("Nenhum produto encontrado com estoque baixo. ")
