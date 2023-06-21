import random

class Rifa:
    def __init__(self):
        self.__numerosDisponiveis = []

    def criar_lista(self):
        self.__numerosDisponiveis = list(range(1, 21))

    def sortear_numero(self):
        if len(self.__numerosDisponiveis) == 0:
            raise ValueError("Não há mais números disponíveis para sorteio.")
        numero_sorteado = random.choice(self.__numerosDisponiveis)
        self.__numerosDisponiveis.remove(numero_sorteado)
        return numero_sorteado

    def mostrar_numeros_disponiveis(self):
        print("Números disponíveis:", self.__numerosDisponiveis)

    @property
    def numeros_disponiveis(self):
        return self.__numerosDisponiveis