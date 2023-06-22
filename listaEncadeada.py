import random

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
        self.__tamanho = 0
    
    def estaVazia(self):
        return self.__tamanho == 0

    def tamanho(self):
        return self.__tamanho

    def __len__(self):
        return self.__tamanho
    
    def getNumero(self):
        return self.__primeiro.chave
    
    def inserirOrdem(self, total):
        for i in range(total):
            self.insereFim(i+1)

    def inserir(self, chave, valor):
        novo_no = No(chave, valor)

        if self.__primeiro is None:
            self.__primeiro = novo_no
        else:
            atual = self.__primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
        self.__tamanho += 1

    def buscar(self, chave):
        atual = self.__primeiro
        while atual is not None:
            if atual.chave == chave:
                return atual.valor
            atual = atual.proximo
        return None

    def __str__(self):
        s = ''
        cursor = self.__primeiro
        while( cursor != None ):
            if cursor.proximo is None:
                s+= f'{cursor.valor}'
            else:
                s += f'{cursor.valor}, '
            cursor = cursor.proximo
        s += ''
        return s