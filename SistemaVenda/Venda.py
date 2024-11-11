import json


class Venda:
    def __init__(self, dataVenda):
        self.__produtos = []
        self.__dataVenda = dataVenda
        self.__total = 0.0

    def get_produtos(self):
        return self.__produtos

    def get_dataVenda(self):
        return self.__dataVenda

    def get_total(self):
        return self.__total

    def set_dataVenda(self, dataVenda):
        self.__dataVenda = dataVenda

    def calcularTotal(self):
        total = 0.0
        for produto in self.__produtos:
            total += produto.get_preco() * produto.get_quantidade()
        self.__total = total
        return total

    def removerProduto(self, nome):
        for produto in self.__produtos:
            if produto.get_nome() == nome:
                self.__produtos.remove(produto)
                print(f"Produto {nome} removido.")
                return
        print(f"Produto {nome} não encontrado.")

    def listarProdutos(self):
        if not self.__produtos:
            print("Nenhum produto na venda.")
        else:
            print(f"\nProdutos na Venda do dia {self.__dataVenda}:")
            for produto in self.__produtos:
                print(f"Nome: {produto.get_nome()}, Preço: R${produto.get_preco():.2f}, Quantidade: {produto.get_quantidade()}")

    def adicionarProduto(self, produto):
        self.__produtos.append(produto)

    def to_dict(self):
        return {
            "dataVenda": self.__dataVenda,
            "total": self.calcularTotal(),
            "produtos": [produto.to_dict() for produto in self.__produtos]
        }

    def salvar_em_json(self, arquivo_nome):
     
        with open(arquivo_nome, 'w') as arquivo:
            json.dump(self.to_dict(), arquivo, indent=4)
        print(f"Venda salva em {arquivo_nome}.")

    def carregar_de_json(self, arquivo_nome):
        with open(arquivo_nome, 'r') as arquivo:
            dados = json.load(arquivo)
            self.__dataVenda = dados["dataVenda"]
            self.__total = dados["total"]
            self.__produtos = [Produto.from_dict(produto) for produto in dados["produtos"]]
        print(f"Venda carregada de {arquivo_nome}.")