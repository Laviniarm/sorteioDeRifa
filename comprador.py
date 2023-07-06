class Comprador:
    def __init__(self, nome, cpf, numero):
        self.__nome = nome
        self.__cpf = cpf
        self.__numeros = []
        self.esq = None
        self.dir = None
        self.altura = 1

    def getCPF(self):
        return self.__cpf
    
    def getNumeros(self):
        return self.__numeros
    
    def addNumeros(self, numero):
        self.__numeros.append(numero)
        self.__numeros.sort()
        return True
    
    def __str__(self):
        return f'Nome: {self.__nome}\nCPF: {self.__cpf}\nNúmeros: {self.__numeros}'
    

if __name__ == "__main__":
    pass