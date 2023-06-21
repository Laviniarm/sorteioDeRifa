from TabelaH import TabelaHash


class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__numeros_comprados = []

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def numeros_comprados(self):
        return self.__numeros_comprados

    def comprar_numero(self, numero, TabelaHash ):
        self.__numeros_comprados.append(numero)
        TabelaHash.adicionar(numero, self.__cpf)