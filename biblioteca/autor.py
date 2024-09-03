class Autor:
    def __init__(self, nome: str, nacionalidade: str, dataNascimento: str):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.dataNascimento = dataNascimento

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome

    def get_nacionalidade(self) -> str:
        return self.nacionalidade

    def set_nacionalidade(self, nacionalidade: str):
        self.nacionalidade = nacionalidade

    def get_dataNascimento(self) -> str:
        return self.dataNascimento

    def set_dataNascimento(self, dataNascimento: str):
        self.dataNascimento = dataNascimento

    def exibirAutor(self) -> str:
        return f"Nome: {self.nome}, Nacionalidade: {self.nacionalidade}, Data de Nascimento: {self.dataNascimento}"