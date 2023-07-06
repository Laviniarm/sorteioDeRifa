class No:
    def __init__(self, info1, registro, chave):
        self.__info1 = info1
        self.__registro = registro
        self.__chave = []
        self.esq = None
        self.dir = None
        self.altura = 1

    def getRegistro(self):
        return self.__registro
    
    def getNumeros(self):
        return self.__chave
    
    def getInfo(self):
        return self.__info1
    
    def addNumeros(self, chave):
        self.__chave.append(chave)
        self.__chave.sort()
        return True
    
    def __str__(self):
        return f'Nome: {self.__info1}\nCPF: {self.__registro}\nNúmeros: {self.__chave}'