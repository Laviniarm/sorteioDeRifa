class Entry:
    __slots__ = ("chave", "valor")

    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor


class TabelaHash:
    def __init__(self, tamanho):
        self._tamanho = tamanho
        self._tabela = [[] for _ in range(tamanho)]

    def __len__(self):
        return self._tamanho

    def hash(self, chave: int):
        return hash(chave) % self._tamanho

    def put(self, chave, valor):
        return self.__put(chave, valor)

    def __put(self, chave, valor):
        indice = self.hash(chave)

        for entry in self._tabela[indice]:
            if entry.chave == indice:
                return -1

        self._tabela[indice].append(Entry(chave, valor))
        return indice

    def get(self, chave):
        return self.__get(chave)

    def __get(self, chave):
        indice = self.hash(chave)

        for entry in self._tabela[indice]:
            if entry.chave == chave:
                return entry.valor

        return -1

    def get_tamanho(self):
        return self.__get_tamanho()

    def __get_tamanho(self):
        return self._tamanho

    def get_valores_vazios(self):
        return [i for i, valor in enumerate(self._tabela) if not valor]

    def get_tabela(self):
        return self.__get_tabela()

    def __get_tabela(self):
        return self._tabela

    def __str__(self):
        s = ""
        for index, items in enumerate(self._tabela):
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


'''Utilizar as implementações codificadas e concluídas em sala de aula;
● Adicionar ao menos um novo método em cada estrutura de dados utilizada, que seja
útil ao domínio do problema (a intenção é não levar para fora da estrutura de dados,
detalhes de implementação que a própria estrutura de dados deveria encapsular e
oferecer de forma abstrata ao programador);
● 'Documentação do código;
● Encapsulamento;
● Tratamento de exceções;
● Interação programa/usuário na exibição das mensagens do sistema (de erro ou alerta,
emitidas pelas estruturas de dados).'''
