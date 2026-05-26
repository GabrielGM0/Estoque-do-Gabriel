from cadastro_de_produtos import cadastrar_produto
from registrar_entrada import registrar_entrada
from registrar_saida import registrar_saida
from consultar_estoque import consultar_estoque
from alertar_estoque_baixo import alertar_estoque_baixo


def menu():

    while True:

        print("\n=== -Estoque de Produtos do Gabriel- ===")
        print("1 - Cadastrar produto")
        print("2 - Adicionar estoque")
        print("3 - Retirar estoque")
        print("4 - Consultar estoque")
        print("5 - Alertar estoque baixo")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            categoria = input("Categoria: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            cadastrar_produto(nome, categoria, quantidade, preco)

        elif opcao == "2":
            produto = input("Produto: ")
            quantidade = int(input("Quantidade de entrada: "))
            registrar_entrada(produto, quantidade)

        elif opcao == "3":
            produto = input("Produto: ")
            quantidade = int(input("Quantidade de saída: "))
            registrar_saida(produto, quantidade)

        elif opcao == "4":
             consultar_estoque()

        elif opcao == "5":
            limite = int(input("Limite mínimo: "))
            alertar_estoque_baixo(limite)

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")
