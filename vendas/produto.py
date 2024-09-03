class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome

    def get_preco(self) -> float:
        return self.preco

    def set_preco(self, preco: float):
        self.preco = preco

    def get_quantidade(self) -> int:
        return self.quantidade

    def set_quantidade(self, quantidade: int):
        self.quantidade = quantidade

    def exibirProduto(self) -> str:
        return f"Nome: {self.nome}, Preço: R${self.preco:.2f}, Quantidade: {self.quantidade}"