import random
from ListaEncadeada import ListaEncadeada

class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.__tabela = [ListaEncadeada() for _ in range(tamanho)]        

    def calcular_indice(self, chave):
        return chave % self.tamanho

    def comprar(self, chave, valor):
        indice = self.calcular_indice(chave)
        self.__tabela[indice].inserir(chave, valor)
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
                v.append(i+1)
        numero_sorteado = random.choice(v)
        cpf = self.buscar(numero_sorteado-1)
        if numero_sorteado < 10:
            return f'Numero sorteado: 0{numero_sorteado}\nCPF do ganhahdor: {cpf}'
        else:
            return f'Numero sorteado: {numero_sorteado}\nCPF do ganhahdor: {cpf}'
    
    def imprimirCPF(self, valor):
        v = []
        for i, item in enumerate(self.__tabela):
            if len(item) != 0:
                if self.buscar(i) == valor:
                    chave = item.getNumero()
                    if chave < 10:
                        v.append(f'0{chave}')
        return f'CPF: {valor}\nNumeros comprados: {v}'