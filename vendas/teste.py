from produto import Produto
from vendas import Venda

def menu():
    venda = Venda("01/01/2024")  # Data inicial de exemplo

    while True:
        print("\nMenu:")
        print("1. Adicionar um novo produto à venda")
        print("2. Remover um produto da venda")
        print("3. Listar todos os produtos da venda e mostrar o total")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome_produto = input("Nome do produto: ")
            preco_produto = float(input("Preço do produto: "))
            quantidade_produto = int(input("Quantidade do produto: "))

            produto = Produto(nome_produto, preco_produto, quantidade_produto)
            venda.adicionarProduto(produto)
            print("Produto adicionado com sucesso.")

        elif escolha == "2":
            nome_produto = input("Nome do produto a ser removido: ")
            venda.removerProduto(nome_produto)
            print("Produto removido com sucesso, se existia.")

        elif escolha == "3":
            print("Produtos na venda:")
            if not venda.get_produtos():
                print("Nenhum produto na venda.")
            else:
                for produto in venda.get_produtos():
                    print(produto.exibirProduto())
                print(f"Total da venda: R${venda.calcularTotal():.2f}")

        elif escolha == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()