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



class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__numeros_comprados = []

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def numeros_comprados(self):
        return self.__numeros_comprados

    def comprar_numero(self, numero, TabelaHash ):
        self.__numeros_comprados.append(numero)
        TabelaHash.adicionar(numero, self.__cpf)
    


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


def realizar_compra_rifas():
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")

    pessoa = Pessoa(nome, cpf)
    rifa = Rifa()
    rifa.criar_lista()

    rifa.mostrar_numeros_disponiveis()
    tabela_hash = TabelaHash(100) 
    quantidade_rifas = int(input("Digite a quantidade de rifas que deseja comprar: "))  
    for _ in range(quantidade_rifas):
        numero_escolhido = int(input("Digite o número que deseja comprar: "))
        if numero_escolhido in rifa.numeros_disponiveis:
            rifa.numeros_disponiveis.remove(numero_escolhido)
            pessoa.comprar_numero(numero_escolhido, tabela_hash)
        else:
            print("Número indisponível. Escolha outro número.")

    rifa.mostrar_numeros_disponiveis()

    cpf = tabela_hash.buscar(numero_escolhido)
    print("CPF associado ao número da rifa:", cpf)

    return pessoa

if __name__ == "__main__":
    pessoa = realizar_compra_rifas()

    print("Números de rifa comprados pela pessoa:", pessoa.numeros_comprados)