from ListaEncadeada2 import No, ListaEncadeada


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.__tabela = [ListaEncadeada() for _ in range(tamanho)]

    def calcular_indice(self, chave):
        return chave % self.tamanho

    def adicionar(self, chave, valor):
        indice = self.calcular_indice(chave)
        self.__tabela[indice].inserir(chave, valor)

    def buscar(self, chave):
        indice = self.calcular_indice(chave)
        return self.__tabela[indice].buscar(chave)