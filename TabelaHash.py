class No:
    def __init__(self, info):
        self.__info = info
        self.__proximo = None

    def get_info(self):
        return self.__info

    def set_info(self, info):
        self.__info = info

    def get_proximo(self):
        return self.__proximo

    def set_proximo(self, proximo):
        self.__proximo = proximo


class ListaNumeros:
    def __init__(self):
        self.numeros = []

    def inicializar(self, quantidade):
        self.numeros = list(range(1, quantidade + 1))

    def remover_numero(self, numero):
        if numero in self.numeros:
            self.numeros.remove(numero)

    def verificar_disponibilidade(self, numero):
        return numero in self.numeros


class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.numeros_comprados = []

    def comprar_numero(self, numero, lista_numeros):
        if lista_numeros.verificar_disponibilidade(numero):
            self.numeros_comprados.append(numero)
            lista_numeros.remover_numero(numero)
            print(f"O número {numero} foi comprado com sucesso!")
        else:
            print(f"O número {numero} não está disponível para compra.")

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nNúmeros comprados: {', '.join(str(num) for num in self.numeros_comprados)}"



class TabelaHash:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__tabela = [None] * tamanho

    def _funcao_hash(self, info):
        return hash(info) % self.__tamanho

    def inserir(self, info):
        indice = self._funcao_hash(info)
        novo = No(info)

        if self.__tabela[indice] is None:
            self.__tabela[indice] = novo
        else:
            leitor = self.__tabela[indice]
            anterior = None
            while leitor is not None and leitor.get_info() <= info:
                anterior = leitor
                leitor = leitor.get_proximo()

            if leitor is not None:
                if anterior is not None:
                    novo.set_proximo(leitor)
                    anterior.set_proximo(novo)
                else:
                    novo.set_proximo(self.__tabela[indice])
                    self.__tabela[indice] = novo
            else:
                anterior.set_proximo(novo)

    def buscar(self, info):
        indice = self._funcao_hash(info)
        no = self.__tabela[indice]

        while no is not None:
            if no.get_info() == info:
                return no
            no = no.get_proximo()

        return None

    def remover(self, info):
        indice = self._funcao_hash(info)
        no = self.__tabela[indice]
        anterior = None

        while no is not None:
            if no.get_info() == info:
                if anterior is None:
                    self.__tabela[indice] = no.get_proximo()
                else:
                    anterior.set_proximo(no.get_proximo())
                return
            anterior = no
            no = no.get_proximo()

    def exibir(self):
        for indice, no in enumerate(self.__tabela):
            print(f"Índice {indice}: ", end="")
            while no is not None:
                print(f"({no.get_info()}) -> ", end="")
                no = no.get_proximo()
            print("None")


