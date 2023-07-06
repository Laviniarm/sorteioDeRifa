class Entry:
    __slots__ = ("__chave", "__valor")

    def __init__(self, chave, valor):
        self.__chave = chave
        self.__valor = valor

    @property
    def chave(self):
        return self.__chave

    @property
    def valor(self):
        return self.__valor


class TabelaHash:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__tabela = [[] for _ in range(tamanho)]

    def __len__(self):
        return self.__tamanho

    def hash(self, chave: int):
        return hash(chave) % self.__tamanho

    def put(self, chave, valor):
        return self.__put(chave, valor)

    def __put(self, chave, valor):
        indice = self.hash(chave)

        for entry in self.__tabela[indice]:
            if entry.chave == indice:
                return -1

        self.__tabela[indice].append(Entry(chave, valor))
        return indice

    def get(self, chave):
        return self.__get(chave)

    def __get(self, chave):
        indice = self.hash(chave)

        for entry in self.__tabela[indice]:
            if entry.chave == chave:
                return entry.valor

        return -1

    def get_tamanho(self):
        return self.__get_tamanho()

    def __get_tamanho(self):
        return self.__tamanho

    def get_tabela(self):
        return self.__get_tabela()

    def __get_tabela(self):
        return self.__tabela

    def __str__(self):
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
