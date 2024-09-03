from biblioteca.autor import Autor
from biblioteca.livro import Livro
from biblioteca.biblioteca import Biblioteca

def menu():
    biblioteca = Biblioteca()

    while True:
        print("\nMenu:")
        print("1. Adicionar um novo livro")
        print("2. Remover um livro")
        print("3. Buscar um livro")
        print("4. Listar todos os livros")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome_autor = input("Nome do autor: ")
            nacionalidade_autor = input("Nacionalidade do autor: ")
            data_nascimento_autor = input("Data de nascimento do autor (dd/mm/aaaa): ")
            titulo_livro = input("Título do livro: ")
            ano_publicacao = int(input("Ano de publicação: "))

            autor = Autor(nome_autor, nacionalidade_autor, data_nascimento_autor)
            livro = Livro(titulo_livro, autor, ano_publicacao)
            biblioteca.adicionarLivro(livro)
            print("Livro adicionado com sucesso.")

        elif escolha == "2":
            titulo_livro = input("Título do livro a ser removido: ")
            biblioteca.removerLivro(titulo_livro)
            print("Livro removido com sucesso, se existia.")

        elif escolha == "3":
            titulo_livro = input("Título do livro a ser buscado: ")
            livro = biblioteca.buscarLivro(titulo_livro)
            if livro:
                print("Livro encontrado:")
                print(livro.exibirLivro())
            else:
                print("Livro não encontrado.")

        elif escolha == "4":
            print("Livros na biblioteca:")
            print(biblioteca.listarLivros())

        elif escolha == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()