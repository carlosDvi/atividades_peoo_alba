from typing import List

from produto import Produto

class Venda:
    def __init__(self, dataVenda: str):
        self.produtos: List[Produto] = []
        self.dataVenda = dataVenda
        self.total = 0.0

    def get_produtos(self) -> List[Produto]:
        return self.produtos

    def set_produtos(self, produtos: List[Produto]):
        self.produtos = produtos

    def get_dataVenda(self) -> str:
        return self.dataVenda

    def set_dataVenda(self, dataVenda: str):
        self.dataVenda = dataVenda

    def get_total(self) -> float:
        return self.total

    def set_total(self, total: float):
        self.total = total

    def calcularTotal(self) -> float:
        self.total = sum(produto.get_preco() * produto.get_quantidade() for produto in self.produtos)
        return self.total

    def adicionarProduto(self, produto: Produto):
        self.produtos.append(produto)
        self.calcularTotal()

    def removerProduto(self, nome: str):
        self.produtos = [produto for produto in self.produtos if produto.get_nome() != nome]
        self.calcularTotal()