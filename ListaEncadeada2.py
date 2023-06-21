class No:
    def __init__(self, chave, valor):
        self.__chave = chave
        self.__valor = valor
        self.__proximo = None

    @property
    def chave(self):
        return self.__chave

    @property
    def valor(self):
        return self.__valor

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, novo_proximo):
        self.__proximo = novo_proximo


class ListaEncadeada:
    def __init__(self):
        self.__primeiro = None

    def inserir(self, chave, valor):
        novo_no = No(chave, valor)

        if self.__primeiro is None:
            self.__primeiro = novo_no
        else:
            atual = self.__primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no

    def buscar(self, chave):
        atual = self.__primeiro
        while atual is not None:
            if atual.chave == chave:
                return atual.valor
            atual = atual.proximo
        return None
