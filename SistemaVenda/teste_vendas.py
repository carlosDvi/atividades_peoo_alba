from Produto import Produto
from Venda import Venda

data = input("Digite a data da venda (formato: DD/MM/AAAA): ")
venda = Venda(data)
opcao = "0"

while opcao != "5":
    print("\nMenu:")
    print("1. Adicionar Produto")
    print("2. Remover Produto")
    print("3. Listar Produtos e Mostrar Total")
    print("4. Salvar Venda em JSON")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do Produto: ")

        preco_valido = False
        while not preco_valido:
            preco = input("Preço do Produto: ")
            preco = preco.replace(',', '.')  # Substitui vírgulas por pontos
            pontos = preco.count('.')
            if pontos <= 1 and all(part.isdigit() for part in preco.split('.')):
                preco = float(preco)
                preco_valido = True
            else:
                print("Preço inválido. Por favor, insira um valor numérico.")

        quantidade_valida = False
        while not quantidade_valida:
            quantidade = input("Quantidade em Estoque: ")
            if quantidade.isdigit():
                quantidade = int(quantidade)
                quantidade_valida = True
            else:
                print("Quantidade inválida. Por favor, insira um número inteiro.")

        produto = Produto(nome, preco, quantidade)
        venda.adicionarProduto(produto)  # Usando o método adicionarProduto

    elif opcao == "2":
        nome = input("Nome do Produto a remover: ")
        venda.removerProduto(nome)

    elif opcao == "3":
        venda.listarProdutos()
        print(f"Total da Venda: R${venda.calcularTotal():.2f}")

    elif opcao == "4":
        arquivo_nome = input("Digite o nome do arquivo JSON para salvar a venda: ")
        venda.salvar_em_json(arquivo_nome)

    elif opcao == "5":
        print("Saindo...")

    else:
        print("Opção inválida, tente novamente.")