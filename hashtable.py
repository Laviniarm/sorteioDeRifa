# from comprador import Comprador

class TabelaHash:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__tabela = [None for i in range(tamanho)]
        self.__comprados = 0

    def __hash(self, chave):
        return hash(chave) % self.__tamanho
    
    def addObjeto(self, obj, chave):
        return self.__addObjeto(obj, chave-1)
    
    def __addObjeto(self, obj, chave):
        if self.__comprados < self.__tamanho:
            slot = self.__hash(chave)
            self.__tabela[slot] = obj
            self.__comprados += 1
    
    '''
    def addTabela(self, nome, cpf, numero):
        return self.__addTabela(nome, cpf, numero)

    def __addTabela(self, nome, cpf, numero):
        if self.__comprados < self.__tamanho:
            slot = self.__hash(numero)
            self.__tabela[slot] = Comprador(nome, cpf, numero)
            self.__comprados += 1
    '''
    
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