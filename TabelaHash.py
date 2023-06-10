class RifaException(Exception):
    pass


class Pessoa:
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        self._rifas = {}

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    # verifica se a pessoa já comprou determinado número. Se ainda não comprou, adicionamos o número à lista de números dessa pessoa.
    def comprar_rifa(self, numero):
        if numero in self._rifas:
            raise RifaException("Este número já foi comprado por essa pessoa.")
        else:
            self._rifas[numero] = True

    def mostrar_rifas(self):
        if self._rifas:
            print("Rifas compradas por", self._nome + ":")
            for numero in self._rifas:
                print(numero)
        else:
            print("Nenhuma rifa comprada por", self._nome)


class TabelaHash:
    def __init__(self):
        self._tamanho = 100
        self._tabela = [None] * self._tamanho

    # esse aqui realiza uma operação simples para converter um CPF em um índice na tabela hash. Pesquisando eu descobri que dessa forma evita de ter colisões.
    def _hash(self, cpf):
        soma = 0
        for caractere in cpf:
            soma += ord(caractere)
        indice = soma % self._tamanho
        return indice

    def adicionar_pessoa(self, pessoa):
        indice = self._hash(pessoa.cpf)
        if self._tabela[indice] is None:
            self._tabela[indice] = [pessoa]
        else:
            for pessoa_existente in self._tabela[indice]:
                if pessoa_existente.cpf == pessoa.cpf:
                    raise RifaException("Essa pessoa já foi adicionada à tabela.")
                return
        self._tabela[indice].append(pessoa)

    def encontrar_pessoa(self, cpf):
        indice = self._hash(cpf)
        if self._tabela[indice] is not None:
            for pessoa in self._tabela[indice]:
                if pessoa.cpf == cpf:
                    return pessoa
        raise RifaException("Pessoa não encontrada na tabela.")
