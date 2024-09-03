class Livro:
    def __init__(self, titulo: str, autor: str, anoPublicacao: int):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao

    def get_titulo(self) -> str:
        return self.titulo

    def set_titulo(self, titulo: str):
        self.titulo = titulo

    def get_autor(self) -> str:
        return self.autor

    def set_autor(self, autor: str):
        self.autor = autor

    def get_anoPublicacao(self) -> int:
        return self.anoPublicacao

    def set_anoPublicacao(self, anoPublicacao: int):
        self.anoPublicacao = anoPublicacao

    def exibirLivro(self) -> str:
        return f"Título: {self.titulo}, Autor: {self.autor.get_nome()}, Ano de Publicação: {self.anoPublicacao}"