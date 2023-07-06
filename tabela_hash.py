class Entry:
    __slots__ = ("__chave", "__valor")

    def __init__(self, chave, valor):
        # Inicialização de uma entrada na tabela hash
        self.__chave = chave  # Chave da entrada
        self.__valor = valor  # Valor da entrada

    @property
    def chave(self):
        return self.__chave

    @property
    def valor(self):
        return self.__valor


class TabelaHash:
    def __init__(self, tamanho):
        # Inicialização da tabela hash
        self.__tamanho = tamanho  # Tamanho da tabela
        self.__tabela = [[] for _ in range(tamanho)]  # Lista de listas para armazenar as entradas

    def __len__(self):
        return self.__tamanho

    def hash(self, chave: int):
        # Função de hash para calcular o índice da tabela baseado na chave
        return hash(chave) % self.__tamanho

    def put(self, chave, valor):
        # Método para inserir uma entrada na tabela hash
        return self.__put(chave, valor)

    def __put(self, chave, valor):
        # Método privado para inserir uma entrada na tabela hash
        indice = self.hash(chave)  # Calcula o índice da tabela para a chave

        for entry in self.__tabela[indice]:
            if entry.chave == indice:
                # Se uma entrada com a mesma chave já existir, retorna -1 para indicar que a inserção falhou
                return -1

        self.__tabela[indice].append(Entry(chave, valor))  # Adiciona a entrada ao compartimento correspondente
        return indice  # Retorna o índice da tabela onde a entrada foi inserida

    def get(self, chave):
        # Método para obter o valor associado a uma chave na tabela hash
        return self.__get(chave)

    def __get(self, chave):
        # Método privado para obter o valor associado a uma chave na tabela hash
        indice = self.hash(chave)  # Calcula o índice da tabela para a chave

        for entry in self.__tabela[indice]:
            if entry.chave == chave:
                # Se a entrada com a chave for encontrada, retorna o valor correspondente
                return entry.valor

        return -1  # Se a chave não for encontrada, retorna -1

    def get_tamanho(self):
        # Método para obter o tamanho da tabela hash
        return self.__get_tamanho()

    def __get_tamanho(self):
        # Método privado para obter o tamanho da tabela hash
        return self.__tamanho

    def get_tabela(self):
        # Método para obter a tabela hash
        return self.__get_tabela()

    def __get_tabela(self):
        # Método privado para obter a tabela hash
        return self.__tabela

    def __str__(self):
        # Método para retornar uma representação em string da tabela hash
        s = ""
        for index, items in enumerate(self.__tabela):
            if index + 1 < 10:
                s += f"0{index + 1}: "
            else:
                s += f"{index + 1}: "
            if items is None:
                s += " "
            else:
                s += items.__str__()
            s += "\n"
        return s