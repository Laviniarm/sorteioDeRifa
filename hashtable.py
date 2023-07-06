import random
from no import Comprador

class TabelaHash:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__tabela = [None for i in range(tamanho)]
        self.__comprados = {}
        self.__numero_sorteado = None
        self.__cpf_sorteado = ''

    def __hash(self, chave):
        return hash(chave) % self.__tamanho
    
    def addObjeto(self, obj, chave):
        return self.__addObjeto(obj, chave-1)
    
    def __addObjeto(self, obj, chave):
        if self.__comprados < self.__tamanho:
            slot = self.__hash(chave)
            self.__tabela[slot] = obj
            self.__comprados += 1
    
    def __str__(self):
        s = ""
        for index, items in enumerate(self.__tabela):
            s += f'{index + 1}: '
            if items is None:
                s += " "
            else:
                s += items.getCPF()
            s += "\n"
        return s