from biblioteca.livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros:list[Livro] = []

    def adicionarLivro(self, livro: Livro):
        self.livros.append(livro)

    def removerLivro(self, titulo: str):
        self.livros = [livro for livro in self.livros if livro.get_titulo() != titulo]

    def buscarLivro(self, titulo: str):
        for livro in self.livros:
            if livro.get_titulo() == titulo:
                return livro
        return None

    def listarLivros(self) -> str:
        if not self.livros:
            return "Nenhum livro na biblioteca."
        return "\n".join(livro.exibirLivro() for livro in self.livros)