class No:
    def __init__(self, chave, valor):
        # Inicialização de um nó da lista encadeada
        self.__chave = chave  # Atributo chave do nó
        self.__valor = valor  # Atributo valor do nó
        self.__proximo = None  # Referência ao próximo nó da lista

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

    @valor.setter
    def valor(self, novo_valor):
        self.__valor = novo_valor


class ListaEncadeada:
    def __init__(self):
        # Inicialização da lista encadeada
        self.__primeiro = None  # Referência ao primeiro nó da lista
        self.__tamanho = 0  # Tamanho da lista

    def tamanho(self):
        return self.__tamanho

    def __len__(self):
        return self.__tamanho

    def inserir(self, chave, valor):
        # Método para inserir um novo nó na lista encadeada
        return self.__inserir(chave, valor)

    def __inserir(self, chave, valor):
        # Método privado para inserir um novo nó na lista encadeada
        novo_no = No(chave, valor)  # Cria um novo nó com a chave e valor fornecidos

        if self.__primeiro is None:
            # Se a lista estiver vazia, o novo nó é definido como o primeiro nó
            self.__primeiro = novo_no
        else:
            # Caso contrário, percorre a lista até encontrar o último nó e o define como o próximo do novo nó
            atual = self.__primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
        self.__tamanho += 1

    def buscar(self, chave):
        # Método para buscar um nó na lista encadeada pelo valor da chave
        return self.__buscar(chave)

    def __buscar(self, chave):
        # Método privado para buscar um nó na lista encadeada pelo valor da chave
        atual = self.__primeiro
        while atual is not None:
            if atual.chave == chave:
                return atual.valor
            atual = atual.proximo
        return None

    def set_valor(self, chave, valor):
        # Método para atualizar o valor de um nó na lista encadeada pelo valor da chave
        atual = self.__primeiro
        while atual is not None:
            if atual.chave == chave:
                atual.valor = valor
            atual = atual.proximo
        return None

    def __str__(self):
        # Método para retornar uma representação em string da lista encadeada
        s = ''
        cursor = self.__primeiro
        while cursor != None:
            if cursor.proximo is None:
                s += f'{cursor.valor}'
            else:
                s += f'{cursor.valor}, '
            cursor = cursor.proximo
        s += ''
        return s
