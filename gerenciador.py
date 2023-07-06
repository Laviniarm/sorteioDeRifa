import random
from hashtable import TabelaHash
from AVL import AVL


class Gerenciador:
    def __init__(self, tamanho):
        self.__tam_tabela = tamanho
        self.__tabela_rifa = TabelaHash(tamanho)
        self.__avl = AVL()
        self.__comprados = []
        self.__disponiveis = []
        self.__numero_sorteado = None
        self.__cpf_sorteado = None
   
    def comprar(self, nome, cpf, numero):
        no = self.__avl.add(nome, cpf, numero)
        self.__tabela_rifa.addObjeto(no, numero)
        self.__comprados.append(numero)


    def buscar(self, cpf):
        self.__avl.busca(cpf)

    def disponiveis(self):
        for i in range(self.__tam_tabela):
            if i+1 not in self.__comprados:
                self.__disponiveis.append(i+1)
        return self.__disponiveis                

    def sorteio(self):
        if self.__numero_sorteado is None:
            numero, vencedor = self.realizar_sorteio()
            self.__numero_sorteado = numero
            self.__cpf_sorteado = vencedor.getCPF()
            return f'\nSORTEIO!\n\nNumero sorteado: {self.__numero_sorteado}\nCPF do ganhador: {self.__cpf_sorteado}\n'
        else:
            return f'\nSORTEIO!\n\nNumero sorteado: {self.__numero_sorteado}\nNome do ganhador: {vencedor.getInfo()}\nCPF do ganhador: {self.__cpf_sorteado}\n'

    def realizar_sorteio(self):
        numero_sorteado = random.randint(0, self.__tamanho)
        return numero_sorteado, self.__tabela[numero_sorteado-1]
    
    def esgotou(self):
        return len(self.__comprados) == self.__tam_tabela