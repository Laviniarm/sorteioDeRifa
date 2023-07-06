import random

from tabela_hash import TabelaHash


class Gerenciador:
    def __init__(self, tamanho):
        # Inicialização do objeto Gerenciador
        self.__tabela_rifa = TabelaHash(tamanho)  # Cria uma instância da classe TabelaHash com o tamanho fornecido
        self.__comprados = {}  # Dicionário vazio para armazenar os números e CPFs comprados
        self.__numero_sorteado = None  # Número sorteado (inicialmente indefinido)
        self.__cpf_sorteado = None  # CPF correspondente ao número sorteado (inicialmente indefinido)

    def comprar(self, numero, cpf):
        # Método para realizar a compra de um número da rifa
        self.__comprados[numero] = cpf  # Adiciona o número e CPF ao dicionário de comprados
        return self.__tabela_rifa.put(numero, cpf)  # Insere o número e CPF na tabela de hash

    def numeros_nao_comprados(self):
        # Método para obter a lista de números não comprados
        return [i for i, valor in enumerate(self.__tabela_rifa.get_tabela()) if not valor]
        # Retorna uma lista de índices em que o valor correspondente na tabela de hash é False (não comprado)

    def sorteio(self):
        # Método para realizar o sorteio de um número da rifa
        if self.__numero_sorteado is None:
            # Se o número sorteado ainda não foi definido
            cpf, numero_sorteado = self.realizar_sorteio()  # Realiza o sorteio e obtém o CPF e número sorteado
            self.__numero_sorteado = numero_sorteado  # Armazena o número sorteado
            self.__cpf_sorteado = cpf  # Armazena o CPF correspondente
            return f'{str(numero_sorteado).zfill(2)}-{cpf}'
        else:
            return f'{str(self.__numero_sorteado).zfill(2)}-{self.__cpf_sorteado}'
            # Retorna uma string formatada com o número sorteado anteriormente e o CPF correspondente

    def realizar_sorteio(self):
        # Método para realizar o sorteio de um número da rifa
        numero_sorteado = random.randint(0, self.__tabela_rifa.get_tamanho())  # Gera um número aleatório
        cpf = self.__tabela_rifa.get(numero_sorteado)  # Obtém o CPF correspondente ao número sorteado
        return [cpf, numero_sorteado]  # Retorna uma lista com o CPF e número sorteado

    def esgotou(self):
        # Verifica se todos os números da rifa foram comprados
        return len(self.__comprados) == self.__tabela_rifa.get_tamanho()

    def get_tamanho(self):
        # Retorna o tamanho da tabela de hash
        return self.__tabela_rifa.get_tamanho()

