import random

from tabela_hash import TabelaHash


class Gerenciador:

    def __init__(self, tamanho):
        self.__tabela_rifa = TabelaHash(tamanho)
        self.__comprados = {}
        self.__numero_sorteado = None
        self.__cpf_sorteado = None

    def comprar(self, numero, cpf):
        self.__comprados[numero] = cpf
        return self.__tabela_rifa.put(numero, cpf)
    
    def numeros_nao_comprados(self):
        return [i for i, valor in enumerate(self.__tabela_rifa.get_tabela()) if not valor]
   
    def sorteio(self):
        if self.__numero_sorteado is None:
            cpf, numero_sorteado = self.realizar_sorteio()
            self.__numero_sorteado = numero_sorteado
            self.__cpf_sorteado = cpf
            return f'\nSORTEIO!\n\nNumero sorteado: {str(numero_sorteado).zfill(2)}\nCPF do ganhador: {cpf}\n'
        else:
            return f'\nSORTEIO!\n\nNumero sorteado: {str(self.__numero_sorteado).zfill(2)}\nCPF do ganhador: {self.__cpf_sorteado}\n'

    def realizar_sorteio(self):
        numero_sorteado = random.randint(0, self.__tabela_rifa.get_tamanho())
        cpf = self.__tabela_rifa.get(numero_sorteado - 1)
        return cpf, numero_sorteado

    def esgotou(self):
        return len(self.__comprados) == self.__tabela_rifa.get_tamanho()

    def get_tamanho(self):
        return self.__tabela_rifa.get_tamanho()

