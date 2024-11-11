class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    def to_dict(self):
       
        return {
            "nome": self.__nome,
            "preco": self.__preco,
            "quantidade": self.__quantidade
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["nome"], data["preco"], data["quantidade"])
