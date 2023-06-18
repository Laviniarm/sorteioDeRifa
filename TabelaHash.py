import random


class Rifa:
    def __init__(self):
        self.__numerosDisponiveis = []

    def criar_lista(self):
        self.__numerosDisponiveis = list(range(1, 21))

    def sortear_numero(self):
        numero_sorteado = random.choice(self.__numerosDisponiveis)
        self.__numerosDisponiveis.remove(numero_sorteado)
        return numero_sorteado

    def mostrar_numeros_disponiveis(self):
        print("Números disponíveis:", self.__numerosDisponiveis)

    @property
    def numeros_disponiveis(self):
        return self.__numerosDisponiveis


class Pessoa:
    def __init__(self, nome, cpf, numeros_comprados):
        self.__nome = nome
        self.__cpf = cpf
        self.__numeros_comprados = numeros_comprados

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def numeros_comprados(self):
        return self.__numeros_comprados


class Nodo:
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
        novo_nodo = Nodo(chave, valor)

        if self.__primeiro is None:
            self.__primeiro = novo_nodo
        else:
            atual = self.__primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def buscar(self, chave):
        atual = self.__primeiro
        while atual is not None:
            if atual.chave == chave:
                return atual.valor
            atual = atual.proximo
        return None


class TabelaHash:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__tabela = [ListaEncadeada() for _ in range(tamanho)]

    def calcular_indice(self, chave):
        return hash(chave) % self.__tamanho

    def inserir(self, chave, valor):
        indice = self.calcular_indice(chave)
        self.__tabela[indice].inserir(chave, valor)

    def buscar(self, chave):
        indice = self.calcular_indice(chave)
        return self.__tabela[indice].buscar(chave)


def realizar_compra_rifas():
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")

    pessoa = Pessoa(nome, cpf, [])

    rifa = Rifa()
    rifa.criar_lista()

    rifa.mostrar_numeros_disponiveis()

    quantidade_rifas = int(
        input("Digite a quantidade de rifas que deseja comprar: "))

    for _ in range(quantidade_rifas):
        numero_escolhido = int(input("Digite o número que deseja comprar: "))
        if numero_escolhido in rifa.numeros_disponiveis:
            rifa.numeros_disponiveis.remove(numero_escolhido)
            pessoa.numeros_comprados.append(numero_escolhido)
        else:
            print("Número indisponível. Escolha outro número.")

    rifa.mostrar_numeros_disponiveis()

    return pessoa


# Criação da tabela hash
tabela_hash = TabelaHash(10)

# Lista de pessoas
lista_pessoas = []

# Realizar a compra de rifas e adicionar objetos Pessoa à lista
pessoa1 = realizar_compra_rifas()
lista_pessoas.append(pessoa1)

pessoa2 = realizar_compra_rifas()
lista_pessoas.append(pessoa2)

# Inserção dos objetos na tabela hash
for pessoa in lista_pessoas:
    tabela_hash.inserir(pessoa.cpf, pessoa)


# Busca de um objeto na tabela hash pelo CPF
cpf_busca = input("Digite o CPF da pessoa que deseja buscar: ")
resultado_busca = tabela_hash.buscar(cpf_busca)

if resultado_busca is not None:
    print("Nome:", resultado_busca.valor.nome)
    print("CPF:", resultado_busca.valor.cpf)
    print("Números comprados:", resultado_busca.valor.numeros_comprados)
else:
    print("Objeto não encontrado na tabela hash.")
