import random
from listaEncadeada import ListaEncadeada

class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.__tabela = [ListaEncadeada() for _ in range(tamanho)]
        self.comprados = 0        

    def calcular_indice(self, chave):
        return chave % self.tamanho

    def comprar(self, chave, valor):
        indice = self.calcular_indice(chave)
        self.__tabela[indice].inserir(chave, valor)
        self.comprados += 1
        return True

    def __len__(self):
        return self.tamanho

    def buscar(self, chave):
        indice = self.calcular_indice(chave)
        return self.__tabela[indice].buscar(chave)
    
    # def comprar(self, cpf, numero):
    #     indice = numero % self.tamanho

    #     if self[indice]:
    #         return False

    #     self[indice] = [cpf, numero]
    #     return True

    def numeros_nao_comprados(self):
        numeros = [i for i, comprador in enumerate(self.__tabela) if not comprador]
        return numeros
    
    def __str__(self):
        s = ""
        for index, items in enumerate(self.__tabela):
            if index+1 < 10:
                s += f"0{index+1}: "
            else:
                s += f"{index+1}: "
            if items == None:
                s += " "
            else:
                s += items.__str__()
            s += "\n"
        return s

    def sorteio(self):
        v = []
        for i, item in enumerate(self.__tabela):
            if len(item) != 0:
                v.append(i)
        numero_sorteado = random.choice(v)
        cpf = self.buscar(numero_sorteado-1)
        if numero_sorteado < 10:
            return f'\nSORTEIO!\n\nNumero sorteado: 0{numero_sorteado}\nCPF do ganhahdor: {cpf}\n'
        else:
            return f'\nSORTEIO!\n\nNumero sorteado: {numero_sorteado}\nCPF do ganhahdor: {cpf}\n'
    
    def imprimirCPF(self, valor):
        v = []
        for i, item in enumerate(self.__tabela):
            if len(item) != 0:
                if self.buscar(i) == valor:
                    chave = item.getNumero()
                    if chave < 10:
                        v.append(f'0{chave}')
        return f'CPF: {valor}\nNumeros comprados: {v}'
    
    def esgotou(self):
        if self.comprados == self.tamanho:
            return True
        else:
            return False

    
if __name__ == '__main__':
    t = TabelaHash(2)
    t.comprar(1, 6824224448)
    # t.comprar(0, 11532391472)
    print(t.numeros_nao_comprados())
    print(t.esgotou())