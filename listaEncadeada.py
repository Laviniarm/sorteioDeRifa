class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None
    
    def estaVazia(self):
        return self.inicio is None
    
    def inserir_no_final(self, dado):
        novo_no = No(dado)
        if self.estaVazia():
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no

    def remover(self, dado):
        if self.estaVazia():
            return
        
        if self.inicio.dado == dado:
            self.inicio = self.inicio.proximo
            return
        
        atual = self.inicio
        anterior = None
        while atual is not None:
            if atual.dado == dado:
                anterior.proximo = atual.proximo
                return
            anterior = atual
            atual = atual.proximo
    
    def exibir(self):
        pass